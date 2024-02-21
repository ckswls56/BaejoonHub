-- 코드를 입력하세요
SELECT a.animal_id,a.animal_type,a.name
from animal_ins as a,animal_outs as b
where a.animal_id = b.animal_id
and sex_upon_intake like '%Intact%' and (sex_upon_outcome like '%Spayed%' or sex_upon_outcome like '%Neutered%')
order by 1