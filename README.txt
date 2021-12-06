# Set up

For this project, we use the npm package for javascript frontend.
For running frontend application, please go to the directory /frontend
and use the following npm commands at the root directory:
cd frontend/
npm i
npm run
npm start

Afterwards, you need to open another terminal window for running
backend.

At the backend we use flask, flask-mysqldb, flask-cors
The following command installs the flask family and APScheduler:
cd backend/
pip install Flask
pip install -U flask-cors
pip install Flask-MySQLdb
pip install APScheduler
bash run.sh
