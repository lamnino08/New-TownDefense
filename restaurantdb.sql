-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: localhost    Database: restaurantdb
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `BillID` int unsigned NOT NULL AUTO_INCREMENT,
  `TableID` int unsigned DEFAULT NULL,
  `IsAvailable` tinyint(1) DEFAULT NULL,
  `TotalPrice` float DEFAULT NULL,
  `IsPayed` tinyint(1) DEFAULT NULL,
  `Time` datetime DEFAULT NULL,
  PRIMARY KEY (`BillID`),
  KEY `FK_Table_Bill` (`TableID`),
  CONSTRAINT `FK_Table_Bill` FOREIGN KEY (`TableID`) REFERENCES `table` (`TableID`)
) ENGINE=InnoDB AUTO_INCREMENT=187 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,1,1,150,1,'2024-10-19 12:00:00'),(2,2,1,200,1,'2024-10-19 13:00:00'),(3,3,1,120,1,'2024-10-19 14:00:00'),(4,4,1,175,1,'2024-10-19 15:00:00'),(5,5,1,95,1,'2024-10-19 16:00:00'),(6,6,1,220,1,'2024-10-19 17:00:00'),(7,7,1,180,1,'2024-10-20 12:00:00'),(8,8,1,145,1,'2024-10-20 13:00:00'),(9,9,1,160,1,'2024-10-20 14:00:00'),(10,10,1,175,1,'2024-10-20 15:00:00'),(11,11,1,250,1,'2024-10-20 16:00:00'),(12,12,1,215,1,'2024-10-20 17:00:00'),(13,13,1,230,1,'2024-10-21 12:00:00'),(14,14,1,185,1,'2024-10-21 13:00:00'),(15,15,1,145,1,'2024-10-21 14:00:00'),(16,16,1,190,1,'2024-10-21 15:00:00'),(17,17,1,130,1,'2024-10-21 16:00:00'),(18,18,1,220,1,'2024-10-21 17:00:00'),(19,19,1,175,1,'2024-10-22 12:00:00'),(20,20,1,165,1,'2024-10-22 13:00:00'),(21,1,1,140,1,'2024-10-22 14:00:00'),(22,2,1,195,1,'2024-10-22 15:00:00'),(23,3,1,220,1,'2024-10-22 16:00:00'),(24,4,1,150,1,'2024-10-22 17:00:00'),(25,5,1,210,1,'2024-10-23 12:00:00'),(26,6,1,185,1,'2024-10-23 13:00:00'),(27,7,1,140,1,'2024-10-23 14:00:00'),(28,8,1,195,1,'2024-10-23 15:00:00'),(29,9,1,250,1,'2024-10-23 16:00:00'),(30,10,1,225,1,'2024-10-23 17:00:00'),(31,11,1,130,1,'2024-10-24 12:00:00'),(32,12,1,145,1,'2024-10-24 13:00:00'),(33,13,1,215,1,'2024-10-24 14:00:00'),(34,14,1,175,1,'2024-10-24 15:00:00'),(35,15,1,230,1,'2024-10-24 16:00:00'),(36,16,1,205,1,'2024-10-24 17:00:00'),(37,17,1,245,1,'2024-10-25 12:00:00'),(38,18,1,135,1,'2024-10-25 13:00:00'),(39,19,1,195,1,'2024-10-25 14:00:00'),(40,20,1,180,1,'2024-10-25 15:00:00'),(41,1,1,175,1,'2024-10-25 16:00:00'),(42,2,1,200,1,'2024-10-25 17:00:00'),(43,3,1,250,1,'2024-10-26 12:00:00'),(44,4,1,150,1,'2024-10-26 13:00:00'),(45,5,1,130,1,'2024-10-26 14:00:00'),(46,6,1,180,1,'2024-10-26 15:00:00'),(47,1,1,150,1,'2024-10-26 12:00:00'),(48,2,1,200,1,'2024-10-26 13:00:00'),(49,3,1,120,1,'2024-10-26 14:00:00'),(50,4,1,175,1,'2024-10-26 15:00:00'),(51,5,1,95,1,'2024-10-26 16:00:00'),(52,6,1,220,1,'2024-10-26 17:00:00'),(53,7,1,180,1,'2024-10-27 12:00:00'),(54,8,1,145,1,'2024-10-27 13:00:00'),(55,9,1,160,1,'2024-10-27 14:00:00'),(56,10,1,175,1,'2024-10-27 15:00:00'),(57,11,1,250,1,'2024-10-27 16:00:00'),(58,12,1,215,1,'2024-10-27 17:00:00'),(59,13,1,230,1,'2024-10-28 12:00:00'),(60,14,1,185,1,'2024-10-28 13:00:00'),(61,15,1,145,1,'2024-10-28 14:00:00'),(62,16,1,190,1,'2024-10-28 15:00:00'),(63,17,1,130,1,'2024-10-28 16:00:00'),(64,18,1,220,1,'2024-10-28 17:00:00'),(65,19,1,175,1,'2024-10-29 12:00:00'),(66,20,1,165,1,'2024-10-29 13:00:00'),(67,1,1,140,1,'2024-10-29 14:00:00'),(68,2,1,195,1,'2024-10-29 15:00:00'),(69,3,1,220,1,'2024-10-29 16:00:00'),(70,4,1,150,1,'2024-10-29 17:00:00'),(71,5,1,210,1,'2024-10-30 12:00:00'),(72,6,1,185,1,'2024-10-30 13:00:00'),(73,7,1,140,1,'2024-10-30 14:00:00'),(74,8,1,195,1,'2024-10-30 15:00:00'),(75,9,1,250,1,'2024-10-30 16:00:00'),(76,10,1,225,1,'2024-10-30 17:00:00'),(77,11,1,130,1,'2024-10-31 12:00:00'),(78,12,1,145,1,'2024-10-31 13:00:00'),(79,13,1,215,1,'2024-10-31 14:00:00'),(80,14,1,175,1,'2024-10-31 15:00:00'),(81,15,1,230,1,'2024-10-31 16:00:00'),(82,16,1,205,1,'2024-10-31 17:00:00'),(83,17,1,245,1,'2024-11-01 12:00:00'),(84,18,1,135,1,'2024-11-01 13:00:00'),(85,19,1,195,1,'2024-11-01 14:00:00'),(86,20,1,180,1,'2024-11-01 15:00:00'),(87,1,1,175,1,'2024-11-01 16:00:00'),(88,2,1,200,1,'2024-11-01 17:00:00'),(89,3,1,250,1,'2024-11-02 12:00:00'),(90,4,1,150,1,'2024-11-02 13:00:00'),(91,5,1,130,1,'2024-11-02 14:00:00'),(92,6,1,180,1,'2024-11-02 15:00:00'),(93,1,1,150,1,'2024-10-12 12:30:00'),(94,2,1,200,1,'2024-10-12 13:45:00'),(95,3,1,175,1,'2024-10-12 14:20:00'),(96,4,1,230,1,'2024-10-12 15:00:00'),(97,5,1,90,1,'2024-10-12 16:15:00'),(98,6,1,120,1,'2024-10-13 12:45:00'),(99,7,1,250,1,'2024-10-13 14:10:00'),(100,8,1,300,1,'2024-10-13 16:00:00'),(101,9,1,220,1,'2024-10-13 17:45:00'),(102,10,1,135,1,'2024-10-13 18:20:00'),(103,11,1,160,1,'2024-10-14 13:30:00'),(104,12,1,215,1,'2024-10-14 14:45:00'),(105,13,1,140,1,'2024-10-14 15:15:00'),(106,14,1,225,1,'2024-10-14 16:10:00'),(107,15,1,180,1,'2024-10-14 17:00:00'),(108,16,1,260,1,'2024-10-15 12:00:00'),(109,17,1,155,1,'2024-10-15 13:30:00'),(110,18,1,195,1,'2024-10-15 14:40:00'),(111,19,1,220,1,'2024-10-15 15:10:00'),(112,20,1,310,1,'2024-10-15 16:50:00'),(113,1,1,240,1,'2024-10-16 12:25:00'),(114,2,1,175,1,'2024-10-16 13:45:00'),(115,3,1,160,1,'2024-10-16 14:10:00'),(116,4,1,210,1,'2024-10-16 15:55:00'),(117,5,1,120,1,'2024-10-16 16:40:00'),(118,6,1,275,1,'2024-10-17 12:15:00'),(119,7,1,200,1,'2024-10-17 13:20:00'),(120,8,1,190,1,'2024-10-17 14:35:00'),(121,9,1,220,1,'2024-10-17 16:15:00'),(122,10,1,195,1,'2024-10-17 17:40:00'),(123,11,1,145,1,'2024-10-18 12:35:00'),(124,12,1,210,1,'2024-10-18 13:50:00'),(125,13,1,185,1,'2024-10-18 14:25:00'),(126,14,1,215,1,'2024-10-18 15:10:00'),(127,15,1,230,1,'2024-10-18 16:55:00'),(128,16,1,260,1,'2024-10-18 17:20:00'),(129,17,1,170,1,'2024-10-18 18:10:00'),(130,18,1,200,1,'2024-10-18 19:05:00'),(131,19,1,220,1,'2024-10-18 20:15:00'),(132,20,1,175,1,'2024-10-18 21:25:00'),(133,1,1,165,1,'2024-10-18 22:00:00'),(134,2,1,180,1,'2024-10-18 23:15:00'),(135,3,1,190,1,'2024-10-18 23:55:00'),(136,4,1,230,1,'2024-10-18 23:59:59'),(137,1,NULL,145.5,NULL,'2024-10-05 12:15:00'),(138,2,NULL,200.75,NULL,'2024-10-05 13:30:00'),(139,3,NULL,98,NULL,'2024-10-05 14:45:00'),(140,4,NULL,250,NULL,'2024-10-05 16:00:00'),(141,5,NULL,320.5,NULL,'2024-10-05 17:30:00'),(142,6,NULL,175,NULL,'2024-10-06 11:00:00'),(143,7,NULL,210.9,NULL,'2024-10-06 12:20:00'),(144,8,NULL,95.25,NULL,'2024-10-06 13:50:00'),(145,9,NULL,400.5,NULL,'2024-10-06 15:15:00'),(146,10,NULL,220.4,NULL,'2024-10-06 16:45:00'),(147,11,NULL,180.6,NULL,'2024-10-07 10:00:00'),(148,12,NULL,340.5,NULL,'2024-10-07 11:20:00'),(149,13,NULL,230.75,NULL,'2024-10-07 12:45:00'),(150,14,NULL,195.2,NULL,'2024-10-07 14:15:00'),(151,15,NULL,280.1,NULL,'2024-10-07 15:50:00'),(152,1,NULL,105.9,NULL,'2024-10-08 11:30:00'),(153,2,NULL,350.8,NULL,'2024-10-08 12:45:00'),(154,3,NULL,215.4,NULL,'2024-10-08 13:30:00'),(155,4,NULL,120.3,NULL,'2024-10-08 15:00:00'),(156,5,NULL,280.5,NULL,'2024-10-08 16:10:00'),(157,6,NULL,130,NULL,'2024-10-09 10:30:00'),(158,7,NULL,250.75,NULL,'2024-10-09 11:45:00'),(159,8,NULL,190.4,NULL,'2024-10-09 12:50:00'),(160,9,NULL,305.5,NULL,'2024-10-09 13:30:00'),(161,10,NULL,400.1,NULL,'2024-10-09 15:15:00'),(162,11,NULL,150.8,NULL,'2024-10-10 10:00:00'),(163,12,NULL,275.6,NULL,'2024-10-10 11:30:00'),(164,13,NULL,230.45,NULL,'2024-10-10 12:20:00'),(165,14,NULL,198.3,NULL,'2024-10-10 13:40:00'),(166,15,NULL,360.25,NULL,'2024-10-10 15:00:00'),(167,1,NULL,180.5,NULL,'2024-10-11 10:45:00'),(168,2,NULL,320.9,NULL,'2024-10-11 11:50:00'),(169,3,NULL,250,NULL,'2024-10-11 13:00:00'),(170,4,NULL,300.2,NULL,'2024-10-11 14:10:00'),(171,5,NULL,410.4,NULL,'2024-10-11 15:30:00'),(172,6,NULL,140.6,NULL,'2024-10-05 12:30:00'),(173,7,NULL,215.3,NULL,'2024-10-06 12:00:00'),(174,8,NULL,390.8,NULL,'2024-10-07 14:20:00'),(175,9,NULL,120.9,NULL,'2024-10-08 10:30:00'),(176,10,NULL,300.5,NULL,'2024-10-09 12:45:00'),(177,11,NULL,270.4,NULL,'2024-10-10 11:30:00'),(178,12,NULL,250.2,NULL,'2024-10-11 14:45:00'),(179,13,NULL,340.9,NULL,'2024-10-11 15:15:00'),(180,14,NULL,245.5,NULL,'2024-10-09 11:50:00'),(181,15,NULL,160.2,NULL,'2024-10-10 13:10:00'),(182,1,NULL,375.3,NULL,'2024-10-06 14:50:00'),(183,2,NULL,210.4,NULL,'2024-10-08 16:20:00'),(184,3,NULL,199.9,NULL,'2024-10-05 13:40:00'),(185,4,NULL,360.5,NULL,'2024-10-07 16:15:00'),(186,5,NULL,420.6,NULL,'2024-10-11 13:50:00');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorydish`
--

DROP TABLE IF EXISTS `categorydish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorydish` (
  `CategoryID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `Description` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`CategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorydish`
--

LOCK TABLES `categorydish` WRITE;
/*!40000 ALTER TABLE `categorydish` DISABLE KEYS */;
INSERT INTO `categorydish` VALUES (1,'Seafood','Dishes made from fresh seafood like fish, shrimp, squid, and oysters.'),(2,'Hot Pot','Various hot pot dishes with flavorful broths, combined with meat and vegetables.'),(3,'Meat','Dishes prepared from beef, chicken, pork, lamb, and more, in diverse styles.'),(4,'Vegetables','Fresh vegetable dishes that provide essential nutrients.'),(5,'Beverages','Various drinks such as juices, smoothies, soft drinks, and cocktails.'),(6,'Fried Dishes','Crispy fried dishes like french fries, fried chicken, and fried seafood.'),(7,'Grilled Dishes','Grilled dishes from meats, seafood to vegetables, packed with flavor.'),(8,'Desserts','Sweet treats including cakes, ice cream, and other desserts.'),(9,'Burgers & Sandwiches','Delicious burgers and sandwiches made with different fillings.'),(10,'Pasta','Pasta dishes like spaghetti, penne, and more with various sauces.'),(11,'Salads','Healthy salads made with fresh greens and a variety of toppings.');
/*!40000 ALTER TABLE `categorydish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cookmethod`
--

DROP TABLE IF EXISTS `cookmethod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cookmethod` (
  `CookMethodID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `Description` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`CookMethodID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cookmethod`
--

LOCK TABLES `cookmethod` WRITE;
/*!40000 ALTER TABLE `cookmethod` DISABLE KEYS */;
INSERT INTO `cookmethod` VALUES (1,'Steak & Ribs','Cooking methods related to steak and ribs.'),(2,'Chicken','Cooking methods related to chicken dishes.'),(3,'Lamb','Cooking methods related to lamb dishes.'),(4,'Seafood','Cooking methods related to seafood dishes.'),(5,'Burgers & Sandwiches','Cooking methods related to burgers and sandwiches.'),(6,'Pasta','Cooking methods related to pasta dishes.'),(7,'Side Dishes','Cooking methods related to side dishes.'),(8,'Bar Bites','Cooking methods related to bar bites or snacks.'),(9,'Salad','Cooking methods related to salads.'),(10,'Liquor','Methods related to liquor and beverages.'),(11,'Classic Cocktails','Methods related to classic cocktails.'),(12,'House Cocktails','Methods related to house cocktails.'),(13,'House Dessert','Methods related to house desserts.'),(14,'Shoney Kid','Methods related to kids menu.'),(15,'Cold Pressed Juice','Methods related to cold pressed juices.'),(16,'Mocktails','Methods related to mocktails.');
/*!40000 ALTER TABLE `cookmethod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `DepartmentID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `Description` text COLLATE utf8mb4_general_ci,
  `Icon` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`DepartmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (7,'Cashier','Cashier Department','⭐'),(8,'Warehouse','Warehouse Department','?'),(9,'Accounting','Accounting Department','?'),(10,'Management','Management Department','?'),(11,'Service','Service Department','?'),(12,'IT','Information Technology Department','?'),(13,'Kitchen','Kitchen Department','?');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dishorder`
--

DROP TABLE IF EXISTS `dishorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dishorder` (
  `DishOrderID` int unsigned NOT NULL AUTO_INCREMENT,
  `BillID` int unsigned DEFAULT NULL,
  `DishID` int unsigned DEFAULT NULL,
  `Number` int DEFAULT NULL,
  `Note` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`DishOrderID`),
  KEY `FK_Bill_DishOrder` (`BillID`),
  KEY `FK_Menu_DishOrder` (`DishID`),
  CONSTRAINT `FK_Bill_DishOrder` FOREIGN KEY (`BillID`) REFERENCES `bill` (`BillID`),
  CONSTRAINT `FK_Menu_DishOrder` FOREIGN KEY (`DishID`) REFERENCES `menu` (`DishID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dishorder`
--

LOCK TABLES `dishorder` WRITE;
/*!40000 ALTER TABLE `dishorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `dishorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feature`
--

DROP TABLE IF EXISTS `feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feature` (
  `FeatureID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `Description` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`FeatureID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature`
--

LOCK TABLES `feature` WRITE;
/*!40000 ALTER TABLE `feature` DISABLE KEYS */;
/*!40000 ALTER TABLE `feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featureofrole`
--

DROP TABLE IF EXISTS `featureofrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `featureofrole` (
  `FeatureOfRoleID` int unsigned NOT NULL AUTO_INCREMENT,
  `RoleID` int unsigned DEFAULT NULL,
  `FeatureID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`FeatureOfRoleID`),
  KEY `FK_Role_FeatureOfRole` (`RoleID`),
  KEY `FK_Feature_FeatureOfRole` (`FeatureID`),
  CONSTRAINT `featureofrole_ibfk_1` FOREIGN KEY (`RoleID`) REFERENCES `role` (`RoleID`),
  CONSTRAINT `featureofrole_ibfk_2` FOREIGN KEY (`FeatureID`) REFERENCES `feature` (`FeatureID`),
  CONSTRAINT `FK_Feature_FeatureOfRole` FOREIGN KEY (`FeatureID`) REFERENCES `feature` (`FeatureID`),
  CONSTRAINT `FK_Role_FeatureOfRole` FOREIGN KEY (`RoleID`) REFERENCES `role` (`RoleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featureofrole`
--

LOCK TABLES `featureofrole` WRITE;
/*!40000 ALTER TABLE `featureofrole` DISABLE KEYS */;
/*!40000 ALTER TABLE `featureofrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `featureofstaff`
--

DROP TABLE IF EXISTS `featureofstaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `featureofstaff` (
  `FeatureOfStaffID` int unsigned NOT NULL AUTO_INCREMENT,
  `StaffID` int unsigned DEFAULT NULL,
  `FeatureID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`FeatureOfStaffID`),
  KEY `FK_Staff_FeatureOfStaff` (`StaffID`),
  KEY `FK_Feature_FeatureOfStaff` (`FeatureID`),
  CONSTRAINT `featureofstaff_ibfk_1` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`),
  CONSTRAINT `featureofstaff_ibfk_2` FOREIGN KEY (`FeatureID`) REFERENCES `feature` (`FeatureID`),
  CONSTRAINT `FK_Feature_FeatureOfStaff` FOREIGN KEY (`FeatureID`) REFERENCES `feature` (`FeatureID`),
  CONSTRAINT `FK_Staff_FeatureOfStaff` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `featureofstaff`
--

LOCK TABLES `featureofstaff` WRITE;
/*!40000 ALTER TABLE `featureofstaff` DISABLE KEYS */;
/*!40000 ALTER TABLE `featureofstaff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `DishID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `CategoryID` int unsigned DEFAULT NULL,
  `CookMethodID` int unsigned DEFAULT NULL,
  `Description` text COLLATE utf8mb4_general_ci,
  `Picture` text COLLATE utf8mb4_general_ci,
  `Price` float DEFAULT NULL,
  `IsAvailable` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`DishID`),
  KEY `FK_CategoryDish_Menu` (`CategoryID`),
  KEY `FK_CookMethod_Menu` (`CookMethodID`),
  CONSTRAINT `FK_CategoryDish_Menu` FOREIGN KEY (`CategoryID`) REFERENCES `categorydish` (`CategoryID`),
  CONSTRAINT `FK_CookMethod_Menu` FOREIGN KEY (`CookMethodID`) REFERENCES `cookmethod` (`CookMethodID`)
) ENGINE=InnoDB AUTO_INCREMENT=198 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (41,'Chicken Chop',2,2,'300g chicken chop',NULL,28,1),(159,'Prime Rib Steak',3,1,'300g rib steak cooked to perfection',NULL,96,1),(160,'Sirloin Steak',3,1,'230g sirloin steak with a side of vegetables',NULL,79,1),(161,'Ribeye Steak',3,1,'Juicy 230g ribeye steak',NULL,96,1),(162,'BBQ Ribs',3,1,'400g of BBQ ribs with house sauce',NULL,59,1),(163,'Grilled Chicken ½ Bird',3,2,'½ Bird of grilled chicken',NULL,33,1),(164,'Southern Fried Chicken ½ Bird',3,2,'Crispy fried ½ bird of chicken',NULL,33,1),(165,'Pan Seared Chicken',3,2,'300g of pan seared chicken',NULL,28,1),(166,'Grilled Lamb Chops',3,3,'Delicious grilled lamb chop',NULL,48,1),(167,'Braised Lamb Shank',3,3,'Braised lamb shank cooked to perfection',NULL,52,1),(168,'Catch of the day',1,4,'Fresh seafood of the day',NULL,46,1),(169,'Grilled Salmon',1,4,'Freshly grilled salmon',NULL,48,1),(170,'Fish & Chips',1,4,'Traditional fish and chips',NULL,35,1),(171,'Classic Cheese Burger',9,5,'Cheesy burger with fries',NULL,30,1),(172,'Hickory Burger',9,5,'Burger with hickory sauce',NULL,30,1),(173,'Fried Chicken Burger',9,5,'Crispy fried chicken burger',NULL,24,1),(174,'Grilled Chicken Burger',9,5,'Grilled chicken burger',NULL,24,1),(175,'Chili Dog',9,5,'Delicious chili dog sandwich',NULL,25,1),(176,'Meatballs Sandwich',9,5,'Meatballs sandwich with house sauce',NULL,25,1),(177,'Shrimp Po Boy',9,5,'Shrimp sandwich with cajun sauce',NULL,32,1),(178,'Bolognese',10,6,'Spaghetti with bolognese sauce',NULL,26,1),(179,'Meat Balls',10,6,'Spaghetti with meatballs',NULL,28,1),(180,'Carbonara',10,6,'Creamy carbonara with penne',NULL,28,1),(181,'Chicken & Mushroom Aglio Olio',10,6,'Penne with chicken and mushroom aglio olio',NULL,28,1),(182,'Chicken Arabiatta',10,6,'Spaghetti with spicy chicken arabiatta',NULL,28,1),(183,'Fries',7,7,'Crispy french fries',NULL,9,1),(184,'Potato Wedges',7,7,'Crispy potato wedges',NULL,9,1),(185,'Garden Salad',11,9,'Fresh garden salad with vinaigrette',NULL,9,1),(186,'Buffalo Wings',8,8,'Delicious buffalo wings',NULL,24,1),(187,'Fried Calamari',8,8,'Crispy fried calamari',NULL,29,1),(188,'Blended Scotch (Black Label)',5,10,'Johnny Walker Black Label 700ml',NULL,310,1),(189,'Blended Scotch (Gold Label)',5,10,'Johnny Walker Gold Label 750ml',NULL,390,1),(190,'American Whisky (Jack Daniel)',5,10,'Jack Daniel\'s Whisky 700ml',NULL,290,1),(191,'Kamikaze',5,11,'Classic Kamikaze cocktail',NULL,28,1),(192,'Mojito',5,11,'Refreshing mojito cocktail',NULL,29,1),(193,'Brownies',8,13,'Delicious warm brownies',NULL,15,1),(194,'American Cheese Cake',8,13,'Classic American cheesecake',NULL,15,1),(195,'Chicken Tenders',11,14,'Tender fried chicken strips',NULL,12,1),(196,'Green Apple',5,15,'Fresh cold pressed green apple juice',NULL,15,1),(197,'Virgin Apple Mojito',5,16,'Non-alcoholic apple mojito',NULL,16,1);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `ReservationID` int unsigned NOT NULL AUTO_INCREMENT,
  `TableNumber` int unsigned DEFAULT NULL,
  `UserID` int unsigned DEFAULT NULL,
  `Time` datetime DEFAULT NULL,
  `IsTaken` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ReservationID`),
  KEY `FK_Table_Reservation` (`TableNumber`),
  KEY `FK_User_Reservation` (`UserID`),
  CONSTRAINT `FK_Table_Reservation` FOREIGN KEY (`TableNumber`) REFERENCES `table` (`TableID`),
  CONSTRAINT `FK_User_Reservation` FOREIGN KEY (`UserID`) REFERENCES `user` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `RoleID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `Description` text COLLATE utf8mb4_general_ci,
  `DepartmentID` int unsigned DEFAULT NULL,
  PRIMARY KEY (`RoleID`),
  KEY `DepartmentID` (`DepartmentID`),
  CONSTRAINT `role_ibfk_1` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`DepartmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Admin','Admin of system',NULL),(2,'Cashier Manager','Manages cashier operations',7),(3,'Cashier Staff','Handles customer payments',7),(4,'Warehouse Manager','Oversees warehouse operations',8),(5,'Stock Controller','Monitors inventory levels',8),(6,'Chief Accountant','Leads accounting team',9),(7,'Accountant','Manages financial records',9),(8,'General Manager','Oversees all operations',10),(9,'Assistant Manager','Assists in management tasks',10),(10,'Head of Service','Leads the service team',11),(11,'Waiter','Serves customers at tables',11),(12,'IT Manager','Leads the IT department',12),(13,'System Administrator','Manages IT infrastructure',12),(14,'Head Chef','Leads kitchen operations',13),(15,'Sous Chef','Assists the head chef',13),(16,'Kitchen Staff','Prepares food',13);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `StaffID` int unsigned NOT NULL,
  `Amount` int DEFAULT NULL,
  PRIMARY KEY (`StaffID`),
  CONSTRAINT `FK_Staff_Salary` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`),
  CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shift`
--

DROP TABLE IF EXISTS `shift`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shift` (
  `ShiftID` int unsigned NOT NULL AUTO_INCREMENT,
  `TimeStart` datetime DEFAULT NULL,
  `TimeEnd` datetime DEFAULT NULL,
  PRIMARY KEY (`ShiftID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shift`
--

LOCK TABLES `shift` WRITE;
/*!40000 ALTER TABLE `shift` DISABLE KEYS */;
/*!40000 ALTER TABLE `shift` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shiftofstaff`
--

DROP TABLE IF EXISTS `shiftofstaff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shiftofstaff` (
  `ShiftOfStaffID` int unsigned NOT NULL AUTO_INCREMENT,
  `ShiftID` int unsigned DEFAULT NULL,
  `StaffID` int unsigned DEFAULT NULL,
  `IsConfirm` tinyint(1) DEFAULT NULL,
  `IsAttendant` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`ShiftOfStaffID`),
  KEY `FK_Shift_ShiftOfStaff` (`ShiftID`),
  KEY `FK_Staff_ShiftOfStaff` (`StaffID`),
  CONSTRAINT `FK_Shift_ShiftOfStaff` FOREIGN KEY (`ShiftID`) REFERENCES `shift` (`ShiftID`),
  CONSTRAINT `FK_Staff_ShiftOfStaff` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`),
  CONSTRAINT `shiftofstaff_ibfk_1` FOREIGN KEY (`ShiftID`) REFERENCES `shift` (`ShiftID`),
  CONSTRAINT `shiftofstaff_ibfk_2` FOREIGN KEY (`StaffID`) REFERENCES `staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shiftofstaff`
--

LOCK TABLES `shiftofstaff` WRITE;
/*!40000 ALTER TABLE `shiftofstaff` DISABLE KEYS */;
/*!40000 ALTER TABLE `shiftofstaff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `StaffID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `PhoneNumber` text COLLATE utf8mb4_general_ci NOT NULL,
  `RoleID` int unsigned DEFAULT NULL,
  `Password` text COLLATE utf8mb4_general_ci,
  `CreateAt` datetime DEFAULT NULL,
  `username` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`StaffID`),
  KEY `RoleID` (`RoleID`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`RoleID`) REFERENCES `role` (`RoleID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'lam','0932536332',1,'123',NULL,'lam'),(2,'John Doe','0932536333',1,'password123','2024-10-18 22:39:24','john_doe'),(3,'Jane Smith','0932363243',2,'password123','2024-10-18 22:39:24','jane_smith'),(4,'Michael Brown','',3,'password123','2024-10-18 22:39:24','michael_brown'),(5,'Sara Johnson','',4,'password123','2024-10-18 22:39:24','sara_johnson'),(6,'David Wilson','',5,'password123','2024-10-18 22:39:24','david_wilson'),(7,'Linda Clark','',6,'password123','2024-10-18 22:39:24','linda_clark'),(8,'Mark Evans','',7,'password123','2024-10-18 22:39:24','mark_evans'),(9,'Emily White','',8,'password123','2024-10-18 22:39:24','emily_white'),(10,'Thomas Hall','',9,'password123','2024-10-18 22:39:24','thomas_hall'),(11,'Nancy Green','',10,'password123','2024-10-18 22:39:24','nancy_green');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table`
--

DROP TABLE IF EXISTS `table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table` (
  `TableID` int unsigned NOT NULL AUTO_INCREMENT,
  `TableNumber` int unsigned DEFAULT NULL,
  `IsAvailable` tinyint(1) DEFAULT NULL,
  `Ability` int DEFAULT NULL,
  PRIMARY KEY (`TableID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table`
--

LOCK TABLES `table` WRITE;
/*!40000 ALTER TABLE `table` DISABLE KEYS */;
INSERT INTO `table` VALUES (1,1,1,4),(2,2,1,4),(3,3,1,4),(4,4,1,4),(5,5,1,6),(6,6,1,6),(7,7,1,6),(8,8,1,6),(9,9,1,8),(10,10,1,8),(11,11,1,2),(12,12,1,2),(13,13,1,2),(14,14,1,2),(15,15,1,10),(16,16,1,10),(17,17,1,4),(18,18,1,4),(19,19,1,8),(20,20,1,8);
/*!40000 ALTER TABLE `table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text COLLATE utf8mb4_general_ci,
  `HashPassword` text COLLATE utf8mb4_general_ci,
  `CreateAt` datetime DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-22 12:19:27
