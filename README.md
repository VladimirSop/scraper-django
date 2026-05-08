#  LinellaLocal

LinellaLocal is a Django web application for searching and browsing products from the Linella store.

The project automatically parses products from the Linella website, stores them in a database, and provides a convenient interface for searching, sorting, and browsing products.

---

#  Features

-  Product Search
-  Product List with Pagination
-  Sorting by Price and Name
-  User Registration and Authorization
-  Django Admin Panel
-  Docker + Docker Compose Support
-  Linella Product Parser
-  Responsive Bootstrap Interface

---

# Technologies

- Python 3
- Django
- SQLite
- Bootstrap 5
- Docker
- Docker Compose
- BeautifulSoup4
- Requests

---

# Project Structure

```bash
LinellaLocal/
│
├── scraper/ # Main Application
├── users/ # Users and Authorization
├── command/
│ └── parse_linella.py # Linella website parser
│
├── manage.py
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

# Installation without Docker

## 1. Clone the repository

```bash
git clone https://github.com/VladimirSop/scraper-django
cd LinellaLocal
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply migrations

```bash
python manage.py migrate
```

---

## 5. Start the server

```bash
python manage.py runserver
```

---

# Run via Docker

## Run the project

```bash
docker compose up --build
```

After launch, the site will be available at:

```bash
http://127.0.0.1:8000/
```

---

# Product parser

The parser is located in:

```bash
command/parse_linella.py
```

It automatically collects products from the Linella website and writes them to the database.

## Running the parser

```bash
python command/parse_linella.py
```

---

# Project Author

Vladimir Șop

---

# Future Plans

- Favorites
- Cart
- Product Rating
- Categories
- Filters
- AJAX Search
- Deploy

---

#  License
