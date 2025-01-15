# 🛠️ Sharp-A-Knife Co. API

Welcome to the **Sharp-A-Knife Co. API**! This application provides a platform to manage knife sharpening orders, customer profiles, and pricing information. Follow the instructions below to set up and run the app locally.

---

## 📋 **Table of Contents**
- [Requirements](#️-requirements)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Running the Application](#-running-the-application)
- [Testing](#-testing)
- [API Documentation](#-api-documentation)

---

## 🛠️ **Requirements**
Before running the app, ensure you have the following installed on your system:
- Python 3.9+
- pip (Python package manager)
- PostgreSQL (if using a database)
- Git

---

## 📥 **Installation**

1. Clone the repository:
   ```bash
   git clone https://git@github.com:An-him/Kisu.git
   ```
2. Create the virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🌐 **Environment Setup**
1. Create a .env file in the root directory and add the following environment variables:
   ```
   SECRET_KEY=SECRET_KEY
   DEBUG=
   JWT_SECRET_KEY=JWT_SECRET_KEY
   ```
2. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

---

## 🚀 **Running the Application**
1. Ensure your virtual environment is activated:
   ```bash
   source venv/bin/activate
   ```
2. Export the API as the default FLASK_APP:
   ```bash
   export FLASK_APP=api
   ```
   or run the server from python:
   ```bash
   python runserver.py
   ```

---

## 🧪 **Testing**
   ```bash
   pytest
   ```

---

## 📄 **API Documentation**
The API documentation is available at http://127.0.0.1:5000/swagger/ once the server is running.

---

## 🛠️ **Routes to Implement**

| METHOD | ROUTE                     | FUNCTIONALITY                  | ACCESS         |
|--------|---------------------------|--------------------------------|----------------|
| POST   | `/auth/signup`            | Register new User              | Public         |
| POST   | `/auth/login`             | User login and authentication  | Public         |
| POST   | `/customers/register`     | Register a new customer        | Public         |
| GET    | `/customers/{customer_id}`| Retrieve customer details      | Authenticated  |
| POST   | `/orders`                 | Create a new sharpening order  | Authenticated  |
| GET    | `/orders/{order_id}/status`| Check order status             | Authenticated  |

**Notes:**
- **Access Levels:**
  - **Public:** No authentication required.
  - **Authenticated:** Requires a valid authentication token.