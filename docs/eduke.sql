-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Mar 30, 2025 at 11:25 AM
-- Server version: 9.1.0
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eduke`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add content type', 1, 'add_contenttype'),
(2, 'Can change content type', 1, 'change_contenttype'),
(3, 'Can delete content type', 1, 'delete_contenttype'),
(4, 'Can view content type', 1, 'view_contenttype'),
(5, 'Can add permission', 12, 'add_permission'),
(6, 'Can change permission', 12, 'change_permission'),
(7, 'Can delete permission', 12, 'delete_permission'),
(8, 'Can view permission', 12, 'view_permission'),
(9, 'Can add group', 13, 'add_group'),
(10, 'Can change group', 13, 'change_group'),
(11, 'Can delete group', 13, 'delete_group'),
(12, 'Can view group', 13, 'view_group'),
(13, 'Can add user', 14, 'add_user'),
(14, 'Can change user', 14, 'change_user'),
(15, 'Can delete user', 14, 'delete_user'),
(16, 'Can view user', 14, 'view_user'),
(17, 'Can add class', 2, 'add_class'),
(18, 'Can change class', 2, 'change_class'),
(19, 'Can delete class', 2, 'delete_class'),
(20, 'Can view class', 2, 'view_class'),
(21, 'Can add subject', 3, 'add_subject'),
(22, 'Can change subject', 3, 'change_subject'),
(23, 'Can delete subject', 3, 'delete_subject'),
(24, 'Can view subject', 3, 'view_subject'),
(25, 'Can add user', 4, 'add_user'),
(26, 'Can change user', 4, 'change_user'),
(27, 'Can delete user', 4, 'delete_user'),
(28, 'Can view user', 4, 'view_user'),
(29, 'Can add student', 5, 'add_student'),
(30, 'Can change student', 5, 'change_student'),
(31, 'Can delete student', 5, 'delete_student'),
(32, 'Can view student', 5, 'view_student'),
(33, 'Can add student evaluation', 6, 'add_studentevaluation'),
(34, 'Can change student evaluation', 6, 'change_studentevaluation'),
(35, 'Can delete student evaluation', 6, 'delete_studentevaluation'),
(36, 'Can view student evaluation', 6, 'view_studentevaluation'),
(37, 'Can add marks', 7, 'add_marks'),
(38, 'Can change marks', 7, 'change_marks'),
(39, 'Can delete marks', 7, 'delete_marks'),
(40, 'Can view marks', 7, 'view_marks'),
(41, 'Can add attendance', 8, 'add_attendance'),
(42, 'Can change attendance', 8, 'change_attendance'),
(43, 'Can delete attendance', 8, 'delete_attendance'),
(44, 'Can view attendance', 8, 'view_attendance'),
(45, 'Can add teacher', 9, 'add_teacher'),
(46, 'Can change teacher', 9, 'change_teacher'),
(47, 'Can delete teacher', 9, 'delete_teacher'),
(48, 'Can view teacher', 9, 'view_teacher'),
(49, 'Can add parent', 10, 'add_parent'),
(50, 'Can change parent', 10, 'change_parent'),
(51, 'Can delete parent', 10, 'delete_parent'),
(52, 'Can view parent', 10, 'view_parent'),
(53, 'Can add chat', 11, 'add_chat'),
(54, 'Can change chat', 11, 'change_chat'),
(55, 'Can delete chat', 11, 'delete_chat'),
(56, 'Can view chat', 11, 'view_chat'),
(57, 'Can add admin', 15, 'add_admin'),
(58, 'Can change admin', 15, 'change_admin'),
(59, 'Can delete admin', 15, 'delete_admin'),
(60, 'Can view admin', 15, 'view_admin'),
(61, 'Can add custom user', 16, 'add_customuser'),
(62, 'Can change custom user', 16, 'change_customuser'),
(63, 'Can delete custom user', 16, 'delete_customuser'),
(64, 'Can view custom user', 16, 'view_customuser'),
(65, 'Can add institution', 15, 'add_institution'),
(66, 'Can change institution', 15, 'change_institution'),
(67, 'Can delete institution', 15, 'delete_institution'),
(68, 'Can view institution', 15, 'view_institution'),
(69, 'Can add users', 17, 'add_users'),
(70, 'Can change users', 17, 'change_users'),
(71, 'Can delete users', 17, 'delete_users'),
(72, 'Can view users', 17, 'view_users'),
(73, 'Can add classes', 18, 'add_classes'),
(74, 'Can change classes', 18, 'change_classes'),
(75, 'Can delete classes', 18, 'delete_classes'),
(76, 'Can view classes', 18, 'view_classes'),
(77, 'Can add quizzes', 19, 'add_quizzes'),
(78, 'Can change quizzes', 19, 'change_quizzes'),
(79, 'Can delete quizzes', 19, 'delete_quizzes'),
(80, 'Can view quizzes', 19, 'view_quizzes'),
(81, 'Can add students', 20, 'add_students'),
(82, 'Can change students', 20, 'change_students'),
(83, 'Can delete students', 20, 'delete_students'),
(84, 'Can view students', 20, 'view_students'),
(85, 'Can add student evaluations', 21, 'add_studentevaluations'),
(86, 'Can change student evaluations', 21, 'change_studentevaluations'),
(87, 'Can delete student evaluations', 21, 'delete_studentevaluations'),
(88, 'Can view student evaluations', 21, 'view_studentevaluations'),
(89, 'Can add questions responses', 22, 'add_questionsresponses'),
(90, 'Can change questions responses', 22, 'change_questionsresponses'),
(91, 'Can delete questions responses', 22, 'delete_questionsresponses'),
(92, 'Can view questions responses', 22, 'view_questionsresponses'),
(93, 'Can add subjects', 23, 'add_subjects'),
(94, 'Can change subjects', 23, 'change_subjects'),
(95, 'Can delete subjects', 23, 'delete_subjects'),
(96, 'Can view subjects', 23, 'view_subjects'),
(97, 'Can add teachers', 24, 'add_teachers'),
(98, 'Can change teachers', 24, 'change_teachers'),
(99, 'Can delete teachers', 24, 'delete_teachers'),
(100, 'Can view teachers', 24, 'view_teachers'),
(101, 'Can add parents', 25, 'add_parents'),
(102, 'Can change parents', 25, 'change_parents'),
(103, 'Can delete parents', 25, 'delete_parents'),
(104, 'Can view parents', 25, 'view_parents'),
(105, 'Can add session', 26, 'add_session'),
(106, 'Can change session', 26, 'change_session'),
(107, 'Can delete session', 26, 'delete_session'),
(108, 'Can view session', 26, 'view_session'),
(109, 'Can add study materials', 27, 'add_studymaterials'),
(110, 'Can change study materials', 27, 'change_studymaterials'),
(111, 'Can delete study materials', 27, 'delete_studymaterials'),
(112, 'Can view study materials', 27, 'view_studymaterials'),
(113, 'Can add announcements', 28, 'add_announcements'),
(114, 'Can change announcements', 28, 'change_announcements'),
(115, 'Can delete announcements', 28, 'delete_announcements'),
(116, 'Can view announcements', 28, 'view_announcements'),
(117, 'Can add quiz response', 29, 'add_quizresponse'),
(118, 'Can change quiz response', 29, 'change_quizresponse'),
(119, 'Can delete quiz response', 29, 'delete_quizresponse'),
(120, 'Can view quiz response', 29, 'view_quizresponse'),
(121, 'Can add quiz questions', 30, 'add_quizquestions'),
(122, 'Can change quiz questions', 30, 'change_quizquestions'),
(123, 'Can delete quiz questions', 30, 'delete_quizquestions'),
(124, 'Can view quiz questions', 30, 'view_quizquestions');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(13, 'auth', 'group'),
(12, 'auth', 'permission'),
(14, 'auth', 'user'),
(1, 'contenttypes', 'contenttype'),
(28, 'main', 'announcements'),
(8, 'main', 'attendance'),
(11, 'main', 'chat'),
(2, 'main', 'class'),
(18, 'main', 'classes'),
(16, 'main', 'customuser'),
(15, 'main', 'institution'),
(7, 'main', 'marks'),
(10, 'main', 'parent'),
(25, 'main', 'parents'),
(22, 'main', 'questionsresponses'),
(30, 'main', 'quizquestions'),
(29, 'main', 'quizresponse'),
(19, 'main', 'quizzes'),
(5, 'main', 'student'),
(6, 'main', 'studentevaluation'),
(21, 'main', 'studentevaluations'),
(20, 'main', 'students'),
(27, 'main', 'studymaterials'),
(3, 'main', 'subject'),
(23, 'main', 'subjects'),
(9, 'main', 'teacher'),
(24, 'main', 'teachers'),
(4, 'main', 'user'),
(17, 'main', 'users'),
(26, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'main', '0001_initial', '2025-01-20 03:15:34.450122'),
(2, 'contenttypes', '0001_initial', '2025-01-20 03:16:43.544109'),
(3, 'contenttypes', '0002_remove_content_type_name', '2025-01-20 03:16:43.629840'),
(4, 'auth', '0001_initial', '2025-01-20 03:17:35.366096'),
(5, 'auth', '0002_alter_permission_name_max_length', '2025-01-20 03:17:35.439530'),
(6, 'auth', '0003_alter_user_email_max_length', '2025-01-20 03:17:35.490838'),
(7, 'auth', '0004_alter_user_username_opts', '2025-01-20 03:17:35.511624'),
(8, 'auth', '0005_alter_user_last_login_null', '2025-01-20 03:17:35.572381'),
(9, 'auth', '0006_require_contenttypes_0002', '2025-01-20 03:17:35.576020'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2025-01-20 03:17:35.584385'),
(11, 'auth', '0008_alter_user_username_max_length', '2025-01-20 03:17:35.649604'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2025-01-20 03:17:35.720839'),
(13, 'auth', '0010_alter_group_name_max_length', '2025-01-20 03:17:35.748815'),
(14, 'auth', '0011_update_proxy_permissions', '2025-01-20 03:17:35.769376'),
(15, 'auth', '0012_alter_user_first_name_max_length', '2025-01-20 03:17:35.834542'),
(16, 'main', '0002_admin_customuser_alter_chat_receiver_and_more', '2025-01-20 05:35:14.414294'),
(17, 'main', '0003_rename_admin_institution_and_more', '2025-01-20 06:55:50.388105'),
(18, 'main', '0004_alter_attendance_options_alter_chat_options_and_more', '2025-01-20 10:09:05.700274'),
(19, 'main', '0005_users_remove_student_class_name_remove_parent_user_and_more', '2025-01-20 11:06:40.192020'),
(20, 'main', '0006_remove_institution_institution_id_and_more', '2025-01-20 11:11:08.460465'),
(21, 'sessions', '0001_initial', '2025-01-21 03:34:36.914637'),
(22, 'main', '0007_rename_student_attendance_student_id_and_more', '2025-01-22 03:10:03.619950'),
(23, 'main', '0008_chat_created_at', '2025-01-27 17:07:53.237571'),
(24, 'main', '0009_rename_student_id_attendance_student_and_more', '2025-02-01 05:53:48.700534'),
(25, 'main', '0010_announcements_studymaterials', '2025-02-08 04:27:31.931904'),
(26, 'main', '0011_studymaterials_announcement_and_more', '2025-02-08 04:32:12.142481'),
(27, 'main', '0012_alter_studymaterials_announcement', '2025-02-08 04:33:59.927843'),
(28, 'main', '0013_remove_announcements_subject', '2025-02-08 06:35:34.189131'),
(29, 'main', '0014_remove_quizzes_student_and_more', '2025-02-09 05:31:30.807981'),
(30, 'main', '0015_remove_quizresponse_quiz_and_more', '2025-02-09 06:32:06.586564'),
(31, 'main', '0016_alter_quizresponse_student_response', '2025-02-09 06:32:06.606555'),
(32, 'main', '0017_alter_quizquestions_quiz_and_more', '2025-02-09 06:32:06.611057'),
(33, 'main', '0018_remove_quizresponse_question_and_more', '2025-02-09 06:32:06.615599'),
(34, 'main', '0019_quizquestions_quizresponse_quizzes_and_more', '2025-02-09 06:32:06.621791'),
(35, 'main', '0020_studentevaluation_delete_studentevaluations', '2025-02-11 03:03:42.624433'),
(36, 'main', '0021_remove_quizresponse_question', '2025-02-11 03:43:41.189869'),
(37, 'main', '0022_quizresponse_question', '2025-02-11 03:43:51.454901'),
(38, 'main', '0023_delete_quizresponse', '2025-02-11 03:43:51.488624'),
(39, 'main', '0024_quizresponse', '2025-02-11 03:45:05.407688'),
(40, 'main', '0025_remove_quizresponse_question_and_more', '2025-02-11 03:58:59.597132'),
(41, 'main', '0026_quizquestions_quizresponse_quizzes_and_more', '2025-02-11 03:59:39.849940'),
(42, 'main', '0027_alter_parents_student', '2025-02-15 13:00:44.890114'),
(43, 'main', '0028_alter_students_roll_no', '2025-02-15 14:14:41.676092'),
(44, 'main', '0029_students_email', '2025-02-16 04:01:32.975174'),
(45, 'main', '0030_alter_studentevaluation_assignment_rating_and_more', '2025-02-21 13:58:05.347099'),
(46, 'main', '0031_attendance_created_at_attendance_hour', '2025-02-22 06:55:17.314560'),
(47, 'main', '0032_remove_studentevaluation_quiz_percentage', '2025-02-23 12:29:02.320365'),
(48, 'main', '0033_rename_homework_completion_rating_studentevaluation_class_performance_rating', '2025-02-23 12:31:20.471846'),
(49, 'main', '0034_rename_class_performance_rating_studentevaluation_class_participation_rating', '2025-02-23 12:50:11.006540'),
(50, 'main', '0035_rename_assignment_rating_studentevaluation_academic_activity_rating', '2025-02-23 12:52:32.379361'),
(51, 'main', '0036_auto_20250320_1246', '2025-03-20 07:17:09.405782'),
(52, 'main', '0037_alter_announcements_id_alter_attendance_id_and_more', '2025-03-22 05:19:18.868641'),
(53, 'main', '0038_alter_students_roll_no', '2025-03-22 05:20:35.492631'),
(54, 'main', '0039_auto_20250323_1236', '2025-03-23 07:06:39.955965'),
(55, 'main', '0040_auto_20250323_1240', '2025-03-23 07:10:12.625290');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0sqw8o0o8mhayjchrhtl2w6v0aj2l3kv', 'eyJjbGFzc19oZWFkX2lkIjoxM30:1teAY3:dJ_S_q8GBRIV6iObczDcnUlK_UUyEYQSl1M_imqWfVs', '2025-02-15 10:16:23.547677'),
('1gpyt7qf0zwgjv0ks3phj8kgky7sujui', 'e30:1tbIQB:POyn-rEoj-sxlUT5I0fZxGB8HipITsS_lEUf11In7UQ', '2025-02-07 12:04:23.929518'),
('h5pc1p9nec27wdykh2qt4mk3x722na02', 'e30:1tbZMT:FdwmYlisd-l-pxW7jS1z9YUv536sEY52rWlm1KIRT8c', '2025-02-08 06:09:41.949257'),
('iy50ymfvuabvrs6zzsg9qqt101y7m2cb', 'eyJjbGFzc19pZCI6MjB9:1towA5:dVEPMlhSNFYXBRQ6Vz46q-kGgEv5dupnuxIfe78K6h0', '2025-03-17 03:08:09.985790'),
('p9rbo3jfob45shgippf65xqmxcwm2px5', 'e30:1tbIQa:t8noblKYAHTQaK-nODwDQhiLUyUu8hZWLBGdoUAPH0Y', '2025-02-07 12:04:48.695025'),
('q2ry82ujy4xq0ubcekh7gjv27mmg3dkm', 'e30:1tbITs:iCq2XiI3lYkOS59VwFcfcfL3j2lOhn_KcFnK5fUGh6c', '2025-02-07 12:08:12.871277'),
('q663wz1plma1getb4y9gh3cxg8sa74yl', 'eyJ0ZWFjaGVyX2lkIjozfQ:1tbAhP:jrYiLIlKpvJjC8qWeaYEh0TyA7l_dr6t_ct2L3D6syg', '2025-02-07 03:49:39.794741'),
('s8bg8ppi7ld6bqexoeg4padni4qucqo6', 'eyJjbGFzc19oZWFkX2lkIjoxM30:1teAX7:4BgPYk55nnCIw1fMWIP3kj9QzQ7b9Ll-UfJUSznFPxg', '2025-02-15 10:15:25.661351'),
('vlr8b57ebhnph935i0hp4aga5dbzlmav', '.eJyrVipILErNK4nPTFGyMjHRUUrOSSwuBvOMLXWUikuTslKTIbJGxkB-SWkKXLV5LQCHrBRg:1twz25:PfUGLl2zRqImg4uC_fXzFWVpZBl0wEQxhTtKPict8dg', '2025-04-08 07:49:09.168728'),
('xuiiy8d7orowqcmqn7wm0xlov7tttahu', 'e30:1tbZMi:Alo1mi87tOh2qUhsmwP8J5rkP9E8ZaqbzrNyep7wJrg', '2025-02-08 06:09:56.751798');

-- --------------------------------------------------------

--
-- Table structure for table `main_announcements`
--

CREATE TABLE `main_announcements` (
  `id` bigint NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `class_obj_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_attendance`
--

CREATE TABLE `main_attendance` (
  `id` bigint NOT NULL,
  `attendance_date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `hour` smallint UNSIGNED NOT NULL
) ;

--
-- Dumping data for table `main_attendance`
--

INSERT INTO `main_attendance` (`id`, `attendance_date`, `status`, `student_id`, `subject_id`, `created_at`, `hour`) VALUES
(40, '2025-03-19', 'present', 47, 23, '2025-03-23 12:45:38.000000', 1),
(41, '2025-03-18', 'present', 47, 23, '2025-03-23 12:45:51.000000', 1),
(42, '2025-03-21', 'present', 47, 23, '2025-03-23 12:46:01.000000', 1),
(43, '2025-03-27', 'absent', 47, 23, '2025-03-23 12:46:11.000000', 1);

-- --------------------------------------------------------

--
-- Table structure for table `main_chat`
--

CREATE TABLE `main_chat` (
  `id` bigint NOT NULL,
  `message` longtext NOT NULL,
  `receiver_id` bigint NOT NULL,
  `sender_id` bigint NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_chat`
--

INSERT INTO `main_chat` (`id`, `message`, `receiver_id`, `sender_id`, `created_at`) VALUES
(87, 'hii', 167, 166, '2025-03-25 13:16:43.000000');

-- --------------------------------------------------------

--
-- Table structure for table `main_classes`
--

CREATE TABLE `main_classes` (
  `id` bigint NOT NULL,
  `institution_id` bigint NOT NULL,
  `class_head` varchar(255) NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_classes`
--

INSERT INTO `main_classes` (`id`, `institution_id`, `class_head`, `class_name`, `email`, `password`, `user_id`) VALUES
(39, 9, 'John Doe', 'MCA', 'john@example.com', 'jjjj', 166);

-- --------------------------------------------------------

--
-- Table structure for table `main_institution`
--

CREATE TABLE `main_institution` (
  `institution_id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  `institution_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_institution`
--

INSERT INTO `main_institution` (`institution_id`, `email`, `institution_name`, `password`) VALUES
(9, 'sainsaburaj@depaul.edu.in', 'De Paul Institute of Science and Technology', 'dddd'),
(15, 'stc@example.com', 'STC THRISSUR', 'ssss'),
(16, 'aloy@example.com', 'St Aloysius', 'aaaa');

-- --------------------------------------------------------

--
-- Table structure for table `main_marks`
--

CREATE TABLE `main_marks` (
  `id` bigint NOT NULL,
  `mark_percentage` double NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_marks`
--

INSERT INTO `main_marks` (`id`, `mark_percentage`, `student_id`, `subject_id`) VALUES
(44, 85, 47, 23);

-- --------------------------------------------------------

--
-- Table structure for table `main_parents`
--

CREATE TABLE `main_parents` (
  `id` bigint NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `student_id` bigint NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_parents`
--

INSERT INTO `main_parents` (`id`, `password`, `name`, `student_id`, `user_id`) VALUES
(44, '1001', NULL, 47, 169);

-- --------------------------------------------------------

--
-- Table structure for table `main_quizquestions`
--

CREATE TABLE `main_quizquestions` (
  `id` bigint NOT NULL,
  `question` longtext NOT NULL,
  `option_a` varchar(255) NOT NULL,
  `option_b` varchar(255) NOT NULL,
  `option_c` varchar(255) NOT NULL,
  `option_d` varchar(255) NOT NULL,
  `correct_option` varchar(1) NOT NULL,
  `quiz_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_quizresponse`
--

CREATE TABLE `main_quizresponse` (
  `id` bigint NOT NULL,
  `student_response` varchar(1) DEFAULT NULL,
  `question_id` bigint NOT NULL,
  `student_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_quizzes`
--

CREATE TABLE `main_quizzes` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `class_obj_id` bigint DEFAULT NULL,
  `subject_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_studentevaluation`
--

CREATE TABLE `main_studentevaluation` (
  `id` bigint NOT NULL,
  `study_time_rating` double DEFAULT NULL,
  `sleep_time_rating` double DEFAULT NULL,
  `class_participation_rating` double DEFAULT NULL,
  `academic_activity_rating` double DEFAULT NULL,
  `attendance_percentage` double DEFAULT NULL,
  `marks_percentage` double DEFAULT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_studentevaluation`
--

INSERT INTO `main_studentevaluation` (`id`, `study_time_rating`, `sleep_time_rating`, `class_participation_rating`, `academic_activity_rating`, `attendance_percentage`, `marks_percentage`, `student_id`, `subject_id`) VALUES
(34, 71, 73.5, 90, 98, 75, 85, 47, 23);

-- --------------------------------------------------------

--
-- Table structure for table `main_students`
--

CREATE TABLE `main_students` (
  `id` bigint NOT NULL,
  `roll_no` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `class_obj_id` bigint DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_students`
--

INSERT INTO `main_students` (`id`, `roll_no`, `password`, `class_obj_id`, `name`, `user_id`, `email`) VALUES
(47, 'MCA-1001', '1001', 39, 'Jack White', 168, 'jack@example.com');

-- --------------------------------------------------------

--
-- Table structure for table `main_studymaterials`
--

CREATE TABLE `main_studymaterials` (
  `id` bigint NOT NULL,
  `file_url` longtext,
  `created_at` datetime(6) NOT NULL,
  `class_obj_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL,
  `announcement` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_subjects`
--

CREATE TABLE `main_subjects` (
  `id` bigint NOT NULL,
  `class_obj_id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `subject_head` varchar(255) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_subjects`
--

INSERT INTO `main_subjects` (`id`, `class_obj_id`, `email`, `password`, `subject_head`, `subject_name`, `user_id`) VALUES
(23, 39, 'ava@example.com', 'aaaa', 'Ava Miller', 'Computer Fundamentals', 167);

-- --------------------------------------------------------

--
-- Table structure for table `main_users`
--

CREATE TABLE `main_users` (
  `id` bigint NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_users`
--

INSERT INTO `main_users` (`id`, `role`) VALUES
(166, 'class_head'),
(167, 'subject_head'),
(168, 'student'),
(169, 'parent');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_announcements`
--
ALTER TABLE `main_announcements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_announcements_class_obj_id_0d0d9d96_fk` (`class_obj_id`);

--
-- Indexes for table `main_attendance`
--
ALTER TABLE `main_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_attendance_student_id_07549adf_fk` (`student_id`),
  ADD KEY `main_attendance_subject_id_723a5c64_fk` (`subject_id`);

--
-- Indexes for table `main_chat`
--
ALTER TABLE `main_chat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_chat_receiver_id_ddcb21d3_fk` (`receiver_id`),
  ADD KEY `main_chat_sender_id_1824ffc2_fk` (`sender_id`);

--
-- Indexes for table `main_classes`
--
ALTER TABLE `main_classes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_classes_institution_id_5083f29a_fk` (`institution_id`),
  ADD KEY `main_classes_user_id_06af4a09_fk` (`user_id`);

--
-- Indexes for table `main_institution`
--
ALTER TABLE `main_institution`
  ADD PRIMARY KEY (`institution_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `main_marks`
--
ALTER TABLE `main_marks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_marks_student_id_46d8b040_fk` (`student_id`),
  ADD KEY `main_marks_subject_id_cd277d76_fk` (`subject_id`);

--
-- Indexes for table `main_parents`
--
ALTER TABLE `main_parents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_parents_user_id_faa417c1_fk` (`user_id`),
  ADD KEY `main_parents_student_id_fk` (`student_id`);

--
-- Indexes for table `main_quizquestions`
--
ALTER TABLE `main_quizquestions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_quizquestions_quiz_id_bddb7bdd_fk` (`quiz_id`);

--
-- Indexes for table `main_quizresponse`
--
ALTER TABLE `main_quizresponse`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_quizresponse_question_id_b2fe2eec_fk` (`question_id`),
  ADD KEY `main_quizresponse_student_id_c1a777b9_fk` (`student_id`);

--
-- Indexes for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_quizzes_class_obj_id_10b981c4_fk` (`class_obj_id`),
  ADD KEY `main_quizzes_subject_id_025453ee_fk` (`subject_id`);

--
-- Indexes for table `main_studentevaluation`
--
ALTER TABLE `main_studentevaluation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_studentevaluation_student_id_a595bb53_fk` (`student_id`),
  ADD KEY `main_studentevaluation_subject_id_58110765_fk` (`subject_id`);

--
-- Indexes for table `main_students`
--
ALTER TABLE `main_students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roll_no` (`roll_no`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_students_user_id_8b7ccf0c_fk` (`user_id`),
  ADD KEY `main_students_class_obj_id_fk` (`class_obj_id`);

--
-- Indexes for table `main_studymaterials`
--
ALTER TABLE `main_studymaterials`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_studymaterials_class_obj_id_fa6c87bb_fk` (`class_obj_id`),
  ADD KEY `main_studymaterials_subject_id_4af51e55_fk` (`subject_id`);

--
-- Indexes for table `main_subjects`
--
ALTER TABLE `main_subjects`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_subjects_class_obj_id_bacc0ce4_fk` (`class_obj_id`),
  ADD KEY `main_subjects_user_id_79302367_fk` (`user_id`);

--
-- Indexes for table `main_users`
--
ALTER TABLE `main_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=125;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `main_announcements`
--
ALTER TABLE `main_announcements`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `main_attendance`
--
ALTER TABLE `main_attendance`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_chat`
--
ALTER TABLE `main_chat`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `main_classes`
--
ALTER TABLE `main_classes`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `main_institution`
--
ALTER TABLE `main_institution`
  MODIFY `institution_id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `main_marks`
--
ALTER TABLE `main_marks`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `main_parents`
--
ALTER TABLE `main_parents`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `main_quizquestions`
--
ALTER TABLE `main_quizquestions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `main_quizresponse`
--
ALTER TABLE `main_quizresponse`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `main_studentevaluation`
--
ALTER TABLE `main_studentevaluation`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `main_students`
--
ALTER TABLE `main_students`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `main_studymaterials`
--
ALTER TABLE `main_studymaterials`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `main_subjects`
--
ALTER TABLE `main_subjects`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `main_users`
--
ALTER TABLE `main_users`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=170;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `main_announcements`
--
ALTER TABLE `main_announcements`
  ADD CONSTRAINT `main_announcements_class_obj_id_0d0d9d96_fk` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`);

--
-- Constraints for table `main_attendance`
--
ALTER TABLE `main_attendance`
  ADD CONSTRAINT `main_attendance_student_id_07549adf_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_attendance_subject_id_723a5c64_fk` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_chat`
--
ALTER TABLE `main_chat`
  ADD CONSTRAINT `main_chat_receiver_id_ddcb21d3_fk` FOREIGN KEY (`receiver_id`) REFERENCES `main_users` (`id`),
  ADD CONSTRAINT `main_chat_sender_id_1824ffc2_fk` FOREIGN KEY (`sender_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_classes`
--
ALTER TABLE `main_classes`
  ADD CONSTRAINT `main_classes_institution_id_5083f29a_fk` FOREIGN KEY (`institution_id`) REFERENCES `main_institution` (`institution_id`),
  ADD CONSTRAINT `main_classes_user_id_06af4a09_fk` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_marks`
--
ALTER TABLE `main_marks`
  ADD CONSTRAINT `main_marks_student_id_46d8b040_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_marks_subject_id_cd277d76_fk` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_parents`
--
ALTER TABLE `main_parents`
  ADD CONSTRAINT `main_parents_student_id_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `main_parents_user_id_faa417c1_fk` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_quizquestions`
--
ALTER TABLE `main_quizquestions`
  ADD CONSTRAINT `main_quizquestions_quiz_id_bddb7bdd_fk` FOREIGN KEY (`quiz_id`) REFERENCES `main_quizzes` (`id`);

--
-- Constraints for table `main_quizresponse`
--
ALTER TABLE `main_quizresponse`
  ADD CONSTRAINT `main_quizresponse_question_id_b2fe2eec_fk` FOREIGN KEY (`question_id`) REFERENCES `main_quizquestions` (`id`),
  ADD CONSTRAINT `main_quizresponse_student_id_c1a777b9_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`);

--
-- Constraints for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  ADD CONSTRAINT `main_quizzes_class_obj_id_10b981c4_fk` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_quizzes_subject_id_025453ee_fk` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_studentevaluation`
--
ALTER TABLE `main_studentevaluation`
  ADD CONSTRAINT `main_studentevaluation_student_id_a595bb53_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_studentevaluation_subject_id_58110765_fk` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_students`
--
ALTER TABLE `main_students`
  ADD CONSTRAINT `main_students_class_obj_id_fk` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `main_students_user_id_8b7ccf0c_fk` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_studymaterials`
--
ALTER TABLE `main_studymaterials`
  ADD CONSTRAINT `main_studymaterials_class_obj_id_fa6c87bb_fk` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_studymaterials_subject_id_4af51e55_fk` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_subjects`
--
ALTER TABLE `main_subjects`
  ADD CONSTRAINT `main_subjects_class_obj_id_bacc0ce4_fk` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_subjects_user_id_79302367_fk` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
