-- lists all cities contained in the database hbtn_0d_usa
SELECT A.id,A.name,B.name FROM cities A JOIN states B ON A.state_id = B.id ORDER BY A.id ASC;
