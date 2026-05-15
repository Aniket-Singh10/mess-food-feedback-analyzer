import streamlit as st


def main():
	st.set_page_config(page_title="Mess Food Feedback", page_icon="🍽️", layout="centered")

	st.title("Mess Food Feedback Form")
	st.write("Please rate each category from 1 to 5.")

	with st.form("feedback_form"):
		food_quality = st.slider("Food Quality", min_value=1, max_value=5, value=3)
		cleanliness = st.slider("Cleanliness", min_value=1, max_value=5, value=3)
		quantity = st.slider("Quantity", min_value=1, max_value=5, value=3)
		taste = st.slider("Taste", min_value=1, max_value=5, value=3)

		submitted = st.form_submit_button("Submit")

	if submitted:
		st.success("Feedback submitted successfully.")
		st.write("Your ratings:")
		st.write(f"Food Quality: {food_quality}")
		st.write(f"Cleanliness: {cleanliness}")
		st.write(f"Quantity: {quantity}")
		st.write(f"Taste: {taste}")


if __name__ == "__main__":
	main()
