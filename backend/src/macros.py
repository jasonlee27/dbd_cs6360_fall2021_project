
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
    MYSQL_PASSWORD = 'password'
    MYSQL_DB = 'bts_db'

    PORT_NUM = 3000
