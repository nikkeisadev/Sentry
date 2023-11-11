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
-- Table structure for table `report_table`
--

DROP TABLE IF EXISTS `report_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_table` (
  `about` mediumtext,
  `datetime` mediumtext,
  `id` mediumtext,
  `information` mediumtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='The main table of reports from illegal activities.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_table`
--

LOCK TABLES `report_table` WRITE;
/*!40000 ALTER TABLE `report_table` DISABLE KEYS */;
INSERT INTO `report_table` VALUES ('[!][RUNTIME][Discord.exe]','2023-07-13 22:29:03',NULL,'Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-14 15:14:14','','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-14 15:16:33','5','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-14 21:44:14','6','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-16 19:17:45','6','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-16 19:20:27','6','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-16 20:10:15','5','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-17 14:48:09','6','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-17 14:58:28','5','Forbidden application in runtime!'),('[!][RUNTIME][Discord.exe]','2023-07-17 14:58:28','5','Forbidden application in runtime!');
/*!40000 ALTER TABLE `report_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-13 17:59:59
