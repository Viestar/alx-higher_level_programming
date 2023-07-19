-- Retrieves only top 3 using LIMIT
SELECT city, temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
