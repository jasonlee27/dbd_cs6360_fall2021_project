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
            cursor.execute('INSERT IGNORE INTO Name VALUES (%s, %s)', (user_info["firstname"], user_info["lastname"]))
            cursor.execute("""INSERT INTO Trader VALUES (
                           (SELECT userid FROM User WHERE userid = %s AND user_password = %s), 
                           (SELECT user_password FROM User WHERE userid = %s AND user_password = %s),
                           %s,
                           (SELECT firstname FROM Name WHERE firstname = %s AND lastname = %s),
                           (SELECT lastname FROM Name WHERE firstname = %s AND lastname = %s),
                           %s, %s)""",
                           (user_info["userid"], user_info["password"],
                            user_info["userid"], user_info["password"],
                            user_info["register_date"],
                            user_info["firstname"], user_info["lastname"],
                            user_info["firstname"], user_info["lastname"],
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
        user_type, userid, flatcurrency = data[0], data[1], data[2]
        cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', [userid])
        old_flatcurrency = cursor.fetchone()
        old_flatcurrency = old_flatcurrency["flatcurrency"]
        cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency + %s) WHERE clientid = %s', [flatcurrency, userid])
        mysql.connection.commit()
        cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', [userid])
        new_flatcurrency = cursor.fetchone()
        new_flatcurrency = new_flatcurrency["flatcurrency"]
        return old_flatcurrency, new_flatcurrency
        
    @classmethod
    def get_assigned_trader_in_db(cls, cursor, mysql, hash_username):
        # hash_username: client id
        cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', [hash_username])
        trader = cursor.fetchone()
        if trader:
            return trader["traderid"]
        # end if
        return trader

    @classmethod
    def get_assigned_clients_in_db(cls, cursor, mysql, hash_username):
        # hash_username: trader id
        cursor.execute('SELECT clientid FROM Assign WHERE traderid = %s', [hash_username])
        clients = cursor.fetchall()
        return clients

    @classmethod
    def get_traders_in_db(cls, cursor, mysql):
        # hash_username: trader id
        cursor.execute('SELECT traderid, firstname, lastname FROM Trader')
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
        bitcoin_transactions, transfer_transactions = None, None
        user_type, userid = data[0], data[1]
        print("uid:",userid)
        if user_type == "client":

            # get bitcoin transactions
            cursor.execute("""SELECT Pt.date, Pt.commission_rate, Pt.commission_type, Pt.fiat_value, Pt.bitcoin_value, Cb.userid
                              FROM PurchaseTransaction Pt, Client_buysell Cb 
                              WHERE Cb.ptrid = Pt.ptrid AND Cb.userid = %s""", [userid])
            bitcoin_transactions = cursor.fetchall()

            # get transfer transactions
            cursor.execute("""SELECT Tt.date, Tt.usd_value, Tr.clientid, Tr.traderid
                              FROM TransferTransaction Tt, Transfer Tr
                              WHERE Tr.ttrid = Tt.ttrid AND Tr.clientid = %s""", [userid])
            transfer_transactions = cursor.fetchall()

        elif user_type == "trader":
            clientid = data[2]
            
            # get bitcoin transactions
            print("clientid",clientid)
            cursor.execute("""SELECT *
                              FROM PurchaseTransaction Pt, Client_buysell Tb 
                              WHERE Tb.ptrid = Pt.ptrid AND Tb.userid = %s""", [clientid])
            bitcoin_transactions = cursor.fetchall()
            # get transfer transactions
            cursor.execute("""SELECT Tt.date, Tt.usd_value, Tr.clientid, Tr.traderid
                              FROM TransferTransaction Tt, Transfer Tr
                              WHERE Tr.ttrid = Tt.ttrid AND Tr.traderid = %s""", [clientid])
            transfer_transactions = cursor.fetchall()
        # end if
        return bitcoin_transactions, transfer_transactions

    @classmethod
    def set_bitcoin_request(cls, cursor, mysql, data):
        # TODO
        user_type, userid, bitcoin_val, purchase_type, commission_type = data[0], data[1], data[2], data[3], data[4]
        
        # find client's trader
        cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', [userid])
        traderid = cursor.fetchone()["traderid"]
        print(traderid)
        print(userid)
        
        cursor.execute('INSERT INTO Request(clientid, traderid, bitcoin_value, commission_type, purchase_type) VALUES (%s, %s, %s, %s, %s)', (userid, traderid, bitcoin_val, commission_type, purchase_type))
        mysql.connection.commit()
        return

    @classmethod
    def get_bitcoin_requests(cls, cursor, mysql, data):
        # get bitcoin requests from client to trader
        userid, user_type = data[0], data[1]
        histories = None
        if user_type == 'client':
            cursor.execute('SELECT * FROM Request WHERE clientid = %s', [userid])
            histories = cursor.fetchall()
        elif user_type == 'trader':
            cursor.execute('SELECT * FROM Request WHERE traderid = %s', [userid])
            histories = cursor.fetchall()
        # end if
        return histories

    @classmethod
    def buysell_bitcoin(cls, cursor, mysql, data):
        user_type, userid = data[0], data[1]
        if user_type == "client":
            bitcoin_val, purchase_type, commission_type, transaction_date, transaction_time = data[2], data[3], data[4], data[5], data[6]
            cursor.execute('SELECT level FROM Client WHERE clientid = %s', [userid])
            client_level = cursor.fetchone()["level"]
            commission_rate = Macros.COMMISSION_RATE['silver']
            if client_level == "gold":
                commission_rate = Macros.COMMISSION_RATE['gold']
            # end if
            fiat_val = Utils.exchange_bitcoin_fiat(bitcoin_val=bitcoin_val)
            if commission_type == "bitcoin":
                commission_fee = float(bitcoin_val)*commission_rate
                if purchase_type == "buy":
                    cursor.execute('UPDATE Client SET bitcoin = (bitcoin + %s - %s), flatcurrency = (flatcurrency - %s) WHERE clientid = %s', (bitcoin_val, commission_fee, fiat_val, userid))
                elif purchase_type == "sell":
                    cursor.execute('UPDATE Client SET bitcoin = (bitcoin - %s - %s), flatcurrency = (flatcurrency + %s) WHERE clientid = %s', (bitcoin_val, commission_fee, fiat_val, userid))
                # end if
            elif commission_type == "fiat":
                commission_fee = fiat_val*commission_rate
                if purchase_type == "buy":
                    cursor.execute('UPDATE Client SET bitcoin = (bitcoin + %s), flatcurrency = (flatcurrency - %s - %s) WHERE clientid = %s', (bitcoin_val, fiat_val, commission_fee, userid))
                elif purchase_type == "sell":
                    cursor.execute('UPDATE Client SET bitcoin = (bitcoin - %s), flatcurrency = (flatcurrency + %s - %s) WHERE clientid = %s', (bitcoin_val, fiat_val, commission_fee, userid))
                # end if
            # end if

            # add the transaction to the transaction table
            cursor.execute('INSERT INTO PurchaseTransaction(date, time, commission_type, commission_rate, bitcoin_value, fiat_value, purchase_type) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (transaction_date, transaction_time, commission_type, commission_rate, bitcoin_val, fiat_val, purchase_type))
                
            # add log for the transfer transaction
            cursor.execute("""SELECT ptrid 
                              FROM PurchaseTransaction 
                              WHERE date = %s AND time = %s AND commission_type = %s AND commission_rate = %s AND bitcoin_value = %s AND fiat_value = %s AND purchase_type = %s""",
                           (transaction_date, transaction_time, commission_type, commission_rate, bitcoin_val, fiat_val, purchase_type))
            ptrid = cursor.fetchone()["ptrid"]

            # add the transaction transaction table and log
            cursor.execute("INSERT INTO Client_buysell(ptrid, userid) VALUES (%s, %s)", (ptrid, userid))
            cursor.execute("INSERT INTO Log(log_type, trid) VALUES (%s, %s)", ["update_purchasetransaction", ptrid])
            mysql.connection.commit()
        elif user_type == "trader":
            request_id = data[2]
            cursor.execute('SELECT clientid, bitcoin_value, commission_type, purchase_type FROM Request WHERE rid = %s', (request_id))
            request_info = cursor.fetchone()
            clientid, bitcoin_val, commission_type, purchase_type = request_info[0], request_info[1], request_info[2], request_info[3]
            
            cursor.execute('SELECT level FROM Client WHERE clientid = %s', [userid])
            client_level = cursor.fetchone()
            commission_rate = Macros.COMMISSION_RATE['silver']
            if client_level == "gold":
                commission_rate = Macros.COMMISSION_RATE['gold']
            # end if

            fiat_val = Utils.exchange_bitcoin_fiat(bitcoin_val=bitcoin_val)
            
            if commission_type == "bitcoin":
                commission_fee = float(bitcoin_val)*commission_rate
                if purchase_type == "buy":
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s - %s), flatcurrency = (flatcurrency - %s) WHERE traderid = %s', (bitcoin_val, commission_fee, fiat_val, userid))
                elif purchase_type == "sell":
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin - %s - %s), flatcurrency = (flatcurrency + %s) WHERE traderid = %s', (bitcoin_val, commission_fee, fiat_val, userid))
                # end if
            elif commission_type == "fiat":
                commission_fee = fiat_val*commission_rate
                if purchase_type == "buy":
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s), flatcurrency = (flatcurrency - %s - %s) WHERE traderid = %s', (bitcoin_val, fiat_val, commission_fee, userid))
                elif purchase_type == "sell":
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin - %s), flatcurrency = (flatcurrency + %s - %s) WHERE traderid = %s', (bitcoin_val, fiat_val, commission_fee, userid))
                # end if
            # end if

            # add the transaction to the transaction table
            cursor.execute('INSERT INTO PurchaseTransaction(date, time, commission_type, commission_rate, bitcoin_value, fiat_value, purchase_type) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (transaction_date, transaction_time, commission_type, commission_rate, bitcoin_val, fiat_val, purchase_type))
                
            # add log for the transfer transaction
            cursor.execute("""SELECT ptrid 
                              FROM PurchaseTransaction 
                              WHERE date = %s AND time = %s AND commission_type = %s AND commission_rate = %s AND bitcoin_value = %s AND fiat_value = %s AND purchase_type = %s""",
                           (transaction_date, transaction_time, commission_type, commission_rate, bitcoin_val, fiat_val, purchase_type))
            ptrid = cursor.fetchone()["ptrid"]
            
            # add the transaction transaction table and log
            cursor.execute("INSERT INTO Trader_buysell(ptrid, userid) VALUES (%s, %s)", (ptrid, userid))
            cursor.execute("INSERT INTO Log(log_type, trid) VALUES (update_purchasetransaction, %s)", [ptrid])
            mysql.connection.commit()
        # end if
        return

    # @classmethod
    # def buysell_bitcoin(cls, cursor, mysql, data):
    #     user_type, userid = data[0], data[1]
    #     # TODO
    #     # 
    #     if user_type == "client":
    #         bitcoin_val, purchase_type = data[2], data[3]

    #         # TODO: buy/sell bitcoin by clients themselves
    #         if cursor.execute('SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (userid, )) == "gold":
                                 
    #             if purchase_type == 'buy':
    #             # we hard coded 1 bitcoin = 10000usd
    #                 #cursor.execute('UPDATE Client SET bitcoin = (bitcoin + %s) * (1 - (SELECT commission_rate FROM PurchaseTransaction WHERE userid = (SELECT userid FROM USER userid = %s))', (bitcoin_val, userid, ))
    #                 cursor.execute('UPDATE Client SET bitcoin = bitcoin + %s WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))
    #                 cursor.execute('UPDATE Client SET flatcurrency = flatcurrency - (10000 * %s) *(1 - 0.001)) WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))             

    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.001, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
    #             elif purchase_type == 'sell':
    #             # cursor.execute('UPDATE Client SET bitcoin = bitcoin - %s', (bitcoin_val, ))
    #                 cursor.execute('UPDATE Client SET bitcoin = bitcoin - %s WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))
    #                 cursor.execute('UPDATE Client SET flatcurrency = flatcurrency + (10000 * %s) *(1 - 0.001)) WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))                                 
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.001, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
    #         elif cursor.execute('SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (userid, )) == "silver":
    #             if purchase_type == 'buy':
    #                 cursor.execute('UPDATE Client SET bitcoin = bitcoin + %s WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))
    #                 cursor.execute('UPDATE Client SET flatcurrency = flatcurrency - (10000 * %s) *(1 - 0.01)) WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))             

    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.01, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
    #             elif purchase_type == 'sell':
    #                 cursor.execute('UPDATE Client SET bitcoin = bitcoin - %s WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))
    #                 cursor.execute('UPDATE Client SET flatcurrency = flatcurrency + (10000 * %s) *(1 - 0.01)) WHERE clientid = (SELECT userid FROM User WHERE userid = %s)', (bitcoin_val, userid, ))                                 
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.01, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
                    
    #         # end if
    #     elif user_type == "trader":
    #         request_id = data[1]
    #         # TODO: find the request given request_id and purchse the requested bitcoin buy/sell
    #         if cursor.execute('SELECT level FROM Client WHERE clientid = (SELECT clientid FROM Request WHERE clientid = %s)', (userid, )) == "gold":
    #             if purchase_type == 'buy':
    #             # cursor.execute('UPDATE Client SET bitcoin = bitcoin + %s', (bitcoin_val, ))
    #                 cursor.execute('UPDATE Trader SET bitcoin = bitcoin + %s WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))
    #                 cursor.execute('UPDATE Trader SET flatcurrency = flatcurrency - (10000 * %s) *(1 - 0.001)) WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))   
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.001, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
                    
    #             elif purchase_type == 'sell':
    #                 cursor.execute('UPDATE Trader SET bitcoin = bitcoin - %s WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))
    #                 cursor.execute('UPDATE Trader SET flatcurrency = flatcurrency + (10000 * %s) *(1 - 0.001)) WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))   
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.001, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
                    
    #         elif cursor.execute('SELECT level FROM Client WHERE clientid = (SELECT clientid FROM Request WHERE clientid = %s)', (userid, )) == "silver":
    #             if purchase_type == 'buy':
    #                 cursor.execute('UPDATE Trader SET bitcoin = bitcoin + %s WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))
    #                 cursor.execute('UPDATE Trader SET flatcurrency = flatcurrency - (10000 * %s) *(1 - 0.01)) WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))   
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.01, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
                    
               
    #             elif purchase_type == 'sell':
    #                 cursor.execute('UPDATE Trader SET bitcoin = bitcoin - %s WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))
    #                 cursor.execute('UPDATE Trader SET flatcurrency = flatcurrency + (10000 * %s) *(1 - 0.01)) WHERE traderid = (SELECT traderid FROM Request WHERE traderid = %s)', (bitcoin_val, request_id, ))   
    #                 cursor.execute('INSERT INTO PurchaseTransaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), (NOW()), (SELECT level FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), 0.01, %s, (SELECT flatcurrecy FROM Client WHERE clientid = (SELECT userid FROM User WHERE userid = %s)), %s, %s, )', (userid, bitcoin_value, userid, purchase_type, userid, ))
    #                 cursor.execute('INSERT INTO Transaction VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), NULL, (SELECT ptrid FROM PurchaseTransaction WHERE userid = (SELECT userid FROM User WHERE userid = %s)))', (userid, ))
    #                 cursor.execute('INSERT INTO Log VALUES ((SELECT FLOOR(200000+RAND()*(1-200000))), 'Bitcoin', (SELECT trid FROM Transaction WHERE purchase_trid = (SELECT ptrid FROM PurchaseTransaction WHERE userid = %s)))', (userid, ))
                    
                
    #     # end if
    #     mysql.connection.commit()
    #     pass

    @classmethod
    def transfer_money(cls, cursor, mysql, data):
        msg = ""
        trader = None
        user_type, userid, usd_val, transaction_date, transaction_time = data[0], data[1], data[2], data[3], data[4]
        if user_type=="client":
            # find the client's trader
            cursor.execute('SELECT traderid FROM Assign WHERE clientid = %s', [userid])
            traderid = cursor.fetchone()["traderid"]
            if traderid:

                cursor.execute('SELECT flatcurrency FROM Client WHERE clientid = %s', [userid])
                fiat_val = cursor.fetchone()["flatcurrency"]

                if float(fiat_val) >= float(usd_val):
                
                    # remove the amount of money from client
                    cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency - %s) WHERE clientid = %s', (usd_val, userid))
                    
                    # add the amount of money from client
                    cursor.execute('UPDATE Trader SET flatcurrency = (flatcurrency + %s)  WHERE traderid = %s', (usd_val, traderid))

                    # add the transaction to the transaction table
                    cursor.execute('INSERT INTO TransferTransaction(date, time, usd_value) VALUES (%s, %s, %s)', (transaction_date, transaction_time, usd_val))
                
                    # add log for the transfer transaction
                    cursor.execute('SELECT ttrid FROM TransferTransaction WHERE date = %s AND time = %s AND usd_value = %s', (transaction_date, transaction_time, usd_val))
                    ttrid = cursor.fetchone()["ttrid"]
                    
                    cursor.execute('INSERT INTO Transfer(ttrid, clientid, traderid) VALUES (%s, %s, %s)', (ttrid, userid, traderid))
                    cursor.execute('INSERT INTO Log(log_type, trid) VALUES (%s, %s)', ["update_transfertransaction", ttrid])
                    mysql.connection.commit()
                    msg = "Succeed"
                else:
                    msg = "Not enough money"
                # end if
            # end if
        # end if
        return msg

    @classmethod
    def cancel_transaction(cls, cursor, mysql, data):
        # log : (logid, log_type, trid)
        # log_type: [update_purchasetransaction, update_transfertransaction, cancel_purchasetransaction, cancel_transfertransaction]
        # only trader can cancel
        user_type, userid, transactionid, transactiontype = data[0], data[1], data[2], data[3]
        if transactiontype=="bitcoin":
            cursor.execute("""SELECT Pt.purchase_type, Pt.bitcoin_value, Pt.fiat_value, Pt.commission_rate Pt.commission_type
                              FROM PurchaseTransaction Pt, Trader_buysell Tb
                              WHERE Pt.ptrid = Tb.ptrid AND Tb.userid = %s""", [transactionid])
            trans_info = cursor.fetchone()
            purchase_type, bitcoin_value, fiat_value, commission_rate, commission_type = trans_info["Pt.purchase_type"], trans_info["Pt.bitcoin_value"], trans_info["Pt.fiat_value"], trans_info["Pt.commission_rate"], trans_info["Pt.commission_type"]
            if purchase_type=="buy":
                if commission_type == "bitcoin":
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin - %s*(1-%s)), flatcurrency = (flatcurrency + %s) WHERE traderid = %s', (bitcoin_value, commission_rate, fiat_value, userid))
                elif commission_type == "fiat":
                    # get the bitcoin and fiat value back to trader
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin - %s), flatcurrency = (flatcurrency + %s*(1+%s)) WHERE traderid = %s', (bitcoin_value, fiat_value, commission_rate, userid))
                # end if
            elif purchase_type=="sell":
                if commission_type == "bitcoin":
                    # get the bitcoin and fiat value back to trader
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s *(1+%s)), flatcurrency = (flatcurrency - %s) WHERE traderid = %s', (bitcoin_value, commission_rate, fiat_value, userid))
                elif commission_type == "fiat":
                    # get the bitcoin and fiat value back to trader
                    cursor.execute('UPDATE Trader SET bitcoin = (bitcoin + %s), flatcurrency = (flatcurrency - %s *(1-%s)) WHERE traderid = %s', (bitcoin_value, fiat_value, commission_rate, userid))
                # end if
            # end if
            
            # delete the tranaction from transaction table
            cursor.execute('DELETE FROM PurchaseTransaction WHERE trid = %s', [transactionid])
            cursor.execute('DELETE FROM Trader_buysell WHERE trid = %s AND userid = %s', (transactionid, userid))
            cursor.execute("INSERT INTO Log(log_type, trid) VALUES (%s, DEFAULT)", ["cancel_purchasetransaction"])
            mysql.connection.commit()
            
        elif transactiontype=="transfer":
            cursor.execute("""SELECT Tt.usd_value, Tr.clientid 
                              FROM TransferTransaction Tt, Tranfer Tr 
                              WHERE Tt.ttrid = Tr.ttrid AND Tr.ttrid = %s AND Tr.traderid = %s""", (transactionid, userid))
            trans_info = cursor.fetchone()
            usd_value, clientid = trans_info["Tt.usd_value"], trans_info["Tr.clientid"]

            # get the fiat value back to trader
            cursor.execute('UPDATE Trader SET flatcurrency = (flatcurrency - %s) WHERE traderid = %s', (usd_value, userid))
            cursor.execute('UPDATE Client SET flatcurrency = (flatcurrency + %s) WHERE clientid = %s', (usd_value, clientid))

            # delete the tranaction from transaction table
            cursor.execute('DELETE FROM TransferTransaction WHERE ttrid = %s', [transactionid])
            cursor.execute('DELETE FROM Transfer WHERE ttrid = %s AND traderid = %s AND clientid = %s', (transactionid, userid, clientid))
            cursor.execute('INSERT INTO Log(log_type, trid) VALUES (%s, %s)', ["cancel_transfertransaction", transactionid])
            mysql.connection.commit()
        # end if
        return

    @classmethod
    def update_level(cls, cursor, mysql, prev_month, cur_month, cur_year):
        fiat_threshold = Macros.fiat_threshold
        date_from = f"{cur_year}-{prev_month}-01"
        date_to = f"{cur_year}-{cur_month}-01"
        # update client's level from silver to gold for whom their fiat_value purchase amount is more than 100k
        cursor.execute("""UPDATE Client C SET level = gold
           WHERE C.clientid IN (
              SELECT clientid
              FROM Client C1
              WHERE %s <= (
                 SELECT SUM(fiat_value)
                 FROM PurchaseTransaction Ptr, Client_buysell Cb
                 WHERE (C1.clientid = Cb.userid) AND (Ptr.ptrid = Cb.ptrid) AND (Ptr.date BETWEEN %s AND %s)
              )
           )""", [str(fiat_threshold), date_from, date_to])

        # update client's level from silver to gold for whom their bitcoin purchase amount is more than 100k
        cursor.execute("""UPDATE Client C SET level = silver
           WHERE C.clientid IN (
              SELECT clientid
              FROM Client C1
              WHERE %s > (
                 SELECT SUM(fiat_value)
                 FROM PurchaseTransaction Ptr, Client_buysell Cb
                 WHERE (C1.clientid = Cb.userid) AND (Ptr.ptrid = Cb.ptrid) AND (Ptr.date BETWEEN %s AND %s)
              )
           )""", [str(fiat_threshold), date_from, date_to])
        mysql.connection.commit()
        return

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

    @classmethod
    def getBitcoinBalance():
        return 
