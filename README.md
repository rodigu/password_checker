# 🔐 Password Strength Checker

[Documento em português](./README_pt.md)

A simple **Python** script that checks the strength of a password and classifies it as **Weak**, **Medium**, or **Strong**.  
Portfolio project to practice **information security concepts** and **regular expressions**.

---

## 🚀 How It Works
The password is analyzed according to the following criteria:

- **Weak**:
  - Less than 6 characters  
  - Or contains only letters or only numbers  

- **Medium**:
  - At least 6 characters  
  - Contains letters and numbers  
  - Does not include special characters  

- **Strong**:
  - At least 8 characters  
  - Contains uppercase, lowercase, numbers, and special characters  

---

## 🛠️ Technologies Used
- Python 3  
- Regular Expressions (regex)

---

## 📂 Project Structure

password_checker/
│── password_checker.py # Main code
│── README.md # Documentation
│── .gitignore # Ignored files
