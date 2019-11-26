-- to lists all genres of the show Dexter.
SELECT name FROM tv_shows A JOIN tv_show_genres B ON A.id = B.show_id JOIN tv_genres C ON C.id = B.genre_id WHERE A.title = 'Dexter' ORDER BY C.name;
