# BMI calculator in Python by using streamlit

import streamlit as st

st.title("🧮 BMI Calculator")

height = st.slider("📏 Enter your height (cm)", 100, 250, 175)
weight = st.slider("⚖️ Enter your weight (kg)", 40, 200, 70)

if st.button("✅ Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    
    st.write(f"💡 **Your BMI is:** `{bmi:.2f}`")

    if bmi < 18.5:
        st.write("🔵 Underweight: BMI is less than 18.5 😟")
    elif 18.5 <= bmi < 25.0:
        st.write("🟢 Normal weight: BMI is between 18.5 and 24.9 😊")
    elif 25.0 <= bmi < 30.0:
        st.write("🟠 Overweight: BMI is between 25 and 29.9 😐")
    else:
        st.write("🔴 Obesity: BMI is 30 or greater 😟")
