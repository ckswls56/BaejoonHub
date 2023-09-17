-- 코드를 입력하세요
SELECT flavor
from first_half
where total_order > 3000 and flavor not in(
    select flavor
    from ICECREAM_INFO
    where INGREDIENT_TYPE = 'sugar_based'
)
order by total_order desc;
