
import streamlit as st

st.title("🌍 My Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Quickly ###")
st.write("Welcome to My App! Please select a category, enter a value, and get the conversion in real time.")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

if category == "Length":
    unit = st.selectbox("Select a conversion", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select a conversion", ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select a conversion", [
        "seconds to minutes", "minutes to seconds",
        "minutes to hours", "hours to minutes",
        "hours to days", "days to hours"
    ])

#User Input
value = st.number_input("Enter the value to convert")

def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
    
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24

    return None 

if st.button("CONVERT"):
    result = convert_unit(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion selected")
