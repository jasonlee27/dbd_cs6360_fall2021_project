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
                        "type": 'manager',
                    }
                # end if
            else:
                clients = None # TODO: get all clients assigned to input trader
                account_info = {
                    "type": 'trader',
                    "bitcoin": account[3],
                    "flatcurrenty": account[4],
                    "clients": clients
                }
            # end if
        else:
            account_info = {
                "type": 'trader',
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
            # TODO: insert client account into DB
        elif user_type=="trader":
            # TODO: insert trader account into DB
        elif user_type=="manager":
            # TODO: insert manager account into DB
        # end if
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
                        "type": 'manager',
                    }
                # end if
            else:
                clients = None # TODO: get all clients assigned to input trader
                account_info = {
                    "type": 'trader',
                    "bitcoin": account[3],
                    "flatcurrenty": account[4],
                    "clients": clients
                }
            # end if
        else:
            account_info = {
                "type": 'trader',
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
    def get_user_transaction_history(cls, cursor, mysql, data):
        user_type, userid, time_period = data[0], data[1], data[2]
        # TODO: select transaction histories given userid
        # user_type: one out of [client, trader, manager]
        # time_period: one out of [daily, weekly, monthly]
        # in case of manager, it shows every transaction history over all
        # client and trader
        cursor.execute('select * from TransferTransaction where date between date_sub(now(),INTERVAL 1 %s) and now()', (time_period,))
        cursor.execute('select * from PurchaseTransaction where date between date_sub(now(),INTERVAL 1 %s) and now()', (time_period,))
        cursor.execute('select * from Transaction where date between date_sub(now(),INTERVAL 1 %s) and now()', (time_period,))
        
        #11/27 will display 3 table (TransferTransaction, PurchaseTransaction, Transaction), from 1 time_period to today's date, week, month, day
        pass

    @classmethod
    def set_bitcoin_request(cls, cursor, mysql, data):
        cliendid, bitcoin_val, purchase_type = data[0], data[1], data[2]
        # TODO: set bitcoin request to client's trader
        cursor.execute('INSERT INTO Request (rid, clientid, traderid, bitcoin_value, purchase_type) VALUES (%s, %s, %s, %s, %s)', (rid, clientid, traderid, bitcoin_val, purchase_type))
        
       
        pass

    @classmethod
    def get_bitcoin_requests(cls, cursor, mysql, data):
        # TODO: get bitcoin requests from client to trader
        userid, user_type = data[0], data[1]
        if user_type == 'client'
            cursor.execute('select * from request where clientid = %s', (userid,))
        else if user_type == 'trader'
            cursor.execute('select * from request where traderid = %s', (userid,))
            
        #11/27 don't know the exact variable name of user_type. I assume variable name is clientid and traderid here
        pass

    @classmethod
    def buysell_bitcoin(cls, cursor, mysql, data):
        # TODO: get bitcoin buy/sell in database
        user_type, bitcoin_val, purchase_type = data[0], data[1], data[2]
        if purchase_type == 'buy'
            cursor.execute('update Client set bitcoin = bitcoin + %s', (bitcoin_val, ))
        else if purchase_type == 'sell'
            cursor.execute('update Client set bitcoin = bitcoin - %s', (bitcoin_val, ))
        #11/27 do we need to determine the user type here, I just classify buy and sell here
        pass

    @classmethod
    def cancel_transaction(cls, cursor, mysql, transactionid):
        # TODO: cancel transaction in database
        # 1. delete transaction specified
        # 2. update log and its status
        cursor.execute('delete from TransferTransaction where trid = %s', (transactionid, ))
        cursor.execute('INSERT INTO Cancel VALUEs(%s, %s, %s)', (cid, traderid, trid, ))
        
        #11/27, should we use table 'Cancel' or 'Log' for the log updating, I just update "Cancel' here. how to hold variable that did not occur in function parameter


        pass    
