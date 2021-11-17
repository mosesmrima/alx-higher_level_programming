-- create user and grant them all priviledges

CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY "user_0d_1_pwd";
GRANT * ON *.* TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;
