-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: FairyBBS
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_profile`
--

DROP TABLE IF EXISTS `account_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `nickname` varchar(12) DEFAULT NULL,
  `use_gravatar` tinyint(1) NOT NULL,
  `location` varchar(20) DEFAULT NULL,
  `avatar_url` varchar(200) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_f8908e88` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_profile`
--

LOCK TABLES `account_profile` WRITE;
/*!40000 ALTER TABLE `account_profile` DISABLE KEYS */;
INSERT INTO `account_profile` VALUES (1,1,NULL,1,NULL,'/static/upload/1.png',NULL),(2,2,NULL,1,NULL,'/static/upload/default.png',NULL),(3,3,NULL,1,NULL,'/static/upload/3.png',NULL),(4,4,NULL,1,NULL,'/static/upload/4.png',NULL),(5,5,NULL,1,NULL,'/static/upload/default.png',NULL),(6,6,NULL,1,NULL,'/static/upload/default.png',NULL);
/*!40000 ALTER TABLE `account_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_social`
--

DROP TABLE IF EXISTS `account_social`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_social` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `access_token` varchar(255) NOT NULL,
  `openid` varchar(255) NOT NULL,
  `avatar` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_f120b943` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_social`
--

LOCK TABLES `account_social` WRITE;
/*!40000 ALTER TABLE `account_social` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_social` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add profile',1,'add_profile'),(2,'Can change profile',1,'change_profile'),(3,'Can delete profile',1,'delete_profile'),(4,'Can add social',2,'add_social'),(5,'Can change social',2,'change_social'),(6,'Can delete social',2,'delete_social'),(7,'Can add topic',3,'add_topic'),(8,'Can change topic',3,'change_topic'),(9,'Can delete topic',3,'delete_topic'),(10,'Can add node',4,'add_node'),(11,'Can change node',4,'change_node'),(12,'Can delete node',4,'delete_node'),(13,'Can add post',5,'add_post'),(14,'Can change post',5,'change_post'),(15,'Can delete post',5,'delete_post'),(16,'Can add notification',6,'add_notification'),(17,'Can change notification',6,'change_notification'),(18,'Can delete notification',6,'delete_notification'),(19,'Can add mention',7,'add_mention'),(20,'Can change mention',7,'change_mention'),(21,'Can delete mention',7,'delete_mention'),(22,'Can add appendix',8,'add_appendix'),(23,'Can change appendix',8,'change_appendix'),(24,'Can delete appendix',8,'delete_appendix'),(25,'Can add log entry',9,'add_logentry'),(26,'Can change log entry',9,'change_logentry'),(27,'Can delete log entry',9,'delete_logentry'),(28,'Can add permission',10,'add_permission'),(29,'Can change permission',10,'change_permission'),(30,'Can delete permission',10,'delete_permission'),(31,'Can add group',11,'add_group'),(32,'Can change group',11,'change_group'),(33,'Can delete group',11,'delete_group'),(34,'Can add user',12,'add_user'),(35,'Can change user',12,'change_user'),(36,'Can delete user',12,'delete_user'),(37,'Can add content type',13,'add_contenttype'),(38,'Can change content type',13,'change_contenttype'),(39,'Can delete content type',13,'delete_contenttype'),(40,'Can add session',14,'add_session'),(41,'Can change session',14,'change_session'),(42,'Can delete session',14,'delete_session'),(43,'Can add theme',15,'add_theme'),(44,'Can change theme',15,'change_theme'),(45,'Can delete theme',15,'delete_theme'),(46,'Can add topic_collect',16,'add_topic_collect'),(47,'Can change topic_collect',16,'change_topic_collect'),(48,'Can delete topic_collect',16,'delete_topic_collect');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$vQXK72VGFiU2$lV1PH2uyDDSHYFzLQThn4UJWwaUJY3MEODX1ED915r8=','2014-12-24 05:58:53',1,'py','','','100503711@qq.com',1,1,'2014-11-20 02:51:28'),(2,'pbkdf2_sha256$12000$LeQzbLvKb86J$kaYGK1cJTvsiLgKgBI0RU+q2SDcNwVpvjS81zNhjK5E=','2014-12-10 04:07:07',0,'test1','','','100503711@qq.com',0,1,'2014-12-08 07:48:08'),(3,'pbkdf2_sha256$12000$3bCGsTffgWWY$s5Amx668DaAN3/RGIq49SIv9MFEjJa7NAUGTW9f32h4=','2014-12-23 08:31:51',0,'sen1','','','100503711@qq.com',0,1,'2014-12-10 03:52:11'),(4,'pbkdf2_sha256$12000$ZoVF65Yqptdr$dl8nsoQeKjtUzt6J685xmX7O0ooOxIhI6kq1Bqj+cgc=','2014-12-10 03:56:16',0,'sen2','','','100503711@qq.com',0,1,'2014-12-10 03:56:15'),(5,'pbkdf2_sha256$12000$WOwqgkRBpywT$H9ug/tGfIR+IATKaE3vQZugwO8LDAeh0Y+f/MMdMUXo=','2014-12-10 04:01:42',0,'sen3','','','100503711@qq.com',0,1,'2014-12-10 04:01:42'),(6,'pbkdf2_sha256$12000$oruqkNErYzjb$6CMquqAXYXLji0V21ZQCER54zWiF7VYiGCZdhyXgmek=','2014-12-10 05:42:06',0,'pony1','','','100503711@qq.com',0,1,'2014-12-10 05:42:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-12-01 05:28:25',1,4,'1','投资交流',1,''),(2,'2014-12-01 05:47:47',1,15,'1','网贷交流',1,''),(3,'2014-12-01 06:20:14',1,4,'1','投资交流',3,''),(4,'2014-12-01 06:21:55',1,4,'2','投资交流',1,''),(5,'2014-12-01 07:59:44',1,15,'2','网贷平台',1,''),(6,'2014-12-01 08:00:13',1,4,'3','重大事件',1,''),(7,'2014-12-01 08:44:29',1,4,'4','平台投诉',1,''),(8,'2014-12-03 03:07:49',1,3,'3','test2',2,'已修改 hot_flag 。'),(9,'2014-12-03 06:06:57',1,3,'4','test3',2,'已修改 hot_flag 。'),(10,'2014-12-19 06:22:16',1,15,'3','网贷新手',1,''),(11,'2014-12-19 06:22:24',1,15,'4','投诉建议',1,''),(12,'2014-12-19 06:23:28',1,4,'5','经验之路',1,''),(13,'2014-12-19 06:23:41',1,4,'6','专家解惑',1,''),(14,'2014-12-19 06:24:30',1,4,'7','平台考察',1,''),(15,'2014-12-19 06:24:43',1,4,'8','平台公告',1,''),(16,'2014-12-19 06:24:54',1,4,'9','平台数据',1,''),(17,'2014-12-19 06:25:16',1,4,'10','网贷百科',1,''),(18,'2014-12-19 06:25:34',1,4,'11','行业信息',1,''),(19,'2014-12-19 06:25:47',1,4,'12','新手交流',1,''),(20,'2014-12-19 06:25:58',1,4,'13','新手提问',1,''),(21,'2014-12-19 06:26:23',1,4,'14','网站投诉',1,''),(22,'2014-12-19 06:26:33',1,4,'15','社区投诉',1,''),(23,'2014-12-19 06:26:44',1,4,'16','奇思妙想',1,''),(24,'2014-12-24 05:59:36',1,3,'25','啦啦啦啦啦创新创效',2,'Changed essence_flag.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'profile','account','profile'),(2,'social','account','social'),(3,'topic','forum','topic'),(4,'node','forum','node'),(5,'post','forum','post'),(6,'notification','forum','notification'),(7,'mention','forum','mention'),(8,'appendix','forum','appendix'),(9,'log entry','admin','logentry'),(10,'permission','auth','permission'),(11,'group','auth','group'),(12,'user','auth','user'),(13,'content type','contenttypes','contenttype'),(14,'session','sessions','session'),(15,'theme','forum','theme'),(16,'topic_collect','forum','topic_collect');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('51ifptt1jl3ychypznh7vkcz0tn3h0vh','YzEzYzk2MGI5YmE2MTIxYzZmZmY0OTc4ODBmMWM2ODVlMDI1MDRjMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-12-04 08:44:45'),('7ll4d4gukh7foqoleucke9d7vok0w5vs','YzEzYzk2MGI5YmE2MTIxYzZmZmY0OTc4ODBmMWM2ODVlMDI1MDRjMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-01-07 05:58:53');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_appendix`
--

DROP TABLE IF EXISTS `forum_appendix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_appendix` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `time_created` datetime NOT NULL,
  `content` longtext NOT NULL,
  `content_rendered` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_appendix_76f18ad3` (`topic_id`),
  CONSTRAINT `topic_id_refs_id_aadd7be5` FOREIGN KEY (`topic_id`) REFERENCES `forum_topic` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_appendix`
--

LOCK TABLES `forum_appendix` WRITE;
/*!40000 ALTER TABLE `forum_appendix` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_appendix` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_mention`
--

DROP TABLE IF EXISTS `forum_mention`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_mention` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `post_id` int(11) DEFAULT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `content` longtext,
  `read` tinyint(1) NOT NULL,
  `time_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_mention_0a681a64` (`sender_id`),
  KEY `forum_mention_066c7a30` (`receiver_id`),
  KEY `forum_mention_87a49a9a` (`post_id`),
  KEY `forum_mention_76f18ad3` (`topic_id`),
  CONSTRAINT `post_id_refs_id_d25b1c63` FOREIGN KEY (`post_id`) REFERENCES `forum_post` (`id`),
  CONSTRAINT `receiver_id_refs_id_4fbd6dad` FOREIGN KEY (`receiver_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `sender_id_refs_id_4fbd6dad` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `topic_id_refs_id_59233832` FOREIGN KEY (`topic_id`) REFERENCES `forum_topic` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_mention`
--

LOCK TABLES `forum_mention` WRITE;
/*!40000 ALTER TABLE `forum_mention` DISABLE KEYS */;
INSERT INTO `forum_mention` VALUES (1,1,1,7,4,NULL,1,'2014-12-25 07:52:48'),(2,1,1,9,4,NULL,1,'2014-12-25 07:57:53');
/*!40000 ALTER TABLE `forum_mention` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_node`
--

DROP TABLE IF EXISTS `forum_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_node` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(12) NOT NULL,
  `description` longtext NOT NULL,
  `theme_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_node`
--

LOCK TABLES `forum_node` WRITE;
/*!40000 ALTER TABLE `forum_node` DISABLE KEYS */;
INSERT INTO `forum_node` VALUES (2,'投资交流','',1),(3,'重大事件','',1),(4,'平台投诉','',2),(5,'经验之路','',1),(6,'专家解惑','',1),(7,'平台考察','',2),(8,'平台公告','',2),(9,'平台数据','',2),(10,'网贷百科','',3),(11,'行业信息','',3),(12,'新手交流','',3),(13,'新手提问','',3),(14,'网站投诉','',4),(15,'社区投诉','',4),(16,'奇思妙想','',4);
/*!40000 ALTER TABLE `forum_node` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_notification`
--

DROP TABLE IF EXISTS `forum_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `topic_id` int(11) DEFAULT NULL,
  `content` longtext,
  `read` tinyint(1) NOT NULL,
  `time_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_notification_0a681a64` (`sender_id`),
  KEY `forum_notification_066c7a30` (`receiver_id`),
  KEY `forum_notification_76f18ad3` (`topic_id`),
  CONSTRAINT `receiver_id_refs_id_9bfcbcd9` FOREIGN KEY (`receiver_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `sender_id_refs_id_9bfcbcd9` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `topic_id_refs_id_702d1de8` FOREIGN KEY (`topic_id`) REFERENCES `forum_topic` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_notification`
--

LOCK TABLES `forum_notification` WRITE;
/*!40000 ALTER TABLE `forum_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `forum_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_post`
--

DROP TABLE IF EXISTS `forum_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `content_rendered` longtext NOT NULL,
  `time_created` datetime NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_post_6340c63c` (`user_id`),
  KEY `forum_post_76f18ad3` (`topic_id`),
  CONSTRAINT `topic_id_refs_id_edcc9b96` FOREIGN KEY (`topic_id`) REFERENCES `forum_topic` (`id`),
  CONSTRAINT `user_id_refs_id_1aca526e` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_post`
--

LOCK TABLES `forum_post` WRITE;
/*!40000 ALTER TABLE `forum_post` DISABLE KEYS */;
INSERT INTO `forum_post` VALUES (1,2,4,'e ','<p>e </p>','2014-12-08 07:48:23',0),(2,6,4,'1234','<p>1234</p>','2014-12-10 05:48:02',0),(3,3,4,'shi a ','<p>shi a </p>','2014-12-11 07:15:19',0),(4,1,4,'sadads','<p>sadads</p>','2014-12-25 06:51:18',0),(5,1,4,'dsadsadasscccc','<p>dsadsadasscccc</p>','2014-12-25 06:51:25',0),(6,1,25,'回覆','<p>回覆</p>','2014-12-25 07:36:30',0),(7,1,4,'@py 的撒是老大是','<p>@<a href=\"/user/1/info/\" class=\"mention\">py</a> 的撒是老大是</p>','2014-12-25 07:52:48',0),(8,1,4,'http://127.0.0.1:8000/static/upload/3.png','<p>http://127.0.0.1:8000/static/upload/3.png</p>','2014-12-25 07:53:36',0),(9,1,4,'@py 的撒旦撒旦','<p>@<a href=\"/user/1/info/\" class=\"mention\">py</a> 的撒旦撒旦</p>','2014-12-25 07:57:53',0);
/*!40000 ALTER TABLE `forum_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_theme`
--

DROP TABLE IF EXISTS `forum_theme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_theme` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(12) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_theme`
--

LOCK TABLES `forum_theme` WRITE;
/*!40000 ALTER TABLE `forum_theme` DISABLE KEYS */;
INSERT INTO `forum_theme` VALUES (1,'网贷交流',''),(2,'网贷平台',''),(3,'网贷新手',''),(4,'投诉建议','');
/*!40000 ALTER TABLE `forum_theme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_topic`
--

DROP TABLE IF EXISTS `forum_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_topic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `title` varchar(160) NOT NULL,
  `content` longtext,
  `content_rendered` longtext,
  `click` int(11) NOT NULL,
  `reply_count` int(11) NOT NULL,
  `node_id` int(11) NOT NULL,
  `time_created` datetime NOT NULL,
  `last_replied` datetime DEFAULT NULL,
  `deleted` tinyint(1) NOT NULL,
  `order` int(11) NOT NULL,
  `hot_flag` tinyint(1) DEFAULT NULL,
  `essence_flag` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_topic_6340c63c` (`user_id`),
  KEY `forum_topic_e453c5c5` (`node_id`),
  CONSTRAINT `node_id_refs_id_5d0660c1` FOREIGN KEY (`node_id`) REFERENCES `forum_node` (`id`),
  CONSTRAINT `user_id_refs_id_2aefb255` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_topic`
--

LOCK TABLES `forum_topic` WRITE;
/*!40000 ALTER TABLE `forum_topic` DISABLE KEYS */;
INSERT INTO `forum_topic` VALUES (2,1,'自从学会了理财，工资都用来零花 新人帖','111','<p>111</p>',18,0,2,'2014-12-01 08:03:25','2014-12-01 08:03:25',0,10,1,1),(3,1,'自从学会了理财，工资都用来零花 新人帖','2222','<p>2222</p>',96,0,3,'2014-12-01 08:03:40','2014-12-01 08:03:40',0,10,1,1),(4,1,'自从学会了理财，工资都用来零花 新人帖','333','<p>333</p>',153,8,2,'2014-12-03 06:06:44','2014-12-25 07:57:53',0,10,1,1),(5,1,'自从学会了理财，工资都用来零花 新人帖','1123','<p>1123</p>',10,0,2,'2014-12-11 09:43:26','2014-12-11 09:43:26',0,10,1,1),(6,1,'自从学会了理财，工资都用来零花 新人帖','aa','<p>aa</p>',2,0,2,'2014-12-11 09:44:16','2014-12-11 09:44:16',0,10,1,1),(7,1,'自从学会了理财，工资都用来零花 新人帖','dasds','<p>dasds</p>',71,0,2,'2014-12-11 09:45:14','2014-12-11 09:45:14',0,10,1,1),(8,3,'测试测试测试仅供测试','sdsadasd','<p>sdsadasd</p>',1,0,3,'2014-12-18 03:21:28','2014-12-18 03:21:28',0,10,1,1),(9,3,'测试测试测试仅供测试','的撒的撒的撒','<p>的撒的撒的撒</p>',2,0,2,'2014-12-18 06:01:21','2014-12-18 06:01:21',0,10,1,1),(10,3,'大的撒的撒的撒','三大的撒的撒','<p>三大的撒的撒</p>',1,0,2,'2014-12-18 06:13:21','2014-12-18 06:13:21',0,10,1,1),(11,3,'的撒的撒的撒','大声地撒大大速度','<p>大声地撒大大速度</p>',1,0,2,'2014-12-18 06:13:48','2014-12-18 06:13:48',0,10,1,1),(12,3,'韩国和法规符合法国和','恢复共和国符合','<p>恢复共和国符合</p>',2,0,2,'2014-12-18 06:13:59','2014-12-18 06:13:59',0,10,1,1),(13,3,'规定法规梵蒂冈','vbcvbcb','<p>vbcvbcb</p>',2,0,2,'2014-12-18 06:14:09','2014-12-18 06:14:09',0,10,1,1),(14,3,'啦啦啦啦啦','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:18','2014-12-18 06:23:18',0,10,1,1),(15,3,'啦啦啦啦啦','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:24','2014-12-18 06:23:24',0,10,1,1),(16,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:40','2014-12-18 06:23:40',0,10,1,1),(17,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:44','2014-12-18 06:23:44',0,10,1,1),(18,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:47','2014-12-18 06:23:47',0,10,1,1),(19,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:49','2014-12-18 06:23:49',0,10,1,1),(20,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:52','2014-12-18 06:23:52',0,10,1,1),(21,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:55','2014-12-18 06:23:55',0,10,1,1),(22,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:23:58','2014-12-18 06:23:58',0,10,1,1),(23,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',1,0,2,'2014-12-18 06:24:00','2014-12-18 06:24:00',0,10,1,1),(24,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',2,0,2,'2014-12-18 06:24:03','2014-12-18 06:24:03',0,10,1,1),(25,3,'啦啦啦啦啦创新创效','嘻嘻嘻嘻嘻嘻','<p>嘻嘻嘻嘻嘻嘻</p>',40,1,2,'2014-12-18 06:24:05','2014-12-25 07:36:30',0,10,1,1),(26,1,'sdas','dasdasd','<p>dasdasd</p>',4,0,3,'2014-12-24 08:22:46','2014-12-24 08:22:46',0,10,0,0),(27,1,'啦啦啦啦啦创新创效','dasdas','<p>dasdas</p>',49,0,4,'2014-12-24 08:23:22','2014-12-24 08:23:22',0,10,0,0),(28,1,'的撒大大廈達','','',1,0,2,'2014-12-25 07:46:49','2014-12-25 07:46:49',0,10,0,0),(29,1,'v剎v剎v','佛擋殺佛','<p>佛擋殺佛</p>',4,0,6,'2014-12-25 07:47:38','2014-12-25 07:47:38',0,10,0,0),(30,1,'大','打算撒都是','<p>打算撒都是</p>',1,0,16,'2014-12-25 08:32:58','2014-12-25 08:32:58',0,10,0,0);
/*!40000 ALTER TABLE `forum_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_topic_collect`
--

DROP TABLE IF EXISTS `forum_topic_collect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forum_topic_collect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_topic_collect_6340c63c` (`user_id`),
  KEY `forum_topic_collect_76f18ad3` (`topic_id`),
  CONSTRAINT `topic_id_refs_id_9375a539` FOREIGN KEY (`topic_id`) REFERENCES `forum_topic` (`id`),
  CONSTRAINT `user_id_refs_id_7414006f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_topic_collect`
--

LOCK TABLES `forum_topic_collect` WRITE;
/*!40000 ALTER TABLE `forum_topic_collect` DISABLE KEYS */;
INSERT INTO `forum_topic_collect` VALUES (18,3,4,1);
/*!40000 ALTER TABLE `forum_topic_collect` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-12-26 16:46:14
