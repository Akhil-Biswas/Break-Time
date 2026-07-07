-- =====================================================================
-- College Canteen Management System
-- Seed Data
-- =====================================================================

-- ---------------------------------------------------------------------
-- Roles
-- ---------------------------------------------------------------------
INSERT INTO roles (name) VALUES
('HOD'),
('Restaurant'),
('Student');

-- ---------------------------------------------------------------------
-- Departments
-- ---------------------------------------------------------------------
INSERT INTO departments (name) VALUES
('Computer Science & Engineering'),
('Electronics & Communication Engineering'),
('Mechanical Engineering'),
('Civil Engineering'),
('Electrical Engineering');

-- ---------------------------------------------------------------------
-- Sections
-- ---------------------------------------------------------------------
INSERT INTO sections (name, department_id) VALUES
('A',1),
('B',1),
('A',2),
('B',2),
('A',3),
('B',3),
('A',4),
('A',5);

-- ---------------------------------------------------------------------
-- Genders
-- ---------------------------------------------------------------------
INSERT INTO genders (name) VALUES
('Male'),
('Female'),
('Other');

-- ---------------------------------------------------------------------
-- Users
-- Password = Password@123
-- BCrypt Hash
-- ---------------------------------------------------------------------
INSERT INTO users
(f_name,m_name,l_name,email,password_hash,phone,photo,address,role_id)
VALUES

-- HODs
('Amit',NULL,'Sharma','amit.sharma@college.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'9876543210',NULL,'Kolkata',1),

('Priya',NULL,'Mukherjee','priya.mukherjee@college.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'9876543211',NULL,'Kolkata',1),

-- Restaurants
('Campus',NULL,'Cafe','cafe@college.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'9000000001',NULL,'Main Campus',2),

('Food',NULL,'Corner','foodcorner@college.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'9000000002',NULL,'North Block',2),

-- Students
('Rahul',NULL,'Das','rahul.das@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000001',NULL,'Kolkata',3),

('Sneha',NULL,'Roy','sneha.roy@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000002',NULL,'Howrah',3),

('Arjun',NULL,'Sen','arjun.sen@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000003',NULL,'Kolkata',3),

('Neha',NULL,'Paul','neha.paul@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000004',NULL,'Kolkata',3),

('Sourav',NULL,'Ghosh','sourav.ghosh@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000005',NULL,'Hooghly',3),

('Ananya',NULL,'Dey','ananya.dey@student.edu',
'$2y$10$7EqJtq98hPqEX7fNZaFWoOHi6A6Q671O5jM90oCbGyF/F7fs/3G2.',
'8000000006',NULL,'Kolkata',3);

-- ---------------------------------------------------------------------
-- HOD Details
-- ---------------------------------------------------------------------
INSERT INTO hod_details
(user_id,department_id)
VALUES
(1,1),
(2,2);

-- ---------------------------------------------------------------------
-- Restaurant Details
-- ---------------------------------------------------------------------
INSERT INTO restaurant_details
(user_id,restaurant_name,opening_time,closing_time,is_open)
VALUES
(3,'Campus Cafe','08:00:00','18:00:00',TRUE),
(4,'Food Corner','09:00:00','20:00:00',TRUE);

-- ---------------------------------------------------------------------
-- Student Details
-- ---------------------------------------------------------------------
INSERT INTO student_details
(user_id,roll_number,department_id,semester,section_id,is_cr,gender_id)
VALUES

(5,'23CSE001',1,5,1,TRUE,1),
(6,'23CSE002',1,5,1,FALSE,2),
(7,'23CSE003',1,5,2,FALSE,1),
(8,'23ECE001',2,3,3,TRUE,2),
(9,'23ME001',3,1,5,FALSE,1),
(10,'23CSE004',1,5,2,FALSE,2);