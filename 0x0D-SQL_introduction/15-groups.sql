-- lists the number of records with the same score in the second_table of the database.
SELECT score, COUNT(*) AS number
FROM {$1}.second_table
GROUP BY score
ORDER BY number DESC;
