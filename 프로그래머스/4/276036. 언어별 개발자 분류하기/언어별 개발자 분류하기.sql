SELECT 
    (
        CASE
            WHEN skill_code & (
                SELECT SUM(CODE) AS code
                FROM skillcodes
                WHERE category = 'Front End'
            ) AND skill_code & (
                SELECT code 
                FROM skillcodes
                WHERE name = 'Python'
            )
            THEN 'A'
            WHEN skill_code & (
                SELECT code
                FROM skillcodes
                WHERE name ='C#'
            )
            THEN 'B'
            WHEN skill_code & (
                SELECT SUM(CODE) AS code
                FROM skillcodes
                WHERE category = 'Front End'
            )
            THEN 'C'
            
        END
    ) AS grade,
    id,
    email
FROM developers
WHERE (
        (
            skill_code & (
                SELECT SUM(CODE) AS code
                FROM skillcodes
                WHERE category = 'Front End'
            )
            AND skill_code & (
                SELECT code 
                FROM skillcodes
                WHERE name = 'Python'
            )
        )
        OR
        (
            skill_code & (
                SELECT code
                FROM skillcodes
                WHERE name ='C#'
            )
        )
        OR
        (
            skill_code & (
                SELECT SUM(CODE) AS code
                FROM skillcodes
                WHERE category = 'Front End'
            )
        )
    )
ORDER BY 1,2;
