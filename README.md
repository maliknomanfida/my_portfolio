# Personal Portfolio Website

A clean, responsive portfolio website built with **Django**, showcasing projects, skills, and a working contact system.

## Key Features
*   **Home Page:** Introduction, About Me, Skills, and Career Goal sections
*   **Projects Page:** Showcases multiple projects with images, descriptions, and technologies used
*   **Contact System:** Functional contact form that stores messages in a SQLite database
*   **Admin Panel:** Built-in Django Admin to manage projects and contact messages

## Tech Stack
*   **Backend:** Python, Django
*   **Database:** SQLite
*   **Frontend:** HTML5, CSS3, Django Templates

## Getting Started

1. Clone the repo: git clone https://github.com/maliknomanfida/my_portfolio.git

2. Navigate to the project folder: cd my_portfolio/portfolio_project

3. Create and activate a virtual environment: python -m venv myenv then myenv\Scripts\activate

4. Install requirements: pip install -r requirements.txt

5. Run migrations: python manage.py migrate

6. Create a superuser: python manage.py createsuperuser

7. Run the project: python manage.py runserver

8. Open in browser: http://127.0.0.1:8000/