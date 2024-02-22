SELECT history_id,
floor(
    case 
    when t is null then date * daily_fee
    else daily_fee * (100-discount_rate)/100 * date
    end
) as fee
FROM CAR_RENTAL_COMPANY_CAR AS a
LEFT JOIN (
    SELECT history_id,
        CASE
            WHEN DATEDIFF(end_date, start_date) + 1 < 7 THEN NULL
            WHEN DATEDIFF(end_date, start_date) + 1 < 30 THEN '7일 이상'
            WHEN DATEDIFF(end_date, start_date) + 1 < 90 THEN '30일 이상'
            ELSE '90일 이상'
        END AS t,DATEDIFF(end_date, start_date) + 1 as date,car_id
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) AS b ON a.car_id = b.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS c ON a.car_type = c.car_type AND b.t = c.duration_type
where a.car_type = '트럭'
order by 2 desc , 1 desc
