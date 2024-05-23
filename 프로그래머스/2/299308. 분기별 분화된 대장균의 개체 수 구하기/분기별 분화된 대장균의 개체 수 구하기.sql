select 
    case 
        when m >= 1 and m < 4 then '1Q'
        when m >= 4 and m < 7 then '2Q'
        when m >= 7 and m < 10 then '3Q'
        else '4Q'
    end as QUARTER,
    sum(c) as ECOLI_COUNT
from (
    select 
        month(differentiation_date) as m, 
        count(*) as c
    from ecoli_data
    group by month(differentiation_date)
) as i
group by QUARTER
