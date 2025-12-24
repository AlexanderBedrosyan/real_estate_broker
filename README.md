## Real estate official app - https://stoyancherelov.com/

# Real Estate Broker

A Django-based web application for a real estate broker showcasing properties, events, investment opportunities, and client consultations.

## Features

- **Home Page**: Introduction, embedded YouTube video (mini-TV and modal), customer testimonials carousel.
- **Events**: List recent events (newest first) with detail pages.
- **Projects**: List property projects (newest first) with pagination.
- **Consultation Form**: Contact form for potential clients.
- **Invest With Me**: Information page for investment opportunities.
- **Contacts**: Display broker contact information.
- **Admin Panel**: Django admin for managing events, projects, consultations, and customers.
- **Responsive UI**: Bootstrap 5, custom CSS, smooth animations.
- **Docker Support**: Docker Compose for local/production deployment with PostgreSQL.

## Project Structure

```
real_estate_broker/
├── real_estate_broker/
│   ├── main_app/          # Core app (views, models for Event, Project, Consultation)
│   ├── account/           # User account management
│   ├── common/            # Shared templates (navbar, footer)
│   ├── settings.py        # Django settings (Postgres, static, apps)
│   ├── settings_local.py  # Local dev settings (SQLite for testing)
│   ├── urls.py            # URL routing
│   └── wsgi.py
├── templates/
│   ├── home.html
│   ├── events.html
│   ├── events_details.html
│   ├── projects.html
│   ├── consultation.html
│   ├── contacts.html
│   ├── invest_with_me.html
│   └── common/
│       ├── navbar.html
│       └── footer.html
├── static/
│   ├── styles/
│   ├── javascript/
│   │   └── home.js        # YouTube embed runtime checks, modal fullscreen
│   └── images/
│       └── logo.png
├── manage.py
├── entrypoint.sh          # Docker entrypoint (wait for DB, migrate, create superuser)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Technology Stack

- **Backend**: Django 4.x / 5.x, Python 3.10+
- **Database**: PostgreSQL 15 (production), SQLite (local dev fallback)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript (ES6+)
- **Containerization**: Docker, Docker Compose
- **Web Server (prod)**: Gunicorn / uWSGI (configured via WSGI)

## Installation & Setup

### Local Development (SQLite)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd real_estate_broker/real_estate_broker
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Use local SQLite settings**
   ```bash
   export DJANGO_SETTINGS_MODULE="real_estate_broker.settings_local"
   # On Windows PowerShell: $env:DJANGO_SETTINGS_MODULE="real_estate_broker.settings_local"
   ```

5. **Run migrations and create superuser**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver 0.0.0.0:8050
   ```

7. Open http://localhost:8050 in your browser.

### Docker Deployment (PostgreSQL)

1. **Ensure Docker Desktop is running**

2. **Create `.env` file in project root** (next to docker-compose.yml)
   ```env
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password

   DJANGO_SUPERUSER_USERNAME=your_admin_username
   DJANGO_SUPERUSER_EMAIL=your_admin_email
   DJANGO_SUPERUSER_PASSWORD=your_admin_password
   ```

3. **Build and start containers**
   ```bash
   docker compose up -d --build
   ```

4. **View logs**
   ```bash
   docker compose logs -f web
   ```

5. Open http://localhost:8050

6. **Stop containers**
   ```bash
   docker compose down -v
   ```

## Usage

- **Admin Panel**: http://localhost:8050/admin (login with superuser credentials)
- **Add Events/Projects**: Use Django admin to create Event and Project objects; they appear on the Events and Projects pages ordered newest first.
- **YouTube Video**: The mini-TV on the home page checks if the video is embeddable at runtime; if not, it shows a fallback link. Clicking opens a modal in fullscreen (where supported).
- **Consultations**: Users submit consultation requests via the /consultation form; submissions are saved to the database and viewable in admin.

## Configuration

- **Settings**: Main settings in `real_estate_broker/settings.py` (uses environment variables for DB config).
- **Local Dev**: Override with `settings_local.py` (SQLite, DEBUG=True).
- **Static Files**: Collected via `python manage.py collectstatic` (for production); served by Django dev server in local mode.
- **Favicon**: All public templates include `<link rel="icon" ... href="{% static 'images/logo.png' %}">`.

## Testing

Run Django tests (if you add test cases):
```bash
python manage.py test
```

## Troubleshooting

- **YouTube Error 153**: Video owner disabled embedding. Change the video ID in `templates/home.html` data-video-id and `static/javascript/home.js` DEFAULT_VIDEO_ID to an embeddable video.
- **Database Connection Error**: Ensure `.env` DB_HOST points to the correct service name (db for Docker Compose) or appropriate host for your database setup.
- **Port Conflict (8050)**: Stop other services using port 8050 or change the port mapping in docker-compose.yml.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is for educational/portfolio purposes.

## Contact

For questions or support, please open an issue in the repository.
