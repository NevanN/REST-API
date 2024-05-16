-- create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS userinfo;

-- use the database
USE userinfo;

-- create the user table
CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `user`
  MODIFY userid int(11) NULL;

-- insert sample data into the user table
INSERT INTO `user` (`userid`, `name`, `email`, `password`) 
VALUES (1, 'John Doe', 'doe@gmail.com', '123'),
       (2, 'Kevin', 'kevin@gmail.com', '123');
