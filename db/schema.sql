-- https://drawsql.app/teams/music-express/diagrams/break-time
-- DDL 


DROP DATABASE IF EXISTS `break_time`;
\! echo -e "\e[31m Dtabase deleted\e[0m"


CREATE DATABASE IF NOT EXISTS `break_time`;
\! echo -e "\e[32m Dtabase Created\e[0m"
USE `break_time`;

\! echo -e "\e[33m Dtabase Change\e[0m"


/*
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `student`;
DROP TABLE IF EXISTS `department`;
DROP TABLE IF EXISTS `section`;
DROP TABLE IF EXISTS `cr`;
DROP TABLE IF EXISTS `menu`;
\! echo -e "\e[31mALL TABLE deleted\e[0m"
*/

-- Create users table
CREATE TABLE IF NOT EXISTS `users`(
    user_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `f_name` char(50) NOT NULL,
    `m_name` char(20),
    `l_name` char(50) NOT NULL,
    `sex_id` char (1) NULL,
    `mobile_number` BIGINT,
    `email_id` VARCHAR(255),
    `pass` VARCHAR(255), -- hash password
    `enrolled_date` DATETIME,
    `last_modify_date` DATETIME,
    --
    CONSTRAINT `chk_mobile_or_email` 
        CHECK (`mobile_number` IS NOT NULL OR `email_id` IS NOT NULL)
    );

\! echo -e "\e[32mCreate users table\e[0m"


-- Create student table 
CREATE TABLE IF NOT EXISTS `sex`(
    `sex_id` CHAR(1) PRIMARY KEY,
    `sex` CHAR(20) NOT NULL
    );
\! echo -e "\e[32mCreate sex table\e[0m"
ALTER TABLE
    `users` ADD CONSTRAINT
    `fk_user_sex`
    FOREIGN KEY (`sex_id`) REFERENCES `sex`(`sex_id`);

-- Create student table 
CREATE TABLE IF NOT EXISTS `student`(
    `students_id` INT UNSIGNED PRIMARY KEY,
    `department` INT UNSIGNED,
    `section` INT UNSIGNED,
    CONSTRAINT 
    `user_student` FOREIGN KEY(`students_id`) REFERENCES `users`(`user_id`)
    );

\! echo -e "\e[32mCreate user.student table\e[0m"

-- Department => year => section
-- Create Department table
CREATE TABLE IF NOT EXISTS `department`(
    `department_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `department_name` CHAR(255) NOT NULL
);
\! echo -e "\e[32mCreate Student Department table\e[0m"

-- academic_year table
CREATE TABLE `academic_year` (
    `year_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `year_name` CHAR(20) NOT NULL,
    `department_id` INT UNSIGNED NOT NULL,
    CONSTRAINT `fk_department_year`
    FOREIGN KEY(`department_id`) REFERENCES `department`(`department_id`),
    CONSTRAINT `uq_year_dept` UNIQUE (year_name, department_id)
);
\! echo -e "\e[32mCreate Student academic_year table\e[0m"


-- Create Section table 
CREATE TABLE IF NOT EXISTS `section`(
    `section_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `section` CHAR(255) NOT NULL,
    `year_id` INT UNSIGNED NOT NULL,
    CONSTRAINT `fk_department_year_section`
    FOREIGN KEY(`year_id`) REFERENCES `academic_year`(`year_id`)
);

\! echo -e "\e[32mCreate Student Section table\e[0m"

ALTER TABLE
    `student` ADD CONSTRAINT
    `fk_student_department`
    FOREIGN KEY (`department`) REFERENCES `department`(`department_id`);

ALTER TABLE
    `student` ADD CONSTRAINT
    `fk_student_section`
    FOREIGN KEY (`section`) REFERENCES `section`(`section_id`);


--cr
CREATE TABLE `cr`(
    `cr_id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `department_id` INT UNSIGNED NOT NULL,
    `section_id` INT UNSIGNED NOT NULL,
    `student_id` INT UNSIGNED NOT NULL,
    CONSTRAINT `department_cr` FOREIGN KEY(`department_id`) REFERENCES `department`(`department_id`),
    CONSTRAINT `section_cr` FOREIGN KEY(`section_id`) REFERENCES `section`(`section_id`),
    CONSTRAINT `student_cr` FOREIGN KEY(`student_id`) REFERENCES `student`(`students_id`)
);

\! echo -e "\e[32m cr Table Created\e[0m"

CREATE TABLE `restaurant`(
    `restaurant_id` INT UNSIGNED NOT NULL,
    `name` VARCHAR(70) NOT NULL,
    `location` VARCHAR(50) NULL,
    `upi1` VARCHAR(50) NOT NULL,
    `upi2` VARCHAR(50) NULL,
    `upi3` VARCHAR(50) NULL,
    CONSTRAINT `fk_restaurant_user` FOREIGN KEY(`restaurant_id`) REFERENCES `users`(`user_id`)
);

\! echo -e "\e[32m Restaurant Table Created\e[0m"


-- menu
CREATE TABLE `menu`(
    `item_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `price` INT UNSIGNED NOT NULL,
    `veg_flag` INT UNSIGNED NOT NULL,
    `category` INT UNSIGNED,
    `restaurant_id` INT UNSIGNED NOT NULL,
    `enrolled_date` DATETIME,
    `last_modify_date` DATETIME,
    CONSTRAINT 
    `fx_restaurant_item` FOREIGN KEY(`restaurant_id`) REFERENCES `restaurant`(`restaurant_id`)
);

\! echo -e "\e[32m menu Table Created\e[0m"


CREATE TABLE `veg_flag`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `flag_name` VARCHAR(255) NOT NULL UNIQUE,
    -- Only allow two possible values 
    CONSTRAINT 
    `Possible_Value` CHECK(`flag_name` IN ('veg','non_veg'))
);

\! echo -e "\e[32m veg_flag Table Created\e[0m"


ALTER TABLE `menu`
ADD CONSTRAINT
`VegType` FOREIGN KEY (`veg_flag`) REFERENCES`veg_flag`(`id`);


CREATE TABLE `category`(
    `category_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `category` VARCHAR(255) NOT NULL
);

\! echo -e "\e[32m category Table Created\e[0m"


CREATE TABLE `item_category`(
    `item_id` BIGINT UNSIGNED NOT NULL,
    `category_id` INT UNSIGNED NOT NULL,
    CONSTRAINT
    `fk_item` FOREIGN KEY (`item_id`) REFERENCES `menu`(`item_id`),
    CONSTRAINT
    `fk_category` FOREIGN KEY (`category_id`) REFERENCES `category`(`category_id`)
);

\! echo -e "\e[32m item_category Table Created\e[0m"


CREATE TABLE `user_fav_items`(
    `user_id` INT UNSIGNED NOT NULL,
    `item_id` BIGINT UNSIGNED NOT NULL,
    CONSTRAINT
    `fk_user_fav` FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`),
    CONSTRAINT
    `fk_fav_item` FOREIGN KEY (`item_id`) REFERENCES `menu`(`item_id`)
);

\! echo -e "\e[32m user_fav_items Table Created\e[0m"


-- ORDER
CREATE TABLE `order_status`(
    `status_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `status_name` CHAR(20) NOT NULL UNIQUE,
    CONSTRAINT `Possible_Value`
    CHECK(`status_name`IN ('placed','confirmed','preparing','delivered','cancelled','failed','returned'))
);

\! echo -e "\e[32m status_code Table Created\e[0m"


CREATE TABLE `payment_status`(
    `status_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `status_name` CHAR(10) NOT NULL UNIQUE,
    CONSTRAINT `Possible_Value`
    CHECK(`status_name`IN ('due','paid','failed'))
);


CREATE TABLE `orders`(
    `order_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `time` DATETIME NOT NULL,
    `user_id` INT UNSIGNED NOT NULL,
    `status_id` INT UNSIGNED NOT NULL,
    `payment_id` BIGINT UNSIGNED NULL, -- user can order without pay (payment done after delivere)
    CONSTRAINT
    `fk_user` FOREIGN KEY(`user_id`) REFERENCES `users`(`user_id`),
    CONSTRAINT
    `fk_order_status` FOREIGN KEY(`status_id`) REFERENCES `order_status`(`status_id`)
);

\! echo -e "\e[32m Orders Table Created\e[0m"


CREATE TABLE `orders_items`(
    `order_id` BIGINT UNSIGNED NOT NULL,
    `item_id` BIGINT UNSIGNED NOT NULL,
    `quantity` INT UNSIGNED NOT NULL,
    `status_id` INT UNSIGNED NOT NULL,
    CONSTRAINT
    `fk_order_id` FOREIGN KEY(`order_id`) REFERENCES `orders`(`order_id`),
    CONSTRAINT
    `fk_item_id` FOREIGN KEY(`item_id`) REFERENCES `menu`(`item_id`),
    CONSTRAINT
    `fk_order_item_status` FOREIGN KEY(`status_id`) REFERENCES `order_status`(`status_id`)
);

\! echo -e "\e[32m orders_items Table Created\e[0m"


CREATE TABLE `payment`(
    `payment_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `amount` INT UNSIGNED NOT NULL,
    `payment_type_id` INT UNSIGNED NOT NULL,
    `status_id` INT UNSIGNED NOT NULL,
    CONSTRAINT
    `fk_payment_status` FOREIGN KEY(`status_id`) REFERENCES `payment_status`(`status_id`)
);


ALTER TABLE `orders`
    ADD CONSTRAINT
    `fk_payment` FOREIGN KEY(`payment_id`) REFERENCES `payment`(`payment_id`);

\! echo -e "\e[32m payment Table Created\e[0m"


CREATE TABLE `payment_type`(
    `payment_type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `payment_name` CHAR(255) NOT NULL UNIQUE,
    CONSTRAINT `Possible_Value`
    CHECK(`payment_name`In('COD','UPI'))
);


ALTER TABLE `payment`
    ADD CONSTRAINT `fk_payment_type` FOREIGN KEY(`payment_type_id`) REFERENCES `payment_type`(`payment_type_id`);

\! echo -e "\e[32m payment_type Table Created\e[0m"