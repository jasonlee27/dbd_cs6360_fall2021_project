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
INSERT INTO `Address` VALUES ('123 example st','apt 123','dallas','12345','tx'),('123 example st','apt 1234','dallas','12345','tx');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assign`
--

LOCK TABLES `Assign` WRITE;
/*!40000 ALTER TABLE `Assign` DISABLE KEYS */;
INSERT INTO `Assign` VALUES (3,'34d701b29bdc6a03bc5c3a95ad8a1aa9','1f97495b9afabdb61c273ba698428369'),(2,'37024c43717c26ef73740bbb49c7d201','c3634bbe395bb171d92259827aa41032'),(4,'3d9197e3b26aae747880c16ad3c7d39b','047e562392f027c9fc4c0761749df8dc'),(7,'468d05de932d6ebdd46692bb7572c774','047e562392f027c9fc4c0761749df8dc'),(6,'8750185290ff8573c28eb4104ace1bd8','1f97495b9afabdb61c273ba698428369'),(1,'f1e7c6edbfc5bfe10b38ada554c8fe25','047e562392f027c9fc4c0761749df8dc'),(5,'f2c323964f4751058196d6ad6859239b','c3634bbe395bb171d92259827aa41032');
/*!40000 ALTER TABLE `Assign` ENABLE KEYS */;
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
INSERT INTO `Client` VALUES ('34d701b29bdc6a03bc5c3a95ad8a1aa9','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:43:08','yibo','li','123 example st','apt 123','dallas','12345','tx','0123456789','0123456789','yibo123@example.com','silver',0.000,600.000),('37024c43717c26ef73740bbb49c7d201','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:42:01','jane','doe','123 example st','apt 123','dallas','12345','tx','0123456789','0123456789','janedoe123@example.com','silver',0.000,600.000),('3d9197e3b26aae747880c16ad3c7d39b','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:44:09','megan','tran','123 example st','apt 123','dallas','12345','tx','0123456789','0123456789','megan123@example.com','silver',0.000,600.000),('468d05de932d6ebdd46692bb7572c774','6a201185e0e1b7409973c8519ca56914','2021-12-05_23:41:37','brian','Ng','123 example st','apt 123','dallas','12345','tx','1234567890','1234567890','brian123@example.com','silver',0.000,1500.000),('8750185290ff8573c28eb4104ace1bd8','6a201185e0e1b7409973c8519ca56914','2021-12-05_23:39:30','messi','lionel','123 example st','apt 1234','dallas','12345','tx','0123456789','0123456789','messi123@example.com','silver',0.000,18000.000),('f1e7c6edbfc5bfe10b38ada554c8fe25','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:41:13','jason','lee','123 example st','apt 123','dallas','12345','tx','0123456789','0123456789','jasonlee123@example.com','silver',0.000,600.000),('f2c323964f4751058196d6ad6859239b','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:45:16','murat','kant','123 example st','apt 123','dallas','12345','tx','0123456789','0123456789','murat123@example.com','silver',0.000,600.000);
/*!40000 ALTER TABLE `Client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Client_buysell`
--

DROP TABLE IF EXISTS `Client_buysell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Client_buysell` (
  `bsid` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) DEFAULT NULL,
  `ptrid` int DEFAULT NULL,
  PRIMARY KEY (`bsid`),
  KEY `userid` (`userid`),
  KEY `ptrid` (`ptrid`),
  CONSTRAINT `client_buysell_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `client_buysell_ibfk_2` FOREIGN KEY (`ptrid`) REFERENCES `PurchaseTransaction` (`ptrid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Client_buysell`
--

LOCK TABLES `Client_buysell` WRITE;
/*!40000 ALTER TABLE `Client_buysell` DISABLE KEYS */;
/*!40000 ALTER TABLE `Client_buysell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log`
--

DROP TABLE IF EXISTS `Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Log` (
  `logid` int NOT NULL AUTO_INCREMENT,
  `log_type` varchar(50) DEFAULT NULL,
  `trid` int DEFAULT NULL,
  PRIMARY KEY (`logid`),
  UNIQUE KEY `log_type` (`log_type`,`trid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log`
--

LOCK TABLES `Log` WRITE;
/*!40000 ALTER TABLE `Log` DISABLE KEYS */;
INSERT INTO `Log` VALUES (1,'update_transfertransaction',1),(2,'update_transfertransaction',2),(3,'update_transfertransaction',3),(4,'update_transfertransaction',4),(5,'update_transfertransaction',5),(6,'update_transfertransaction',6),(7,'update_transfertransaction',7);
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
INSERT INTO `Manager` VALUES ('127c1a6429a7767aae1b8bcb2c5f242e','6a201185e0e1b7409973c8519ca56914');
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
INSERT INTO `Name` VALUES ('brian','Ng'),('james','lee'),('jane','doe'),('jason','lee'),('megan','tran'),('messi','lionel'),('murat','kant'),('sam','kim'),('yibo','li');
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
  `time` varchar(50) DEFAULT NULL,
  `commission_type` varchar(50) DEFAULT NULL,
  `commission_rate` float(3,3) DEFAULT NULL,
  `bitcoin_value` float(8,3) DEFAULT NULL,
  `fiat_value` float(8,3) DEFAULT NULL,
  `purchase_type` varchar(4) DEFAULT NULL,
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
  `commission_type` varchar(50) DEFAULT NULL,
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
INSERT INTO `Trader` VALUES ('047e562392f027c9fc4c0761749df8dc','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:38:48','jason','lee',0.000,1300.000),('1f97495b9afabdb61c273ba698428369','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:39:30','sam','kim',0.000,2400.000),('c3634bbe395bb171d92259827aa41032','6a201185e0e1b7409973c8519ca56914','2021-12-05_22:39:11','james','lee',0.000,800.000);
/*!40000 ALTER TABLE `Trader` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trader_buysell`
--

DROP TABLE IF EXISTS `Trader_buysell`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Trader_buysell` (
  `bsid` int NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) DEFAULT NULL,
  `ptrid` int DEFAULT NULL,
  PRIMARY KEY (`bsid`),
  KEY `userid` (`userid`),
  KEY `ptrid` (`ptrid`),
  CONSTRAINT `trader_buysell_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `Trader` (`traderid`),
  CONSTRAINT `trader_buysell_ibfk_2` FOREIGN KEY (`ptrid`) REFERENCES `PurchaseTransaction` (`ptrid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trader_buysell`
--

LOCK TABLES `Trader_buysell` WRITE;
/*!40000 ALTER TABLE `Trader_buysell` DISABLE KEYS */;
/*!40000 ALTER TABLE `Trader_buysell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transfer`
--

DROP TABLE IF EXISTS `Transfer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Transfer` (
  `tfid` int NOT NULL AUTO_INCREMENT,
  `ttrid` int DEFAULT NULL,
  `clientid` varchar(50) DEFAULT NULL,
  `traderid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tfid`),
  KEY `ttrid` (`ttrid`),
  KEY `clientid` (`clientid`),
  KEY `traderid` (`traderid`),
  CONSTRAINT `transfer_ibfk_1` FOREIGN KEY (`ttrid`) REFERENCES `TransferTransaction` (`ttrid`),
  CONSTRAINT `transfer_ibfk_2` FOREIGN KEY (`clientid`) REFERENCES `Client` (`clientid`),
  CONSTRAINT `transfer_ibfk_3` FOREIGN KEY (`traderid`) REFERENCES `Trader` (`traderid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transfer`
--

LOCK TABLES `Transfer` WRITE;
/*!40000 ALTER TABLE `Transfer` DISABLE KEYS */;
INSERT INTO `Transfer` VALUES (1,1,'f1e7c6edbfc5bfe10b38ada554c8fe25','047e562392f027c9fc4c0761749df8dc'),(2,2,'37024c43717c26ef73740bbb49c7d201','c3634bbe395bb171d92259827aa41032'),(3,3,'34d701b29bdc6a03bc5c3a95ad8a1aa9','1f97495b9afabdb61c273ba698428369'),(4,4,'3d9197e3b26aae747880c16ad3c7d39b','047e562392f027c9fc4c0761749df8dc'),(5,5,'f2c323964f4751058196d6ad6859239b','c3634bbe395bb171d92259827aa41032'),(6,6,'468d05de932d6ebdd46692bb7572c774','047e562392f027c9fc4c0761749df8dc'),(7,7,'8750185290ff8573c28eb4104ace1bd8','1f97495b9afabdb61c273ba698428369');
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
  `time` varchar(50) DEFAULT NULL,
  `usd_value` float(8,3) DEFAULT NULL,
  PRIMARY KEY (`ttrid`),
  CONSTRAINT `transfer_usdvalue_constraint` CHECK ((`usd_value` >= 0.0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransferTransaction`
--

LOCK TABLES `TransferTransaction` WRITE;
/*!40000 ALTER TABLE `TransferTransaction` DISABLE KEYS */;
INSERT INTO `TransferTransaction` VALUES (1,'2021-12-05','22:52:28',400.000),(2,'2021-12-05','22:52:50',400.000),(3,'2021-12-05','22:53:04',400.000),(4,'2021-12-05','22:53:22',400.000),(5,'2021-12-05','22:53:39',400.000),(6,'2021-12-05','23:42:09',500.000),(7,'2021-12-05','23:42:33',2000.000);
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
INSERT INTO `User` VALUES ('047e562392f027c9fc4c0761749df8dc','6a201185e0e1b7409973c8519ca56914'),('127c1a6429a7767aae1b8bcb2c5f242e','6a201185e0e1b7409973c8519ca56914'),('1f97495b9afabdb61c273ba698428369','6a201185e0e1b7409973c8519ca56914'),('34d701b29bdc6a03bc5c3a95ad8a1aa9','6a201185e0e1b7409973c8519ca56914'),('37024c43717c26ef73740bbb49c7d201','6a201185e0e1b7409973c8519ca56914'),('3d9197e3b26aae747880c16ad3c7d39b','6a201185e0e1b7409973c8519ca56914'),('468d05de932d6ebdd46692bb7572c774','6a201185e0e1b7409973c8519ca56914'),('8750185290ff8573c28eb4104ace1bd8','6a201185e0e1b7409973c8519ca56914'),('c3634bbe395bb171d92259827aa41032','6a201185e0e1b7409973c8519ca56914'),('f1e7c6edbfc5bfe10b38ada554c8fe25','6a201185e0e1b7409973c8519ca56914'),('f2c323964f4751058196d6ad6859239b','6a201185e0e1b7409973c8519ca56914');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-05 23:42:43
