-- 코드를 입력하세요
SELECT rest_id,rest_name,food_type,favorites,address,round(score,2) as score
from rest_info,(select avg(review_score) as score ,rest_id as r
                from rest_review
                group by rest_id) as o
where address like '서울%' and rest_info.rest_id = r
order by score desc,favorites desc