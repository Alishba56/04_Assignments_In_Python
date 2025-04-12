import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("💪 BMI Calculator")

    st.write("Enter your weight and height to calculate your Body Mass Index.")

    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, step=0.5)
    height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, step=0.01)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        st.success(f"Your BMI is: {bmi}")
        st.info(f"Category: {classification}")

if __name__ == "__main__":
    main()
