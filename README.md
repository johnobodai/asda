# ASDA Learning Center Website

This is the repository for the ASDA Learning Center website, built using FastAPI.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## About

The ASDA Learning Center website is designed to showcase information about the school, its courses, staff, blog, and contact details. The website is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- Responsive web design
- Dynamic content rendering with Jinja2 templates
- Modular routing and structure using FastAPI
- Navigation between home, courses, about, enroll, blog, staff, and contact pages

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [FastAPI](https://fastapi.tiangolo.com/) and dependencies (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/asda-learning-center.git

Usage

    Run the FastAPI application:

    bash

    uvicorn main:app --reload

    Open your browser and go to http://127.0.0.1:8000 to view the ASDA Learning Center website.

Folder Structure

.
├── app
│   ├── dependencies.py
│   ├── init.py
│   ├── pycache
│   │   └── init.cpython-3X.pyc
│   └── routes
│   ├── about.py
│   ├── admin.py
│   ├── blog.py
│   ├── contact.py
│   ├── courses.py
│   ├── enroll.py
│   ├── home.py
│   ├── init.py
│   ├── pycache
│   │   ├── about.cpython-3X.pyc
│   │   ├── admin.cpython-3X.pyc
│   │   ├── blog.cpython-3X.pyc
│   │   ├── contact.cpython-3X.pyc
│   │   ├── courses.cpython-3X.pyc
│   │   ├── enroll.cpython-3X.pyc
│   │   ├── home.cpython-3X.pyc
│   │   └── staff.cpython-3X.pyc
│   └── staff.py
├── data
│   ├── courses.json
│   └── students.json
├── main.py
├── models
│   ├── course.py
│   └── student.py
├── pycache
│   └── main.cpython-3X.pyc
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   ├── img
│   │   ├── background1.png
│   │   └── background.png
│   └── js
├── templates
│   ├── about.html
│   ├── admin.html
│   ├── admissions.html
│   ├── base.html
│   ├── blog.html
│   ├── confirmation.html
│   ├── contact.html
│   ├── courses.html
│   ├── enroll.html
│   ├── home.html
│   ├── index.html
│   └── staff.html
└── utils
├── auth.py
└── database.py


Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.
