-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Feb 07, 2025 at 05:33 PM
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
(108, 'Can view session', 26, 'view_session');

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
(19, 'main', 'quizzes'),
(5, 'main', 'student'),
(6, 'main', 'studentevaluation'),
(21, 'main', 'studentevaluations'),
(20, 'main', 'students'),
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
(24, 'main', '0009_rename_student_id_attendance_student_and_more', '2025-02-01 05:53:48.700534');

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
('p9rbo3jfob45shgippf65xqmxcwm2px5', 'e30:1tbIQa:t8noblKYAHTQaK-nODwDQhiLUyUu8hZWLBGdoUAPH0Y', '2025-02-07 12:04:48.695025'),
('q2ry82ujy4xq0ubcekh7gjv27mmg3dkm', 'e30:1tbITs:iCq2XiI3lYkOS59VwFcfcfL3j2lOhn_KcFnK5fUGh6c', '2025-02-07 12:08:12.871277'),
('q663wz1plma1getb4y9gh3cxg8sa74yl', 'eyJ0ZWFjaGVyX2lkIjozfQ:1tbAhP:jrYiLIlKpvJjC8qWeaYEh0TyA7l_dr6t_ct2L3D6syg', '2025-02-07 03:49:39.794741'),
('s8bg8ppi7ld6bqexoeg4padni4qucqo6', 'eyJjbGFzc19oZWFkX2lkIjoxM30:1teAX7:4BgPYk55nnCIw1fMWIP3kj9QzQ7b9Ll-UfJUSznFPxg', '2025-02-15 10:15:25.661351'),
('xuiiy8d7orowqcmqn7wm0xlov7tttahu', 'e30:1tbZMi:Alo1mi87tOh2qUhsmwP8J5rkP9E8ZaqbzrNyep7wJrg', '2025-02-08 06:09:56.751798');

-- --------------------------------------------------------

--
-- Table structure for table `main_attendance`
--

CREATE TABLE `main_attendance` (
  `id` int NOT NULL,
  `attendance_date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `student_id` int NOT NULL,
  `subject_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_chat`
--

CREATE TABLE `main_chat` (
  `id` int NOT NULL,
  `message` longtext NOT NULL,
  `receiver_id` int NOT NULL,
  `sender_id` int NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_chat`
--

INSERT INTO `main_chat` (`id`, `message`, `receiver_id`, `sender_id`, `created_at`) VALUES
(48, 'Hii Arun Sir!', 49, 40, '2025-02-04 18:57:35.000000'),
(64, 'Hii Arun', 49, 32, '2025-02-07 11:39:31.000000'),
(69, 'Hii Arun, its me ben', 49, 43, '2025-02-07 17:23:35.000000'),
(70, 'Hii Albert', 40, 49, '2025-02-07 13:51:35.157618'),
(71, 'Hello', 40, 49, '2025-02-07 13:51:45.698774'),
(72, 'Hello', 41, 49, '2025-02-07 13:52:06.964392'),
(73, 'Hii BOB', 42, 49, '2025-02-07 13:54:44.992713');

-- --------------------------------------------------------

--
-- Table structure for table `main_classes`
--

CREATE TABLE `main_classes` (
  `id` int NOT NULL,
  `institution_id` int NOT NULL,
  `class_head` varchar(255) NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_classes`
--

INSERT INTO `main_classes` (`id`, `institution_id`, `class_head`, `class_name`, `email`, `password`, `user_id`) VALUES
(13, 9, 'Jack', 'MCA', 'jack@example.com', 'jjjj', 32),
(14, 9, 'John', 'BCA', 'john@example.com', 'john', 33),
(15, 9, 'Jasmine', 'B. Com', 'jasmine@example.com', 'jjjj', 34);

-- --------------------------------------------------------

--
-- Table structure for table `main_institution`
--

CREATE TABLE `main_institution` (
  `institution_id` int NOT NULL,
  `email` varchar(254) NOT NULL,
  `institution_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_institution`
--

INSERT INTO `main_institution` (`institution_id`, `email`, `institution_name`, `password`) VALUES
(9, 'sainsaburaj@depaul.edu.in', 'De Paul Institute of Science and Technology', 'dddd'),
(10, 'stc@example.com', 'STC THRISSUR', 'ssss');

-- --------------------------------------------------------

--
-- Table structure for table `main_marks`
--

CREATE TABLE `main_marks` (
  `id` int NOT NULL,
  `mark_percentage` double NOT NULL,
  `student_id` int NOT NULL,
  `subject_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_parents`
--

CREATE TABLE `main_parents` (
  `id` int NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `student_id` varchar(20) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_parents`
--

INSERT INTO `main_parents` (`id`, `password`, `name`, `student_id`, `user_id`) VALUES
(11, '1001', 'Joseph', '1001', 41),
(12, '1002', 'Ben', '1002', 43),
(13, '1303', NULL, '1303', 52);

-- --------------------------------------------------------

--
-- Table structure for table `main_quizzes`
--

CREATE TABLE `main_quizzes` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `subject_id` int NOT NULL,
  `class_obj_id` int DEFAULT NULL,
  `correct_option` varchar(1) NOT NULL,
  `option_a` varchar(255) NOT NULL,
  `option_b` varchar(255) NOT NULL,
  `option_c` varchar(255) NOT NULL,
  `option_d` varchar(255) NOT NULL,
  `question` longtext NOT NULL DEFAULT (_utf8mb3'Default Question'),
  `student_response` varchar(1) DEFAULT NULL,
  `student_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_studentevaluations`
--

CREATE TABLE `main_studentevaluations` (
  `id` int NOT NULL,
  `study_time_rating` int NOT NULL,
  `sleep_time_rating` int NOT NULL,
  `homework_completion_rating` int NOT NULL,
  `class_participation_rating` int NOT NULL,
  `test_preparation_rating` int NOT NULL,
  `class_difficulty_rating` int NOT NULL,
  `parent_rating` int NOT NULL,
  `teacher_rating` int NOT NULL,
  `student_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_students`
--

CREATE TABLE `main_students` (
  `id` int NOT NULL,
  `roll_no` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `class_obj_id` int DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_students`
--

INSERT INTO `main_students` (`id`, `roll_no`, `password`, `class_obj_id`, `name`, `user_id`) VALUES
(14, '1001', '1001', 13, 'Albert', 40),
(15, '1002', '1002', 13, 'Bob', 42),
(16, '1303', '1303', 14, 'Vaseem', 51);

-- --------------------------------------------------------

--
-- Table structure for table `main_subjects`
--

CREATE TABLE `main_subjects` (
  `id` int NOT NULL,
  `class_obj_id` int NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(255) NOT NULL,
  `subject_head` varchar(255) NOT NULL,
  `subject_name` varchar(255) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_subjects`
--

INSERT INTO `main_subjects` (`id`, `class_obj_id`, `email`, `password`, `subject_head`, `subject_name`, `user_id`) VALUES
(1, 13, 'arun@example.com', 'aaaa', 'Arun', 'Machine Learning', 49),
(2, 13, 'rose@example.com', 'rrrr', 'Rosemary', 'Computer Organization', 50),
(3, 13, 'reena@example.com', 'rrrr', 'Reena', 'Operating System', 53),
(4, 14, 'sophia@example.com', 'ssss', 'Sophia', 'Software Engineering', 54);

-- --------------------------------------------------------

--
-- Table structure for table `main_users`
--

CREATE TABLE `main_users` (
  `id` int NOT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `main_users`
--

INSERT INTO `main_users` (`id`, `role`) VALUES
(32, 'class_head'),
(33, 'class_head'),
(34, 'class_head'),
(40, 'student'),
(41, 'parent'),
(42, 'student'),
(43, 'parent'),
(49, 'subject_head'),
(50, 'subject_head'),
(51, 'student'),
(52, 'parent'),
(53, 'subject_head'),
(54, 'subject_head');

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
-- Indexes for table `main_attendance`
--
ALTER TABLE `main_attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_attendance_student_id_07549adf_fk_main_students_id` (`student_id`),
  ADD KEY `main_attendance_subject_id_723a5c64_fk_main_subjects_id` (`subject_id`);

--
-- Indexes for table `main_chat`
--
ALTER TABLE `main_chat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_chat_receiver_id_ddcb21d3_fk_main_users_id` (`receiver_id`),
  ADD KEY `main_chat_sender_id_1824ffc2_fk_main_users_id` (`sender_id`);

--
-- Indexes for table `main_classes`
--
ALTER TABLE `main_classes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_classes_institution_id_5083f29a_fk_main_inst` (`institution_id`),
  ADD KEY `main_classes_user_id_06af4a09_fk_main_users_id` (`user_id`);

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
  ADD KEY `main_marks_student_id_46d8b040_fk_main_students_id` (`student_id`),
  ADD KEY `main_marks_subject_id_cd277d76_fk_main_subjects_id` (`subject_id`);

--
-- Indexes for table `main_parents`
--
ALTER TABLE `main_parents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_parents_user_id_faa417c1_fk_main_users_id` (`user_id`),
  ADD KEY `main_parents_student_id_eb1d3ba3_fk` (`student_id`);

--
-- Indexes for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_quizzes_class_obj_id_10b981c4_fk_main_classes_id` (`class_obj_id`),
  ADD KEY `main_quizzes_subject_id_025453ee_fk_main_subjects_id` (`subject_id`),
  ADD KEY `main_quizzes_student_id_3537662e_fk_main_students_id` (`student_id`);

--
-- Indexes for table `main_studentevaluations`
--
ALTER TABLE `main_studentevaluations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_studentevaluations_student_id_7838dbe4_fk_main_students_id` (`student_id`);

--
-- Indexes for table `main_students`
--
ALTER TABLE `main_students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roll_no` (`roll_no`),
  ADD KEY `main_students_class_obj_id_fe626842_fk_main_classes_id` (`class_obj_id`),
  ADD KEY `main_students_user_id_8b7ccf0c_fk_main_users_id` (`user_id`);

--
-- Indexes for table `main_subjects`
--
ALTER TABLE `main_subjects`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `main_subjects_class_obj_id_bacc0ce4_fk_main_classes_id` (`class_obj_id`),
  ADD KEY `main_subjects_user_id_79302367_fk_main_users_id` (`user_id`);

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `main_attendance`
--
ALTER TABLE `main_attendance`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_chat`
--
ALTER TABLE `main_chat`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT for table `main_classes`
--
ALTER TABLE `main_classes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `main_institution`
--
ALTER TABLE `main_institution`
  MODIFY `institution_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `main_marks`
--
ALTER TABLE `main_marks`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_parents`
--
ALTER TABLE `main_parents`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_studentevaluations`
--
ALTER TABLE `main_studentevaluations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_students`
--
ALTER TABLE `main_students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `main_subjects`
--
ALTER TABLE `main_subjects`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `main_users`
--
ALTER TABLE `main_users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

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
-- Constraints for table `main_attendance`
--
ALTER TABLE `main_attendance`
  ADD CONSTRAINT `main_attendance_student_id_07549adf_fk_main_students_id` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_attendance_subject_id_723a5c64_fk_main_subjects_id` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_chat`
--
ALTER TABLE `main_chat`
  ADD CONSTRAINT `main_chat_receiver_id_ddcb21d3_fk_main_users_id` FOREIGN KEY (`receiver_id`) REFERENCES `main_users` (`id`),
  ADD CONSTRAINT `main_chat_sender_id_1824ffc2_fk_main_users_id` FOREIGN KEY (`sender_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_classes`
--
ALTER TABLE `main_classes`
  ADD CONSTRAINT `main_classes_institution_id_5083f29a_fk_main_inst` FOREIGN KEY (`institution_id`) REFERENCES `main_institution` (`institution_id`),
  ADD CONSTRAINT `main_classes_user_id_06af4a09_fk_main_users_id` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_marks`
--
ALTER TABLE `main_marks`
  ADD CONSTRAINT `main_marks_student_id_46d8b040_fk_main_students_id` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_marks_subject_id_cd277d76_fk_main_subjects_id` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_parents`
--
ALTER TABLE `main_parents`
  ADD CONSTRAINT `main_parents_student_id_eb1d3ba3_fk` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`roll_no`),
  ADD CONSTRAINT `main_parents_user_id_faa417c1_fk_main_users_id` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_quizzes`
--
ALTER TABLE `main_quizzes`
  ADD CONSTRAINT `main_quizzes_class_obj_id_10b981c4_fk_main_classes_id` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_quizzes_student_id_3537662e_fk_main_students_id` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`),
  ADD CONSTRAINT `main_quizzes_subject_id_025453ee_fk_main_subjects_id` FOREIGN KEY (`subject_id`) REFERENCES `main_subjects` (`id`);

--
-- Constraints for table `main_studentevaluations`
--
ALTER TABLE `main_studentevaluations`
  ADD CONSTRAINT `main_studentevaluations_student_id_7838dbe4_fk_main_students_id` FOREIGN KEY (`student_id`) REFERENCES `main_students` (`id`);

--
-- Constraints for table `main_students`
--
ALTER TABLE `main_students`
  ADD CONSTRAINT `main_students_class_obj_id_fe626842_fk_main_classes_id` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_students_user_id_8b7ccf0c_fk_main_users_id` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);

--
-- Constraints for table `main_subjects`
--
ALTER TABLE `main_subjects`
  ADD CONSTRAINT `main_subjects_class_obj_id_bacc0ce4_fk_main_classes_id` FOREIGN KEY (`class_obj_id`) REFERENCES `main_classes` (`id`),
  ADD CONSTRAINT `main_subjects_user_id_79302367_fk_main_users_id` FOREIGN KEY (`user_id`) REFERENCES `main_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
