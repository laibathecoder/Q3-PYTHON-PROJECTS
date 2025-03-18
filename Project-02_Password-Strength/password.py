import streamlit as st
import re

st.set_page_config(page_title = "Password Stregth" , page_icon = "🔒")
st.title("💪Strong Password Stregth checker✅")

st.markdown(""" ### Welcome to the Strong Password Checker 🔒app """)
st.markdown("Use our powerful tool to check the strength of your password and get suggestions on how to make it stronger. We also provide helpful and superb tips to enhance the security of your password, making it more resilient and hack proof. 🔐")


password = st.text_input("Enter your password" , type = "password")
feedback = []
score = 0

if password :
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌🔢Password should be at lest 8 characters long")
    
    if re.search(r"[A-Z]" , password): 
        score += 1
    else:
        feedback.append("Password should contain Upper(A-Z) case characters or latters")

    if re.search(r"[a-z]" , password):
        score += 1
    else:
        feedback.append("Password should contain Lower(a-z) case characters or latters")

    if re.search(r"\d" , password):
        score += 1 
    else:
        feedback.append("Your password should contain at lest 1 digit")

    if re.search(r"[@$&*#%+!]" , password):
        score += 1
    else:
        feedback.append("Your password should contain at leat one special characters[@ , $ , & , * , # , % , + , !]")


    if score == 5:
        feedback.append("✅ Your pasword is strong and secure 🔐")
        st.ballons()

    elif score == 4 :
        feedback.append("💹 Yor password is medium strong. It could me more stronger")

    elif score == 3 :
        feedback.append("📉 Your password is not Strong and Not weak.👨‍💻 Make it more strong 💪 for security 🔐")

    else:
        feedback.append("❌Your password is weak. Please make it Strong and secure.")


    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)


else:
    st.info("Please enter your password to get started")
