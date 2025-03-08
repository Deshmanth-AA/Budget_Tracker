-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 09, 2024 at 02:19 PM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bgt`
--

-- --------------------------------------------------------

--
-- Table structure for table `auditor`
--

DROP TABLE IF EXISTS `auditor`;
CREATE TABLE IF NOT EXISTS `auditor` (
  `audID` int NOT NULL AUTO_INCREMENT,
  `aname` text NOT NULL,
  `phnum` bigint NOT NULL,
  `pwd` text NOT NULL,
  PRIMARY KEY (`audID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `audits`
--

DROP TABLE IF EXISTS `audits`;
CREATE TABLE IF NOT EXISTS `audits` (
  `audID` int NOT NULL,
  `budgetID` int NOT NULL,
  PRIMARY KEY (`audID`,`budgetID`),
  KEY `budgetID` (`budgetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `budget`
--

DROP TABLE IF EXISTS `budget`;
CREATE TABLE IF NOT EXISTS `budget` (
  `budgetID` int NOT NULL AUTO_INCREMENT,
  `head` text NOT NULL,
  `amnt_san` int NOT NULL,
  `dateofsan` date NOT NULL,
  `deptID` int NOT NULL,
  `empID` int NOT NULL,
  PRIMARY KEY (`budgetID`),
  KEY `deptID` (`deptID`),
  KEY `empID` (`empID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `budget`
--

INSERT INTO `budget` (`budgetID`, `head`, `amnt_san`, `dateofsan`, `deptID`, `empID`) VALUES
(1, 'sssss', 222222, '2024-02-28', 1, 1),
(2, 'sssss', 222222, '2024-02-28', 2, 1),
(3, 'ffffff', 300000, '2024-03-06', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
CREATE TABLE IF NOT EXISTS `department` (
  `deptID` int NOT NULL AUTO_INCREMENT,
  `dname` text NOT NULL,
  `location` text NOT NULL,
  `pwd` text NOT NULL,
  PRIMARY KEY (`deptID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`deptID`, `dname`, `location`, `pwd`) VALUES
(1, 'AIML', 'Library Block', '9f6e6800cfae7749eb6c486619254b9c'),
(2, 'CS', 'cs block', '77963b7a931377ad4ab5ad6a9cd718aa'),
(3, 'CSE', 'CSE Block', '271226cb355bdda491d38bfaf40f675d'),
(4, 'CSE', 'cs block', 'fcd0c398ba3c9bc0dbd90153ddb6d637');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `empID` int NOT NULL AUTO_INCREMENT,
  `ename` text NOT NULL,
  `position` text NOT NULL,
  `deptID` int NOT NULL,
  PRIMARY KEY (`empID`),
  KEY `deptID` (`deptID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`empID`, `ename`, `position`, `deptID`) VALUES
(1, 'shabarish', 'Manager', 1),
(2, 'Abhishek', 'manager', 2),
(3, 'saishri', 'sweeper', 1);

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

DROP TABLE IF EXISTS `expense`;
CREATE TABLE IF NOT EXISTS `expense` (
  `expID` int NOT NULL AUTO_INCREMENT,
  `edate` date NOT NULL,
  `purpose` text NOT NULL,
  `amount` int NOT NULL,
  `budgetID` int NOT NULL,
  PRIMARY KEY (`expID`),
  KEY `budgetID` (`budgetID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`expID`, `edate`, `purpose`, `amount`, `budgetID`) VALUES
(2, '2024-02-21', 'dwefr', 12345, 2);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `audits`
--
ALTER TABLE `audits`
  ADD CONSTRAINT `audits_ibfk_2` FOREIGN KEY (`audID`) REFERENCES `auditor` (`audID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `audits_ibfk_3` FOREIGN KEY (`budgetID`) REFERENCES `budget` (`budgetID`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `budget`
--
ALTER TABLE `budget`
  ADD CONSTRAINT `budget_ibfk_1` FOREIGN KEY (`deptID`) REFERENCES `department` (`deptID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `budget_ibfk_2` FOREIGN KEY (`empID`) REFERENCES `employee` (`empID`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`deptID`) REFERENCES `department` (`deptID`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `expense`
--
ALTER TABLE `expense`
  ADD CONSTRAINT `expense_ibfk_1` FOREIGN KEY (`budgetID`) REFERENCES `budget` (`budgetID`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
