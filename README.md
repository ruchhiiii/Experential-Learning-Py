# 🔐 Password Strength Analyzer Using Hashing

## 📌 Project Overview

The Password Strength Analyzer is a Python-based application that evaluates password strength using different validation rules. It helps users understand whether a password is Weak, Medium, or Strong and provides suggestions to improve password security.

The project also demonstrates password hashing using the SHA-256 algorithm. An interactive web interface is developed using Streamlit to make the application simple and user-friendly.

## 🎯 Objectives

- To analyze password strength using predefined validation rules.
- To check password length and character combinations.
- To identify missing password requirements.
- To provide suggestions for improving password strength.
- To understand the concept of hashing using Python.
- To develop an interactive and user-friendly application.
- To improve awareness of password security.

## 🛠️ Technologies Used

- **Python:** Used to implement password validation and hashing logic.
- **Streamlit:** Used to create the interactive web interface.
- **Regular Expressions:** Used to check password character patterns.
- **Hashlib:** Used to generate SHA-256 hash values.
- **GitHub:** Used to store and manage the project source code.

## 📂 Project Development Phases

### 🔹 Phase 1: Basic Password Strength Analysis

In Phase 1, a basic password strength analysis program was developed using Python. The program checks password length, uppercase letters, lowercase letters, numbers, and special characters.

Based on the conditions satisfied, the program calculates a strength score and classifies the password as Weak, Medium, or Strong.

### 🔹 Phase 2: Password Hashing

In Phase 2, password hashing was explored using Python's `hashlib` module. The SHA-256 algorithm converts input text into a fixed-length hash value.

The `encode()` method converts text into bytes, while the `hexdigest()` method returns the hash as a hexadecimal string.

### 🔹 Phase 3: Interactive Web Application

In Phase 3, the Password Strength Analyzer was developed into an interactive web application using Streamlit.

The application provides password validation, a strength indicator, a checklist of security conditions, suggestions for improvement, and SHA-256 hash generation.

The interface makes password analysis simple and easy to understand.

## ✨ Features

- 🔑 Password strength analysis.
- 📏 Password length validation.
- 🔠 Uppercase and lowercase letter checking.
- 🔢 Number validation.
- 🔣 Special character validation.
- 📊 Password strength score and visual indicator.
- 💡 Suggestions for improving password strength.
- 🔒 SHA-256 hash generation.
- 🖥️ Interactive web interface.
- 🎨 User-friendly design.

## ⚙️ How It Works

1. The user enters a sample password into the application.
2. The program checks the password against predefined security conditions.
3. Each satisfied condition contributes to the strength score.
4. The application displays the password strength category.
5. Missing conditions and improvement suggestions are displayed.
6. The application generates a SHA-256 hash of the entered text.

## 📊 Password Strength Criteria

| Criteria | Description |
|---|---|
| Length | Checks whether the password contains at least 8 characters. |
| Uppercase | Checks for at least one uppercase letter. |
| Lowercase | Checks for at least one lowercase letter. |
| Number | Checks for at least one numeric digit. |
| Special Character | Checks for at least one special character. |

The application evaluates these conditions and calculates a strength score according to the implemented validation rules.

## 🗂️ Project Structure

```text
Experiential-Learning-Py/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── passAnalyser.pdf
```

*Note: Keep only the filenames that actually exist in your GitHub repository.*

## 🚀 Installation and Execution

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/ruchhiiii/Experiential-Learning-Py.git
```

### Step 2: Open the Project Folder

```bash
cd Experiential-Learning-Py
```

### Step 3: Install the Required Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python -m streamlit run streamlit_app.py
```

The application will open in your web browser.

## 🧪 Testing

The application can be tested using sample passwords with different lengths and character combinations.

| Test Case | Expected Result |
|---|---|
| Short password | A lower strength score is expected. |
| Password containing only lowercase letters | Missing conditions should be identified. |
| Password containing uppercase and lowercase letters | The score should reflect the satisfied conditions. |
| Password containing numbers and special characters | Additional conditions should be satisfied. |
| Password satisfying all five conditions | The highest strength score should be achieved. |

*Actual results depend on the validation and scoring logic implemented in the application.*
## 🚀 Deployment

The Password Strength Analyzer is deployed using Streamlit Community Cloud, allowing users to access the application through a web browser.

### 🌐 Live Application

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://password-strength-analyzer-ruchika.streamlit.app/)

🔗 **Live Demo:** [Password Strength Analyzer](https://password-strength-analyzer-ruchika.streamlit.app/)

### Deployment Platform
- **Platform:** Streamlit Community Cloud
- **Framework:** Streamlit
- **Source Code:** [GitHub Repository](https://github.com/ruchhiiii/Experiential-Learning-Py)

## 🔒 Security Considerations

This project demonstrates basic password strength analysis and SHA-256 hashing for educational purposes.

SHA-256 alone is not recommended for storing real user passwords because it is a general-purpose hash function rather than a dedicated password-hashing algorithm. Real applications should use suitable password-hashing algorithms such as Argon2id, bcrypt, or scrypt.

**Important:** Use sample passwords while testing this educational application. Do not enter passwords used for your actual accounts.

## 🔮 Future Enhancements

- Add more advanced password validation rules.
- Improve the user interface.
- Add more comprehensive test cases.
- Deploy the application online.
- Improve password security recommendations.
- Explore dedicated password-hashing techniques.

## 📝 Conclusion

The Password Strength Analyzer demonstrates how Python can be used to evaluate password strength and generate hash values. The project combines password validation, conditional statements, character checking, and hashing with an interactive Streamlit interface.

It provides practical experience in Python programming, web application development, and basic password security concepts.

## 🔗 Project Repository

Explore the source code on GitHub:

[**Password Strength Analyzer – GitHub Repository**](https://github.com/ruchhiiii/Experiential-Learning-Py)

## 🌐 Live Application

The live application link will be added after successful deployment.

---

⭐ **Developed as part of an Experiential Learning Project.**
