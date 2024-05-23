

select count(b.ID) as fish_count,fish_name
from fish_name_info as a
join fish_info as b on a.fish_type = b.fish_type
group by fish_name
order by 1 desc