-- lists the number of records with the same score in the second_table of the database.
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score DESC;
