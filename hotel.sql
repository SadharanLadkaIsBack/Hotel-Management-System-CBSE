-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 27, 2022 at 06:23 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_order`
--

DROP TABLE IF EXISTS `customer_order`;
CREATE TABLE IF NOT EXISTS `customer_order` (
  `Order_Id` varchar(50) NOT NULL,
  `room_no` int(50) NOT NULL,
  `Total_amt` varchar(100) NOT NULL,
  `Employee_Id` varchar(100) NOT NULL,
  `Bill_Status` varchar(100) NOT NULL DEFAULT 'PENDING',
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_order`
--

INSERT INTO `customer_order` (`Order_Id`, `room_no`, `Total_amt`, `Employee_Id`, `Bill_Status`, `Date`) VALUES
('3185', 401, '3735', 'NG2024', 'PAID', '2022-04-22 14:48:07'),
('2837', 401, '990', 'NG2024', 'PAID', '2022-04-22 14:52:30'),
('5035', 401, '1900', 'NG2024', 'PAID', '2022-04-22 14:53:58'),
('2721', 501, '3843', 'NG2024', 'PAID', '2022-04-23 06:07:34'),
('6478', 401, '3420', 'NG2024', 'PENDING', '2022-04-24 14:18:49'),
('2821', 801, '14465', 'NG2024', 'PAID', '2022-04-24 14:32:58'),
('2821', 801, '2670', 'NG2024', 'PAID', '2022-04-24 14:33:13');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `Employee_Id` varchar(50) NOT NULL,
  `Employee_Name` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `Employee_email` varchar(100) NOT NULL,
  PRIMARY KEY (`Employee_Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`Employee_Id`, `Employee_Name`, `password`, `Employee_email`) VALUES
('NG2024', 'Nitin Gupta', 'Nit@1234', 'nitingupta1906@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
CREATE TABLE IF NOT EXISTS `food` (
  `Catagories` varchar(100) DEFAULT NULL,
  `Menu` varchar(100) DEFAULT NULL,
  `Price` int(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`Catagories`, `Menu`, `Price`) VALUES
('Salad', 'Carrot Salad', 50),
('Salad', 'Caesar Salad', 100),
('Salad', 'Raw Papaya Salad', 80),
('pizza', 'Margherita Pizza', 149),
('pizza', 'Cheese & Corn Pizza', 165),
('pizza', 'Cheese & Tomato Pizza', 155),
('pizza', 'Double Cheese Margherita', 189),
('pizza', 'Fresh Veggie Pizza', 185),
('pizza', 'Peppy Paneer Pizza', 215),
('pizza', 'Veggie Paradise Pizza', 195),
('pizza', 'Deluxe Veggie Pizza', 235),
('pizza', 'Indi Tandoori Paneer', 249),
('pizza', 'Chicken Sausage', 169),
('pizza', 'Pepper Barbecue Chicken', 185),
('pizza', 'Pepper Barbecue & Onion', 195),
('pizza', 'Chicken Golden Delight', 235),
('pizza', 'Chicken Pepperoni', 305),
('pizza', 'Chicken Dominator', 310),
('pizza', 'Non Veg Supreme', 310),
('pizza', 'Indi Chiken Tikka', 310),
('noodles', 'Veg Hakka Noodles', 100),
('noodles', 'Veg Sezwan Noodles', 120),
('noodles', 'Chicken Hakka Noodles', 120),
('noodles', 'Chicken Sezwan Noodles', 130),
('noodles', 'Egg Noodles', 140),
('noodles', 'Schezwan Egg Noodles', 140),
('noodles', 'Mixeded Noodles', 195),
('noodles', 'Dragon Noodles', 215),
('noodles', 'Schezwan Mixeded', 200),
('starter', 'Veg Fingers Starters', 85),
('starter', 'Cheese Shotz ', 89),
('starter', 'Crispy Chicken', 160),
('starter', 'Chicken Kebab', 200),
('starter', 'Chicken Tikka', 180),
('starter', 'Chicken Tikka', 180),
('starter', 'Sabudana Tikki', 110),
('starter', 'Sweet Potato Tikki', 100),
('starter', 'Paneer Tikka', 120),
('breveges', 'Dark Frappe', 221),
('breveges', 'Devil?s Own Vanilla Cream', 185),
('breveges', 'Toffee Latte', 165),
('breveges', 'Signature Hot Chocolate', 145),
('breveges', 'Iced Shaken Tea', 160),
('breveges', 'Green Tea Latte', 160),
('main_course', 'Veg Kadai', 200),
('main_course', 'Veg Kolhapuri', 165),
('main_course', 'Mixeded Veg Curry', 150),
('main_course', 'Paneer Masala Button', 175),
('main_course', 'Paneer Chilli', 145),
('main_course', 'Paneer Chilli Manchurian', 190),
('main_course', 'Paneer Kolhapuri', 190),
('main_course', 'Paneer Kadai', 190),
('main_course', 'Masala Mushroom', 180),
('main_course', 'Mushroom Chilli', 165),
('main_course', 'Mushroom Manchurian', 165),
('main_course', 'Mushroom Kolhapuri', 165),
('main_course', 'Mushroom Kadai', 165),
('main_course', 'Gobi Manchurian', 165),
('main_course', 'Chilli Gobi', 155),
('main_course', 'Afghani Chicken', 185),
('main_course', 'Family Platter Regular', 185),
('main_course', 'Veg Biryani', 150),
('main_course', 'Mutton Biryani', 275),
('main_course', 'Chicken Biryani', 250),
('sandwiches', 'Alu Matar Sandwich', 25),
('sandwiches', 'Paneer Grilled Sandwich', 75),
('sandwiches', 'Veg Club Sandwich', 40),
('sandwiches', 'Veg Cheese Sandwich', 70),
('sandwiches', 'Pizza Sandwich', 89),
('sandwiches', 'Grilled Tandoori Sandwich', 110),
('sandwiches', 'Vegetable Sandwich', 20),
('sandwiches', 'Garden Sandwich', 60),
('sandwiches', 'Grilled Pasta Sandwich', 90),
('sandwiches', 'Mayo Sandwich', 30),
('sandwiches', 'Grilled Sandwich', 40),
('sandwiches', 'Cheese Chutney Sandwich', 60),
('sandwiches', 'Toasted Veg Sandwich', 50),
('breveges', 'White Chocolate Mocha', 210),
('breveges', 'Caffe Mocha', 200),
('breveges', 'Caramel Macchiato', 180),
('breveges', 'Hazelnut Latte', 170),
('breveges', 'Vanilla Latte', 180),
('breveges', 'Caffe Latte', 145),
('breveges', 'Cappuccino', 145),
('breveges', 'Caffe Americano', 115),
('breveges', 'Espresso Con Panna', 125),
('breveges', 'Espresso Macchiato', 130),
('breveges', 'Espresso', 120),
('dessert', 'Cheese Cake', 89),
('dessert', 'Chocolate Cake', 69),
('dessert', 'Red Velvet Cake', 69),
('dessert', 'Mango Ice Cream', 99),
('dessert', 'Cold Coco', 119),
('dessert', 'Apple Pie', 139),
('dessert', 'Mawa Cake', 69),
('dessert', 'Kulfi', 59),
('dessert', 'Malai Falooda', 95),
('dessert', 'Royal Falooda', 85),
('dessert', 'Pista Ice Cream', 99),
('dessert', 'Strawberry Ice Cream', 99),
('dessert', 'Vanilla Ice Cream', 99),
('dessert', 'Chocolate Ice Cream', 99),
('dessert', 'Chocolate Chip Brownie', 89),
('dessert', 'Gulab Jamun', 39),
('dessert', 'Nutella Pancakes', 99),
('dessert', 'Hot Fudge Nut Sundae', 110),
('dessert', 'Jalebis', 49),
('dessert', 'Chocolate Sandwich', 129),
('dessert', 'Malai Kulfi', 49),
('starter', 'Chilli Garlic Pops', 99),
('starter', 'Veg Hara Bhara Kebab', 299),
('starter', 'Tandoori Aloo', 80),
('starter', 'Tandoori Gobi', 110),
('starter', 'Pudina Paneer Tikka', 129),
('starter', 'Mushroom Tikka', 130),
('starter', 'Paneer Pahadi', 150),
('starter', 'Malai Paneer Tikka', 180),
('starter', 'Paneer Achari', 140);

-- --------------------------------------------------------

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
CREATE TABLE IF NOT EXISTS `guest` (
  `room_no` int(50) DEFAULT NULL,
  `guest_name` varchar(100) DEFAULT NULL,
  `guest_email` varchar(100) NOT NULL,
  `guest_phone` bigint(30) DEFAULT NULL,
  `guest_Id` varchar(100) DEFAULT NULL,
  `guest_ChekIn_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `guest_ChekOut_date` timestamp NULL DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guest`
--

INSERT INTO `guest` (`room_no`, `guest_name`, `guest_email`, `guest_phone`, `guest_Id`, `guest_ChekIn_date`, `guest_ChekOut_date`) VALUES
(601, 'Omkar Ambre', '', 1418529635, '741852963852', '2022-04-22 20:14:12', '2022-04-22 15:00:11'),
(401, 'Nitin', '', 9999999999, '999999999988', '2022-04-22 20:15:52', '2022-04-22 14:55:43'),
(501, 'Nitin', 'nitin@gmail', 4567945615, '123456789456', '2022-04-23 11:35:59', '2022-04-23 06:08:59'),
(401, 'Nitin', 'nitin1906@gmail.com', 4567894521, '456789456123', '2022-04-24 19:42:47', NULL),
(801, 'Nitin Gupta', 'nitin1906@gmail.com', 4567854123, '789456123456', '2022-04-24 19:52:16', '2022-04-24 14:36:36');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `UserId` varchar(20) NOT NULL,
  `First_name` varchar(50) DEFAULT NULL,
  `Last_name` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`UserId`, `First_name`, `Last_name`, `Password`, `Email`) VALUES
('Nitin', 'Nitin', 'Gupta', 'Nit@1234', 'nitingupta1906@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE IF NOT EXISTS `payment` (
  `pay_Id` int(20) NOT NULL AUTO_INCREMENT,
  `mode` varchar(100) DEFAULT NULL,
  `room_no` int(50) DEFAULT NULL,
  `Total_Amt` int(100) DEFAULT NULL,
  `Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pay_Id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`pay_Id`, `mode`, `room_no`, `Total_Amt`, `Date`) VALUES
(1, 'CASH', 601, 600, '2022-04-22 15:00:11'),
(2, 'UPI', 501, 4443, '2022-04-23 06:08:59'),
(3, 'UPI', 801, 17735, '2022-04-24 14:36:36');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
CREATE TABLE IF NOT EXISTS `room` (
  `room_No` int(10) NOT NULL,
  `room_price` int(50) NOT NULL,
  `room_status` varchar(100) DEFAULT 'AVAILABLE',
  PRIMARY KEY (`room_No`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_No`, `room_price`, `room_status`) VALUES
(101, 500, 'AVAILABLE'),
(201, 500, 'AVAILABLE'),
(301, 500, 'AVAILABLE'),
(501, 600, 'AVAILABLE'),
(401, 500, 'BOOKED'),
(601, 600, 'AVAILABLE'),
(701, 600, 'AVAILABLE'),
(801, 600, 'AVAILABLE'),
(901, 600, 'AVAILABLE');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
