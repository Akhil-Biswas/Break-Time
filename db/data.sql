USE `break_time`;
\! echo -e "\e[33m Database Changed \e[0m";

-- ========================
-- SEX
-- ========================
INSERT IGNORE INTO sex (sex_id, sex)
VALUES ('M','male'), ('F','female');
\! echo -e "\e[34m Data inserted into sex \e[0m";

-- ========================
-- VEG FLAG
-- ========================
INSERT IGNORE INTO veg_flag (flag_name)
VALUES ('veg'), ('non_veg');
\! echo -e "\e[34m Data inserted into veg_flag \e[0m";

-- ========================
-- PAYMENT STATUS
-- ========================
INSERT IGNORE INTO payment_status (status_name)
VALUES ('due'), ('paid'), ('failed');
\! echo -e "\e[34m Data inserted into payment_status \e[0m";

-- ========================
-- PAYMENT TYPE
-- ========================
INSERT IGNORE INTO payment_type (payment_name)
VALUES ('COD'), ('UPI');
\! echo -e "\e[34m Data inserted into payment_type \e[0m";

-- ========================
-- ORDER STATUS
-- ========================
INSERT IGNORE INTO order_status (status_name)
VALUES 
('placed'),
('confirmed'),
('preparing'),
('delivered'),
('cancelled'),
('failed'),
('returned');
\! echo -e "\e[34m Data inserted into order_status \e[0m";