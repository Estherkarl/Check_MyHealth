# CheckMyHealth

CheckMyHealth is a user-friendly web application designed to help individuals identify potential health conditions based on their symptoms. Whether you're feeling under the weather or just curious about certain symptoms, CheckMyHealth provides a streamlined and easy-to-use interface to get preliminary insights about your health.

## Features
- **Symptom Checker**: Input symptoms via a user-friendly form or select from a comprehensive list of common symptoms.
- **Comprehensive Database**: Cross-checks symptoms with a list of common health conditions.
- **Instant Diagnosis Suggestions**: Get potential conditions or illnesses based on the symptoms provided.
- **Responsive Design**: Works seamlessly across devices, providing an optimized experience on desktop, tablet, and mobile.

## Technologies Used
- **Python**: Backend logic and health condition analysis
- **Django**: Web framework for handling routing, form processing, and the overall structure.
- **HTML/CSS**: Front-end design for user-friendly interaction.
- **SQLite**: Database for storing symptoms and conditions.
- **Bootstrap**: For responsive, modern design elements.

## How to Run the Project
### Clone the Repository:
```bash
git clone https://github.com/Estherkarl/CheckMyHealth.git
cd CheckMyHealth
 ```
### Set up a Virtual Environment:
```bash
 python3 -m venv env
 source env/bin/activate  # On Windows: env\Scripts\activate
 ```
### Install Dependencies:
```bash
pip install -r requirements.txt
 ```
### Run Database Migrations:
```bash
python manage.py migrate
 ```
### Run the Server:
```bash
python manage.py runserver
 
Open your browser and go to http://127.0.0.1:8000/diagnose/ to use CheckMyHealth.
