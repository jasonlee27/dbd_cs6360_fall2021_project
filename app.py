from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_mysqldb import MySQL

import re


import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rock96321478'
app.config['MYSQL_DB'] = 'bts_db'



mysql = MySQL(app)

#con = mysql.connect()
#cursor = con.cursor()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User WHERE userid = % s AND user_password = % s', (username, password))
        Users = cursor.fetchone()
        if Users:
            session['loggedin'] = True

            session['userid'] = Users['userid']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    #session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'client_id' in request.form and 'client_password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'address1' in request.form and 'address2' in request.form and 'city' in request.form and 'zipcode' in request.form and 'cellphone' in request.form and 'phone' in request.form and 'level' in request.form and 'bitcoin' in request.form and 'flatcurrency' in request.form:

        username = request.form['username']
        password = request.form['password']
        '''
        clientid = request.form['clientid']
        client_password = request.form['client_password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        address1 = request.form['address1']
        address2 = request.form['address2']
        city = request.form['city']
        state = request.form['state']

        zipcode = request.form['zipcode']
        cellphone = request.form['cellphone']
        phone = request.form['phone']
        level = request.form['level']
        bitcoin = request.form['bitcoin']
        flatcurrency = request.form['flatcurrency']
        '''
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User WHERE userid = %s', (username, ))
        Users = cursor.fetchone()
        if Users:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO User VALUES (%s, %s)',
                           (username, password, ))
            #cursor.execute(
             #   'INSERT INTO Client VALUES (%s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s )',
              #  (clientid, client_password, firstname, lastname, address1, address2, city, zipcode, state, cellphone,
               #  phone, email, level, bitcoin, flatcurrency, ))
            #cursor.execute('INSERT INTO Name VALUES (% s, % s )', (firstname, lastname, ))
            #cursor.execute('INSERT INTO Address VALUES (% s, % s, % s, % s, % s)',
                           #(address1, address2, city, zipcode, state, ))
            mysql.connection.commit()

            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)

@app.route("/index", methods=['GET', 'POST'])
def index():

    msg = ''
    if 'loggedin' in session:

        if request.method == 'POST' and 'clientid' in request.form and 'client_password' in request.form and 'firstname' in request.form and 'lastname' in request.form and 'email' in request.form and 'address1' in request.form and 'address2' in request.form and 'city' in request.form  and 'zipcode' in request.form and 'cellphone' in request.form and 'phone' in request.form and 'level' in request.form and 'bitcoin' in request.form and 'flatcurrency' in request.form:

            clientid = request.form['clientid']
            client_password = request.form['client_password']
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']

            address1 = request.form['address1']
            address2 = request.form['address2']
            city = request.form['city']
            state = request.form['state']

            zipcode = request.form['zipcode']
            cellphone = request.form['cellphone']
            phone = request.form['phone']
            level = request.form['level']
            bitcoin = request.form['bitcoin']
            flatcurrency = request.form['flatcurrency']




            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #cursor.execute('SELECT * FROM User WHERE userid = % s', (clientid,))
            #account = cursor.fetchone()
            #if account:
                #msg = 'Account already exists !'

            #else:
            cursor.execute('INSERT INTO Address VALUES (% s, % s, % s, % s, % s)',
                           (address1, address2, city, zipcode, state,))
            cursor.execute('INSERT INTO Name VALUES (% s, % s )', (firstname, lastname,))
            cursor.execute('INSERT INTO Client VALUES (% s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s )',
                               (clientid, client_password, firstname, lastname, address1, address2, city, zipcode, state, cellphone, phone, email, level, bitcoin, flatcurrency, ))
                #cursor.execute('INSERT INTO Name VALUES (% s, % s )', (firstname, lastname, ))
                #cursor.execute('INSERT INTO Address VALUES (% s, % s, % s, % s, % s)', (address1, address2, city, zipcode, state, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
        elif request.method == 'POST':
                msg = 'Please fill out the form !'
    return render_template("index.html", msg=msg)

    #return render_template("index.html")

    return redirect(url_for('login'))

@app.route("/display")
def display():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute('SELECT * FROM User WHERE userid = % s', (session['userid'], ))
        cursor.execute('SELECT * FROM Client WHERE clientid = % s', (session['userid'],))
        User = cursor.fetchone()
        return render_template("display.html", User = User)
    return redirect(url_for('login'))
'''
@app.route("/update", methods =['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            organisation = request.form['organisation']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            postalcode = request.form['postalcode']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'name must contain only characters and numbers !'
            else:
                cursor.execute(
                    'UPDATE accounts SET  username =% s, password =% s, email =% s, organisation =% s, address =% s, city =% s, state =% s, country =% s, postalcode =% s WHERE id =% s',
                    (username, password, email, organisation, address, city, state, country, postalcode,
                     (session['id'],),))
                mysql.connection.commit()
                msg = 'You have successfully updated !'
        elif request.method == 'POST':
            msg = 'Please fill out the form !'
        return render_template("update.html", msg=msg)
    return redirect(url_for('login'))
'''
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))