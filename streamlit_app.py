import streamlit as st
import hashlib
import re

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

# Background and page design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #172554, #111827);
    color: white;
}

.main .block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, p, label {
    color: #f8fafc !important;
}

.subtitle {
    color: #b8c5dc;
    text-align: center;
    font-size: 17px;
}

.card {
    background-color: rgba(30, 41, 59, 0.9);
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin: 12px 0;
}

.result {
    background-color: #1e293b;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #475569;
}

.tip {
    background-color: #172554;
    padding: 12px;
    border-left: 4px solid #60a5fa;
    border-radius: 6px;
    margin: 8px 0;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 12px;
    font-weight: bold;
}

.stButton > button:hover {
    border: 1px solid #93c5fd;
    color: white;
}

.stTextInput input {
    background-color: #1e293b;
    color: white;
    border: 1px solid #475569;
    border-radius: 8px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Heading
st.markdown(
    "<h1 style='text-align:center;'>🔐 Password Strength Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Check your password, improve its strength, "
    "and explore SHA-256 hashing.</p>",
    unsafe_allow_html=True
)

st.write("")

st.markdown("""
<div class="card">
<h3>🛡️ Password Security Check</h3>
<p>Check five basic password requirements and get suggestions
to improve your result.</p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "Privacy notice: Use a sample password for this demonstration. "
    "Do not enter a real or reused password."
)


# Password checking function
def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append(
            "Increase the length to at least 8 characters."
        )

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append(
            "Include at least one uppercase letter (A-Z)."
        )

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append(
            "Include at least one lowercase letter (a-z)."
        )

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add at least one number (0-9)."
        )

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append(
            "Add a special character, such as @, #, or !."
        )

    return score, suggestions


# Password input
password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Type your sample password..."
)

if st.button("🔍 Analyze Password"):

    if password == "":
        st.error("⚠️ Password field is empty. Please enter a sample password.")

    else:
        score, suggestions = check_password(password)

        # Determine strength
        if score <= 2:
            strength = "WEAK"
            color = "#f87171"
            message = "Your password needs improvement."
            st.error("⚠️ Weak password: Several security checks are missing.")

        elif score <= 4:
            strength = "MEDIUM"
            color = "#fbbf24"
            message = "Your password meets some requirements."
            st.warning("⚠️ Medium strength: Follow the suggestions below.")

        else:
            strength = "STRONG"
            color = "#4ade80"
            message = "All five basic checks have passed."
            st.success("✅ Strong result: All five basic checks passed.")

        # Result card
        st.markdown(f"""
        <div class="result">
            <p style="color:#cbd5e1;">PASSWORD STRENGTH</p>
            <h1 style="color:{color};">{strength}</h1>
            <p>{message}</p>
            <h3>{score}/5 checks passed</h3>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar
        st.write("### Strength Meter")
        st.progress(score / 5)

        # Suggestions
        st.write("### 💡 Security Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.markdown(
                    f'<div class="tip">⚠️ {suggestion}</div>',
                    unsafe_allow_html=True
                )
        else:
            st.success(
                "All five checks passed. Consider using a longer, "
                "unique passphrase for additional protection."
            )

        # Display check summary
        st.write("### 📋 Security Checklist")

        checks = [
            ("Minimum 8 characters", len(password) >= 8),
            ("Uppercase letter", bool(re.search(r"[A-Z]", password))),
            ("Lowercase letter", bool(re.search(r"[a-z]", password))),
            ("Number", bool(re.search(r"[0-9]", password))),
            ("Special character", bool(re.search(r"[^A-Za-z0-9]", password)))
        ]

        for name, passed in checks:
            if passed:
                st.write(f"✅ {name}")
            else:
                st.write(f"❌ {name}")

        # SHA-256 hashing
        st.write("### 🔑 SHA-256 Hash")

        hash_value = hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

        st.code(hash_value, language="text")

        st.caption(
            "SHA-256 generates a fixed-length hash. Hashing is not "
            "encryption and does not determine password strength."
        )

        st.info(
            "Educational project only: SHA-256 alone is not suitable "
            "for storing real user passwords. This demonstration does "
            "not intentionally save the entered password."
        )


# Footer
st.markdown("---")

st.markdown(
    "<p style='text-align:center;color:#94a3b8;'>"
    "Password Strength Analyzer | Phase 3<br>"
    "Python • Streamlit • Regular Expressions • SHA-256"
    "</p>",
    unsafe_allow_html=True
)
