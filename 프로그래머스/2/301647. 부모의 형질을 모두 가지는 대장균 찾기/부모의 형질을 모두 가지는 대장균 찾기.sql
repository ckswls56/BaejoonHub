-- 코드를 작성해주세요
select q.id,q.genotype,q.parent_genotype
from(
select id,genotype,
(
    select genotype
    from ecoli_data i
    where i.id = o.parent_id
) as parent_genotype
from ecoli_data o) as q
where q.genotype & q.parent_genotype = q.parent_genotype
order by 1