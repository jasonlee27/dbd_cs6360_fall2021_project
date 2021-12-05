# This script contains all methods that operates database

from macros import Macros
from utils import Utils

import os

class Database:

    @classmethod
    def user_exists_in_db(cls, cursor, mysql, hash_username, hash_password=None):
        account_info = None
        account = None
        if hash_password is not None:
            cursor.execute('SELECT * FROM Client WHERE clientid = %s AND client_password = %s', (hash_username, hash_password))
        else:
            cursor.execute('SELECT * FROM Client WHERE clientid = %s', (hash_username,))
        # end if
        
        account = cursor.fetchone()
        if not account:
            if hash_password is not None:
                cursor.execute('SELECT * FROM Trader WHERE traderid = %s AND trader_password = %s', (hash_username, hash_password))
            else:
                cursor.execute('SELECT * FROM Trader WHERE traderid = %s', (hash_username,))
            # end if
            account = cursor.fetchone()
            if not account:
                if hash_password is not None:
                    cursor.execute('SELECT * FROM Manager WHERE managerid = %s AND manager_password = %s', (hash_username, hash_password))
                else:
                    cursor.execute('SELECT * FROM Manager WHERE managerid = %s', (hash_username,))
                # end if
                account = cursor.fetchone()
                if account:
                    account_info = {
                        "user_type": 'manager',
                    }
                # end if
            else:
                clients = None # TODO: get all clients assigned to input trader
                account_info = {
                    "user_type": 'trader',
                    "bitcoin": account[3],
                    "flatcurrenty": account[4],
                    "clients": clients
                }
            # end if
        else:
            account_info = {
                "user_type": 'trader',
                "userid": hash_username,
                "first_name": account[3],
                "last_name": account[4],
                "address1": account[5],
                "address2": account[6],
                "city": account[7],
                "zipcode": account[8],
                "state": account[9],
                "cellphone": account[10],
                "phone": account[11],
                "email": account[12],
                "level": account[13],
                "bitcoin": account[14],
                "flatcurrenty": account[15]
            }
        # end if
        return account_info

    @classmethod
    def insert_user_record(cls, cursor, mysql, user_info):
        user_type = user_info["user_type"]
        if user_type=="client":
            cursor.execute('INSERT IGNORE INTO User VALUES (%s, %s)', (user_info["userid"], user_info["password"]))
            cursor.execute('INSERT IGNORE INTO Name VALUES (%s, %s)', (user_info["firstname"], user_info["lastname"]))
            cursor.execute('INSERT IGNORE INTO Address VALUES (%s, %s, %s, %s, %s)', (user_info["address1"], user_info["address2"],user_info["city"], user_info["zipcode"], user_info["state"]))
            cursor.execute("""INSERT INTO Client VALUES (
                           (SELECT userid FROM User WHERE userid = %s AND user_password = %s), 
                           (SELECT user_password FROM User WHERE userid = %s AND user_password = %s),
                           %s,
                           (SELECT firstname FROM Name WHERE firstname = %s AND lastname = %s), 
                           (SELECT lastname FROM Name WHERE firstname = %s AND lastname = %s), 
                           (SELECT address1 FROM Address WHERE address1 = %s AND address2 = %s AND city = %s AND zipcode = %s AND state = %s), 
                           (SELECT address2 FROM Address WHERE address1 = %s AND address2 = %s AND city = %s AND zipcode = %s AND state = %s), 
                           (SELECT city FROM Address WHERE address1 = %s AND address2 = %s AND city = %s AND zipcode = %s AND state = %s), 
                           (SELECT zipcode FROM Address WHERE address1 = %s AND address2 = %s AND city = %s AND zipcode = %s AND state = %s), 
                           (SELECT state FROM Address WHERE address1 = %s AND address2 = %s AND city = %s AND zipcode = %s AND state = %s), 
                           %s, %s, %s, %s, %s, %s)""",
                           (user_info["userid"], user_info["password"],
                            user_info["userid"], user_info["password"],
                            user_info["register_date"],
                            user_info["firstname"], user_info["lastname"],
                            user_info["firstname"], user_info["lastname"],
                            user_info["address1"], user_info["address2"], user_info["city"], user_info["zipcode"], user_info["state"],
                            user_info["address1"], user_info["address2"], user_info["city"], user_info["zipcode"], user_info["state"],
                            user_info["address1"], user_info["address2"], user_info["city"], user_info["zipcode"], user_info["state"],
                            user_info["address1"], user_info["address2"], user_info["city"], user_info["zipcode"], user_info["state"],
                            user_info["address1"], user_info["address2"], user_info["city"], user_info["zipcode"], user_info["state"],
                            user_info["cphone"], user_info["phone"],
                            user_info["email"], user_info["level"],
                            user_info["bitcoin"], user_info["flatcurrency"]))
        elif user_type=="trader":
            cursor.execute('INSERT IGNORE INTO User VALUES (%s, %s)', (user_info["userid"], user_info["password"]))
            cursor.execute("""INSERT INTO Trader VALUES (
                           (SELECT userid FROM User WHERE userid = %s AND user_password = %s), 
                           (SELECT user_password FROM User WHERE userid = %s AND user_password = %s),
                           %s, %s)""",
                           (user_info["userid"], user_info["password"],
                            user_info["userid"], user_info["password"],
                            user_info["bitcoin"], user_info["flatcurrency"]))
        elif user_type=="manager":
            cursor.execute('INSERT IGNORE INTO User VALUES (%s, %s)', (user_info["userid"], user_info["password"]))
            cursor.execute("""INSERT INTO Manager VALUES (
                           (SELECT userid FROM User WHERE userid = %s AND user_password = %s), 
                           (SELECT user_password FROM User WHERE userid = %s AND user_password = %s))""",
                           (user_info["userid"], user_info["password"],
                            user_info["userid"], user_info["password"]))
        # end if
        mysql.connection.commit()
        return

    @classmethod
    def user_exists_in_db(cls, cursor, mysql, hash_username, hash_password=None):
        account_info = None
        account = None
        if hash_password is not None:
            cursor.execute('SELECT * FROM Client WHERE clientid = %s AND client_password = %s', (hash_username, hash_password))
        else:
            cursor.execute('SELECT * FROM Client WHERE clientid = %s', (hash_username,))
        # end if
        account = cursor.fetchone()
        if not account:
            if hash_password is not None:
                cursor.execute('SELECT * FROM Trader WHERE traderid = %s AND trader_password = %s', (hash_username, hash_password))
            else:
                cursor.execute('SELECT * FROM Trader WHERE traderid = %s', (hash_username,))
            # end if
            account = cursor.fetchone()
            if not account:
                if hash_password is not None:
                    cursor.execute('SELECT * FROM Manager WHERE managerid = %s AND manager_password = %s', (hash_username, hash_password))
                else:
                    cursor.execute('SELECT * FROM Manager WHERE managerid = %s', (hash_username,))
                # end if

                account = cursor.fetchone()
                if account:
                    account_info = {
                        "user_type": 'manager',
                    }
                # end if
            else:
                clients = None # TODO: get all clients assigned to input trader
                account_info = {
                    "user_type": 'trader',
                    "bitcoin": account["bitcoin"],
                    "flatcurrenty": account["flatcurrency"],
                }
            # end if
        else:
            account_info = {
                "user_type": 'client',
                "first_name": account["firstname"],
                "last_name": account["lastname"],
                "address1": account["address1"],
                "address2": account["address2"],
                "city": account["city"],
                "zipcode": account["zipcode"],
                "state": account["state"],
                "cellphone": account["cellphone"],
                "phone": account["phone"],
                "email": account["email"],
                "level": account["level"],
                "bitcoin": account["bitcoin"],
                "flatcurrency": account["flatcurrency"]
            }
        # end if
        return account_info

    @classmethod
    def add_client_money(cls, cursor, mysql, data):
        user_type, hash_username, flatcurrency = data[0], data[1], data[2]
        cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', (hash_username))
        old_flatcurrency = cursor.fetchone()
        cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency + %s) WHERE clientid = %s', (flatcurrency))
        mysql.connection.commit()
        cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', (hash_username))
        new_flatcurrency = cursor.fetchone()
        return old_flatcurrency, new_flatcurrency
        
    @classmethod
    def get_assgned_trader_in_db(cls, cursor, mysql, hash_username):
        # hash_username: client id
        cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', (hash_username))
        trader = cursor.fetchone()
        return trader

    @classmethod
    def get_assgned_clients_in_db(cls, cursor, mysql, hash_username):
        # hash_username: trader id
        cursor.execute('SELECT clientid FROM Assign WHERE traderid = %s', (hash_username))
        clients = cursor.fetchall()
        return clients

    @classmethod
    def get_traders_in_db(cls, cursor, mysql):
        # hash_username: trader id
        cursor.execute('SELECT traderid FROM Trader')
        traders = cursor.fetchall()
        return traders

    @classmethod
    def assign_trader(cls, cursor, mysql, data):
        hash_username, traderid = data[0], data[1]
        # hash_username: trader id
        cursor.execute('INSERT INTO Assign(clientid, traderid) VALUES (%s, %s)', (hash_username, traderid))
        mysql.connection.commit()
        return
    
                
    @classmethod
    def get_user_transaction_history(cls, cursor, mysql, data):
        # TODO
        user_type, userid, time_period = data[0], data[1], data[2]
        # user_type: one out of [client, trader, manager]
        # time_period: one out of [daily, weekly, monthly]
        # in case of manager, it shows every transaction history over all
        # client and trader
        cursor.execute('SELECT * FROM Transaction WHERE transfer_trid = (SELECT ttrid FROM TransferTransaction WHERE ttrid = %s) AND TransferTransaction.date between date_sub(now(),INTERVAL 1 %s) AND now()', (ttrid, time_period,))
        cursor.execute('SELECT * FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE ptrid = %s) AND PurchaseTransaction.date between date_sub(now(),INTERVAL 1 %s) AND now()', (ttrid, time_period,))

        pass

    @classmethod
    def set_bitcoin_request(cls, cursor, mysql, data):
        # TODO
        clientid, bitcoin_val, purchase_type = data[0], data[1], data[2]
        cursor.execute('INSERT INTO Request VALUES (%s, (SELECT clientid FROM CLient WHERE clientid = %s), (SELECT traderid FROM Trader WHERE traderid = %s), %s, %s)', (rid, clientid, traderid, bitcoin_val, purchase_type))
        cursor.execute('SELECT * FROM Request',)
        mysql.connection.commit()
        pass

    @classmethod
    def get_bitcoin_requests(cls, cursor, mysql, data):
        # get bitcoin requests from client to trader
        userid, user_type = data[0], data[1]
        histories = None
        if user_type == 'client':
            cursor.execute('SELECT R.rid, R.traderid, R.bitcoin_value, R.purchase_type FROM Request R WHERE R.clientid = %s', (clientid))
            histories = cursor.fetchall()
        elif user_type == 'trader':
            cursor.execute('SELECT R.rid, R.clientid, R.bitcoin_value, R.purchase_type FROM Request R WHERE R.traderid = %s', (traderid,))
            histories = cursor.fetchall()
        # end if
        return histories

    @classmethod
    def buysell_bitcoin(cls, cursor, mysql, data):
        user_type, userid = data[0], data[1]
        # TODO
        # please let me know more about "level' in user table
        if user_type == "client":
            bitcoin_val, purchase_type = data[2], data[3]

            # TODO: buy/sell bitcoin by clients themselves
            if purchase_type == 'buy':
                # cursor.execute('UPDATE Client SET bitcoin = bitcoin + %s', (bitcoin_val, ))
                cursor.execute('UPDATE Client SET bitcoin = (bitcoin + %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction)', (bitcoin_val, ))
                cursor.execute('INSERT INTO Transaction VALUES (%s, %s, %s)', (trid, transfer_trid, purchase_trid, ))
                cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue ))
            elif purchase_type == 'sell':
                # cursor.execute('UPDATE Client SET bitcoin = bitcoin - %s', (bitcoin_val, ))
                cursor.execute('UPDATE Client SET bitcoin = (bitcoin - %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction)', (bitcoin_val, ))
                cursor.execute('INSERT INTO Transaction VALUES (%s, %s, %s)', (trid, transfer_trid, purchase_trid, ))
                cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))

            # end if
        elif user_type == "trader":
            request_id = data[1]
            # TODO: find the request given request_id and purchse the requested bitcoin buy/sell
            if purchase_type == 'buy':
                cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction)', (bitcoin_val, ))
                cursor.execute('INSERT INTO Transaction VALUES (%s, %s, %s)', (trid, transfer_trid, purchase_trid, ))
                cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))
            elif purchase_type == 'sell':
                cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction)', (bitcoin_val, ))
                cursor.execute('INSERT INTO Transaction VALUES (%s, %s, %s)', (trid, transfer_trid, purchase_trid, ))
                cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))
        # end if
        mysql.connection.commit()
        pass

    @classmethod
    def transfer_money(cls, cursor, mysql, data):
        trader = None
        user_type, userid, usd_val = data[0], data[1], data[2]
        # from my previous experience, you dont need to find the client id to update as long as you are logged in, i.e use the "session"
        if user_type=="client":
            # find the client's trader
            cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', (userid))
            traderid = cursor.fetchone()
            if traderid:
                # get the old usd value
                cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', (userid))
                old_value = cursor.fetchone()
                
                # remove the amount of money from client
                cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency - %s) WHERE clientid = %s', (usd_val, userid))

                # add the amount of money from client
                cursor.execute('UPDATE Trader SET flatcurrency = (flatcurrency + %s)  WHERE clientid = %s', (usd_val, traderid))
                mysql.connection.commit()

                # get the new usd value
                cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', (userid))
                new_value = cursor.fetchone()

                # add log for the transfer transaction
                cursor.execute("INSERT INTO Log(log_type, oldvalue, newvalue) VALUES ('update_transfertransaction', %s, %s)", (old_value, new_value))
            
                mysql.connection.commit()
            # end if
        # end if
        return

    @classmethod
    def cancel_transaction(cls, cursor, mysql, data):
        # log : (logid, log_type, trid)
        # log_type: [update_purchasetransaction, update_transfertransaction, cancel_purchasetransaction, cancel_transfertransaction]
        user_type, userid, transactionid, transactiontype = data[0], data[1], data[2], data[3]
        if transactiontype=="bitcoin":
            cursor.execute('SELECT purchase_type, bitcoin_value, fiat_value, commission_rate FROM PurchaseTransaction WHERE ptrid = %s', (transactionid))
            trans_info = cursor.fetchone()
            purchase_type, bitcoin_value, fiat_value, commission_rate = trans_info[0], trans_info[1], trans_info[2], trans_info[3]
            if purchase_type=="buy":
                # get the bitcoin and fiat value back to trader
                cursor.execute('UPDATE Trader SET bitcoin = (bitcoin - %s), flatcurrency = (flatcurrency + %s *(1+%s)) WHERE traderid = %s', (bitcoin_value, fiat_value, commission_rate, userid))
                # delete the tranaction from transaction table
            elif purchase_type=="sell":
                # get the bitcoin and fiat value back to trader
                cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s), flatcurrency = (flatcurrency - %s *(1+%s)) WHERE traderid = %s', (bitcoin_value, fiat_value, commission_rate, userid))
            # end if
            
            # delete the tranaction from transaction table
            cursor.execute('DELETE FROM PurchaseTransaction WHERE trid = %s', (transactionid))
            cursor.execute("INSERT INTO Log(log_type, trid) VALUES ('cancel_purchasetransaction', DEFAULT)")
            mysql.connection.commit()
            
        elif transactiontype=="transfer":
            cursor.execute('SELECT usd_value, clientid FROM TransferTransaction WHERE ttrid = %s AND traderid = %s', (transactionid, userid))
            trans_info = cursor.fetchone()
            usd_value, clientid = trans_info[0], trans_info[1]

            # get the fiat value back to trader
            cursor.execute('UPDATE Trader SET flatcurrency = (flatcurrency - %s) WHERE traderid = %s', (usd_value, userid))
            cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency + %s) WHERE clientid = %s', (usd_value, clientid))

            # delete the tranaction from transaction table
            cursor.execute('DELETE FROM TransferTransaction WHERE ttrid = %s', (transactionid))
            cursor.execute("INSERT INTO Log(log_type, trid) VALUES ('cancel_transfertransaction', DEFAULT)")
            mysql.connection.commit()
        # end if
        return

    @classmethod
    def update_level(cls, cursor, mysql, data):
        # TODO
        pass

                
    @classmethod
    def get_all_transaction_history(cls, cursor, mysql, data):
        user_type, userid, date_range, start_date, end_date = data[0], data[1], data[2], data[3], data[4]
        start_year, start_month, start_day = start_date.split("-")
        end_year, end_month, end_day = end_date.split("-")
        purchase_trans_history, transfer_trans_history = None, None
        if date_range == "daily":
            cursor.execute("""SELECT * FROM PurchaseTransaction WHERE date BETWEEN %s AND %s """, (start_date, end_date))
            purchase_trans_history = cursor.fetchall()
            cursor.execute("""SELECT * FROM TransferTransaction WHERE date BETWEEN %s AND %s """, (start_date, end_date))
            transfer_trans_history = cursor.fetchall()
        elif date_range == "monthly":
            _start_date = f"{start_year}-{start_month}-01"
            _end_month = int(end_month)
            if _end_month in [1,3,5,7,8,10,12]:
                _end_date = f"{end_year}-{end_month}-31"
            elif _end_month in [4,6,9,11]:
                _end_date = f"{end_year}-{end_month}-30"
            else:
                _end_year = int(end_year)
                if _end_year%4==0:
                    # it is leap year having 29 days for feb
                    _end_date = f"{end_year}-{end_month}-29"
                else:
                    _end_date = f"{end_year}-{end_month}-28"
                # end if
            # end if
            cursor.execute("""SELECT * FROM PurchaseTransaction WHERE date BETWEEN %s AND %s """, (_start_date, _end_date))
            purchase_trans_history = cursor.fetchall()
            cursor.execute("""SELECT * FROM PurchaseTransaction WHERE date BETWEEN %s AND %s """, (_start_date, _end_date))
            transfer_trans_history = cursor.fetchall()
        else: # date_range == "yearly"
            _start_date = f"{start_year}-01-01"
            _end_date = f"{end_year}-12-31"
            cursor.execute("""SELECT * FROM PurchaseTransaction WHERE date BETWEEN %s AND %s """, (_start_date, _end_date))
            purchase_trans_history = cursor.fetchall()
            cursor.execute("""SELECT * FROM PurchaseTransaction WHERE date BETWEEN %s AND %s """, (_start_date, _end_date))
            transfer_trans_history = cursor.fetchall()
        # end if
        return purchase_trans_history, transfer_trans_history
