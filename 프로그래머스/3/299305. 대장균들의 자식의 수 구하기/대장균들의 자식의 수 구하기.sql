select id, COALESCE(a.CHILD_COUNT, 0) as CHILD_COUNT
from ecoli_data as b
left outer join 
(select count(*) as CHILD_COUNT , parent_id
from ecoli_data
group by parent_id) as a on a.parent_id = b.id
order by 1