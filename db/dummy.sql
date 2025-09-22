USE `break_time`;
\! echo -e "\e[33m Database Changed \e[0m";

-- ========================
-- USERS
-- ========================
INSERT INTO users (f_name,m_name, l_name,sex_id, mobile_number,email_id,pass, enrolled_date ,last_modify_date) 
VALUES 
('Radhe',NULL,'Krishna','M',8016627566,NULL,'akhil',NOW(),NOW()),
('Restaurant',NULL,'Owner','M',8374648883,NULL,'ownerpass',NOW(),NOW()),
('Sita',NULL,'Devi','F',9123456789,'sita@example.com','sita123',NOW(),NOW()),
('Amit','Kumar','Sharma','M',9988776655,'amit@example.com','amit123',NOW(),NOW()),
('Priya',NULL,'Singh','F',8877665544,'priya@example.com','priya123',NOW(),NOW());

\! echo -e "\e[34m Dummy users inserted \e[0m";

-- ========================
-- DEPARTMENT
-- ========================
INSERT INTO department (department_name) VALUES
('BCA'),
('BBA'),
('BTECH'),
('Civil');

\! echo -e "\e[34m Dummy departments inserted \e[0m";

-- ========================
-- ACADEMIC YEAR
-- ========================
INSERT INTO academic_year (year_name, department_id) VALUES
('First Year',1),
('Second Year',1),
('Third Year',1),
('First Year',2),
('Second Year',2);

\! echo -e "\e[34m Dummy academic years inserted \e[0m";

-- ========================
-- SECTION
-- ========================
INSERT INTO section (section, year_id) VALUES
('A',1),
('B',1),
('A',2);

\! echo -e "\e[34m Dummy sections inserted \e[0m";

-- ========================
-- STUDENT (link users to departments/sections)
-- ========================
INSERT INTO student (students_id, department, section) VALUES
(1,1,1), -- Radhe -> BCA, First Year, Sec A
(3,1,2), -- Sita -> BCA, First Year, Sec B
(4,1,3), -- Amit -> BCA, Second Year, Sec A
(5,2,1); -- Priya -> BBA, First Year, Sec A

\! echo -e "\e[34m Dummy students inserted \e[0m";

-- ========================
-- CR (class representatives)
-- ========================
INSERT INTO cr (department_id, section_id, student_id) VALUES
(1,1,1),
(1,2,3),
(1,3,4),
(2,1,5);

\! echo -e "\e[34m Dummy CRs inserted \e[0m";

-- ========================
-- RESTAURANT
-- ========================
INSERT INTO restaurant (restaurant_id,name,location,upi1,upi2,upi3) VALUES
(2, 'Central Canteen','Q9CG+29W','abc@ybl','8374648883@ybl',NULL),
(3,'Campus Canteen','Block A','canteen@ybl','canteen2@ybl',NULL),
(4,'Main Mess','Block B','mess@ybl',NULL,NULL),
(5,'Food Court','Block C','foodcourt@ybl','fc2@ybl','fc3@ybl');

\! echo -e "\e[34m Dummy restaurants inserted \e[0m";

-- ========================
-- CATEGORY
-- ========================
INSERT INTO category (category) VALUES
('Snacks'),
('Beverages'),
('Main Course'),
('Desserts');

\! echo -e "\e[34m Dummy categories inserted \e[0m";

-- ========================
-- MENU
-- ========================
INSERT INTO menu (name,price,veg_flag,category,restaurant_id,enrolled_date,last_modify_date) VALUES
('Sandwich',30,1,1,3,NOW(),NOW()),
('Juice',25,1,2,3,NOW(),NOW()),
('Paneer Thali',120,1,3,4,NOW(),NOW()),
('Chicken Curry',150,2,3,4,NOW(),NOW()),
('Ice Cream',50,1,4,5,NOW(),NOW()),
('Burger',60,2,1,5,NOW(),NOW());

\! echo -e "\e[34m Dummy menu inserted \e[0m";

-- ========================
-- ITEM CATEGORY
-- ========================
INSERT INTO item_category (item_id,category_id) VALUES
(1,1),
(2,2),
(3,3),
(4,3),
(5,4),
(6,1);

\! echo -e "\e[34m Dummy item_category inserted \e[0m";

-- ========================
-- USER FAV ITEMS
-- ========================
INSERT INTO user_fav_items (user_id,item_id) VALUES
(1,1),
(3,2),
(4,3),
(5,4),
(1,5),
(2,6);

\! echo -e "\e[34m Dummy user fav items inserted \e[0m";

-- ========================
-- PAYMENT
-- ========================
INSERT INTO payment (amount,payment_type_id,status_id) VALUES
(100,1,2), -- paid COD
(50,2,1),  -- due UPI
(200,2,2), -- paid UPI
(150,1,3); -- failed COD

\! echo -e "\e[34m Dummy payments inserted \e[0m";

-- ========================
-- ORDERS
-- ========================
INSERT INTO orders (`time`,`user_id`,`status_id`,`payment_id`) VALUES
(NOW(),1,1,1),
(NOW(),3,2,2),
(NOW(),4,4,3),
(NOW(),5,5,4);

\! echo -e "\e[34m Dummy orders inserted \e[0m";

-- ========================
-- ORDERS ITEMS
-- ========================
INSERT INTO orders_items (order_id,item_id,quantity,status_id) VALUES
(1,1,2,1), -- Sandwich x2
(1,2,1,2), -- Juice x1
(2,3,1,3), -- Paneer Thali
(3,4,2,4), -- Chicken Curry x2
(4,5,1,5), -- Ice Cream
(4,6,3,1); -- Burger x3

\! echo -e "\e[34m Dummy orders_items inserted \e[0m";