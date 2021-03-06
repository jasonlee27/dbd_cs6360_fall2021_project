CREATE DATABASE IF NOT EXISTS `bts_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `bts_db`;

CREATE TABLE IF NOT EXISTS User(
    userid VARCHAR(50) not null,
    user_password VARCHAR(50) not null,
    PRIMARY KEY(userid)
);

CREATE TABLE IF NOT EXISTS Name(
    firstname VARCHAR(15),
    lastname VARCHAR(15),
    PRIMARY KEY(firstname, lastname)
);

CREATE TABLE IF NOT EXISTS Address(
    address1 VARCHAR(30),
    address2 VARCHAR(30),
    city VARCHAR(25),
    zipcode VARCHAR(10),
    state VARCHAR(2),
    PRIMARY KEY(address1, address2, city, zipcode, state)
);

CREATE TABLE IF NOT EXISTS Client(
    clientid VARCHAR(50) not null,
    client_password VARCHAR(50) not null,
    register_date VARCHAR(50),
    firstname VARCHAR(15),
    lastname VARCHAR(15),
    address1 VARCHAR(30),
    address2 VARCHAR(30),
    city VARCHAR(25),
    zipcode VARCHAR(10),
    state VARCHAR(2),
    cellphone VARCHAR(15),
    phone VARCHAR(15),
    email VARCHAR(30),
    level VARCHAR(10),
    bitcoin FLOAT(8,3),
    flatcurrency FLOAT(8,3),
    PRIMARY KEY(clientid),
    FOREIGN KEY (clientid) REFERENCES User(userid) ON DELETE CASCADE,
    FOREIGN KEY (firstname, lastname) REFERENCES Name(firstname, lastname) ON UPDATE NO ACTION,
    FOREIGN KEY (address1, address2, city, zipcode, state) REFERENCES Address(address1, address2, city, zipcode, state) ON UPDATE NO ACTION,
    CONSTRAINT client_bitcoin_constraint CHECK (bitcoin>=0.0),
    CONSTRAINT clientflatcurrency_constraint CHECK (flatcurrency>=0.0)
);

CREATE TABLE IF NOT EXISTS Trader(
    traderid VARCHAR(50) not null,
    trader_password VARCHAR(50) not null,
    register_date VARCHAR(50),
    firstname VARCHAR(15),
    lastname VARCHAR(15),
    bitcoin FLOAT(8,3),
    flatcurrency FLOAT(8,3),
    PRIMARY KEY(traderid),
    FOREIGN KEY (traderid) REFERENCES User(userid) ON DELETE CASCADE,
    FOREIGN KEY (firstname, lastname) REFERENCES Name(firstname, lastname) ON UPDATE NO ACTION,
    CONSTRAINT trader_bitcoin_constraint CHECK (bitcoin>=0.0),
    CONSTRAINT trader_flatcurrency_constraint CHECK (flatcurrency>=0.0)
);

CREATE TABLE IF NOT EXISTS Manager(
    managerid VARCHAR(50) not null,
    manager_password VARCHAR(50) not null,
    PRIMARY KEY(managerid),
    FOREIGN KEY (managerid) REFERENCES User(userid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS TransferTransaction(
    ttrid INT AUTO_INCREMENT not null,
    date VARCHAR(50),
    time VARCHAR(50),
    usd_value FLOAT(8,3),
    -- clientid VARCHAR(50),
    -- traderid VARCHAR(50),
    PRIMARY KEY(ttrid),
    CONSTRAINT transfer_usdvalue_constraint CHECK (usd_value>=0.0)
);

CREATE TABLE IF NOT EXISTS PurchaseTransaction(
    ptrid INT AUTO_INCREMENT not null,
    date VARCHAR(50),
    time VARCHAR(50),
    commission_type VARCHAR(50),
    commission_rate FLOAT(3,3),
    -- commission_fee FLOAT(8,3),
    bitcoin_value FLOAT(8,3),
    fiat_value FLOAT(8,3),
    purchase_type VARCHAR(4), -- buy or sell bitcoin
    -- userid VARCHAR(50),
    PRIMARY KEY(ptrid),
    CONSTRAINT purchase_bitcoinvalue_constraint CHECK (bitcoin_value>=0.0)
);

CREATE TABLE IF NOT EXISTS Log(
    logid INT AUTO_INCREMENT not null,
    log_type VARCHAR(50),
    trid INT DEFAULT NULL,
    UNIQUE(log_type, trid),
    PRIMARY KEY(logid)
);

CREATE TABLE IF NOT EXISTS Assign(
    aid INT AUTO_INCREMENT not null,
    clientid VARCHAR(50) not null,
    traderid VARCHAR(50) not null,
    PRIMARY KEY (aid),
    UNIQUE(clientid, traderid),
    FOREIGN KEY (clientid) REFERENCES Client(clientid),
    FOREIGN KEY (traderid) REFERENCES Trader(traderid)
);

CREATE TABLE IF NOT EXISTS Request(
    rid INT AUTO_INCREMENT not null,
    clientid VARCHAR(50) not null,
    traderid VARCHAR(50) not null,
    bitcoin_value FLOAT(8,3) not null,
    commission_type VARCHAR(50),
    purchase_type VARCHAR(5) not null,
    PRIMARY KEY (rid),
    FOREIGN KEY (clientid) REFERENCES Client(clientid),
    FOREIGN KEY (traderid) REFERENCES Trader(traderid)
);

CREATE TABLE IF NOT EXISTS Transfer(
    tfid INT AUTO_INCREMENT not null,
    ttrid INT,
    clientid VARCHAR(50),
    traderid VARCHAR(50),
    PRIMARY KEY (tfid),
    FOREIGN KEY (ttrid) REFERENCES TransferTransaction(ttrid),
    FOREIGN KEY (clientid) REFERENCES Client(clientid),
    FOREIGN KEY (traderid) REFERENCES Trader(traderid)
);

CREATE TABLE IF NOT EXISTS Client_buysell(
   bsid INT AUTO_INCREMENT not null,
   userid VARCHAR(50),
   ptrid INT,
   PRIMARY KEY (bsid),
   FOREIGN KEY (userid) REFERENCES Client(clientid),
   FOREIGN KEY (ptrid) REFERENCES PurchaseTransaction(ptrid)
);

CREATE TABLE IF NOT EXISTS Trader_buysell(
   bsid INT AUTO_INCREMENT not null,
   userid VARCHAR(50),
   ptrid INT,
   PRIMARY KEY (bsid),
   FOREIGN KEY (userid) REFERENCES Trader(traderid),
   FOREIGN KEY (ptrid) REFERENCES PurchaseTransaction(ptrid)
);

-- CREATE TABLE IF NOT EXISTS Cancel(
--     cid INT AUTO_INCREMENT not null,
--     traderid VARCHAR(50),
--     transactionid INT not null,
--     PRIMARY KEY(cid),
--     FOREIGN KEY (traderid) REFERENCES Trader(traderid),
--     FOREIGN KEY (transactionid) REFERENCES Transaction(trid)
-- );
