/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.35 : Database - ddos attack
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ddos attack` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `ddos attack`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add branch',7,'add_branch'),
(26,'Can change branch',7,'change_branch'),
(27,'Can delete branch',7,'delete_branch'),
(28,'Can view branch',7,'view_branch'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add user',9,'add_user'),
(34,'Can change user',9,'change_user'),
(35,'Can delete user',9,'delete_user'),
(36,'Can view user',9,'view_user'),
(37,'Can add transaction',10,'add_transaction'),
(38,'Can change transaction',10,'change_transaction'),
(39,'Can delete transaction',10,'delete_transaction'),
(40,'Can view transaction',10,'view_transaction'),
(41,'Can add report_table',11,'add_report_table'),
(42,'Can change report_table',11,'change_report_table'),
(43,'Can delete report_table',11,'delete_report_table'),
(44,'Can view report_table',11,'view_report_table'),
(45,'Can add feedback',12,'add_feedback'),
(46,'Can change feedback',12,'change_feedback'),
(47,'Can delete feedback',12,'delete_feedback'),
(48,'Can view feedback',12,'view_feedback'),
(49,'Can add complaint',13,'add_complaint'),
(50,'Can change complaint',13,'change_complaint'),
(51,'Can delete complaint',13,'delete_complaint'),
(52,'Can view complaint',13,'view_complaint'),
(53,'Can add account_details',14,'add_account_details'),
(54,'Can change account_details',14,'change_account_details'),
(55,'Can delete account_details',14,'delete_account_details'),
(56,'Can view account_details',14,'view_account_details'),
(57,'Can add request',15,'add_request'),
(58,'Can change request',15,'change_request'),
(59,'Can delete request',15,'delete_request'),
(60,'Can view request',15,'view_request'),
(61,'Can add request_table',15,'add_request_table'),
(62,'Can change request_table',15,'change_request_table'),
(63,'Can delete request_table',15,'delete_request_table'),
(64,'Can view request_table',15,'view_request_table'),
(65,'Can add log_tb',16,'add_log_tb'),
(66,'Can change log_tb',16,'change_log_tb'),
(67,'Can delete log_tb',16,'delete_log_tb'),
(68,'Can view log_tb',16,'view_log_tb');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$SsqsxefogKCy7utzajNfKm$ydXSm/pNpYTU7LL77/o8RNScbABCLjiRsDC3icy44+U=','2024-03-19 05:32:59.684615',1,'admin','','','admin@gmail.com',1,1,'2023-12-30 08:55:33.726918');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(14,'dos','account_details'),
(7,'dos','branch'),
(13,'dos','complaint'),
(12,'dos','feedback'),
(16,'dos','log_tb'),
(8,'dos','login'),
(11,'dos','report_table'),
(15,'dos','request_table'),
(10,'dos','transaction'),
(9,'dos','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-12-03 05:18:04.430692'),
(2,'auth','0001_initial','2023-12-03 05:18:08.216875'),
(3,'admin','0001_initial','2023-12-03 05:18:09.763250'),
(4,'admin','0002_logentry_remove_auto_add','2023-12-03 05:18:09.794490'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-12-03 05:18:09.810111'),
(6,'contenttypes','0002_remove_content_type_name','2023-12-03 05:18:10.741086'),
(7,'auth','0002_alter_permission_name_max_length','2023-12-03 05:18:11.018165'),
(8,'auth','0003_alter_user_email_max_length','2023-12-03 05:18:11.268085'),
(9,'auth','0004_alter_user_username_opts','2023-12-03 05:18:11.283705'),
(10,'auth','0005_alter_user_last_login_null','2023-12-03 05:18:12.220906'),
(11,'auth','0006_require_contenttypes_0002','2023-12-03 05:18:12.299005'),
(12,'auth','0007_alter_validators_add_error_messages','2023-12-03 05:18:12.423965'),
(13,'auth','0008_alter_user_username_max_length','2023-12-03 05:18:12.580169'),
(14,'auth','0009_alter_user_last_name_max_length','2023-12-03 05:18:13.392405'),
(15,'auth','0010_alter_group_name_max_length','2023-12-03 05:18:13.454884'),
(16,'auth','0011_update_proxy_permissions','2023-12-03 05:18:13.501747'),
(17,'auth','0012_alter_user_first_name_max_length','2023-12-03 05:18:13.642324'),
(18,'dos','0001_initial','2023-12-03 05:18:15.482981'),
(19,'sessions','0001_initial','2023-12-03 05:18:15.842237'),
(20,'dos','0002_auto_20231212_0056','2023-12-12 05:57:00.335932'),
(21,'dos','0003_branch_login','2023-12-12 06:12:45.599472'),
(22,'dos','0004_auto_20231212_0510','2023-12-12 10:10:59.484226'),
(23,'dos','0005_rename_request_request_table','2023-12-20 04:25:41.809704'),
(24,'dos','0006_auto_20240208_0239','2024-02-08 07:39:40.073181'),
(25,'dos','0007_log_tb','2024-03-19 05:34:43.976421');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('acadnw9hrib89ggqof35bwlzz5bbqxdk','.eJxVjDsOwyAQBe9CHSEWw5pNmT5nQMsnwYmFJWNXUe6eILlxOzPvfcQ8JXG1F-F534rfW159JwLEiQWO71y7SC-uz0XGpW7rFGRP5GGbvC8pz7ejPR0UbuW_JkKtHaFSDHrEFEkbxjxEHSCnAcBFZchYZTQwOwrorEGTeYAR6QHi-wMaIjhp:1rJVga:xP1gMw6ofe7ZTA87wbdT1XbEkAfX-eojQCTN5gVXuSI','2024-01-13 09:31:16.992034'),
('rgyzlynqw4zj2bbvovzevdzk43iuog1u','.eJxVjDsOwyAQBe9CHSEWw5pNmT5nQMsnwYmFJWNXUe6eILlxOzPvfcQ8JXG1F-F534rfW159JwLEiQWO71y7SC-uz0XGpW7rFGRP5GGbvC8pz7ejPR0UbuW_JkKtHaFSDHrEFEkbxjxEHSCnAcBFZchYZTQwOwrorEGTeYAR6QHi-wMaIjhp:1rXxXg:gGQpTgn9iv-EbFeuoczayMkIVeZ-fOZKVR_19cRB-tY','2024-02-22 06:05:48.617298'),
('wgxhe4wz4xvxr8wafxaln29k6up0hwh3','.eJxVjDsOwyAQBe9CHSEg_Jwyfc6AlmUJTiyQjF1FuXuC5MbtzLz3Ycuc2E1eWIB9K2HvtIZBmGQnFgHfVIdIL6jPxrHVbZ0jHwk_bOePlmi5H-3poEAv_7WRTohpQhGT0kqDISO0s5IEeae8jdaRNQY9ZDJWowXtMQNqd5WZnGffHyj2OWY:1rmS5r:g8N9lxTM_ejEOfY7xx_fBkggkiS2bcGANH6w8BSb1q8','2024-04-02 05:32:59.715752');

/*Table structure for table `dos_account_details` */

DROP TABLE IF EXISTS `dos_account_details`;

CREATE TABLE `dos_account_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `Account_No` int NOT NULL,
  `USER_id` bigint NOT NULL,
  `BRANCH_id` bigint NOT NULL,
  `Balance` double NOT NULL,
  `pin_num` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_account_details_USER_id_50cbba85_fk_dos_user_id` (`USER_id`),
  KEY `dos_account_details_BRANCH_id_687ecabb_fk_dos_branch_id` (`BRANCH_id`),
  CONSTRAINT `dos_account_details_BRANCH_id_687ecabb_fk_dos_branch_id` FOREIGN KEY (`BRANCH_id`) REFERENCES `dos_branch` (`id`),
  CONSTRAINT `dos_account_details_USER_id_50cbba85_fk_dos_user_id` FOREIGN KEY (`USER_id`) REFERENCES `dos_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_account_details` */

insert  into `dos_account_details`(`id`,`Account_No`,`USER_id`,`BRANCH_id`,`Balance`,`pin_num`) values 
(4,1234,1,3,200,123456),
(5,0,2,7,666,456),
(6,34650,11,4,100,9090),
(7,34567,11,7,0,8654),
(8,2345,12,7,200,243),
(9,234567896,1,7,0,435621);

/*Table structure for table `dos_branch` */

DROP TABLE IF EXISTS `dos_branch`;

CREATE TABLE `dos_branch` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `IFSC` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_branch_LOGIN_id_ba5bbead_fk_dos_login_id` (`LOGIN_id`),
  CONSTRAINT `dos_branch_LOGIN_id_ba5bbead_fk_dos_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `dos_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_branch` */

insert  into `dos_branch`(`id`,`name`,`place`,`IFSC`,`post`,`pin`,`phone`,`email`,`LOGIN_id`) values 
(3,'WANDOOR','WDR','PNB9008754','wandoor',123456,9876543214,'wdr@gmail.com',4),
(4,'CALICUT','CLCT','PNB7000890','calicut',678543,9876543214,'clt@gmail.com',18),
(7,'MALAPPURAM','MLP','PNB4008714','chathangottupuram',679328,1254324567,'mlpr@gmail.com',22);

/*Table structure for table `dos_complaint` */

DROP TABLE IF EXISTS `dos_complaint`;

CREATE TABLE `dos_complaint` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_complaint_USER_id_0866d660_fk_dos_user_id` (`USER_id`),
  CONSTRAINT `dos_complaint_USER_id_0866d660_fk_dos_user_id` FOREIGN KEY (`USER_id`) REFERENCES `dos_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_complaint` */

insert  into `dos_complaint`(`id`,`complaint`,`date`,`reply`,`USER_id`) values 
(1,'bad','2023-12-03','ok',1),
(2,'Too bad','2023-12-12','ok',1),
(3,'average','2023-12-13','yes',2),
(4,'sdfghb','2023-12-14','Nil',2),
(5,'rtfgh','2023-12-20','Nil',2),
(6,'ty','2023-12-30','Nil',2),
(7,'','2024-02-21','Nil',2),
(8,'','2024-02-21','Nil',2),
(9,'uh','2024-02-21','Nil',11);

/*Table structure for table `dos_feedback` */

DROP TABLE IF EXISTS `dos_feedback`;

CREATE TABLE `dos_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_feedback_USER_id_6d199927_fk_dos_user_id` (`USER_id`),
  CONSTRAINT `dos_feedback_USER_id_6d199927_fk_dos_user_id` FOREIGN KEY (`USER_id`) REFERENCES `dos_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_feedback` */

insert  into `dos_feedback`(`id`,`date`,`feedback`,`USER_id`) values 
(1,'2023-12-11','fdfgjhjk',1),
(2,'2023-12-08','sdfghj',2),
(3,'2023-12-20','sdfghjn',2),
(4,'2023-12-28','bank',2),
(5,'2023-12-28','zxcvbn',2),
(6,'2023-12-30','dfg',2),
(7,'2024-02-21','dfghj',2),
(8,'2024-02-21','sfghj',2),
(9,'2024-02-21','sdfg',11),
(10,'2024-02-27','accept meeeeeeeeee',12);

/*Table structure for table `dos_log_tb` */

DROP TABLE IF EXISTS `dos_log_tb`;

CREATE TABLE `dos_log_tb` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) NOT NULL,
  `date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_log_tb` */

/*Table structure for table `dos_login` */

DROP TABLE IF EXISTS `dos_login`;

CREATE TABLE `dos_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_login` */

insert  into `dos_login`(`id`,`username`,`password`,`type`) values 
(1,'bank','bank','bank'),
(4,'branch3','123','branch'),
(5,'user1','123','user'),
(10,'user2','123','user'),
(11,'lulu','123','user'),
(12,'lulu','123','user'),
(13,'lulu','123','user'),
(14,'lulu','123','user'),
(15,'user','123','user'),
(16,'user123','123','user'),
(17,'user123','123','user'),
(18,'bbb','b','branch'),
(22,'brnmlp','123','branch'),
(23,'shareefat','12345','user'),
(24,'sitharatk','sithara22','user');

/*Table structure for table `dos_report_table` */

DROP TABLE IF EXISTS `dos_report_table`;

CREATE TABLE `dos_report_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `report` longtext NOT NULL,
  `date` date NOT NULL,
  `BRANCH_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_report_table_BRANCH_id_0d43db36_fk_dos_branch_id` (`BRANCH_id`),
  CONSTRAINT `dos_report_table_BRANCH_id_0d43db36_fk_dos_branch_id` FOREIGN KEY (`BRANCH_id`) REFERENCES `dos_branch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_report_table` */

insert  into `dos_report_table`(`id`,`report`,`date`,`BRANCH_id`) values 
(9,'IMG_3726.JPG','2024-02-01',7),
(10,'IMG_3726.JPG','2024-02-01',7);

/*Table structure for table `dos_request_table` */

DROP TABLE IF EXISTS `dos_request_table`;

CREATE TABLE `dos_request_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `BRANCH_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_request_BRANCH_id_d4cac0ef_fk_dos_branch_id` (`BRANCH_id`),
  KEY `dos_request_USER_id_3e46f4ef_fk_dos_user_id` (`USER_id`),
  CONSTRAINT `dos_request_BRANCH_id_d4cac0ef_fk_dos_branch_id` FOREIGN KEY (`BRANCH_id`) REFERENCES `dos_branch` (`id`),
  CONSTRAINT `dos_request_USER_id_3e46f4ef_fk_dos_user_id` FOREIGN KEY (`USER_id`) REFERENCES `dos_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_request_table` */

insert  into `dos_request_table`(`id`,`status`,`date`,`BRANCH_id`,`USER_id`) values 
(3,'pending','2023-12-20',3,2),
(11,'Accepted','2024-02-21',3,11),
(12,'Rejected','2024-02-21',7,11),
(13,'Accepted','2024-02-21',7,11),
(14,'Accepted','2024-02-27',7,1),
(15,'Accepted','2024-02-27',7,12);

/*Table structure for table `dos_transaction` */

DROP TABLE IF EXISTS `dos_transaction`;

CREATE TABLE `dos_transaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `Amount` double NOT NULL,
  `ACC_NO_id` bigint NOT NULL,
  `Transaction_type` varchar(100) NOT NULL,
  `Type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_transaction_ACC_NO_id_aa6b9e73_fk_dos_account_details_id` (`ACC_NO_id`),
  CONSTRAINT `dos_transaction_ACC_NO_id_aa6b9e73_fk_dos_account_details_id` FOREIGN KEY (`ACC_NO_id`) REFERENCES `dos_account_details` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_transaction` */

insert  into `dos_transaction`(`id`,`date`,`Amount`,`ACC_NO_id`,`Transaction_type`,`Type`) values 
(9,'2024-02-21',23456,4,'online','credit'),
(10,'2024-02-21',54332,4,'online','credit'),
(11,'2024-02-21',10000,7,'online','credit'),
(12,'2024-02-21',500,4,'offline','debit'),
(13,'2024-02-21',500,7,'online','debit');

/*Table structure for table `dos_user` */

DROP TABLE IF EXISTS `dos_user`;

CREATE TABLE `dos_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `signature` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dos_user_LOGIN_id_381abe9c_fk_dos_login_id` (`LOGIN_id`),
  CONSTRAINT `dos_user_LOGIN_id_381abe9c_fk_dos_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `dos_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `dos_user` */

insert  into `dos_user`(`id`,`first_name`,`last_name`,`signature`,`place`,`phone`,`gender`,`dob`,`idproof`,`LOGIN_id`,`email`) values 
(1,'demo','demo','demo','demo',877,'demo','2023-12-01','demo',1,'1'),
(2,'abc','abc','abc','abc',89,'abc','2023-12-19','abc',5,'1'),
(10,'lulu','bayan','IMG_3727_HKiO2iT.JPG','ddfgh',7636765487,'female','2024-02-06','IMG_3721_flhrq0l.JPG',17,'lulubayanishak@gmail.com'),
(11,'mohammed','shareef','IMG_3721_Te610bl.JPG','pandikkad',7559062166,'male','2002-05-17','IMG_3727_8Lejsh3.JPG',23,'shareef@gmail.com'),
(12,'fathima','sithara','IMG_3727_dbEB4Sp.JPG','areekode',8590702430,'female','2001-04-14','IMG_3767.HEIC',24,'fathimasitharatk2002@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
