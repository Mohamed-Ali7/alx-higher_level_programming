-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

-- This script  lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title FROM tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
