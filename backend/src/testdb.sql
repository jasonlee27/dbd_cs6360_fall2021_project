-- MySQL dump 10.13  Distrib 8.0.26, for macos11.3 (x86_64)
--
-- Host: localhost    Database: bts_db
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Address` (
  `address1` varchar(30) NOT NULL,
  `address2` varchar(30) NOT NULL,
  `city` varchar(25) NOT NULL,
  `zipcode` varchar(10) NOT NULL,
  `state` varchar(2) NOT NULL,
  PRIMARY KEY (`address1`,`address2`,`city`,`zipcode`,`state`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
INSERT INTO `Address` VALUES ('123 example st','apt 123','dallas','12345','tx'),('123 example2 st','apt 123','dallas','12345','tx'),('123 example3 st','apt 123','dallas','12345','tx'),('123 example4 st','apt 123','dallas','12345','tx'),('123 example5 st','apt 123','dallas','12345','tx'),('123 example6 st','apt 123','dallas','12345','tx'),('123 example7 st','apt 123','dallas','12345','tx');
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Assign`
--

DROP TABLE IF EXISTS `Assign`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Assign` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `clientid` varchar(50) NOT NULL,
  `traderid` varchar(50) NOT NULL,
  PRIMARY KEY (`aid`),
  UNIQUE KEY `clientid` (`clientid`,`traderid`),
  KEY `traderid` (`traderid`),
  CONSTRAINT `assign_ibfk_1` FOREIGN KEY (`clientid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `assign_ibfk_2` FOREIGN KEY (`traderid`) REFERENCES `Trader` (`traderid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assign`
--

LOCK TABLES `Assign` WRITE;
/*!40000 ALTER TABLE `Assign` DISABLE KEYS */;
/*!40000 ALTER TABLE `Assign` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Buysell`
--

DROP TABLE IF EXISTS `Buysell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Buysell` (
  `bsid` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) DEFAULT NULL,
  `transactionid` int NOT NULL,
  PRIMARY KEY (`bsid`),
  KEY `userid` (`userid`),
  KEY `transactionid` (`transactionid`),
  CONSTRAINT `buysell_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `buysell_ibfk_2` FOREIGN KEY (`transactionid`) REFERENCES `Transaction` (`trid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Buysell`
--

LOCK TABLES `Buysell` WRITE;
/*!40000 ALTER TABLE `Buysell` DISABLE KEYS */;
/*!40000 ALTER TABLE `Buysell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Client`
--

DROP TABLE IF EXISTS `Client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Client` (
  `clientid` varchar(50) NOT NULL,
  `client_password` varchar(50) NOT NULL,
  `register_date` varchar(50) DEFAULT NULL,
  `firstname` varchar(15) DEFAULT NULL,
  `lastname` varchar(15) DEFAULT NULL,
  `address1` varchar(30) DEFAULT NULL,
  `address2` varchar(30) DEFAULT NULL,
  `city` varchar(25) DEFAULT NULL,
  `zipcode` varchar(10) DEFAULT NULL,
  `state` varchar(2) DEFAULT NULL,
  `cellphone` varchar(15) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `level` varchar(10) DEFAULT NULL,
  `bitcoin` float(8,3) DEFAULT NULL,
  `flatcurrency` float(8,3) DEFAULT NULL,
  PRIMARY KEY (`clientid`),
  KEY `firstname` (`firstname`,`lastname`),
  KEY `address1` (`address1`,`address2`,`city`,`zipcode`,`state`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`clientid`) REFERENCES `User` (`userid`) ON DELETE CASCADE,
  CONSTRAINT `client_ibfk_2` FOREIGN KEY (`firstname`, `lastname`) REFERENCES `Name` (`firstname`, `lastname`),
  CONSTRAINT `client_ibfk_3` FOREIGN KEY (`address1`, `address2`, `city`, `zipcode`, `state`) REFERENCES `Address` (`address1`, `address2`, `city`, `zipcode`, `state`),
  CONSTRAINT `client_bitcoin_constraint` CHECK ((`bitcoin` >= 0.0)),
  CONSTRAINT `clientflatcurrency_constraint` CHECK ((`flatcurrency` >= 0.0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Client`
--

LOCK TABLES `Client` WRITE;
/*!40000 ALTER TABLE `Client` DISABLE KEYS */;
INSERT INTO `Client` VALUES ('210b093ccbc29f51ec1f53bcc8229dbb','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:35:56','megan','tran','123 example4 st','apt 123','dallas','12345','tx','4691234567','4691234567','megantran123@example.com','silver',0.000,0.000),('37024c43717c26ef73740bbb49c7d201','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:34:07','jane','doe','123 example2 st','apt 123','dallas','12345','tx','4691234567','4691234567','janedoe123@example.com','silver',0.000,0.000),('3882ad191059fcabcdc2e77931965657','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:37:34','gab','goldstein','123 example5 st','apt 123','dallas','12345','tx','4691234567','4691234567','gabgold123@example.com','silver',0.000,0.000),('47ea35a30fc66924cf8662185b62f63b','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:39:49','mestan','firat','123 example7 st','apt 123','dallas','12345','tx','4691234567','4691234567','firat123@example.com','silver',0.000,0.000),('c3aa8559e20a699fb91eab3887105eb5','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:35:05','yibo','li','123 example3 st','apt 123','dallas','12345','tx','4691234567','4691234567','yiboli123@example.com','silver',0.000,0.000),('f1e7c6edbfc5bfe10b38ada554c8fe25','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:33:10','jason','lee','123 example st','apt 123','dallas','12345','tx','4691234567','4691234567','jasonlee123@example.com','silver',0.000,0.000),('f2c323964f4751058196d6ad6859239b','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:38:44','murat','kant','123 example6 st','apt 123','dallas','12345','tx','4691234567','4691234567','murat123@example.com','silver',0.000,0.000);
/*!40000 ALTER TABLE `Client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log`
--

DROP TABLE IF EXISTS `Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Log` (
  `logid` int NOT NULL AUTO_INCREMENT,
  `log_type` varchar(10) DEFAULT NULL,
  `trid` int DEFAULT NULL,
  PRIMARY KEY (`logid`),
  UNIQUE KEY `log_type` (`log_type`,`trid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log`
--

LOCK TABLES `Log` WRITE;
/*!40000 ALTER TABLE `Log` DISABLE KEYS */;
/*!40000 ALTER TABLE `Log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Manager` (
  `managerid` varchar(50) NOT NULL,
  `manager_password` varchar(50) NOT NULL,
  PRIMARY KEY (`managerid`),
  CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`managerid`) REFERENCES `User` (`userid`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES ('4b4226e7f52d16351ce8c5a13b7d4a18','30fd57c60df172ced919ae6fd460abad');
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Name`
--

DROP TABLE IF EXISTS `Name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Name` (
  `firstname` varchar(15) NOT NULL,
  `lastname` varchar(15) NOT NULL,
  PRIMARY KEY (`firstname`,`lastname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Name`
--

LOCK TABLES `Name` WRITE;
/*!40000 ALTER TABLE `Name` DISABLE KEYS */;
INSERT INTO `Name` VALUES ('gab','goldstein'),('james','smith'),('jane','doe'),('jason','lee'),('maria','smith'),('megan','tran'),('mestan','firat'),('murat','kant'),('sam','smith'),('yibo','li');
/*!40000 ALTER TABLE `Name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PurchaseTransaction`
--

DROP TABLE IF EXISTS `PurchaseTransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PurchaseTransaction` (
  `ptrid` int NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `commision_type` varchar(50) DEFAULT NULL,
  `commission_rate` float(3,3) DEFAULT NULL,
  `bitcoin_value` float(8,3) DEFAULT NULL,
  `fiat_value` float(8,3) DEFAULT NULL,
  `purchase_type` varchar(4) DEFAULT NULL,
  `userid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ptrid`),
  CONSTRAINT `purchase_bitcoinvalue_constraint` CHECK ((`bitcoin_value` >= 0.0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PurchaseTransaction`
--

LOCK TABLES `PurchaseTransaction` WRITE;
/*!40000 ALTER TABLE `PurchaseTransaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `PurchaseTransaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Request`
--

DROP TABLE IF EXISTS `Request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Request` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `clientid` varchar(50) NOT NULL,
  `traderid` varchar(50) NOT NULL,
  `bitcoin_value` float(8,3) NOT NULL,
  `purchase_type` varchar(5) NOT NULL,
  PRIMARY KEY (`rid`),
  KEY `clientid` (`clientid`),
  KEY `traderid` (`traderid`),
  CONSTRAINT `request_ibfk_1` FOREIGN KEY (`clientid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `request_ibfk_2` FOREIGN KEY (`traderid`) REFERENCES `Trader` (`traderid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Request`
--

LOCK TABLES `Request` WRITE;
/*!40000 ALTER TABLE `Request` DISABLE KEYS */;
/*!40000 ALTER TABLE `Request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trader`
--

DROP TABLE IF EXISTS `Trader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Trader` (
  `traderid` varchar(50) NOT NULL,
  `trader_password` varchar(50) NOT NULL,
  `register_date` varchar(50) DEFAULT NULL,
  `firstname` varchar(15) DEFAULT NULL,
  `lastname` varchar(15) DEFAULT NULL,
  `bitcoin` float(8,3) DEFAULT NULL,
  `flatcurrency` float(8,3) DEFAULT NULL,
  PRIMARY KEY (`traderid`),
  KEY `firstname` (`firstname`,`lastname`),
  CONSTRAINT `trader_ibfk_1` FOREIGN KEY (`traderid`) REFERENCES `User` (`userid`) ON DELETE CASCADE,
  CONSTRAINT `trader_ibfk_2` FOREIGN KEY (`firstname`, `lastname`) REFERENCES `Name` (`firstname`, `lastname`),
  CONSTRAINT `trader_bitcoin_constraint` CHECK ((`bitcoin` >= 0.0)),
  CONSTRAINT `trader_flatcurrency_constraint` CHECK ((`flatcurrency` >= 0.0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trader`
--

LOCK TABLES `Trader` WRITE;
/*!40000 ALTER TABLE `Trader` DISABLE KEYS */;
INSERT INTO `Trader` VALUES ('1f97495b9afabdb61c273ba698428369','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:44:29','sam','smith',0.000,0.000),('c3634bbe395bb171d92259827aa41032','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:42:46','james','smith',0.000,0.000),('f3a95a7279d65d1ba379978e09ca461f','6a201185e0e1b7409973c8519ca56914','2021-12-05_13:43:59','maria','smith',0.000,0.000);
/*!40000 ALTER TABLE `Trader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaction`
--

DROP TABLE IF EXISTS `Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transaction` (
  `trid` int NOT NULL AUTO_INCREMENT,
  `transfer_trid` int DEFAULT NULL,
  `purchase_trid` int DEFAULT NULL,
  PRIMARY KEY (`trid`),
  KEY `transfer_trid` (`transfer_trid`),
  KEY `purchase_trid` (`purchase_trid`),
  CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`transfer_trid`) REFERENCES `TransferTransaction` (`ttrid`),
  CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`purchase_trid`) REFERENCES `PurchaseTransaction` (`ptrid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaction`
--

LOCK TABLES `Transaction` WRITE;
/*!40000 ALTER TABLE `Transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transfer`
--

DROP TABLE IF EXISTS `Transfer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transfer` (
  `tid` int NOT NULL AUTO_INCREMENT,
  `clientid` varchar(50) DEFAULT NULL,
  `transactionid` int NOT NULL,
  PRIMARY KEY (`tid`),
  KEY `clientid` (`clientid`),
  KEY `transactionid` (`transactionid`),
  CONSTRAINT `transfer_ibfk_1` FOREIGN KEY (`clientid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `transfer_ibfk_2` FOREIGN KEY (`transactionid`) REFERENCES `Transaction` (`trid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transfer`
--

LOCK TABLES `Transfer` WRITE;
/*!40000 ALTER TABLE `Transfer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transfer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TransferTransaction`
--

DROP TABLE IF EXISTS `TransferTransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TransferTransaction` (
  `ttrid` int NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `usd_value` float(8,3) DEFAULT NULL,
  `clientid` varchar(50) DEFAULT NULL,
  `traderid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ttrid`),
  CONSTRAINT `transfer_usdvalue_constraint` CHECK ((`usd_value` >= 0.0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransferTransaction`
--

LOCK TABLES `TransferTransaction` WRITE;
/*!40000 ALTER TABLE `TransferTransaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `TransferTransaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `userid` varchar(50) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('1f97495b9afabdb61c273ba698428369','6a201185e0e1b7409973c8519ca56914'),('210b093ccbc29f51ec1f53bcc8229dbb','6a201185e0e1b7409973c8519ca56914'),('37024c43717c26ef73740bbb49c7d201','6a201185e0e1b7409973c8519ca56914'),('3882ad191059fcabcdc2e77931965657','6a201185e0e1b7409973c8519ca56914'),('47ea35a30fc66924cf8662185b62f63b','6a201185e0e1b7409973c8519ca56914'),('4b4226e7f52d16351ce8c5a13b7d4a18','30fd57c60df172ced919ae6fd460abad'),('c3634bbe395bb171d92259827aa41032','6a201185e0e1b7409973c8519ca56914'),('c3aa8559e20a699fb91eab3887105eb5','6a201185e0e1b7409973c8519ca56914'),('f1e7c6edbfc5bfe10b38ada554c8fe25','6a201185e0e1b7409973c8519ca56914'),('f2c323964f4751058196d6ad6859239b','6a201185e0e1b7409973c8519ca56914'),('f3a95a7279d65d1ba379978e09ca461f','6a201185e0e1b7409973c8519ca56914');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'bts_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-05 13:47:23
