-- 코드를 입력하세요
select user_id,nickname,price as TOTAL_SALES
from(
SELECT writer_id,sum(price) as price
from used_goods_board
group by writer_id,STATUS
having price >= 700000 and status = 'DONE') as i , used_goods_user
where writer_id = user_id
order by 3