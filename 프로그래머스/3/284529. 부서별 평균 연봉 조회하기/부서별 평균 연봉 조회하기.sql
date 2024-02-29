-- 코드를 작성해주세요
select dept_id,dept_name_en,avg_sal
from hr_department
join(
select dept_id as d,round(avg(sal)) as avg_sal
from hr_employees
group by dept_id) as i on dept_id = d
order by 3 desc