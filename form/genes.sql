-- phpMyAdmin SQL Dump
-- version 3.2.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 20, 2014 at 05:32 PM
-- Server version: 5.1.40
-- PHP Version: 5.3.15

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `PCBio`
--

-- --------------------------------------------------------

--
-- Table structure for table `genes`
--

DROP TABLE IF EXISTS `genes`;
CREATE TABLE IF NOT EXISTS `genes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `taxon` varchar(64) NOT NULL,
  `gene` varchar(64) NOT NULL,
  `sequence` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
