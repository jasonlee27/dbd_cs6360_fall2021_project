# Setup&Run

For this project, we use the npm package for javascript frontend.
For running frontend application, please go to the directory /frontend
and use the following npm commands at the root directory:
cd frontend/
npm i
npm run
npm start


Afterwards, you need to open another terminal window for running
backend.
in backend/src directory there are sql files for initiallizing tables

backend/src/tables.sql: declaring the tables
backend/src/testdb.sql: initializing 5 clients, 3 traders and 1
manager

Those files are run on mysql in run.sh.

At the backend we use flask, flask-mysqldb, flask-cors and APScheduler
for python, and mysql for SQL suqeries.
The following command installs the flask family and APScheduler:
cd backend/
pip install Flask
pip install -U flask-cors
pip install Flask-MySQLdb
pip install APScheduler
bash run.sh
