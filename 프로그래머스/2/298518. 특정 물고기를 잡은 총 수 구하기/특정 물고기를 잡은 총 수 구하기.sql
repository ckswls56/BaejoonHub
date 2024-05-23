select sum(c) as fish_count from (select count(*) as c
from fish_info as a
join fish_name_info as b on a.fish_type = b.fish_type
group by fish_name
Having  fish_name = 'BASS' or fish_name = 'SNAPPER') as i
