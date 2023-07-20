-- imports database 
SELECT `city`,
    AVG(`value`) AS `av_tmp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `av_tmp` DESC;