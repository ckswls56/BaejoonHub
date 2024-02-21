-- 코드를 입력하세요

select y, m,count(*),round(count(*)/total,1)
from
(
SELECT user_id,month(sales_date) as m , year(sales_date) as y
FROM online_sale  
group by user_id,month(sales_date)
) as z,
(
    select user_id
    from user_info
    where year(joined)='2021'
) as i,
(
    select count(*) as total
    from user_info
    where year(joined)='2021'
) as zzz
where z.user_id = i.user_id
group by y,m
order by 1,2