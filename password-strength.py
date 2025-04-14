import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔐Password Strength Checker")
st.markdown("""
### wellcome to the Password Strength Checker!👋
use this tool to check the strength of your password and get tips on how to make it stronger.
            we will give you helpful tips to create a **Strong Password** 🔒 """) 

password = st.text_input("**Enter your password:**", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:    
        feedback.append("❌ password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1    
    else:
        feedback.append("❌ password should contain at least one digit.") 
    if re.search(r"[!@#$%&*]", password):
        score += 1  
    else:
        feedback.append("❌ password should contain at least one special character (e.g., !@#$%&*).")
    if score == 4:
        feedback.append("✅Your password is strong!💪")
    elif score == 3:
        feedback.append("🟡Your password is moderate. Consider adding more complexity.")
    else:
        feedback.append("❌Your password is weak. Please make it stronger.")
    
    if feedback:
        st.markdown("## Improvement Suggestions:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to get staeted.")