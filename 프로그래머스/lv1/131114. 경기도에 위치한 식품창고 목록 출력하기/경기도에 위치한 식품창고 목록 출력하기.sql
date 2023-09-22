-- 코드를 입력하세요
SELECT warehouse_id,warehouse_name,address,
    CASE 
        WHEN FREEZER_YN IS NULL THEN 'N'
        ELSE FREEZER_YN
    END AS FREEZER_YN
from food_warehouse
where warehouse_name like '%경기%'
order by 1