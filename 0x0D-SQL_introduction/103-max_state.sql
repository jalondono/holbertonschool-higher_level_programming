-- script that lists all records of the table second_table
SELECT state,MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
