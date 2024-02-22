-- 코드를 입력하세요
select user_id,nickname,concat(city," ",street_address1," ",street_address2),concat_ws('-',left(tlno,3),mid(tlno,4,4),right(tlno,4))
from used_goods_user
where user_id in(
SELECT writer_id
from used_goods_board
group by writer_id
having count(*) >= 3)
order by 1 desc