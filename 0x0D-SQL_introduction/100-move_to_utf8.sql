-- This script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- You need to convert all of the following to UTF8:

-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table

ALTER DATABASE hbtn_0c_0 COLLATE=utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table COLLATE=utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;