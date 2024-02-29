-- 코드를 작성해주세요
select score,emp_no,emp_name,position,email
from hr_employees
join(
select emp_no as e,sum(score) as score
from hr_grade
group by emp_no
order by 2 desc limit 1
    )as i  on emp_no = e