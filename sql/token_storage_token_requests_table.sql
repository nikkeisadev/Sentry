-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: token_storage
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `token_requests_table`
--

DROP TABLE IF EXISTS `token_requests_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_requests_table` (
  `request_table` mediumtext COMMENT 'The main table of regquests.',
  `username_table` mediumtext,
  `hash_value` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='All pending token requests are here!';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_requests_table`
--

LOCK TABLES `token_requests_table` WRITE;
/*!40000 ALTER TABLE `token_requests_table` DISABLE KEYS */;
INSERT INTO `token_requests_table` VALUES ('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','',NULL),('Pending new token request from','Barta Attila',NULL),('Pending new token request from','Varga Thomas',NULL),('Pending new token request from','Barta Attila',NULL),('Pending new token request from','Barta Attila',NULL),('Pending new token request from','Barta Attila',NULL),('Pending new token request from','Barta Attila',NULL),('Pending new token request from','Barta Attila','7158f341e1c6334c7664b27d34a34f9eb5febfc4563885369e193024c3c84cef'),('Pending new token request from','Barta Attila','f74a79401b956093c283e579097c08fd501cc5965564248e7d525a28bcbbfdb7'),('Pending new token request from','Barta Attila','f74a79401b956093c283e579097c08fd501cc5965564248e7d525a28bcbbfdb7');
/*!40000 ALTER TABLE `token_requests_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-13 17:59:58
