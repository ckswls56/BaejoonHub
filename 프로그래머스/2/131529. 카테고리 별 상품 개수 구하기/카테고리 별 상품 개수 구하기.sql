-- 코드를 입력하세요
SELECT 
(
    left(PRODUCT_CODE,2)
) as i , count(*)
from product
group by i
order by 1