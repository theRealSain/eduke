-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jan 20, 2025 at 11:55 AM
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
-- Table structure for table `attendances`
--

CREATE TABLE `attendances` (
  `id` bigint NOT NULL,
  `attendance_date` date NOT NULL,
  `status` varchar(10) NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(68, 'Can view institution', 15, 'view_institution');

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
-- Table structure for table `chats`
--

CREATE TABLE `chats` (
  `id` bigint NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `receiver_id` bigint NOT NULL,
  `sender_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `institution_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `custom_users`
--

CREATE TABLE `custom_users` (
  `id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role` varchar(10) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL
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
(16, 'main', 'customuser'),
(15, 'main', 'institution'),
(7, 'main', 'marks'),
(10, 'main', 'parent'),
(5, 'main', 'student'),
(6, 'main', 'studentevaluation'),
(3, 'main', 'subject'),
(9, 'main', 'teacher'),
(4, 'main', 'user');

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
(18, 'main', '0004_alter_attendance_options_alter_chat_options_and_more', '2025-01-20 10:09:05.700274');

-- --------------------------------------------------------

--
-- Table structure for table `institutions`
--

CREATE TABLE `institutions` (
  `id` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  `institution_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `institutions`
--

INSERT INTO `institutions` (`id`, `email`, `institution_name`, `password`, `created_at`) VALUES
(1, 'sainsaburaj@depaul.edu.in', 'De Paul Institute of Science and Technology', 'pbkdf2_sha256$870000$dknWPcTE9VsqcWh1oDKVER$TBqimrL5hIji2layhZIoiXMTwj+R20MzkARamBvk+74=', '2025-01-20 09:20:15.150015');

-- --------------------------------------------------------

--
-- Table structure for table `marks`
--

CREATE TABLE `marks` (
  `id` bigint NOT NULL,
  `mark_percentage` decimal(5,2) NOT NULL,
  `student_id` bigint NOT NULL,
  `subject_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `parents`
--

CREATE TABLE `parents` (
  `id` bigint NOT NULL,
  `password` varchar(255) NOT NULL,
  `student_id` bigint NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` bigint NOT NULL,
  `roll_number` bigint NOT NULL,
  `password` varchar(255) NOT NULL,
  `class_name_id` bigint NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `student_evaluations`
--

CREATE TABLE `student_evaluations` (
  `id` bigint NOT NULL,
  `study_time_rating` int DEFAULT NULL,
  `sleep_time_rating` int DEFAULT NULL,
  `stress_handling_rating` int DEFAULT NULL,
  `homework_completion_rating` int DEFAULT NULL,
  `class_participation_rating` int DEFAULT NULL,
  `focus_rating` int DEFAULT NULL,
  `test_preparation_rating` int DEFAULT NULL,
  `class_difficulty_rating` int DEFAULT NULL,
  `parent_rating` int DEFAULT NULL,
  `teacher_rating` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `student_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL,
  `subject_id` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `id` bigint NOT NULL,
  `institution_id` bigint NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendances`
--
ALTER TABLE `attendances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_attendance_student_id_07549adf_fk_main_student_id` (`student_id`),
  ADD KEY `main_attendance_subject_id_723a5c64_fk_main_subject_id` (`subject_id`);

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
-- Indexes for table `chats`
--
ALTER TABLE `chats`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_chat_receiver_id_ddcb21d3_fk_main_customuser_id` (`receiver_id`),
  ADD KEY `main_chat_sender_id_1824ffc2_fk_main_customuser_id` (`sender_id`);

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_class_institution_id_da939486_fk_main_institution_id` (`institution_id`);

--
-- Indexes for table `custom_users`
--
ALTER TABLE `custom_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

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
-- Indexes for table `institutions`
--
ALTER TABLE `institutions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `marks`
--
ALTER TABLE `marks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_marks_student_id_46d8b040_fk_main_student_id` (`student_id`),
  ADD KEY `main_marks_subject_id_cd277d76_fk_main_subject_id` (`subject_id`);

--
-- Indexes for table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_parent_student_id_3921969f_fk_main_student_id` (`student_id`),
  ADD KEY `main_parent_user_id_9bb94389_fk_main_customuser_id` (`user_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roll_number` (`roll_number`),
  ADD KEY `main_student_class_name_id_22ab90c6_fk_main_class_id` (`class_name_id`),
  ADD KEY `main_student_user_id_32abd1a3_fk_main_customuser_id` (`user_id`);

--
-- Indexes for table `student_evaluations`
--
ALTER TABLE `student_evaluations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `subject_id` (`subject_id`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_teacher_institution_id_e21fa5f6_fk_main_institution_id` (`institution_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendances`
--
ALTER TABLE `attendances`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `chats`
--
ALTER TABLE `chats`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `custom_users`
--
ALTER TABLE `custom_users`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `institutions`
--
ALTER TABLE `institutions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `marks`
--
ALTER TABLE `marks`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `parents`
--
ALTER TABLE `parents`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `student_evaluations`
--
ALTER TABLE `student_evaluations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendances`
--
ALTER TABLE `attendances`
  ADD CONSTRAINT `main_attendance_student_id_07549adf_fk_main_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `main_attendance_subject_id_723a5c64_fk_main_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`);

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
-- Constraints for table `chats`
--
ALTER TABLE `chats`
  ADD CONSTRAINT `main_chat_receiver_id_ddcb21d3_fk_main_customuser_id` FOREIGN KEY (`receiver_id`) REFERENCES `custom_users` (`id`),
  ADD CONSTRAINT `main_chat_sender_id_1824ffc2_fk_main_customuser_id` FOREIGN KEY (`sender_id`) REFERENCES `custom_users` (`id`);

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `main_class_institution_id_da939486_fk_main_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institutions` (`id`);

--
-- Constraints for table `marks`
--
ALTER TABLE `marks`
  ADD CONSTRAINT `main_marks_student_id_46d8b040_fk_main_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `main_marks_subject_id_cd277d76_fk_main_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`);

--
-- Constraints for table `parents`
--
ALTER TABLE `parents`
  ADD CONSTRAINT `main_parent_student_id_3921969f_fk_main_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `main_parent_user_id_9bb94389_fk_main_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `custom_users` (`id`);

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `main_student_class_name_id_22ab90c6_fk_main_class_id` FOREIGN KEY (`class_name_id`) REFERENCES `classes` (`id`),
  ADD CONSTRAINT `main_student_user_id_32abd1a3_fk_main_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `custom_users` (`id`);

--
-- Constraints for table `student_evaluations`
--
ALTER TABLE `student_evaluations`
  ADD CONSTRAINT `main_studentevaluation_student_id_a595bb53_fk_main_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`);

--
-- Constraints for table `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `main_teacher_institution_id_e21fa5f6_fk_main_institution_id` FOREIGN KEY (`institution_id`) REFERENCES `institutions` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
