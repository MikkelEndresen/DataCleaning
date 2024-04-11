# DataCleaning

A web application that processes and displays data. 
Input a .csv file and it returns the data with the correct dtypes. 
You can also manually select other dtypes if needed.
Uses React.js for the frontend. 

## Prerequisites

Make sure you have the following installed on your machine:
- Python 3.x
- Node.js
- npm

## Getting started

Follow the steps below.

First clone the github repo

### Backend

- pip install -r requirements.txt
- Create a new file in dataCleaning/myapi/ called api_keys.py and add a GOOGLE_API_KEY for the gemini LLM
- cd dataCleaning/
- python manage.py migrate
- python manage.py runserver

### Frontend
Open new terminal
- cd myapp
- npm install
- npm start
- open http://localhost:3000/


