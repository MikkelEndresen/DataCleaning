# DataCleaning

A web application that processes and displays data, focusing on data type inference and conversion for datasets using Python and Pandas.

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


