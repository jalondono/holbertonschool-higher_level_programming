-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres A JOIN tv_genres B ON A.genre_id = B.id GROUP BY name ORDER BY number_of_shows DESC;
