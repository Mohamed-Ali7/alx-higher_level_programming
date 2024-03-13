-- This script Import in hbtn_0c_0 database this table dump:
-- download https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql (same as Temperatures #0)

-- Write a script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)

SELECT city, avg(value) AS avg_temp FROM temperatures WHERE month in (7, 8)
GROUP BY (city) ORDER BY avg_temp DESC LIMIT 3;
