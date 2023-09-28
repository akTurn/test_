-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: python_db
-- ------------------------------------------------------
-- Server version	5.5.5-10.10.2-MariaDB

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
-- Table structure for table `card_details`
--

DROP TABLE IF EXISTS `card_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `card_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `card_type` varchar(50) NOT NULL,
  `card_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `card_details`
--

LOCK TABLES `card_details` WRITE;
/*!40000 ALTER TABLE `card_details` DISABLE KEYS */;
INSERT INTO `card_details` VALUES (1,'Credit','ICICI'),(2,'Debit','Citi'),(3,'Credit','Indus Bank'),(4,'Credit','Stanchart'),(5,'Food coupen','Sodexo');
/*!40000 ALTER TABLE `card_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_categories`
--

DROP TABLE IF EXISTS `expense_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expense_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_categories`
--

LOCK TABLES `expense_categories` WRITE;
/*!40000 ALTER TABLE `expense_categories` DISABLE KEYS */;
INSERT INTO `expense_categories` VALUES (1,'Housing'),(2,'Transportation'),(3,'Food'),(4,'Utilities'),(5,'Healthcare'),(6,'Debt Payments'),(7,'Entertainment'),(8,'Personal Care'),(9,'Savings and Investments'),(10,'Education'),(11,'Travel'),(12,'Charity and Donations'),(13,'Shopping'),(14,'Insurance'),(15,'Taxes'),(16,'Emergency Fund'),(17,'Miscellaneous'),(18,'Farming');
/*!40000 ALTER TABLE `expense_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_subcategories`
--

DROP TABLE IF EXISTS `expense_subcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expense_subcategories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `expense_subcategories_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `expense_categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_subcategories`
--

LOCK TABLES `expense_subcategories` WRITE;
/*!40000 ALTER TABLE `expense_subcategories` DISABLE KEYS */;
INSERT INTO `expense_subcategories` VALUES (1,'Packers/Movers',1),(2,'Rent Advance Payments',1),(3,'Rent or Mortgage',1),(4,'Electricity',1),(5,'Water and Sewer',1),(6,'Gas',1),(7,'Grocery',1),(8,'Mobile',1),(9,'Repairs and Maintenance',1),(10,'Gasoline/Fuel',2),(11,'Public Transportation',2),(12,'Vehicle Maintenance',2),(13,'Insurance',2),(14,'Parking and Tolls',2),(15,'Seeds',18),(16,'Fertilizers',18),(17,'Pesticides and Herbicides',18),(18,'Irrigation',18),(19,'Soil Testing',18),(20,'Tractors and Implements',18),(21,'Harvesting Equipment',18),(22,'Farm Vehicles',18),(23,'Maintenance and Repairs',18),(24,'Farm Workers\' Wages',18),(25,'Seasonal Labor',18),(26,'Contract Labor',18),(27,'Land Purchase ',18),(28,'Land Improvement',18),(29,'Fuel (e.g., for generators)',18),(30,'Packaging',18),(31,'Land Lease',18),(32,'Sales and Distribution Costs',18),(33,'Crop Insurance',18),(34,'Equipment Insurance',18),(35,'Income Tax Payments',15),(36,'Property Tax Payments',15),(37,'Sales Tax',15),(38,'Health Insurance',14),(39,'Bike Insurance',14),(40,'Car Insurance',14),(41,'Clothing and Apparel',13),(42,'Electronics and Gadgets',13),(43,'Home and Kitchen',13),(44,'Gifts and Presents',13),(45,'Charitable Contributions',12),(46,'Donations to Nonprofits',12),(47,'Parking/Tolls Charges',11),(48,'Flight/Bus/Train Tickets',11),(49,'Car/Bike Fuel',11),(50,'Accommodation',11),(51,'Food and Dining',11),(52,'Activities and Attractions',11),(53,'Dining Out',3),(54,'Takeout and Delivery',3),(55,'Health Insurance',5),(56,'Medical Expenses',5),(57,'Prescription Medications',5),(58,'Credit Card Payments',6),(59,'BankLoan Payments',6),(60,'AgreeLoan Payments',6),(61,'Advance Salary Payments',6),(62,'Credit Limit Payments',6),(63,'Movies and Shows',7),(64,'Concerts and Events',7),(65,'Streaming Services',7),(66,'Hobbies and Leisure Activities',7),(67,'Haircuts and Grooming',8),(68,'Health and Beauty Products',8),(69,'PostOffice Account Contributions',9),(70,'Investment Purchases',9),(71,'Tuition and Fees',10),(72,'Books and Supplies',10),(73,'Educational Services',10);
/*!40000 ALTER TABLE `expense_subcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `spend_to` enum('MD','Family') DEFAULT 'MD',
  `expense_category_id` int(11) NOT NULL,
  `expense_subcategory_id` int(11) NOT NULL,
  `payment_type` enum('Card','Cash') DEFAULT 'Card',
  `card_id` int(11) DEFAULT NULL,
  `amount_paid` float NOT NULL,
  `description` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `expense_category_id` (`expense_category_id`),
  KEY `expense_subcategory_id` (`expense_subcategory_id`),
  KEY `card_id` (`card_id`),
  CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `expenses_ibfk_2` FOREIGN KEY (`expense_category_id`) REFERENCES `expense_categories` (`id`),
  CONSTRAINT `expenses_ibfk_3` FOREIGN KEY (`expense_subcategory_id`) REFERENCES `expense_subcategories` (`id`),
  CONSTRAINT `expenses_ibfk_4` FOREIGN KEY (`card_id`) REFERENCES `card_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (1,'2023-09-11','MD',1,7,'Card',3,690,'surf,mysoore sandal,deepam oil',2),(2,'2023-09-11','MD',1,7,'Cash',1,400,'veg + oil',2),(6,'2023-09-11','MD',1,3,'Card',2,15000,'Rent',2),(7,'2023-09-01','Family',1,4,'Card',4,1045,'            \r\n                test update\r\n            \r\n        ',2),(8,'2023-09-13','Family',18,24,'Card',2,10000,'            \r\n       Ploughing ',2),(10,'2023-08-08','Family',13,42,'Card',1,18000,'       Mobile phone     \r\n        ',2),(11,'2023-09-02','MD',6,58,'Card',2,30000,'test payment',2);
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `income`
--

DROP TABLE IF EXISTS `income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `income` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `source` varchar(255) NOT NULL,
  `amount` float NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `card_id` int(11) DEFAULT NULL,
  `tax_deductions` float DEFAULT NULL,
  `tax_year` int(11) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `card_id` (`card_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `income_ibfk_1` FOREIGN KEY (`card_id`) REFERENCES `card_details` (`id`),
  CONSTRAINT `income_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `income`
--

LOCK TABLES `income` WRITE;
/*!40000 ALTER TABLE `income` DISABLE KEYS */;
INSERT INTO `income` VALUES (1,'2023-04-01','Salary',5000,'Direct Deposit',1,NULL,2023,'Monthly salary',1),(2,'2023-04-20','Freelance Work',1200.5,'Bank Transfer',NULL,50.25,2023,'Payment for freelance project',1),(3,'2023-09-01','Salary',115200,'Direct Deposit',2,NULL,2023,'Monthly salary',2),(4,'2023-02-25','Investment Dividends',350.25,'Bank Transfer',NULL,15.75,2023,'test data',2);
/*!40000 ALTER TABLE `income` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test','teset123','test@test.com'),(2,'root','sha256$CkjHGwvaegvOQbjW$3e2df553a58676caf0728ba1658766f64591a8cbfd4c8c4e208c0fa119f6aae4','root@test.com'),(3,'jwt ','sha256$ibt8kZ39uXfYGrlH$9bcbb35efde422e37dde9a83001f5131d3a62e5f979720f2c1aa040aa696cc01','jwt@test.com'),(4,'max ','sha256$uAj1KepqCBGo5D7w$144030eb1371677a1ee8a5fef52071535f542ad4abeff1896e00721ece255200','max@test.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-21 13:38:13
