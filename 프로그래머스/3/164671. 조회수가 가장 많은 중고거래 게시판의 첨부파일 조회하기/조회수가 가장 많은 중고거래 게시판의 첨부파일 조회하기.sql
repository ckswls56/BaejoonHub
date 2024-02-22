-- 코드를 입력하세요
select concat('/home/grep/src/',a.board_id,+'/',file_id,file_name,file_ext) as FILE_PATH
from used_goods_file as a , (
SELECT * 
from used_goods_board
order by 8 desc limit 1
    ) as b
where a.board_id = b.board_id
order by file_id desc


