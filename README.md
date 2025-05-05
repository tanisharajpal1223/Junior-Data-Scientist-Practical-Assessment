# Junior-Data-Scientist-Practical-Assessment
This project showcases an end-to-end solution to manage and analyze patient data in a healthcare setting. The solution includes database design, backend API implementation, data analysis, and a frontend dashboard for interacting with the data.

Project Structure

Part 1: Database & Backend Engineering
Relational database schema for storing patient data.
Backend services built with Flask to expose key data and insights through APIs.
Part 2: Data Science & Analytics
Data exploration, insights generation, and visualization using patient vitals and other healthcare data.
Key insights to support clinical decision-making.
Part 3: Frontend Dashboard
Full-stack web application built using React to visualize patient data and trends.
Setup Instructions

Part 1: Database & Backend Setup
Clone the Repository:
Clone the repository to your local machine:
git clone https://github.com/tanisharajpal1223/healthcare-data-science.git
cd healthcare-data-science
Set Up the Database:
You need a MySQL database to store the patient data. Create a new database (e.g., hospital_db) and configure your MySQL connection.
Install Backend Dependencies:
Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
Install the required Python packages:
pip install -r requirements.txt
Database Initialization:
Open a Python shell and run the following to create the necessary tables in your database:
from app import db
db.create_all()
Run the Flask App:
Start the Flask application:
python app.py
The Flask server will run on http://localhost:5000.
Part 2: Data Science & Analytics Setup
Install Jupyter Notebook (if not already installed):
pip install notebook
Install Required Libraries:
Make sure the following Python libraries are installed for data analysis:
pip install pandas matplotlib seaborn
Running the Jupyter Notebook:
Open the data_analysis.ipynb Jupyter notebook.
Ensure the patient_data.xlsx and vitals_data.xlsx files are available in your working directory.
Run the notebook to explore the data and generate insights.
Part 3: Frontend Dashboard Setup
Install Node.js:
Ensure that Node.js and npm (Node Package Manager) are installed on your machine.
You can download and install Node.js from here.
Install Frontend Dependencies:
Navigate to the frontend directory and install the required dependencies:
cd frontend
npm install
Run the React App:
Start the React development server:
npm start
The React app will be accessible at http://localhost:3000.
Key Features

Backend API:
GET /patients: Fetches a list of all patients.
GET /patients/{id}: Fetches detailed information for a specific patient by ID.
POST /patients: Adds a new patient to the database.
Data Analysis:
Analysis of vital data including blood pressure, heart rate, and temperature.
Identifies trends in the data, such as high-risk patients with abnormal vitals.
Visualizations of key trends and correlations between various health metrics.
Frontend Dashboard:
Displays a list of patients.
Interactive table to view patient details.
Fetches data dynamically from the Flask backend.
SQL Schema Design

The relational database includes the following tables:

patients: Stores basic information about patients (e.g., name, gender, date of birth).
vitals: Stores vital data such as blood pressure, heart rate, and temperature for each patient.
followup: Stores information about follow-up appointments for patients.
delivery: Stores information related to patient deliveries (e.g., delivery date, method, complications).
Each table is normalized, and foreign keys are used to link data across tables.

Insights & Analysis

Age Distribution: Visualized the age distribution of patients in the dataset.
Correlation Analysis: Performed correlation analysis between vital signs (e.g., blood pressure, heart rate).
High-Risk Patient Detection: Identified patients at high risk based on abnormal blood pressure and heart rate data.
Actionable Insights: Recommendations for clinical decision-making, such as follow-up scheduling for high-risk patients
