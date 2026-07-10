CREATE TABLE `Coordinator` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `mobile_no` varchar(255),
  `email` varchar(255),
  `district` varchar(255),
  `block` varchar(255),
  `is_active` bool,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `farmers` (
  `id` int PRIMARY KEY,
  `coordinator_id` int,
  `name` varchar(255),
  `mobile_number` varchar(255),
  `district` varchar(255),
  `block` varchar(255),
  `village` varchar(255),
  `crop_type` varchar(255),
  `sowing_date` date,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `plots` (
  `id` int PRIMARY KEY,
  `farmer_id` int,
  `survey_number` varchar(255),
  `plot_name` varchar(255),
  `area_acres` float,
  `latitude` float,
  `longitude` float,
  `boundary_geojson` text,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `tokens` (
  `id` int PRIMARY KEY,
  `farmer_id` int,
  `coordinator_id` int,
  `token` varchar(255),
  `is_used` boolean,
  `expires_at` timestamp,
  `created_at` timestamp
);

CREATE TABLE `otp_logs` (
  `id` int PRIMARY KEY,
  `mobile_number` varchar(255),
  `otp` varchar(255),
  `attempts` int,
  `is_verified` boolean,
  `expires_at` timestamp,
  `created_at` timestamp
);

CREATE TABLE `ngos` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `contact_person` varchar(255),
  `mobile_number` varchar(255),
  `email` varchar(255),
  `district` varchar(255),
  `created_at` timestamp
);

ALTER TABLE `farmers` ADD FOREIGN KEY (`coordinator_id`) REFERENCES `Coordinator` (`id`);

ALTER TABLE `plots` ADD FOREIGN KEY (`farmer_id`) REFERENCES `farmers` (`id`);

ALTER TABLE `tokens` ADD FOREIGN KEY (`farmer_id`) REFERENCES `farmers` (`id`);

ALTER TABLE `tokens` ADD FOREIGN KEY (`coordinator_id`) REFERENCES `Coordinator` (`id`);
