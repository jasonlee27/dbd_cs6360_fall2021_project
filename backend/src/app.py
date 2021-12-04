from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_cors import CORS

from macros import Macros
from utils import Utils
from database import Database

import MySQLdb.cursors

# import package for scheduler
# import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)
app.secret_key = Macros.SECRETE_KEY

# DB connection details
# app.config['MYSQL_HOST'] = Macros.MYSQL_HOST
app.config['MYSQL_USER'] = Macros.MYSQL_USER
# app.config['MYSQL_PASSWORD'] = Macros.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Macros.MYSQL_DB #str(Macros.DB_FILE)

mysql = MySQL(app)
# Macros.DB_DIR.mkdir(parents=True, exist_ok=True)

def update_level():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    Database.update_level(cursor, mysql)
    cursor.close()
    msg = "User level successfully updated."
    return

scheduler = BackgroundScheduler()
scheduler.add_job(func=update_level, trigger='cron', day='1st mon')

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
#     return response

@app.route("/status", methods=['GET'])
def status():
  return "running"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # test id
    # clientid: jasonlee123
    # password: password
    msg = ''
    account_info = None
    if request.method =='POST' and \
       'userid' in request.form and \
       'password' in request.form:
        userid = request.form["userid"]
        password = request.form["password"]
        hash_userid = Utils.hashing(userid)
        hash_password = Utils.hashing(password)
        
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        account_info = Database.user_exists_in_db(cursor, mysql, hash_userid, hash_password=hash_password)
        if account_info:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['userid'] = hash_userid
            session['user_type'] = account_info["user_type"]
            msg = "Successfully logged in!"
        else:
            msg = 'Incorrect username/password!'
        # end if
        cursor.close()
    # end if
    print(msg)
    return jsonify(
        msg=msg,
        account_info=account_info
    )

# http://localhost:5000/api/logout
# This will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('userid', None)
    
    msg = 'Successfully logged out'
    return jsonify(
        msg=msg
    )

# http://localhost:5000/api/register
# this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = 'No input parameters'
    #register_html = Macros.FRONTEND_DIR / 'register.html'
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and \
       'userid' in request.form and \
       'password' in request.form and \
       'email' in request.form:
        
        # Create variables for easy access
        userid = request.form['userid']
        password = request.form['password']
        hash_userid = Utils.hashing(userid)
        hash_password = Utils.hashing(password)
        user_type = request.form["usertype"]
        user_info = None
        if user_type=="client":
            # client info
            user_info = {
                "user_type": user_type,
                "userid": hash_userid,
                "password": hash_password,
                "register_date": Utils.get_cur_time(),
                "firstname": request.form['firstname'],
                "lastname": request.form['lastname'],
                "address1": request.form['address1'],
                "address2": request.form['address2'],
                "city": request.form['city'],
                "zipcode": request.form['zipcode'],
                "state": request.form['state'],
                "cphone": request.form['cphone'],
                "phone": request.form['phone'],
                "email": request.form['email'],
                "level": "silver",
                "bitcoin": 0.0,
                "flatcurrency": 0.0
            }
        elif user_type=="trader":
            # trader info
            user_info = {
                "user_type": user_type,
                "userid": hash_userid,
                "password": hash_password,
                "bitcoin": 0.0,
                "flatcurrency": 0.0
            }
        elif user_type=="manager":
            # trader info
            user_info = {
                "user_type": user_type,
                "userid": hash_userid,
                "password": hash_password,
            }
        else:
            msg = f"Invalid user type {user_type}"
            return jsonify(
                msg=msg,
            )
        # end if

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        # If account exists show error and validation checks
        account = Database.user_exists_in_db(cursor, mysql, hash_userid)
        if account:
            msg = 'Account already exists!'
        elif not Utils.isvalid_username(userid):
            msg = 'Username must contain only characters and numbers!'
        elif not Utils.isvalid_password(password):
            msg = 'Invalid password format!'
        elif not userid or not password:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            # cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s...)', user_info)
            # mysql.connection.commit()
            Database.insert_user_record(cursor, mysql, user_info)
            msg = 'Successfully registered'
        # end if
        cursor.close()
    # end if
    print(msg)
    return jsonify(
        msg=msg,
        userid = hash_userid
    )

# @app.route('/profile', methods=['GET', 'POST'])
# def profile():
#     userid = session['userid']
#     user_type = session['user_type']
#     pass

@app.route('/profile', methods=['GET', 'POST'])
def transaction_history():
    # This method shows clients and trader their transaction histories
    # daily, weekly, or monthly
    if request.method == 'POST' and 'time_period' in request.form:
        userid = session['userid']
        user_type = session['user_type']
        time_period = request.form['time_period']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        transaction_histories = Database.get_user_transaction_history(
            cursor, mysql,
            [user_type, userid, time_period]
        )
        cursor.close()
    # end if
    return jsonify(
        msg=msg,
        transaction_histories=transaction_histories
    )

@app.route('/profile', methods=['GET', 'POST'])
def request_history(userid):
    # This method shows trader their requests received from clients
    if request.method == 'POST':
        userid = session['userid']
        user_type = session['user_type']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # request_histories:
        # for client: each row consists of [rid, traderid, bitcoin_value, purchase_type]
        # for trader: each row consists of [rid, clientid, bitcoin_value, purchase_type]
        request_histories = Database.get_bitcoin_requests(
            cursor, mysql,
            [userid, user_type]
        )
        cursor.close()
    # end if
    return jsonify(
        msg=msg,
        request_histories=request_histories
    )

@app.route('/profile/transfer_from_bank', methods=['GET', 'POST'])
def tansfer_from_bank(userid):
    pass

@app.route('/api/profile/request', methods=['GET', 'POST'])
def request_bitcoin(userid):
    # This method is for clients to request buy/sell bitcoin to trader
    msg = ''
    if request.method == 'POST' and \
       'bitcoin_val' in request.form and \
       'purchase_type' in request.form:
        
        # Create variables for easy access
        clientid = session['userid']
        user_type = session['user_type']
        if user_type == 'client':
            bitcoin_val = request.form['bitcoin_val']
            purchase_type = request.form['purchase_type']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # not yet finished
            new_request = Database.set_bitcoin_request(
                cursor, mysql,
                [cliendid, bitcoin_val, purchase_type]
            )
            # new_request: [rid, traderid, bitcoin_value, purchase_type]
            msg = "Successfully requested"
            cursor.close()
        # end if
    # end if
    return jsonify(
        msg=msg,
        request=new_request
    )   

@app.route('/profile/buysell', methods=['GET', 'POST'])
def buysell_bitcoin(userid):
    # This method is for client/trader to buy/sell bitcoin
    msg = ''
    if request.method == 'POST' and \
       'userid' in request.form and \
       'user_type' in request.form:
        userid = session['userid']
        user_type = session['user_type']
        if user_type == 'client':
            bitcoin_val = request.form['bitcoin_val']
            purchase_type = request.form['purchase_type']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # not yet finished
            Database.buysell_bitcoin(
                cursor, mysql,
                [user_type, bitcoin_val, purchase_type]
            )
            msg = "Successfully purchased."
            cursor.close()
        elif user_type =='trader':
            request_id = request.form['request_id']
            # not yet finished
            Database.buysell_bitcoin(
                cursor, mysql,
                [user_type, request_id]
            )
        # end if
    # end if
    return jsonify(
        msg=msg
    )

@app.route('/profile/transfer', methods=['GET', 'POST'])
def transfer_money(userid):
    # This method is for client to transfer money to trader
    msg = ''
    if request.method == 'POST' and \
       'usd_val' in request.form:
        userid = session['userid']
        user_type = session['user_type']
        if user_type == 'client':
            purchase_type = request.form['usd_val']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            Database.transfer_money(
                cursor, mysql,
                [userid, usd_val]
            )
            msg = "Successfully purchased."
            cursor.close()
        # end if
    # end if
    return jsonify(
        msg=msg
    )

@app.route('/api/profile/cancel', methods=['GET', 'POST'])
def cancel_tansaction(userid):
    # This method is for trader to cancel his/her transactions
    msg = ''
    if request.method == 'POST' and \
       'transactionid' in request.form:
        userid = session['userid']
        user_type = session['user_type']
        if user_type == 'trader':
            transactionid = request.form['transactionid']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            Database.cancel_transaction(
                cursor, mysql, transactionid
            )
            msg = "Transaction successfully canceled."
            cursor.close()
        # end if
    # end if
    return jsonify(
        msg=msg
    )




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
