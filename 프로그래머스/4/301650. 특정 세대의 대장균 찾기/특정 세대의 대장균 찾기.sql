-- 코드를 작성해주세요


select id
from ecoli_data
where parent_id in
(
select o.id
from ecoli_data as o
,
(
    select id
    from ecoli_data
    where parent_id is null
) as i
where parent_id is not null and o.parent_id = i.id
)
order by 1




