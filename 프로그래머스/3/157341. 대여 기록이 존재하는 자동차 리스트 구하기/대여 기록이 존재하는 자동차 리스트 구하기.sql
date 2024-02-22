-- 코드를 입력하세요
SELECT distinct a.car_id
from CAR_RENTAL_COMPANY_CAR as a, CAR_RENTAL_COMPANY_RENTAL_HISTORY as b
where a.car_id=b.car_id and month(start_date) ='10' and car_type = '세단'
order by 1 desc
