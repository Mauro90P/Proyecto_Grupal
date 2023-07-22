CREATE DATABASE  IF NOT EXISTS `db_proyecto1` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_proyecto1`;
-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: db_proyecto1
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `creador_job` int NOT NULL,
  `usuario_id` int unsigned DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_job_user_idx` (`usuario_id`),
  CONSTRAINT `fk_job_user` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (4,'dddfdf','dgdgdgdgdg','dgdgdgdg',3,3,'2023-07-10 04:23:42','2023-07-10 04:23:42'),(5,'ddasdsa','dasasddsa','saddsadsa',3,3,'2023-07-10 04:26:58','2023-07-10 04:26:58'),(6,'dggd','gdfg','dfgdg',3,3,'2023-07-10 04:30:02','2023-07-10 04:30:02'),(7,'dsff','sdfdfs','dsffds',3,3,'2023-07-10 04:31:13','2023-07-10 04:31:13'),(8,'ffd','fdssds','dfsdfs',3,3,'2023-07-10 04:35:18','2023-07-10 04:35:18'),(9,'CXCCV','CXBCBB','BCXBCXCBX',3,3,'2023-07-10 04:43:56','2023-07-10 04:43:56'),(10,'DDAA','DASADS','DSASAD',3,3,'2023-07-10 04:45:12','2023-07-10 04:45:12'),(11,'ddffd','fddfd','dfdffd',3,NULL,'2023-07-10 05:00:08','2023-07-10 05:00:08'),(12,'FDGF','DGFGF','DFDFGFD',3,3,'2023-07-10 05:01:51','2023-07-10 05:01:51'),(13,'CVXXVXVC','VCXCVXVCXCVX','CVXCXVCVXCVXCV',3,NULL,'2023-07-10 05:04:11','2023-07-10 05:04:11'),(15,'VIAJE A MEXICO','Lindo Viaje a mexico con todo incluido','SALIDA EN LAS CONDES 123',2,NULL,'2023-07-10 05:59:03','2023-07-10 05:59:03'),(17,'CANARIAS PLAYAS ','Lindo lugar para experimentar un lugar nuevo','ECUADOR 2345',2,NULL,'2023-07-10 06:44:40','2023-07-10 06:44:40'),(19,'TORRES DEL PAINE ','LUGAR HERMOSO','SALIDA DE COPIAPO 2345',1,NULL,'2023-07-10 07:25:16','2023-07-10 07:25:16'),(20,'COLCHANE','FRIO ','SANTIAGO 34',1,NULL,'2023-07-10 07:27:15','2023-07-10 07:27:15'),(21,'lOSS PATOS ARMANDO','SSFFSSF','DDDFD34',1,NULL,'2023-07-10 07:35:33','2023-07-10 07:35:33');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'ARMANDO','PEREZ','AMRPERRES@GMAIL.COM','$2b$12$Cx.mQ7qSPOk6oHoZEN5bZ.17EkVXvBqmXIkOo.4GzHCVB/5RXkBtO'),(2,'RAQUEL ','ARGANDOÑA','RAQEU@MAIL.COM','$2b$12$59esH0kA2CrtkuHEsp4YzOAQro1pAGGJYsgqeX8J/0F.LhmvU6N/O'),(3,'JULIO','MARDONES','JULIOMARDOLES@GMAIL.COM','$2b$12$nFoM.5QVwloIJO27Tfysm.UtofZu/ocFBmfRT3F7WVxgixU5knLri');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-10  9:06:22
