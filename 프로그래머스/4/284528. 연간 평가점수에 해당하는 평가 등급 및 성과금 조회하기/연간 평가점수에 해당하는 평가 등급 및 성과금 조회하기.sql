-- 코드를 작성해주세요
select emp_no, emp_name,
(
    case
        when score >= 96 then 'S'
        when score >= 90 then 'A'
        when score >= 80 then 'B'
        else 'C'
    end
) as grade,
(
    case
        when score >= 96 then sal * 0.2
        when score >= 90 then sal * 0.15
        when score >= 80 then sal * 0.10
        else 0
    end
) as bonus
from hr_employees
join(
select emp_no as e,avg(score) as score
from hr_grade
group by emp_no) as i on emp_no = e
order by 1