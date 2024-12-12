# 📚 Campus Connect

# 🌐 Live Site
Check out the live site: [Campus Connect](https://campusconnect0.pythonanywhere.com/)

Welcome to **Campus Connect**, a comprehensive platform designed to streamline campus activities, announcements, and events. This project is built using Django and integrates various features to enhance the campus experience.

# 🌟 Features

- 📢 **Announcements**: Post and view campus-wide announcements.Which gets auto deleted in 14 days automatically. So that your space is utilised properly.
- 📄 **Pagination**: Efficiently navigate through lists of announcements as in one page only 5 posts are shown, also if you click on username - you get all the announcements that user made which is paginated too.
- 🎉 **Events**: Create and manage campus events- View via calender what events are there and you can schedule one too with categories of cultural/technical/sports/other types.
- 🌐 **Google Login**: One Tap Easy login/Sign up with Google integration.
- 🔒 **User Authentication**: Secure login and registration using Django AllAuth.
- 🖼️ **Profile Management**: Update and manage user profiles with profile pictures and bios.For every new user there is default picture and logo which can be changed.
- 🎓 **Placements**: Information and updates about placement opportunities.
- 📊 **Responsive Design**: Mobile-friendly and responsive design using Bootstrap.
  - **About College**: Learn about the college's mission, vision, and facilities.
  - **Cultural Event**: Explore various cultural events and activities.
  - **Technical Event**: Discover technical events, workshops, and clubs.
  - **Sports Event**: Stay updated on sports events and competitions.
  - **Habba Event**: Get details about the annual college fest conducted.
- 📧 **Email Verification**: Secure email verification for user accounts.
  

## 🛠️ Setup Instructions

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.10+
- PostgreSQL (if using PostgreSQL)
- Virtualenv

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chaitra-adiga/campus_connect.git
   cd campus_connect
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - If using SQLite (default):
     ```bash
     python manage.py migrate
     ```

   - If using PostgreSQL, update `DATABASES` in `settings.py` and then:
     ```bash
     python manage.py migrate
     ```

5. **Create a .env file**:
   ```plaintext
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

6. **Load environment variables**:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

7. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development**

server:
   ```bash
   python manage.py runserver
   ```
9. **Media Files**
- Create `media` directory in project root
- Add default profile picture as `media/default.png`
- Media files are not version controlled

### 📂 Directory Structure

```plaintext
campus_connect/
├── announcements/  #app
├── bulletin/       #app
├── campus_connect/ #main project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
│   └── default.png
├── templates/
│   └── base.html
├── manage.py
├── requirements.txt
└── .env
```

### 🚀 Deployment

For deployment, follow these additional steps:

1. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

2. **Configure your web server** (e.g., Gunicorn, Nginx).

3. **Set up environment variables** on your server.

4. **Run migrations** on the production database:
   ```bash
   python manage.py migrate
   ```

## 📧 Contact

For any questions or support, please contact [itsca03@gmail.com](mailto:itsca03@gmail.com).

---

Enjoy using **Campus Connect**! 🎉

This README file includes an overview of the project, features, setup instructions, and deployment steps.

