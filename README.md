# Appointment Booking System

This is a Flask-based appointment booking system. Users can book appointments by selecting available time slots and services. Admin users can view all booked appointments.

## Features

- User authentication (login/logout)
- Calendar to select appointment dates
- Time slots selection
- Booking multiple services
- Admin dashboard to view all appointments
- Responsive design for mobile devices

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/maikl88/flask_appointment.git
   cd flask_appointment
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate  # For Windows
   # source venv/bin/activate  # For MacOS/Linux
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Add services:**

   ```bash
   python add_services.py
   ```

6. **Initialization DB**
   ```bash
   python init_db.py
   ```
username `admin` and the password `admin`. **Make sure to change the password after the first login.**

7. **Run the Flask project:**

   ```bash
   python run.py
   ```

## Usage

- **Booking Appointments:**

  - Enter your name.
  - Select a date from the calendar.
  - Choose an available time slot.
  - Select one or more services.
  - Click the "Book" button to confirm your appointment.

- **Admin Dashboard:**
  - Log in with the admin credentials.
  - Navigate to the `/appointments` URL to view all booked appointments.

## File Structure

```plaintext
flask_appointment/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── appointments.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
├── migrations/
├── venv/
├── init_db.py
├── config.py
├── requirements.txt
└── README.md
```
