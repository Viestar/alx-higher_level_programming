-- Retrieves only top 3 using LIMIT
SELECT `city`,
    AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE MONTH IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;