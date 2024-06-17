CREATE DATABASE  IF NOT EXISTS `taller` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `taller`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: taller
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `autos`
--

DROP TABLE IF EXISTS `autos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autos` (
  `patente` varchar(7) NOT NULL,
  `id_Cliente` bigint NOT NULL,
  `marca` varchar(20) NOT NULL,
  `modelo` varchar(20) NOT NULL,
  `color` varchar(20) NOT NULL,
  PRIMARY KEY (`patente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autos`
--

LOCK TABLES `autos` WRITE;
/*!40000 ALTER TABLE `autos` DISABLE KEYS */;
INSERT INTO `autos` VALUES ('AB123CD',20987654320,'Toyota','Etios','Blanco'),('ase986',20123456789,'Toyota','Corolla','Rojo'),('IJ789KL',27234567890,'Chevrolet ','Cruze','Negro'),('QR345ST',23123456780,'Volkswagen','Golf','Gris');
/*!40000 ALTER TABLE `autos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `dni_cuit` bigint NOT NULL,
  `apeynom` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`dni_cuit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (20123456789,'Juan Perez','Calle Falsa 123','1234567890','juan.perez@example.com'),(20987654320,'Luis Fernandez','Avenida Libertador 1234','4567890123','luis.fernandez@example.com'),(20987654321,'Maria Gomez','Avenida Siempre Viva 742','0987654321','maria.gomez@example.com'),(23123456780,'Ana Martinez','Calle de la Amargura 789','3456789012','ana.martinez@example.com'),(27234567890,'Carlos Lopez','Boulevard de los Sueños Rotos 555','2345678901','carlos.lopez@example.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mecanicos`
--

DROP TABLE IF EXISTS `mecanicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mecanicos` (
  `idmeca` int NOT NULL AUTO_INCREMENT,
  `apeynom` varchar(50) NOT NULL,
  `especialidad` varchar(15) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmeca`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mecanicos`
--

LOCK TABLES `mecanicos` WRITE;
/*!40000 ALTER TABLE `mecanicos` DISABLE KEYS */;
INSERT INTO `mecanicos` VALUES (1,'Juan Castro','Motor','1234567890','juan.perez@example.com'),(2,'Daniel Rojas','Suspensión','2345678901','maria.lopez@example.com'),(3,'Gustavo Dominguez','Frenos','3456789012','carlos.garcia@example.com');
/*!40000 ALTER TABLE `mecanicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordenes`
--

DROP TABLE IF EXISTS `ordenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordenes` (
  `idOrden` int NOT NULL AUTO_INCREMENT,
  `patente` varchar(7) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `averia` varchar(120) NOT NULL,
  `fecha_egreso` varchar(10) DEFAULT '0000-00-00',
  `estado` varchar(15) NOT NULL DEFAULT 'INGRESADO',
  `mecanico` int DEFAULT '0',
  PRIMARY KEY (`idOrden`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordenes`
--

LOCK TABLES `ordenes` WRITE;
/*!40000 ALTER TABLE `ordenes` DISABLE KEYS */;
INSERT INTO `ordenes` VALUES (5,'ab123cd','2024-06-13','Cambio de aceite','0000-00-00','ASIGNADO',3),(6,'ij789kl','2024-06-13','Service 10000 kilometros','0000-00-00','INGRESADO',0),(7,'qr345st','2024-06-13','Calentamiento del motor','0000-00-00','ASIGNADO',1);
/*!40000 ALTER TABLE `ordenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `idstock` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(15) DEFAULT NULL,
  `descripcion` varchar(45) NOT NULL,
  `existencia` int NOT NULL,
  PRIMARY KEY (`idstock`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
INSERT INTO `stock` VALUES (101,'Toyota','Filtro de aire',50),(102,'Honda','Pastillas de freno',30),(103,'Ford','Aceite de motor',20),(104,'Nissan','Batería',15),(105,'Chevrolet','Llanta',25);
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'taller'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-13 23:47:02
