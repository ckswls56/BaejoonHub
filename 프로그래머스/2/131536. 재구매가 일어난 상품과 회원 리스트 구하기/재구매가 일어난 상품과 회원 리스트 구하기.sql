
select user_id,product_id
from
(SELECT count(*) as c,user_id,product_id
from online_sale
group by user_id,product_id
order by user_id,product_id desc) as o
where c>1

