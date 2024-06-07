select round(avg(l),2) as AVERAGE_LENGTH
from (select 
        case
            when length is null then 10
            else length
        end as l
     from fish_info
     )
     as i

