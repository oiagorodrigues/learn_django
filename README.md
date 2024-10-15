# Learning django

## Project Overview

Monolithic web application built using Django as a hands-on self-learning project. It's going to manage a invoice generation system to help creating invoices for various clients.

Its main features are:

- [ ] Manage external clients
- [ ] Manage invoices
- [ ] Manage expenses (taxes, personnel, etc)
- [ ] Manage withdrawals, transactions (using third party payment systems)
- [ ] Social login

## Installation

> Be sure to have Python 3.12.1 and Django 5.1 installed

```bash
# Clone the repository
git clone https://github.com/oiagorodrigues/learn_django.git

# Navigate to the project directory
cd learn_django

# Create a Python virtual environment https://docs.python.org/3/library/venv.html
mkdir .venv && python3 -m venv ./venv

# Install dependencies
pip install -r requirements.txt

# Add a sqlite database to the root
touch db.sqlite3
```

## Usage

Instructions on how to use the project.

```bash
# run the dev server
python3 manage.py runserver

# detects changes on models and create migrations
python3 manage.py makemigrations

# updates the database table schemas with the migrations
python3 manage.py migrate
```

## Learning Path

- [x] MVT structure
- [x] URLConf
- [x] Models
- [x] Views
- [x] Templates
- [ ] Error handling
- [ ] Forms
- [ ] Authentication
- [ ] Authorization
- [ ] Styling
- [ ] CI/CD

#### Learning Path Improvements

- [ ] Moving to Rest APIs
- [ ] Integration with a FE user interface javascript library (Vue, React, etc)

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Coursera's Meta Back-End Developer Specialization](https://www.coursera.org/specializations/meta-back-end-developer)
