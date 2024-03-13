-- Import in hbtn_0c_0 database this table dump:
-- download https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql (same as Temperatures #0)

-- This script displays the max temperature of each state (ordered by State name).

SELECT state, max(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state
