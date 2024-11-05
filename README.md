# L7_python_proj

# Chocolate House Application

Welcome to the Chocolate House Application! This is a web application designed for managing seasonal chocolate flavors, ingredient inventory, and customer suggestions. It is built using Flask and SQLite, providing a simple interface to interact with chocolate offerings.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Testing the Application](#testing-the-application)
- [Database Implementation](#database-implementation)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Features
- Manage seasonal flavor offerings.
- Track ingredient inventory.
- Collect customer flavor suggestions and allergy concerns.

## Technologies Used
- **Python**: Backend logic.
- **Flask**: Web framework.
- **SQLite**: Database management.
- **HTML/CSS**: Frontend design.
- **Docker**: Containerization.

## Getting Started

### Prerequisites
Ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://www.docker.com/get-started) (optional, if you prefer to run in a container)

### Installing Dependencies
Run the following command to install required Python packages:


bash
pip install -r requirements.txt





Running the Application

from app import get_db_connection  
get_db_connection()  


Run the Flask Application:
python app.py





# Step 1: Navigate to Your Project Directory
Use the cd command to change your directory to the location of your Chocolate House project. For example:
cd C:\Users\91761\OneDrive\Desktop\chocolate1
# Step 2: Create a Virtual Environment
To create a virtual environment, use the following command:
python -m venv env
This command creates a new directory named env in your project folder, which contains the Python interpreter and libraries for your virtual environment.
# Step 3: Activate the Virtual Environment
.\env\Scripts\activate
After activation, your command prompt should change to indicate that the virtual environment is active, typically showing (env) at the beginning of the line.
# Step 4: Install Required Packages
While in the activated virtual environment, install the necessary packages for your project using pip:
This command will install Flask and Flask-SQLAlchemy, which are required for your application to run.
# Step 5: Run the Application
Now that you have installed the required packages, you can run your application. Use the following command:
python app.py
# Step 6: Open Your Browser
Once the application is running, you will see output indicating that the server is running, such as:
Running on http://127.0.0.1:5000





Testing the Application
Test Steps
Navigate to the home page to ensure it loads correctly.

Add a Flavor:

Click on the "Add Flavor" button.
Enter a flavor name and description.
Click "Add Flavor" and verify it appears in the flavor list.
View Ingredients:

Navigate to the "Inventory" page.
Add a new ingredient.
Verify that it shows up in the inventory list.
Add Customer Suggestions:

Go to the "Suggestions" page.
Submit a suggestion and verify it is recorded.
Validate Database Entries:

Use a SQLite viewer or run queries to ensure data is stored correctly.





# Use a Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

