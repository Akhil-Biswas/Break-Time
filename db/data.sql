USE `break_time`;
\! echo -e "\e[33m Dtabase Change\e[0m"

--veg_flag
INSERT IGNORE INTO veg_flag(flag_name)
VALUES ('veg'),('non_veg');
\! echo -e "\e[34m Data inserted into veg_flag \e[0m"

INSERT IGNORE INTO payment_status (status_name)
VALUES ('due'),('paid');
\! echo -e "\e[34m Data inserted into payment_status \e[0m"

INSERT IGNORE INTO payment_type (payment_name)
VALUES ('COD'),('UPI');
\! echo -e "\e[34m Data inserted into payment_type \e[0m"

INSERT IGNORE INTO order_status (status_name)
VALUES ('successful'),('delivered'),('not available'),('return');
\! echo -e "\e[34m Data inserted into order_status \e[0m"