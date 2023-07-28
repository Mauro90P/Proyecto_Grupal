CREATE DATABASE  IF NOT EXISTS `db_video` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_video`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: db_video
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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) NOT NULL,
  `apellido` varchar(80) NOT NULL,
  `username` varchar(80) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `usuarioscol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (6,'Mauricio','Pardo','Mauro','mauriciopardo.figueroa@gmail.com','$2b$12$5BwHMOPzSLLD6LBT/G908.3Nzn47WJh7Hu7J1FcKsyfYF4xEXndi.',NULL),(7,'Julio','Alva ','JULIO8','SEJUALRI1234@GMAIL.COM','$2b$12$BvwrmB2IKUm32ptWKqBXLupPjLfn8BvuxUYNm5EgNUJocYW2a3ZxK',NULL),(8,'martin','garces','martincito','martin2@gmail.com','$2b$12$oJOFerVc7H/oq2LEcJPs9uCQashE8/BFmLSFtutR6TyjVdAUGoyhC',NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `video` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_video` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `url_video` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url_video_UNIQUE` (`url_video`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video`
--

LOCK TABLES `video` WRITE;
/*!40000 ALTER TABLE `video` DISABLE KEYS */;
INSERT INTO `video` VALUES (1,'Curso C#','https://i.ytimg.com/vi/gPkKXoBG9a4/maxresdefault.jpg','30','https://www.youtube.com/watch?v=axHut2e84fc&ab_channel=ProgramadorX','2023-07-28 00:31:03','2023-07-28 11:45:06'),(2,'CURSO DE JAVA FULL','https://static.vecteezy.com/system/resources/previews/020/111/553/original/java-editorial-logo-free-download-free-vector.jpg','50','https://www.youtube.com/watch?v=L1oMLsiMusQ&list=PLyvsggKtwbLX9LrDnl1-K6QtYo7m0yXWB','2023-07-28 01:22:27','2023-07-28 11:23:47'),(5,'CURSO DE SQL 2023','https://www.macworld.com/wp-content/uploads/2023/01/setup_learn_sql_mac.jpg?quality=50&strip=all','60','https://www.youtube.com/watch?v=DFg1V-rO6Pg','2023-07-28 01:29:17','2023-07-28 11:16:09'),(7,'CURSO DE CUCUMBER 2023','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-A9HITtzWIUp7gEyLGKwSzoK-YImIhDektprQPRv9sDMQ5pnFYN9i1AaBq3chaBQIH9c&usqp=CAU','80','https://www.youtube.com/watch?v=G1DOhBMIFkI&list=PLHBdlNTbF1h5XwqAc18Z5xcJpbO6rq6mm','2023-07-28 01:42:07','2023-07-28 11:24:21'),(8,'CURSO DE ORACLE FULL','https://image.shutterstock.com/image-photo/image-260nw-2317696753.jpg','60','https://www.youtube.com/watch?v=ibOzwFRm32w&list=PLiLpmqwkwkCt0QeXD8j7BwIoOaBGBRrZC','2023-07-28 02:39:51','2023-07-28 09:13:33'),(9,'Curso TypeScript','https://pbs.twimg.com/media/FzzzbKKX0AE-IAW.jpg:large','60','https://www.youtube.com/watch?v=-xDZwb-PY0M&ab_channel=HolaMundo','2023-07-28 02:53:01','2023-07-28 11:24:39'),(10,'Curso Git','https://logowik.com/content/uploads/images/git6963.jpg','50','https://www.youtube.com/watch?v=VdGzPZ31ts8&ab_channel=HolaMundo','2023-07-28 03:13:31','2023-07-28 11:25:45'),(11,'curso de python','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiy4wU1DkeKbYN4s4hUrY-bx1k3KqbG_wVd3XB7X_Wu8d7N4g6ebftQixcwvm95B1SaiE&usqp=CAU','50','https://www.youtube.com/watch?v=tQZy0U8s9LY&t=1s&ab_channel=HolaMundo','2023-07-28 08:16:08','2023-07-28 11:29:22'),(15,'curso de linux','https://upload.wikimedia.org/wikipedia/commons/8/8d/Linux_Logo.jpg','50','https://www.youtube.com/watch?v=L906Kti3gzE&ab_channel=HolaMundo','2023-07-28 08:29:41','2023-07-28 11:28:05'),(16,'curso de html','https://www.oxfordwebstudio.com/user/pages/06.da-li-znate/sta-je-html/sta-je-html.jpg','50','https://www.youtube.com/watch?v=MJkdaVFHrto&t=4s&ab_channel=HolaMundo','2023-07-28 09:22:26','2023-07-28 11:27:34'),(17,'curso css','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAicqanSBqPlYyVh6qKLki7LtQqLpoJwHX6E3z31JxnR5BTUIq4YNxU2wDlV91E47Dq9k&usqp=CAU','40','https://www.youtube.com/watch?v=wZniZEbPAzk&t=2s&ab_channel=HolaMundo','2023-07-28 10:22:50','2023-07-28 11:28:31');
/*!40000 ALTER TABLE `video` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-28  5:46:28
