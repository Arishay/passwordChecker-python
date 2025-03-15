import streamlit as st
import re

st.title("Welcome to Arishay's Password Checker 🤗")

# User input
password = st.text_input("Enter your password", type="password")


Feedback = []


score = 0


if st.button("Check Password"):
  
    if len(password) >= 8:
        score += 1
    else:
        Feedback.append("❌ The length of the password must be at least 8 characters long")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        Feedback.append("❌ The password must contain both uppercase and lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        Feedback.append("❌ The password must contain digits.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        Feedback.append("❌ The password must contain special characters.")

 
    if score == 4:
        Feedback.append("✅ Strong Password!")
    elif score == 3:
        Feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        Feedback.append("🔴 Weak Password - Improve it using the suggestions above.")

   
    if Feedback:
        st.markdown("💡 Improvement Suggestions:")
        for tip in Feedback:
            st.write(tip)
    else:
        st.info("👉 Enter your Password to get started")

# Footer message
st.info("Password Checker by Arisha.\n")
st.info("🤷‍♂️ What are you waiting for?\n")
st.info("Check your password's strength now❗")
