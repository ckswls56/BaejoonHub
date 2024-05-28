-- 코드를 작성해주세요
select id,
(
    case
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) <=0.25 then 'CRITICAL'
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) <=0.5 then 'HIGH'
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) <=0.75 then 'MEDIUM'
    when PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) <=1 then 'LOW'
    end
    ) as colony_name
from ECOLI_DATA 
order by 1
