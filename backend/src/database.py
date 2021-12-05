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
    def get_assgned_trader_in_db(cls, cursor, mysql, hash_username):
        # hash_username: client id
        cursor.execute('SELECT * FROM Client WHERE clientid = %s', (hash_username))
        account = cursor.fetchone()
        if account:
            cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', (hash_username))
        # end if
        return account

    @classmethod
    def get_assgned_clients_in_db(cls, cursor, mysql, hash_username):
        # hash_username: trader id
        cursor.execute('SELECT * FROM Trader WHERE traderid = %s', (hash_username))
        account = cursor.fetchone()
        if account:
            cursor.execute('SELECT clientid FROM Assign WHERE traderid = %s', (hash_username))
        # end if
        return account
                
    @classmethod
    def get_user_transaction_history(cls, cursor, mysql, data):
        user_type, userid, time_period = data[0], data[1], data[2]
        # user_type: one out of [client, trader, manager]
        # time_period: one out of [daily, weekly, monthly]
        # in case of manager, it shows every transaction history over all
        # client and trader
        # TODO: do not access to transfertransaction and purchagetransaction directly, but access them via where clause from transaction table, but why?
        cursor.execute('SELECT * FROM Transaction t, TransferTransaction t1, PurchaseTransaction t3 WHERE t.transfer_trid = t1.ttrid AND t.purchase_trid = t2.ptrid AND date between date_sub(now(),INTERVAL 1 %s) AND now()', (time_period,))

        pass

    @classmethod
    def set_bitcoin_request(cls, cursor, mysql, data):
        clientid, bitcoin_val, purchase_type = data[0], data[1], data[2]
        # TODO: find traderid given clients's id
        # TODO: get the request info as output for show cleint the request
        cursor.execute('INSERT INTO Request (clientid, traderid, bitcoin_value, purchase_type) VALUES (%s, %s, %s, %s, %s)', (rid, clientid, traderid, bitcoin_val, purchase_type))
        cursor.execute('SELECT * FROM Request',)
        mysql.connection.commit()
        pass

    @classmethod
    def get_bitcoin_requests(cls, cursor, mysql, data):
        # get bitcoin requests from client to trader
        userid, user_type = data[0], data[1]
        histories = None
        if user_type == 'client':
            cursor.execute('SELECT R.rid, R.traderid, R.bitcoin_value, R.purchase_type FROM Request R WHERE R.clientid = %s', (userid,))
            histories = cursor.fetchall()
        elif user_type == 'trader':
            cursor.execute('SELECT R.rid, R.clientid, R.bitcoin_value, R.purchase_type FROM Request R WHERE R.traderid = %s', (userid,))
            histories = cursor.fetchall()
        # end if
        return histories

    @classmethod
    def buysell_bitcoin(cls, cursor, mysql, data):
        user_type = data[0]
        # TODO: given bitcoin value
        # TODO: append log for this transaction
        if user_type == "client":
            bitcoin_val, purchase_type = data[1], data[2]
            # TODO: buy/sell bitcoin by clients themselves
            if purchase_type == 'buy':
                # cursor.execute('UPDATE Client SET bitcoin = bitcoin + %s', (bitcoin_val, ))
                cursor.execute('UPDATE Client SET bitcoin = (bitcoin + %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction)', (bitcoin_val, ))
                cursor.execute('INSERT INTO Transaction VALUES (%s, %s, %s)', (trid, transfer_trid, purchase_trid, ))
                cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))
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
        user_type, usd_val = data[0], data[1]
        # TODO: transfer USD to clients's trader and append log for it
        cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency - %s)', (usd_val, ))
        cursor.execute('UPDATE Trader SET flatcurrency = (flatcurrency + %s)', (usd_val, ))
        cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))
        mysql.connection.commit()
        pass

    @classmethod
    def cancel_transaction(cls, cursor, mysql, transactionid):
        # TODO: cancel transaction in database
        # 1. delete transaction specified
        # 2. update log and its status
        cursor.execute('DELETE FROM TransferTransaction WHERE trid = %s', (transactionid, ))
        cursor.execute('INSERT INTO Cancel VALUES(%s, %s, %s)', (cid, traderid, trid, ))
        cursor.execute('INSERT INTO Log VALUES (%s, %s, %s)', (logid, oldvalue, newvalue, ))
        mysql.connection.commit()
        pass    

    @classmethod
    def update_level(cls, cursor, mysql, data):
        
        pass
