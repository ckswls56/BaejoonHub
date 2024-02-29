-- 코드를 작성해주세요
select route,
concat(round(sum(d_between_dist),1),'km') as TOTAL_DISTANCE,
concat(round(AVG(d_between_dist),2),'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE
group by route
order by 1 desc