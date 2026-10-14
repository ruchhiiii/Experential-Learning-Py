import streamlit as st
import hashlib
import re

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐")
st.title("🔐 Password Strength Analyzer")
st.caption("PASSWORD SECURITY AND STRENGTH ANALYSIS")
st.write("Analyze password strength and improve security.")
st.divider()
st.warning("Use a sample password, not your real password.")

password = st.text_input("Enter Sample Password", type="password")

def check_password(p):
    patterns = [
        len(p) >= 8, r"[A-Z]", r"[a-z]", r"[0-9]",
        r"[!@#$%^&*(),.?\":{}|<>]"
    ]
    checks = [patterns[0]] + [bool(re.search(x, p)) for x in patterns[1:]]
    tips = [
        "Use at least 8 characters.", "Add an uppercase letter.",
        "Add a lowercase letter.", "Add a number.",
        "Add a special character."
    ]
    return sum(checks), checks, [tips[i] for i, x in enumerate(checks) if not x]

if st.button("Analyze Password", type="primary", use_container_width=True):
    if not password:
        st.warning("Please enter a sample password.")
    else:
        score, checks, suggestions = check_password(password)
        st.subheader("Password Analysis")
        c1, c2 = st.columns(2)
        c1.metric("Security Score", f"{score}/5")

        if score <= 2:
            c2.error("WEAK")
            st.error("⚠️ Your password is WEAK!")
        elif score <= 4:
            c2.warning("MEDIUM")
            st.warning("Improve your password for better security.")
        else:
            c2.success("STRONG")
            st.success("✅ All five checks passed!")

        st.progress(score / 5)
        st.divider()
        st.subheader("Security Checklist")

        names = ["At least 8 characters", "Uppercase letter",
                 "Lowercase letter", "Number", "Special character"]
        for name, passed in zip(names, checks):
            st.write(("✅ " if passed else "❌ ") + name)

        st.divider()
        st.subheader("Suggestions")
        if suggestions:
            for tip in suggestions:
                st.write("•", tip)
        else:
            st.success("All password checks passed!")

        st.divider()
        st.subheader("SHA-256 Hash")
        st.code(hashlib.sha256(password.encode("utf-8")).hexdigest())
        st.caption("SHA-256 converts input text into a fixed-length hash.")
        st.warning("SHA-256 alone is not suitable for storing real passwords.")

st.divider()
st.caption("Password Strength Analyzer | Python | Streamlit | SHA-256")
