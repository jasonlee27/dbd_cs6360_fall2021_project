#!/bin/bash

readonly _DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
readonly SRC_DIR="${_DIR}/src"
readonly DB_INIT_FILE="${SRC_DIR}/tables.sql"
readonly OS_TYPE="${OSTYPE}"

function main() {        
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
                # linux
                main_linux
        elif [[ "$OSTYPE" == "darwin"* ]]; then
                # Mac OSX
                main_macos
        fi
}

function main_linux() {
        sudo service mysql start # start mysql server
        # sudo service mysql status
        sudo mysql -u root < ${DB_INIT_FILE}
        (cd ${SRC_DIR}
         python app.py
        )
        sudo service mysql stop # stop mysql server
        # sudo service mysql status
}
function main_macos() {
        mysql.server start
        mysql -u root < ${DB_INIT_FILE}
        (cd ${SRC_DIR}
         python app.py
        )
        mysql.server stop
}

main
