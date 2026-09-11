# 🚀 Python REST API Client

A Python application that consumes the **GitHub REST API**, processes JSON responses, handles API failures, and displays GitHub user information.

Built using **Python + Requests + GitHub REST API**.

---

## 🧠 Overview

This application allows users to:

- Enter a GitHub username
- Fetch user information using the GitHub REST API
- Process the JSON response
- Display useful user details
- Handle invalid usernames and API failures
- Run automated tests using Pytest

### Example

**Input**

```text
Enter GitHub username: Dhatchayani11
```

**Output**

```text
GitHub User Information
-----------------------
Username: Dhatchayani11
Name: None
Public Repositories: 4
Followers: 0
Following: 0
Profile: https://github.com/Dhatchayani11
```

### System Flow

```text
User Input
    ↓
Python Application
    ↓
GitHub REST API
    ↓
JSON Response
    ↓
Process JSON Data
    ↓
Display User Information
```

---

## 🛠 Tech Stack

- Python
- REST API
- JSON
- Requests
- Pytest
- Git & GitHub

---

## 🔐 Features

- GitHub REST API integration
- JSON response processing
- HTTP status code handling
- Invalid user handling
- Network/API error handling
- Automated tests using Pytest
- Virtual environment support

---

## ⚙️ Setup & Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Dhatchayani11/python-rest-api-project.git
cd python-rest-api-project
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Application

```bash
python main.py
```

Enter a GitHub username when prompted.

Example:

```text
Enter GitHub username: octocat
```

---

## 🧪 Run Tests

Run the automated tests using:

```bash
pytest
```

The test suite covers:

- Successful GitHub API response
- Valid JSON response processing
- Invalid GitHub username handling

---

## ❌ Error Handling

The application handles common API failures such as:

### User Not Found

```text
Error: GitHub user not found
```

### API Failure

```text
Something went wrong: API request failed
```

This prevents the application from crashing unexpectedly when an API request fails.

---

## 📁 Project Structure

```text
python-rest-api-project/
│
├── main.py
├── api.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── tests/
    └── test_api.py
```

### File Responsibilities

| File               | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `main.py`          | Handles user input and displays API results |
| `api.py`           | Handles GitHub API requests and errors      |
| `requirements.txt` | Lists project dependencies                  |
| `.gitignore`       | Excludes unnecessary files from Git         |
| `test_api.py`      | Contains automated tests                    |
| `README.md`        | Project documentation                       |

---

## 🎯 Learning Outcomes

This project demonstrates the fundamentals of building a Python API-consuming application:

- Making REST API requests using Python
- Understanding HTTP status codes
- Working with JSON responses
- Handling API and network failures
- Writing basic automated tests
- Managing Python dependencies
- Using virtual environments
- Structuring a Python project
- Using Git and GitHub for version control

---

## 🚀 Future Improvements

Possible enhancements include:

- Display additional GitHub user information
- Add repository information
- Add API timeout handling
- Add logging
- Add API response mocking for tests
- Build a simple web interface

---

📜 **License**

This project is for educational and portfolio purposes.
