-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 31, 2018 at 12:30 PM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hackathon`
--

-- --------------------------------------------------------

--
-- Table structure for table `adhardata`
--

CREATE TABLE `adhardata` (
  `adharnum` varchar(12) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `dateofbirth` date NOT NULL,
  `gender` int(1) NOT NULL,
  `contact` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adhardata`
--

INSERT INTO `adhardata` (`adharnum`, `name`, `address`, `dateofbirth`, `gender`, `contact`) VALUES
('111122223111', 'shivani patel', 'anand', '2002-04-09', 2, '8837722211'),
('111122223322', 'pragna thakkar', '56  City hall, gotri Road, anand', '2001-04-02', 2, '8448822211'),
('111122223332', 'jayesh thakkar', '6 race  Padra Road, Vadodara', '2002-09-21', 3, '8833822555'),
('111122223333', 'Rohan Pradhan', '202, City hall, Padra Road, Vadodara', '2000-04-23', 1, '8888822222'),
('111122223344', 'richa thakkar', '600 City hall, Padra Road, Vadodara', '2002-04-23', 2, '8833822211'),
('111122223349', 'meet thakkar', '600  town hall Road, ahmedabad', '2002-09-29', 2, '8837722211'),
('111122223366', 'keshani thakkar', '69  town hall Road, ahmedabad', '2002-04-26', 2, '883552212'),
('111125523344', 'rohit patel', '6 City hall, Padra Road, surat', '2007-04-23', 1, '8833822578'),
('111129893111', 'jay movaliya', 'surat', '2002-08-07', 1, '4543216789'),
('111199223344', 'viral shah', '6 City hall, Padra Road, rajkot', '2002-03-02', 5, '8877822211'),
('111332223344', 'pranay patel', '6  gg hall, Padra Road, surat', '2007-04-28', 1, '8866822211'),
('111662223344', 'khush chopda', '6 City hall, Padra Road, valsad', '2002-04-02', 1, '8773382221'),
('113322223344', 'shivani pathak', '88 City hall, Padra Road, Vadodara', '2008-04-23', 1, '8833822999'),
('115522223344', 'jay patel', '6 City hall, Padra Road,delhi', '2002-04-08', 1, '8877822211'),
('116122223111', 'keshani vyas', 'bharuch', '2000-03-16', 2, '9099121234'),
('211122223111', 'vivek baraiya', 'bhavnagar', '2002-09-29', 1, '6767543218'),
('218561823111', 'harsh patel', 'vadodara', '2001-09-11', 1, '9843215678'),
('218809023111', 'gargi vaniya', '7 pooja,anand', '2000-07-01', 2, '5654321567'),
('218822223111', 'dixita vyas', 'rajkot', '2002-08-29', 2, '1212121212'),
('218872223111', 'yashvi patel', 'diu', '2000-06-09', 2, '6767432190'),
('218889823111', 'kartik arya', '6 race course road, anand', '2000-09-09', 1, '5632787766'),
('218889824341', 'palak shah', 'ahmedabad', '2003-03-25', 2, '6767432156'),
('218889874111', 'prushty taylor', 'bharuch', '2000-03-09', 1, '4532178654'),
('219972223111', 'eva seth', '99 gotri road,vadodara', '2000-01-22', 2, '3434'),
('222233334444', 'Gangadhar Patel', '105, City hall, Padra Road, Vadodara', '2000-02-23', 1, '2222288888'),
('290989823111', 'bina vyas', 'jamnagar', '2003-09-11', 2, '5632168901');

-- --------------------------------------------------------

--
-- Table structure for table `certificate`
--

CREATE TABLE `certificate` (
  `srno` int(11) NOT NULL,
  `studentid` int(11) NOT NULL,
  `teacherid` int(11) NOT NULL,
  `certiname` varchar(20) NOT NULL,
  `certidate` date NOT NULL,
  `certiorg` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `level` varchar(20) NOT NULL,
  `rank` varchar(8) NOT NULL,
  `verified` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `certificate`
--

INSERT INTO `certificate` (`srno`, `studentid`, `teacherid`, `certiname`, `certidate`, `certiorg`, `type`, `level`, `rank`, `verified`) VALUES
(6, 70, 1, 'running', '2018-03-06', 'utk.org', 'sports', 'national', '2', 1),
(7, 71, 2, 'swimming', '2018-03-02', 'utk.org', 'sports', 'national', '1', 0),
(8, 99, 5, 'runnig', '2018-03-01', 'bvm.in', 'sports', 'state', '3', 0),
(9, 77, 4, 'quiz', '2017-11-08', 'xyz.org.in', 'acadamic', 'national', '2', 0),
(10, 123, 7, 'swimming', '2017-12-03', 'abc.in', 'academic', 'national', '3', 0),
(11, 44, 2, 'iq test', '2017-07-04', 'utk.in', 'academic', 'state', '3', 0),
(12, 33, 1, 'jk test', '2018-03-20', 'bvm.in', 'academic', 'state', '1', 0),
(13, 7, 6, 'long jump', '2018-03-07', 'xyz.org.in', 'sports', 'state', '2', 1),
(14, 1, 5, 'cricket', '2017-12-01', 'alembic.org', 'sports', 'international', '1', 1),
(15, 1, 3, 'hockey', '2017-11-21', 'ice.in', 'sports', 'national', '1', 1),
(16, 2, 4, 'foolball', '2018-03-01', 'fc.in', 'sports', 'state', '5', 1),
(17, 2, 4, 'singing', '2017-12-02', 'song.in', 'cultural', 'school', '2', 1),
(18, 3, 4, 'acting', '2018-03-01', 'act.n', 'cultural', 'state', '1', 1),
(19, 3, 4, 'vollyball', '2017-12-13', 'voo.in', 'sports', 'school', '2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `class_subject`
--

CREATE TABLE `class_subject` (
  `srno` int(11) NOT NULL,
  `sub_id` int(3) NOT NULL,
  `class` int(11) NOT NULL,
  `schoolid` int(11) NOT NULL,
  `subject` varchar(20) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `class_subject`
--

INSERT INTO `class_subject` (`srno`, `sub_id`, `class`, `schoolid`, `subject`, `year`) VALUES
(1, 0, 1, 1, 'Maths', 2018),
(2, 0, 1, 1, 'Science', 2018),
(4, 4, 2, 7, 'Maths', 2018),
(5, 4, 2, 7, 'hindi', 2018),
(6, 9, 6, 7, 'Maths', 2018),
(7, 999, 5, 6, 'Science', 2018),
(8, 30, 3, 2, 'science', 2018),
(9, 60, 6, 2, 'english', 2109),
(10, 20, 2, 6, 'science', 2017),
(11, 44, 4, 4, 'english', 2018),
(12, 68, 6, 1, 'Maths', 2018),
(13, 44, 4, 2, 'english', 2018),
(14, 23, 2, 6, 'science', 2018);

-- --------------------------------------------------------

--
-- Table structure for table `interest`
--

CREATE TABLE `interest` (
  `srno` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `studentid` int(11) NOT NULL,
  `interest` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `interest`
--

INSERT INTO `interest` (`srno`, `tid`, `studentid`, `interest`) VALUES
(1, 5, 1, 'cricket'),
(2, 6, 3, 'sining'),
(3, 4, 70, 'sports'),
(4, 2, 5, 'dance'),
(5, 5, 8, 'maths'),
(6, 9, 3, 'science'),
(7, 7, 10, 'cricket'),
(8, 6, 11, 'basketball');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `srno` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pwd` varchar(15) NOT NULL,
  `type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`srno`, `username`, `pwd`, `type`) VALUES
(1, 'khvyas1997@gmail.com', 'khv97', 'teacher'),
(2, 'hod@gmail.com', 'hod', 'princi'),
(3, 'hr12@gmail.com', '1212', 'teacher'),
(4, 'ric22@gmail.com', 'rere', 'teacher'),
(5, 'tt22@gmail.com', 'wwqq', 'princi'),
(6, 'khv@gmail.com', 'dede', 'teacher'),
(7, 'hi2323@gmail.com', '23ytyt448', 'princi'),
(8, 'aa@gmail.com', 'aa', 'teacher'),
(9, 'ht@gmail.com', 'gfgf', 't'),
(10, 'richa66@gmail.com', 'riccc', 'teacher'),
(11, 'kesh121@yahoo.com', 'khvv11', 'princi'),
(12, 'jay121@gmail.com', 'jaa12', 'princi'),
(13, 'shiv121@gmail.com', 'shiv@gmail.com', 'teacher');

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `srno` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `noti_des` varchar(500) NOT NULL,
  `seen_status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `notification`
--

INSERT INTO `notification` (`srno`, `tid`, `noti_des`, `seen_status`) VALUES
(3, 5, '70:  running  not verified', 1),
(4, 4, 'std 4th  roll no 58 not verified', 0),
(5, 4, 'std  4th roll no 7 not verified', 0);

-- --------------------------------------------------------

--
-- Table structure for table `principal`
--

CREATE TABLE `principal` (
  `srno` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` int(11) NOT NULL,
  `address` varchar(30) NOT NULL,
  `email` varchar(20) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `principal`
--

INSERT INTO `principal` (`srno`, `name`, `contact`, `address`, `email`, `qualification`, `pwd`) VALUES
(1, 'hod', 999818284, 'abccdsfg snu', 'hod@gmail.com', 'phd', 'hod'),
(7, 'hod1', 2147483647, '1jladjljd', 'hod1@gmail.com', 'phD', 'abcd'),
(8, 'jk thakkar', 2147483647, 'vadodara', 'jk@gmail.com', 'm.tech', 'jkjk'),
(9, 'keshani thakkar', 2147483647, 'anand', 'tyty@gmail.com', 'B.E', 'trt1212'),
(10, 'rohit patel ', 454545451, 'anand', 'df@gmail.com', 'b.e', 'sfesxc'),
(11, 'darshak', 2147483647, 'anand', 'dgt121@gmail.com', 'phd', 'dgttt'),
(12, 'tannavala', 2147483647, 'ahmedabad', 'tanna@gmail.com', 'm.tech', 'tanna1');

-- --------------------------------------------------------

--
-- Table structure for table `school`
--

CREATE TABLE `school` (
  `srno` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `schoolid` varchar(10) NOT NULL,
  `pwd` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `website` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school`
--

INSERT INTO `school` (`srno`, `name`, `address`, `schoolid`, `pwd`, `email`, `website`) VALUES
(1, 'Kendriya Vidhyalaya', '12,sanskar bhavan road,vadodar', 'S5612', 'oppo97', 'kendriya@gmail.com', 'kdvb.ac.in'),
(2, 'Narmada Vidhyalaya', '21,sanskar bhavan road,bharuch', 'S5712', 'one97', 'bvbs@gmail.com', 'bvbs.ac.in'),
(3, 'Narmada Vidhyalaya11', '11,sanskar bhavan road,bharuch', 'S5712', 'abcs', 'bvbs11@gmail.com', 'bvbs11.ac.in'),
(4, 'tejas vidyalaya', 'vadodara', '3', 'tejas', 'tejas@gmail.com', 'tejas.in'),
(5, 'utkarsh', 'anand', '6', 'utk', 'utk@gmail.com', 'utk.vid.in'),
(6, 'nootan vidyalaya', 'bharuch ', '9', 'nootan22', 'nootana6@gmail.com', 'ntnte.in'),
(8, 'narayan vidyalaya', 'surat', '10', 'narya', 'narya88@gmail.com', 'narya.in');

-- --------------------------------------------------------

--
-- Table structure for table `school_facilities`
--

CREATE TABLE `school_facilities` (
  `srno` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `facility` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school_facilities`
--

INSERT INTO `school_facilities` (`srno`, `sid`, `facility`) VALUES
(2, 1, 'Projectors'),
(3, 1, 'Canteen');

-- --------------------------------------------------------

--
-- Table structure for table `school_principal`
--

CREATE TABLE `school_principal` (
  `srno` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `pid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school_principal`
--

INSERT INTO `school_principal` (`srno`, `sid`, `pid`) VALUES
(1, 1, 1),
(2, 3, 7),
(3, 3, 1),
(4, 2, 6),
(5, 5, 6),
(6, 5, 7),
(7, 7, 1),
(8, 7, 2),
(9, 8, 8),
(10, 8, 6);

-- --------------------------------------------------------

--
-- Table structure for table `school_teacher`
--

CREATE TABLE `school_teacher` (
  `srno` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `tid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school_teacher`
--

INSERT INTO `school_teacher` (`srno`, `sid`, `tid`) VALUES
(1, 1, 5),
(2, 2, 1),
(3, 1, 6),
(4, 1, 7),
(5, 2, 44),
(6, 21, 76),
(7, 7, 99),
(8, 7, 100),
(9, 10, 6),
(10, 10, 9),
(11, 3, 4),
(12, 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL,
  `srno` int(10) NOT NULL,
  `adharnum` varchar(16) NOT NULL,
  `parentincome` int(11) NOT NULL,
  `joiningstd` int(11) NOT NULL,
  `currentschoolid` int(11) NOT NULL,
  `pwdstatus` int(1) NOT NULL,
  `parent_priority` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`student_id`, `srno`, `adharnum`, `parentincome`, `joiningstd`, `currentschoolid`, `pwdstatus`, `parent_priority`) VALUES
(71, 1, '111122223322', 70000, 2, 5, 0, 0),
(77, 2, '111122223366', 60000, 6, 5, 0, 0),
(44, 3, '111332223344', 45000, 1, 2, 1, 2),
(7, 4, '111332223344', 32323, 1, 2, 0, 1),
(77, 5, '111662223344', 67676, 3, 3, 1, 3),
(33, 6, '111199223344', 21212, 3, 3, 0, 1),
(1, 7, '218889823111', 60000, 2, 2, 0, 3),
(3, 11, '218889823111', 45000, 1, 2, 0, 1),
(2, 12, '111122223349', 43433, 2, 3, 1, 2),
(5, 13, '111122223349', 23232, 0, 4, 0, 2),
(9, 14, '111188223349', 43432, 1, 5, 1, 4),
(1, 15, '111122223344', 90000, 1, 2, 0, 3),
(2, 16, '111125523344', 56543, 1, 4, 0, 3),
(3, 17, '211122223111', 21212, 2, 4, 0, 3),
(4, 18, '111129893111', 45454, 4, 2, 0, 3),
(5, 19, '116122223111', 43217, 2, 6, 0, 2),
(6, 20, '111122223111', 54321, 2, 4, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `student_class`
--

CREATE TABLE `student_class` (
  `srno` int(11) NOT NULL,
  `studentid` int(11) NOT NULL,
  `class` int(11) NOT NULL,
  `schoolid` int(11) NOT NULL,
  `remarks` varchar(50) NOT NULL,
  `overall_rank` float NOT NULL,
  `rank` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_class`
--

INSERT INTO `student_class` (`srno`, `studentid`, `class`, `schoolid`, `remarks`, `overall_rank`, `rank`, `year`) VALUES
(1, 1, 7, 1, 'good at academics ', 4, 92, 2018),
(2, 2, 2, 4, 'good at academics ', 3.4, 70, 2108),
(3, 3, 2, 3, 'good at academics ', 4.5, 95, 2018),
(4, 4, 4, 5, 'good at cultural', 3.5, 80, 2018),
(5, 5, 2, 6, 'good at cultural', 4, 92, 2018),
(6, 6, 3, 2, 'good at sports', 3.6, 80, 2018);

-- --------------------------------------------------------

--
-- Table structure for table `subject_marks`
--

CREATE TABLE `subject_marks` (
  `srno` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `subjid` int(11) NOT NULL,
  `marks` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject_marks`
--

INSERT INTO `subject_marks` (`srno`, `student_id`, `subjid`, `marks`, `year`) VALUES
(1, 70, 70, 69, 2018),
(2, 70, 71, 60, 2018),
(3, 71, 31, 77, 2018),
(4, 71, 33, 60, 2018),
(5, 3, 55, 77, 2018),
(6, 3, 51, 90, 2018),
(7, 4, 44, 60, 2018),
(8, 4, 41, 90, 2018);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `srno` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `contact` int(11) NOT NULL,
  `address` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`srno`, `name`, `contact`, `address`, `email`, `qualification`, `pwd`) VALUES
(1, 'keshani bhatt', 999801029, 'kdldjdjladjladjljd', 'khvyas1997@gmail.com', 'computer eng.', '1'),
(5, 'shivani pathak', 999807027, '1jladjljd', 'jsk7667@gmail.com', 'dlekk eng.', 'keshani3'),
(6, 'rohit shah', 999807029, '1jladjljd', 'jsk77667@gmail.com', 'dlekk eng.', 'lucy'),
(7, 'richa rajvir', 999807021, 'vadodara', 'js2227667@gmail.com', 'comp.eng.', '1212'),
(8, 'jay oatel', 2147483647, 'surat', 'jay121@gmail.com', 'b.e comp', 'jay'),
(9, 'vivek thakore', 2147483647, 'diu', 'viviek1212@gmail.com', 'mca', 'vivek11');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_class`
--

CREATE TABLE `teacher_class` (
  `srno` int(11) NOT NULL,
  `tid` int(11) NOT NULL,
  `class` int(11) NOT NULL,
  `year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teacher_class`
--

INSERT INTO `teacher_class` (`srno`, `tid`, `class`, `year`) VALUES
(1, 1, 1, 2018),
(2, 2, 2, 2018),
(3, 6, 3, 2018),
(4, 5, 4, 2018),
(5, 2, 2, 2018),
(6, 3, 3, 2018),
(7, 4, 4, 2018);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adhardata`
--
ALTER TABLE `adhardata`
  ADD PRIMARY KEY (`adharnum`);

--
-- Indexes for table `certificate`
--
ALTER TABLE `certificate`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `class_subject`
--
ALTER TABLE `class_subject`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `interest`
--
ALTER TABLE `interest`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `principal`
--
ALTER TABLE `principal`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `school`
--
ALTER TABLE `school`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `school_facilities`
--
ALTER TABLE `school_facilities`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `school_principal`
--
ALTER TABLE `school_principal`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `school_teacher`
--
ALTER TABLE `school_teacher`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `student_class`
--
ALTER TABLE `student_class`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `subject_marks`
--
ALTER TABLE `subject_marks`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `teacher_class`
--
ALTER TABLE `teacher_class`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `certificate`
--
ALTER TABLE `certificate`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `class_subject`
--
ALTER TABLE `class_subject`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `interest`
--
ALTER TABLE `interest`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT for table `notification`
--
ALTER TABLE `notification`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `principal`
--
ALTER TABLE `principal`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `school`
--
ALTER TABLE `school`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `school_facilities`
--
ALTER TABLE `school_facilities`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `school_principal`
--
ALTER TABLE `school_principal`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `school_teacher`
--
ALTER TABLE `school_teacher`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `srno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT for table `student_class`
--
ALTER TABLE `student_class`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `subject_marks`
--
ALTER TABLE `subject_marks`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `teacher_class`
--
ALTER TABLE `teacher_class`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
