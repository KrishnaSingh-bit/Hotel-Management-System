# 🏦 Bank Management System

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-orange)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A **Python CLI-based Bank Management System** that integrates with MySQL.  
Admins can manage accounts, loans, and feedback, while users can view and update their account information.

---

## ⚡ Features

### Admin Features
- ✅ Add new bank accounts
- ✅ View all loan details
- ✅ Update loan status
- ✅ Check loan defaulters
- ✅ View user feedback
- ✅ Add new loan accounts

### User Features
- ✅ View account details
- ✅ Update personal information (name, email, phone number, address)
- ✅ Give feedback
- ✅ View loan status

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend CLI program |
| MySQL      | Database management |
| mysql-connector-python | Python-MySQL connectivity |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/yourusername/bank-management-system.git
cd bank-management-system
```
### 2. Install Python Dependency
```
pip install mysql-connector-python
```
### 3. Setup MySQL Database
```MySql
-- Create database
CREATE DATABASE IF NOT EXISTS bank_management_system;
USE bank_management_system;

-- Create tables
CREATE TABLE IF NOT EXISTS acct_holder (
    acc_no BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    acct_holder_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(255),
    initial_balance INT NOT NULL,
    loan_taken ENUM('yes','no') DEFAULT 'no'
);

CREATE TABLE IF NOT EXISTS user_data (
    username VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    acc_no BIGINT NOT NULL,
    FOREIGN KEY (acc_no) REFERENCES acct_holder(acc_no) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS admin_data (
    username VARCHAR(50) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS loan_acct (
    acct_no BIGINT NOT NULL,
    name VARCHAR(100) NOT NULL,
    loan_amount INT NOT NULL,
    loan_type VARCHAR(50),
    status_of_loan ENUM('cleared','pending') DEFAULT 'pending',
    number_of_months_from_which_interest_is_not_paid INT DEFAULT 0,
    FOREIGN KEY (acct_no) REFERENCES acct_holder(acc_no) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS feedback (
    feedback_text TEXT NOT NULL,
    acc_no BIGINT NOT NULL,
    FOREIGN KEY (acc_no) REFERENCES acct_holder(acc_no) ON DELETE CASCADE
);

-- Optional: Add default admin
INSERT INTO admin_data (username, password) VALUES ('admin', 'admin123');

```
### 4. Run the Program
```
python bank_management_system.py
```

---

## 🧭 Usage

Admin Login: Use default credentials username: admin, password: admin123

User Login: Users must be created by the admin first

Follow the on-screen menus to navigate between functionalities.

---

## 📂 Project Structure
```
bank-management-system/
│
├── bank_management_system.py    # Main Python CLI program
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

```
## 📄 License

This project is licensed under the MIT License.

---
