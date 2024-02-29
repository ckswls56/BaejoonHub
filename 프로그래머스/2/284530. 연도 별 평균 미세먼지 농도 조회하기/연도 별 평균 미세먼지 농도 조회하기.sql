SELECT YEAR(ym) AS Year,
       ROUND(AVG(pm_val1), 2) AS PM10,
       ROUND(AVG(pm_val2), 2) AS 'PM2.5'
FROM air_pollution
WHERE LOCATION2 = '수원'
GROUP BY YEAR(ym)
order by 1
