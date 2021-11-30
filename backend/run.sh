#!/bin/bash

readonly _DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
readonly SRC_DIR="${_DIR}/src"
readonly DB_INIT_FILE="${SRC_DIR}/tables.sql"

function main() {
        init_sql_tables
        (cd ${SRC_DIR}
         python app.py
        )
        mysql.server stop
}

function init_sql_tables() {
        mysql.server start
        mysql -u root < ${DB_INIT_FILE}
}

main
