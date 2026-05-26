"""
MessFood Feedback Analyzer 🍽️
A professional Streamlit app to predict and analyze mess food ratings.
Built for GSSoC 2026.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import joblib
import io
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage
)

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="MessFood Feedback Analyzer",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# CUSTOM CSS  — dark card theme
# ──────────────────────────────────────────────
st.markdown("""
<style>
/* ---- global background ---- */
.stApp { background-color: #0f1117; color: #e0e0e0; }

/* ---- sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1f2e 0%, #161b2e 100%);
    border-right: 1px solid #2d3561;
}

/* ---- metric cards ---- */
[data-testid="metric-container"] {
    background: #1e2235;
    border: 1px solid #2d3561;
    border-radius: 12px;
    padding: 16px;
}

/* ---- card div ---- */
.card {
    background: #1e2235;
    border: 1px solid #2d3561;
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
}

/* ---- section title ---- */
.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #7c83ff;
    margin-bottom: 12px;
}

/* ---- rating badge ---- */
.rating-badge {
    display: inline-block;
    background: linear-gradient(135deg, #7c83ff, #a78bfa);
    color: white;
    font-size: 36px;
    font-weight: 800;
    padding: 12px 32px;
    border-radius: 50px;
    text-align: center;
    margin: 8px 0;
}

/* ---- footer ---- */
.footer {
    text-align: center;
    color: #555;
    font-size: 13px;
    padding: 20px 0;
    border-top: 1px solid #2d3561;
    margin-top: 40px;
}

/* ---- button override ---- */
.stButton > button {
    background: linear-gradient(135deg, #7c83ff, #a78bfa);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 10px 24px;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# HELPER FUNCTIONS
# ──────────────────────────────────────────────

@st.cache_resource
def load_model():
    """Load the trained ML model from disk (cached so it loads once)."""
    model_path = os.path.join(os.path.dirname(__file__), "model", "model.pkl")
    return joblib.load(model_path)


def rating_label(rating: float) -> str:
    """Return a human-friendly label for a numeric rating."""
    if rating >= 4.5:
        return "⭐ Excellent"
    elif rating >= 3.5:
        return "😊 Good"
    elif rating >= 2.5:
        return "😐 Average"
    elif rating >= 1.5:
        return "😟 Below Average"
    else:
        return "😡 Poor"


def validate_csv(df: pd.DataFrame) -> tuple[bool, str]:
    """
    Check that the uploaded CSV has the required columns.
    Returns (is_valid, error_message).
    """
    required = {"food_quality", "cleanliness", "quantity", "taste"}
    missing = required - set(df.columns.str.lower())
    if missing:
        return False, f"Missing columns: {', '.join(missing)}"
    return True, ""


def fig_to_bytes(fig) -> bytes:
    """Convert a matplotlib figure to PNG bytes for embedding in the PDF."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120, bbox_inches="tight",
                facecolor="#1e2235")
    buf.seek(0)
    return buf.read()


def generate_pdf(df: pd.DataFrame, figures: list[bytes]) -> bytes:
    """
    Build a downloadable PDF report from the analysed dataframe and charts.
    Returns raw PDF bytes.
    """
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Custom paragraph styles
    title_style = ParagraphStyle(
        "title", parent=styles["Title"],
        fontSize=22, textColor=colors.HexColor("#7c83ff"),
        spaceAfter=6,
    )
    heading_style = ParagraphStyle(
        "heading", parent=styles["Heading2"],
        fontSize=14, textColor=colors.HexColor("#a78bfa"),
        spaceBefore=14, spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "body", parent=styles["Normal"],
        fontSize=10, textColor=colors.HexColor("#333333"),
        spaceAfter=4,
    )

    story = []

    # ── Title ──
    story.append(Paragraph("🍽️ MessFood Feedback Analyzer — Report", title_style))
    story.append(Paragraph(
        f"Generated on: {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
        body_style
    ))
    story.append(Spacer(1, 16))

    # ── Dataset Summary ──
    story.append(Paragraph("Dataset Summary", heading_style))
    summary_data = [
        ["Metric", "Value"],
        ["Total Rows", str(len(df))],
        ["Columns", ", ".join(df.columns.tolist())],
        ["Avg Predicted Rating", f"{df['Predicted_Rating'].mean():.2f}"],
        ["Min Predicted Rating", f"{df['Predicted_Rating'].min():.2f}"],
        ["Max Predicted Rating", f"{df['Predicted_Rating'].max():.2f}"],
    ]
    t = Table(summary_data, colWidths=[200, 280])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#7c83ff")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.HexColor("#f5f5ff"), colors.white]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 16))

    # ── Factor Averages ──
    story.append(Paragraph("Average Factor Scores", heading_style))
    factor_cols = [c for c in ["food_quality", "cleanliness", "quantity", "taste"]
                   if c in df.columns]
    factor_data = [["Factor", "Average Score"]] + [
        [col.replace("_", " ").title(), f"{df[col].mean():.2f}"]
        for col in factor_cols
    ]
    t2 = Table(factor_data, colWidths=[200, 280])
    t2.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#a78bfa")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.HexColor("#f5f5ff"), colors.white]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ("PADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t2)
    story.append(Spacer(1, 16))

    # ── Charts ──
    if figures:
        story.append(Paragraph("Visualizations", heading_style))
        for png_bytes in figures:
            img_buf = io.BytesIO(png_bytes)
            img = RLImage(img_buf, width=5 * inch, height=3 * inch)
            story.append(img)
            story.append(Spacer(1, 12))

    # ── Footer ──
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "Built for GSSoC 2026 · MessFood Feedback Analyzer · Open Source Project",
        ParagraphStyle("footer", parent=body_style,
                       textColor=colors.HexColor("#999999"), alignment=1)
    ))

    doc.build(story)
    return buf.getvalue()


# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🍽️ MessFood Analyzer")
    st.markdown("*AI-powered mess food rating predictor*")
    st.divider()

    page = st.radio(
        "Navigate",
        ["🏠 Home", "🔮 Predict Rating", "📂 Bulk CSV Analysis",
         "📊 Visualizations", "📄 Download Report"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown("""
    **About**  
    Predict mess food ratings using Machine Learning based on:
    - 🥘 Food Quality  
    - 🧹 Cleanliness  
    - 🍱 Quantity  
    - 😋 Taste  
    """)
    st.divider()
    st.markdown('<p style="color:#555;font-size:12px;">Built for GSSoC 2026 🚀</p>',
                unsafe_allow_html=True)

# Load model once
model = load_model()

# Shared session state for CSV predictions
if "predicted_df" not in st.session_state:
    st.session_state.predicted_df = None


# ──────────────────────────────────────────────
# PAGE: HOME
# ──────────────────────────────────────────────

if page == "🏠 Home":
    st.markdown("# 🍽️ MessFood Feedback Analyzer")
    st.markdown(
        "A **modern ML-powered platform** for college mess food feedback analysis. "
        "Predict ratings, visualise trends, and download full reports — all in one place."
    )
    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("ML Model", "Linear Regression")
    col2.metric("Input Features", "4")
    col3.metric("Rating Scale", "1 – 5")
    col4.metric("Report Format", "PDF")

    st.divider()

    st.markdown("### ✨ Features")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card">
            <div class="section-title">🔮 Single Prediction</div>
            Use sliders to rate each factor and get an instant predicted mess rating.
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div class="section-title">📂 Bulk CSV</div>
            Upload a CSV with multiple feedback rows and predict ratings for all of them at once.
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card">
            <div class="section-title">📊 Visualizations</div>
            Explore factor distributions, rating trends, and a correlation heatmap.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">Built for GSSoC 2026 · MessFood Feedback Analyzer · Open Source</div>
    """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# PAGE: SINGLE PREDICTION
# ──────────────────────────────────────────────

elif page == "🔮 Predict Rating":
    st.markdown("# 🔮 Predict Mess Food Rating")
    st.markdown("Adjust the sliders and click **Predict** to get the model's rating.")
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        food_quality = st.slider("🥘 Food Quality", 1, 5, 3,
                                 help="Rate the overall quality of the food (1 = very bad, 5 = excellent)")
        cleanliness = st.slider("🧹 Cleanliness", 1, 5, 3,
                                help="Rate the cleanliness of the mess area")
        quantity = st.slider("🍱 Quantity", 1, 5, 3,
                             help="Rate whether the quantity of food was sufficient")
        taste = st.slider("😋 Taste", 1, 5, 3,
                          help="Rate how the food tasted overall")
        predict_btn = st.button("🔮 Predict Rating", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if predict_btn:
            with st.spinner("Running model..."):
                features = np.array([[food_quality, cleanliness, quantity, taste]])
                prediction = model.predict(features)[0]
                # Clamp to valid range
                prediction = float(np.clip(prediction, 1, 5))

            label = rating_label(prediction)

            st.markdown(f"""
            <div class="card" style="text-align:center;">
                <div class="section-title" style="text-align:center;">Predicted Rating</div>
                <div class="rating-badge">{prediction:.2f} / 5</div>
                <p style="font-size:22px; margin-top:12px;">{label}</p>
            </div>
            """, unsafe_allow_html=True)

            # Progress bar visual
            st.progress(prediction / 5, text=f"Score: {prediction:.2f} / 5")

            # Factor breakdown
            st.markdown("**Your Input Summary**")
            factor_df = pd.DataFrame({
                "Factor": ["Food Quality", "Cleanliness", "Quantity", "Taste"],
                "Score": [food_quality, cleanliness, quantity, taste],
            })
            fig = px.bar(factor_df, x="Factor", y="Score",
                         color="Score", color_continuous_scale="Viridis",
                         range_y=[0, 5], template="plotly_dark",
                         title="Factor Scores")
            fig.update_layout(paper_bgcolor="#1e2235", plot_bgcolor="#1e2235",
                              margin=dict(t=40, b=10))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown("""
            <div class="card" style="text-align:center; padding:60px;">
                <p style="font-size:48px;">🍽️</p>
                <p style="color:#555;">Adjust sliders and click <b>Predict Rating</b></p>
            </div>
            """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# PAGE: BULK CSV ANALYSIS
# ──────────────────────────────────────────────

elif page == "📂 Bulk CSV Analysis":
    st.markdown("# 📂 Bulk CSV Analysis")
    st.markdown("Upload a CSV with columns: `food_quality`, `cleanliness`, `quantity`, `taste`")
    st.divider()

    # Sample download
    sample_csv = ("food_quality,cleanliness,quantity,taste\n"
                  "4,3,5,4\n3,4,3,5\n2,2,2,3\n5,5,4,5\n1,2,1,1\n")
    st.download_button("⬇️ Download Sample CSV", sample_csv,
                       file_name="sample_mess_feedback.csv",
                       mime="text/csv")

    uploaded = st.file_uploader("Upload your CSV", type=["csv"])

    if uploaded:
        with st.spinner("Reading CSV..."):
            df = pd.read_csv(uploaded)
            df.columns = df.columns.str.lower().str.strip()

        valid, err = validate_csv(df)
        if not valid:
            st.error(f"❌ {err}")
        else:
            st.success(f"✅ File loaded — {len(df)} rows detected")

            with st.spinner("Predicting ratings for all rows..."):
                X = df[["food_quality", "cleanliness", "quantity", "taste"]]
                df["Predicted_Rating"] = np.clip(model.predict(X), 1, 5).round(2)
                df["Rating_Label"] = df["Predicted_Rating"].apply(rating_label)
                st.session_state.predicted_df = df

            st.markdown("### 📋 Predicted Results")
            st.dataframe(df, use_container_width=True, height=350)

            # Download predictions
            csv_out = df.to_csv(index=False).encode()
            st.download_button("⬇️ Download Predictions CSV", csv_out,
                               file_name="predicted_ratings.csv",
                               mime="text/csv")
    else:
        st.markdown("""
        <div class="card" style="text-align:center; padding:60px;">
            <p style="font-size:48px;">📂</p>
            <p style="color:#555;">Upload a CSV file to get started</p>
        </div>
        """, unsafe_allow_html=True)


# ──────────────────────────────────────────────
# PAGE: VISUALIZATIONS
# ──────────────────────────────────────────────

elif page == "📊 Visualizations":
    st.markdown("# 📊 Visualizations")
    st.divider()

    df = st.session_state.predicted_df

    if df is None:
        st.warning("⚠️ Please upload a CSV in **Bulk CSV Analysis** first.")
        st.stop()

    factor_cols = ["food_quality", "cleanliness", "quantity", "taste"]

    # ── 1. Average Factor Scores ──
    st.markdown("### 🎯 Average Factor Scores")
    avg_scores = df[factor_cols].mean().reset_index()
    avg_scores.columns = ["Factor", "Average Score"]
    avg_scores["Factor"] = avg_scores["Factor"].str.replace("_", " ").str.title()
    fig1 = px.bar(avg_scores, x="Factor", y="Average Score",
                  color="Average Score", color_continuous_scale="Teal",
                  template="plotly_dark", range_y=[0, 5],
                  title="Average Score per Factor")
    fig1.update_layout(paper_bgcolor="#1e2235", plot_bgcolor="#1e2235")
    st.plotly_chart(fig1, use_container_width=True)

    # ── 2. Rating Distribution ──
    st.markdown("### 📈 Predicted Rating Distribution")
    fig2 = px.histogram(df, x="Predicted_Rating", nbins=10,
                        color_discrete_sequence=["#7c83ff"],
                        template="plotly_dark",
                        title="Distribution of Predicted Ratings")
    fig2.update_layout(paper_bgcolor="#1e2235", plot_bgcolor="#1e2235")
    st.plotly_chart(fig2, use_container_width=True)

    # ── 3. Correlation Heatmap (matplotlib/seaborn) ──
    st.markdown("### 🔥 Correlation Heatmap")
    corr = df[factor_cols + ["Predicted_Rating"]].corr()
    fig3, ax = plt.subplots(figsize=(7, 5))
    fig3.patch.set_facecolor("#1e2235")
    ax.set_facecolor("#1e2235")
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                linewidths=0.5, ax=ax,
                annot_kws={"color": "white"})
    plt.xticks(color="white")
    plt.yticks(color="white")
    ax.tick_params(colors="white")
    plt.title("Feature Correlation Heatmap", color="white")
    st.pyplot(fig3)
    plt.close(fig3)

    # ── 4. Best / Worst factor ──
    st.markdown("### 🏆 Best & Worst Factor")
    means = df[factor_cols].mean()
    best = means.idxmax().replace("_", " ").title()
    worst = means.idxmin().replace("_", " ").title()
    c1, c2 = st.columns(2)
    c1.success(f"✅ **Best Factor:** {best} ({means.max():.2f} / 5)")
    c2.error(f"❌ **Worst Factor:** {worst} ({means.min():.2f} / 5)")

    # ── 5. Trend (row index as proxy for time) ──
    st.markdown("### 📉 Rating Trend Across Submissions")
    fig4 = px.line(df.reset_index(), x="index", y="Predicted_Rating",
                   markers=True, template="plotly_dark",
                   title="Predicted Rating per Submission",
                   labels={"index": "Submission #", "Predicted_Rating": "Rating"})
    fig4.update_traces(line_color="#7c83ff")
    fig4.update_layout(paper_bgcolor="#1e2235", plot_bgcolor="#1e2235")
    st.plotly_chart(fig4, use_container_width=True)


# ──────────────────────────────────────────────
# PAGE: DOWNLOAD REPORT
# ──────────────────────────────────────────────

elif page == "📄 Download Report":
    st.markdown("# 📄 Download Feedback Report")
    st.markdown("Generate a comprehensive PDF report from your uploaded dataset.")
    st.divider()

    df = st.session_state.predicted_df

    if df is None:
        st.warning("⚠️ Please upload a CSV in **Bulk CSV Analysis** first.")
        st.stop()

    if st.button("🖨️ Generate PDF Report", use_container_width=True):
        with st.spinner("Building report... this may take a few seconds"):
            factor_cols = ["food_quality", "cleanliness", "quantity", "taste"]
            figs_bytes = []

            # Chart 1 — avg factor scores
            avg = df[factor_cols].mean()
            fig_a, ax_a = plt.subplots(figsize=(6, 3))
            fig_a.patch.set_facecolor("#1e2235")
            ax_a.set_facecolor("#1e2235")
            bars = ax_a.bar(
                [c.replace("_", " ").title() for c in factor_cols],
                avg.values,
                color=["#7c83ff", "#a78bfa", "#60a5fa", "#34d399"],
            )
            ax_a.set_ylim(0, 5)
            ax_a.set_title("Average Factor Scores", color="white")
            ax_a.tick_params(colors="white")
            for spine in ax_a.spines.values():
                spine.set_edgecolor("#2d3561")
            figs_bytes.append(fig_to_bytes(fig_a))
            plt.close(fig_a)

            # Chart 2 — rating distribution
            fig_b, ax_b = plt.subplots(figsize=(6, 3))
            fig_b.patch.set_facecolor("#1e2235")
            ax_b.set_facecolor("#1e2235")
            ax_b.hist(df["Predicted_Rating"], bins=10,
                      color="#7c83ff", edgecolor="#2d3561")
            ax_b.set_title("Predicted Rating Distribution", color="white")
            ax_b.tick_params(colors="white")
            for spine in ax_b.spines.values():
                spine.set_edgecolor("#2d3561")
            figs_bytes.append(fig_to_bytes(fig_b))
            plt.close(fig_b)

            pdf_bytes = generate_pdf(df, figs_bytes)

        st.success("✅ Report generated!")
        st.download_button(
            "⬇️ Download PDF Report",
            data=pdf_bytes,
            file_name=f"messfood_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    # Preview summary
    st.markdown("### Preview")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Rows", len(df))
    c2.metric("Avg Predicted Rating", f"{df['Predicted_Rating'].mean():.2f}")
    c3.metric("Best Rating", f"{df['Predicted_Rating'].max():.2f}")

# ──────────────────────────────────────────────
# GLOBAL FOOTER
# ──────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built for <b>GSSoC 2026</b> · MessFood Feedback Analyzer 🍽️ · Open Source Project
</div>
""", unsafe_allow_html=True)
