-- 코드를 작성해주세요

select f.id,fish_name,f.length
from
(
select fish_type,max(length) as length
from fish_info as a
group by fish_type
) as i , fish_info as f
join fish_name_info as n on n.fish_type = f.fish_type
where i.fish_type = f.fish_type and i.length = f.length
order by 1
    