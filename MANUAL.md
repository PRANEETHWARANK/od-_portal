# Amrita OD Portal — User Manual & Operations Guide

The **Amrita OD Portal** is a web-based workflow application designed to streamline the request, tracking, verification, and approval processes of student **On-Duty (OD)** applications. The portal establishes a structured multi-level approval pipeline involving **Advisors**, **Chairpersons**, and the **Principal**.

---

## 📋 System Requirements

To host or run the application locally or in a production environment, ensure the following dependencies are installed:

| Requirement | Details |
| :--- | :--- |
| **Python** | Version `3.10` or higher |
| **Framework** | Django `5.x` |
| **Primary Database** | MySQL (Recommended, default configured via port `3306`) |
| **Fallback Database** | SQLite (Utilized automatically if MySQL settings are missing/defaulted) |
| **Core Libraries** | `django-environ` / `python-dotenv` |
| **PDF Generation** | `reportlab` |
| **Excel Uploads** | `openpyxl` (Required for importing student rosters via Excel) |
| **SMTP Server** | An active email SMTP relay (e.g., Gmail) to send parent notification emails |

---

## 🛠️ Setup & Execution Procedure

1. **Clone the Repository** and navigate to the project directory.
2. **Environment Configuration**: Create a `.env` file in the project root with the following variables:
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   
   DB_NAME=amrita_od_db
   DB_USER=root
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_gmail_app_password
   
   STAFF_REGISTRATION_KEY=avvpnagercoil
   ```
3. **Install Dependencies**:
   ```bash
   pip install django python-dotenv reportlab openpyxl mysqlclient
   ```
4. **Database Migrations & Startup**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   *Access the web panel at: `http://127.0.0.1:8000/`*

---

## 🔄 Workflow & User Roles (How to Use)

The application implements four distinct user levels. Each has its specific interface and privileges:

### 1. 🎓 Student Workflow
* **Registration / Login**: Students can register with their roll number, department, email, parent's email, and assigned Advisor & Chairperson.
* **Apply for OD (`/od/apply/`)**:
  * Input **From Date**, **To Date**, and **Reason**.
  * Upload a scanned/digital **Proof** (PDF or Image format).
* **Track History & Evidence (`/od/history/`)**:
  * View current approval states (Advisor ➡️ Chairperson ➡️ Principal).
  * **Event Evidence Upload**: Once an OD is fully approved, students must upload participation evidence (e.g., certificate).
  * ⚠️ *Note: Evidence uploaded will be automatically purged after 14 days.*

### 2. 🧑‍🏫 Advisor Workflow
* **Dashboard Overview**: Access assigned students, pending review alerts, and historical activity.
* **Student Roster Upload (`/accounts/upload-students/`)**: Bulk import student records using a CSV or Excel (`.xlsx`) sheet. Expected columns: `roll_number`, `email`, `name`, `parent_email`, and `department`.
* **Actioning Requests**: Review student applications, add remarks, and either **Approve** (forwarding to Chairperson) or **Reject** the OD application.

### 3. 🏢 Chairperson Workflow
* **Approval Step 2**: Receives applications that have been approved by the Advisor.
* **Roster Upload**: Identical bulk upload privileges to configure rosters for the department.
* **Actioning Requests**: Review advisor remarks, append chairperson feedback, and either **Approve** (forward to Principal) or **Reject**.

### 4. 🎓 Principal Workflow
* **Final Approval Step 3**: Receives requests approved by both the Advisor and the Chairperson.
* **Actioning Requests**: Review application details and previous remarks. Make the final **Approve** or **Reject** decision.
* **Parent Notifications**: Upon the Principal's approval, the portal automatically triggers an email notification to the student's registered parent email address.

---

## 📊 Exporting Reports (For Staff)
Staff users can generate and download summarized records of OD applications:
* **Format Options**: Available in **CSV** and **PDF** structures.
* **Filtering**: Filter records by month and duration (e.g., requests lasting $\ge$ 5 days).
