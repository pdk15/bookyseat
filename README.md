# BookMySeat – Movie Ticket Booking System

A full-stack Movie Ticket Booking System built with Django. It allows users to browse movies, select seats, book tickets, and manage their bookings through a simple and user-friendly interface.

## Features

- User Registration & Login
- Movie Listings
- Movie Details
- Theater & Show Management
- Seat Selection
- Ticket Booking
- Booking History
- User Profile Management
- Admin Dashboard
- Responsive UI

## Tech Stack

- Python
- Django
- HTML
- CSS
- Bootstrap
- JavaScript
- PostgreSQL / SQLite
- Git & GitHub

## Project Structure

```
bookmyseat/
├── accounts/
├── booking/
├── movies/
├── theater/
├── templates/
├── static/
├── media/
├── requirements.txt
└── manage.py
```

## Installation

### Clone the repository

```bash
git clone https://github.com/pdk15/bookmyseat.git
cd bookmyseat
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

## Future Improvements

- Online Payment Integration
- QR Code Ticket Generation
- Email Ticket Confirmation
- Movie Reviews & Ratings
- Booking Cancellation
- Recommendation System
- Multi-Theater Support

## Author

**Pranav Khanolkar**

GitHub: https://github.com/pdk15
