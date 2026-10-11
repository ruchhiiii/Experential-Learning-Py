import streamlit as st
import hashlib
import re

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Analyzer")
st.caption("PASSWORD SECURITY AND STRENGTH ANALYSIS")
st.write("Analyze your password strength and improve its security.")
st.divider()

st.warning("Security Warning: Do not enter your real or reused password. Use a sample password for this project.")

password = st.text_input("Enter Sample Password", type="password")

def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    return score, suggestions

if st.button("Analyze Password", type="primary", use_container_width=True):
    if password == "":
        st.warning("Please enter a sample password.")

    else:
        score, suggestions = check_password(password)

        st.subheader("Password Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Security Score", f"{score}/5")

        with col2:
            if score <= 2:
                st.error("WEAK")
            elif score <= 4:
                st.warning("MEDIUM")
            else:
                st.success("STRONG")

        st.progress(score / 5)

        if score <= 2:
            st.error("⚠️ Your password is WEAK! Please create a stronger password.")
        elif score <= 4:
            st.warning("⚠️ Your password is MEDIUM. Improve it for better security.")
        else:
            st.success("✅ Your password is STRONG! All five checks passed.")

        st.divider()
        st.subheader("Security Checklist")
        checks = [
            ("At least 8 characters", len(password) >= 8),
            ("Uppercase letter", bool(re.search(r"[A-Z]", password))),
            ("Lowercase letter", bool(re.search(r"[a-z]", password))),
            ("Number", bool(re.search(r"[0-9]", password))),
            ("Special character", bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)))
        ]
        for name, passed in checks:
            if passed:
                st.write("✅", name)
            else:
                st.write("❌", name)
        st.divider()
        st.subheader("Suggestions to Improve Your Password")
        if suggestions:
            for suggestion in suggestions:
                st.write("•", suggestion)
        else:
            st.success("All password checks passed!")

        st.divider()
        st.subheader("SHA-256 Hash")

        hash_value = hashlib.sha256(password.encode("utf-8")).hexdigest()
        st.code(hash_value, language="text")

        st.caption("SHA-256 generates a fixed-length hash from the entered text.")

        st.warning("Important: SHA-256 alone is not suitable for storing real user passwords. This feature is for educational demonstration only.")

st.divider()
st.caption("Password Strength Analyzer | Python | Streamlit | SHA-256")
