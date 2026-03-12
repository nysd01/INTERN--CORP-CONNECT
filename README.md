# 🚀 Intern Corp Connect

A Django-based platform connecting companies seeking interns with talented candidates.

## ✨ Features

- 🏢 Company and intern registration with separate dashboards
- 📄 Companies can post internships and view applicants/documents
- 🧑‍💻 Interns can search/apply for internships, upload required documents
- 💬 Real-time messaging system with file/document linking
- 📊 Application tracking for both companies and interns
- 👤 Profile management for companies and interns
- 🔔 Notifications for application status and messages
- 🛡️ Admin moderation
- 🔐 Secure authentication and password reset
- 🌗 Responsive, modern UI with dark/light mode

## ⚡ Quick Start

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. **Access the app**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 📝 Usage

- 📝 Register as a company or intern.
- 🏢 Companies: Post internships and view applicants/documents at `/company/applications/`.
- 🧑‍💻 Interns: Search/apply for internships, upload documents, and chat with companies.
- 💬 Use the messaging system for real-time communication. If a message contains "attach", it links to the applicant's documents.

## 🚀 Deployment

- Ready for deployment with static/media file support and production settings.
- Configure environment variables and database for production use.

## 📄 License

MIT License
