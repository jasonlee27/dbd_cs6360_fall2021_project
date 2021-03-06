
from typing import *

import os
import hashlib

from pathlib import Path

class Macros:

    KEY_STR = "jasonlee_secret_key"
    SECRETE_KEY = hashlib.sha256(KEY_STR.encode('utf-8')).hexdigest()

    SRC_DIR: Path = Path(os.path.dirname(os.path.realpath(__file__)))
    ROOT_DIR: Path = SRC_DIR.parent.parent
    BACKEND_DIR: Path = SRC_DIR.parent
    FRONTEND_DIR: Path = ROOT_DIR / "frontend"

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Password2021!'
    MYSQL_DB = 'bts_db'

    PORT_NUM = 3306


    # commission rate in percentage
    COMMISSION_RATE = {
        'silver': 0.01,
        'gold': 0.005
    }

    # threshold amount of fiat currency for deciding client's level
    fiat_threshold = 100000
