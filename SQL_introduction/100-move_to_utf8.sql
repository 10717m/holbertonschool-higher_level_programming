-- Convert the database charset and collation
ALTER DATABASE hbtn_0c_0
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;

-- Select the database to work on
USE hbtn_0c_0;

-- Convert the table charset and collation
ALTER TABLE first_table
  CONVERT TO CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Modify the 'name' column charset and collation
ALTER TABLE first_table
  MODIFY name VARCHAR(256)
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

