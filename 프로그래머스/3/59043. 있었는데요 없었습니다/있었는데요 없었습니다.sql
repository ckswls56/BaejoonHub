-- 코드를 입력하세요
SELECT a.animal_id,a.name
from animal_ins as a,animal_outs as b
where a.datetime > b.datetime and a.animal_id = b.animal_id
order by a.datetime