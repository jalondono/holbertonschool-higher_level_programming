-- lists all Comedy shows in the database hbtn_0d_tvshow
SELECT title FROM tv_show_genres A JOIN tv_genres B ON A.genre_id = B.id join tv_shows C ON C.id = A.show_id WHERE B.name = 'Comedy' ORDER BY C.title;
