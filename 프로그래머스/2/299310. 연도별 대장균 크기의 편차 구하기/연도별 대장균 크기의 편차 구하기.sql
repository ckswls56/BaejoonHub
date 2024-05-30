SELECT 
    YEAR(e.differentiation_date) AS year,
    i.maxs - e.size_of_colony AS year_dev,
    e.id
FROM 
    ecoli_data AS e
JOIN 
    (SELECT 
         YEAR(differentiation_date) AS y,
         MAX(size_of_colony) AS maxs
     FROM 
         ecoli_data
     GROUP BY 
         YEAR(differentiation_date)) AS i
ON 
    i.y = YEAR(e.differentiation_date)
ORDER BY 
    1,2;
