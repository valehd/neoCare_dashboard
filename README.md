# NeoCare Dashboard

## Maternal & Neonatal Healthcare Analytics Platform

NeoCare Dashboard is a healthcare analytics application designed to monitor and analyze maternal and neonatal clinical data through interactive dashboards and visualizations.

The project models the complete maternal-neonatal care pathway, from pregnancy and labor to newborn adaptation and neonatal outcomes.

Developed as part of my transition from Neonatal Intensive Care Unit (NICU) Midwife to Software Engineering, NeoCare combines healthcare domain expertise with data analytics and software development.

---
## Live Demo

https://tu-app.streamlit.app

## Features

### Overview Dashboard

* Maternal, pregnancy, delivery, and newborn KPIs
* Delivery type distribution
* Birth weight and APGAR score indicators
* Executive summary of healthcare activity

### Maternal Analysis

* Maternal age distribution
* Blood type distribution
* Maternal risk factors analysis
* Interactive filtering by age, condition, and blood type

### Pregnancy Management

* Gestational age analysis
* Prenatal control monitoring
* Multiple pregnancy tracking
* Pregnancy condition distribution

### Labor & Delivery Analytics

* Delivery type analysis
* Rupture of membranes monitoring
* Clinical intervention indicators
* Birth outcome analysis

### Newborn Analysis

* Birth weight distribution
* APGAR score monitoring
* Sex distribution
* Gestational age assessment

### Neonatal Monitoring

* Vital signs monitoring
* Heart rate trends
* Respiratory rate analysis
* Temperature monitoring
* Oxygen saturation tracking
* Neonatal adaptation indicators

### Neonatal Outcomes

* Neonatal destination analysis
* Hospital admission tracking
* Outcome monitoring and visualization

---

## Technology Stack

### Programming & Data

* Python
* Pandas
* SQL

### Dashboard & Visualization

* Streamlit
* Plotly

### Database

* MySQL

### Version Control

* Git
* GitHub

---

## Database Design

The system is built on a relational database designed to represent the maternal-neonatal care process.

### Main Entities

* Mother
* Pregnancy
* Delivery
* Newborn
* Neonatal Control
* Neonatal Outcome

---

## Project Structure

```text
neoCare_dashboard/

├── Overview.py
├── pages/
│   ├── Mothers.py
│   ├── Pregnancy.py
│   ├── Deliveries.py
│   ├── Newborn.py
│   ├── Monitoring.py
│   └── Outcomes.py
│
├── database/
│   ├── connection.py
│   └── queries/
│
├── components/
│   ├── theme.py
│   ├── sidebar.py
│   └── footer.py
│
├── assets/
│   ├── logo/
│   └── screenshots/
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## Screenshots

### Overview

*Add screenshot here*

### Maternal Analysis

*Add screenshot here*

### Labor & Delivery

*Add screenshot here*

### Neonatal Monitoring

*Add screenshot here*

---

## Installation

### Clone repository

```bash
git clone https://github.com/valehd/neoCare_dashboard.git
cd neoCare_dashboard
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file based on `.env.example`.

```env
DB_HOST=localhost
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=maternal_database
```

### Run application

```bash
streamlit run Overview.py
```

---

## Future Improvements

* User authentication and authorization
* Data export to Excel and PDF
* Clinical report generation
* Advanced healthcare KPIs
* Predictive analytics
* Deployment to cloud infrastructure

---

## Author

### Valentina Hernández

Former NICU Midwife transitioning into Software Engineering.

Interested in:

* Healthcare Technology
* Health Informatics
* Data Analytics
* SQL & Database Development
* Digital Health Transformation
