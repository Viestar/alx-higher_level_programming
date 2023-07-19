-- imports database 
SELECT `city`, AVG(`valu`) AS average_temperature
FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temperature` DESC;
