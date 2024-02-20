-- 코드를 입력하세요
select food_type,rest_id,rest_name,favorites
from rest_info,(
SELECT food_type as f,max(favorites) as m
from rest_info
group by food_type) as i
where food_type = f and favorites = m
order by 1 desc

