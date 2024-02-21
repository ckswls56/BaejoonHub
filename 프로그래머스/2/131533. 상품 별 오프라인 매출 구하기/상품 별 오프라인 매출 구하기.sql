-- 코드를 입력하세요
select product_code,price * s
from product,(
SELECT product_id,sum(sales_amount) as s
from offline_sale
group by product_id
    ) as i
where product.product_id = i.product_id

order by 2 desc , 1