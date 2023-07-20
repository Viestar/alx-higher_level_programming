-- displays descending average of value(temperature) by city
SELECT city,
    AVG(value) AS av_tmp
FROM hbtn_0c_0.temperatures
GROUP BY city
ORDER BY av_tmp DESC;