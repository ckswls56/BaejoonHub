select count(*) as fish_count,max(len) as max_length , fish_type
from (
    SELECT 
    fish_type,
    CASE 
        WHEN length <= 10 or length is null THEN 10
        ELSE length
    END AS len
FROM 
    fish_info) as i
group by fish_type
having avg(i.len)>=33
order by 3


