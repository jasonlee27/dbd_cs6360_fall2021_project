from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_mysqldb import MySQL

from macros import Macros
from utils import Utils
from database import Database

import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = Macros.SECRETE_KEY

# DB connection details
# app.config['MYSQL_HOST'] = Macros.MYSQL_HOST
app.config['MYSQL_USER'] = Macros.MYSQL_USER
# app.config['MYSQL_PASSWORD'] = Macros.MYSQL_PASSWORD
app.config['MYSQL_DB'] = Macros.MYSQL_DB #str(Macros.DB_FILE)

mysql = MySQL(app)
Macros.DB_DIR.mkdir(parents=True, exist_ok=True)

@app.route("/api/status", methods=['GET'])
def status():
  return "running"

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    msg = ''
    account_info = None
    if request.method =='POST' and \
       'userid' in request.form and \
       'password' in request.form:
        userid = request.form['userid']
        password = request.form['password']
        #username = Utils.hashing(username)
        #password = Utils.hashing(password)
        
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        account = Database.user_exists_in_db(cursor, mysql, userid, hash_password=password)
        if account_info:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['userid'] = account['userid']
            msg = "Successfully logged in!"
        else:
            msg = 'Incorrect username/password!'
        # end if
    # end if
    cursor.close()
    return jsonify(
        msg=msg,
    )

# http://localhost:5000/api/logout
# This will be the logout page
@app.route('/api/logout')
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
@app.route('/api/register', methods=['GET', 'POST'])
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
        hash_userid = Utils.hashing(userid) if userid else None
        hash_password = Utils.hashing(password) if password else None
        user_type = request.form["user_type"]
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
                "zipcode": request.form['zipcode']
                "state": request.form['state'],
                "cphone": request.form['cellphone'],
                "phone": request.form['phone'],
                "email": request.form['email'],
                "level": request.form['level'],
                "bitcoin": 0.,
                "flatcurrency" = 0.
            }
        elif user_type=="trader":
            # trader info
            user_info = {
                "user_type": user_type,
                "userid": hash_userid,
                "password": hash_password,
                "bitcoin": 0.,
                "flatcurrency" = 0.
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
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            # cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s...)', user_info)
            # mysql.connection.commit()
            Database.insert_user_record(cursor, mysql, user_info)
            msg = 'Successfully registered'
        # end if
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # end if
    cursor.close()
    return jsonify(
        msg=msg,
        userid = hash_userid
    )

@app.route('/api/<userid>/transaction-history', methods=['GET', 'POST'])
def transaction_history(userid):
    # This method shows clients and trader their transaction histories 
    if request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        transaction_histories = Database.get_user_transaction_history(cursor, mysql, userid)
    # end if
    cursor.close()
    return jsonify(
        msg=msg,
        transaction_histories=transaction_histories
    )

@app.route('/api/<userid>/request-history', methods=['GET', 'POST'])
def request_history(userid):
    # This method shows trader their requests received from clients
    if request.method == 'POST' and \
       'user_type' in request.form:
        user_type = request.form["user_type"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        request_histories = Database.get_bitcoin_requests(
            cursor, mysql,
            [userid, user_type]
        )
    # end if
    cursor.close()
    return jsonify(
        msg=msg,
        request_histories=request_histories
    )

@app.route('/api/profile/<userid>/transfer_from_bank', methods=['GET', 'POST'])
def tansfer_from_bank(userid):
    pass

@app.route('/api/<userid>/request', methods=['GET', 'POST'])
def request(userid):
    # This method is for clients to request buy/sell bitcoin to trader
    msg = ''
    if request.method == 'POST' and \
       'clientid' in request.form and \
       'bitcoin_val' in request.form and \
       'purchase_type' in request.form:
        
        # Create variables for easy access
        clientid = request.form['clientid']
        bitcoin_val = request.form['bitcoin_val']
        purchase_type = request.form['purchase_type']
        Database.set_bitcoin_request(
            cursor, mysql,
            [cliendid, bitcoin_val, purchase_type]
        )
        msg = "Successfully requested"
    # end if
    cursor.close()
    return jsonify(
        msg=msg
    )   

@app.route('/api/<userid>/buysell', methods=['GET', 'POST'])
def buysell_bitcoin(userid):
    # This method is for client/trader to buy/sell bitcoin
    msg = ''
    if request.method == 'POST' and \
       'user_type' in request.form and \
       'bitcoin_val' in request.form and \
       'purchase_type' in request.form:
        user_type = request.form["user_type"]
        bitcoin_val = request.form['bitcoin_val']
        purchase_type = request.form['purchase_type']
        Database.buysell_bitcoin(
            cursor, mysql,
            [user_type, bitcoin_val, purchase_type]
        )
        msg = "Successfully purchased."
    # end if
    curcor.close()
    return jsonify(
        msg=msg
    )

@app.route('/api/<userid>/transfer', methods=['GET', 'POST'])
def transfer_money(userid):
    # This method is for client to transfer money to trader
    msg = ''
    if request.method == 'POST' and \
       'usd_val' in request.form:
        purchase_type = request.form['usd_val']
        Database.buysell_bitcoin(
            cursor, mysql,
            [userid usd_val]
        )
        msg = "Successfully purchased."
    # end if
    curcor.close()
    return jsonify(
        msg=msg
    )

@app.route('/api/profile/<userid>/cancel', methods=['GET', 'POST'])
def cancel_tansaction(userid):
    pass

@app.route('/api/update_level', methods=['GET', 'POST'])
def update_level():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
