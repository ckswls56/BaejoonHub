-- 코드를 입력하세요
SELECT apnt_no,pt_name,a.pt_no,a.mcdp_cd,dr_name,apnt_ymd
from appointment as a,patient as b,doctor as c
where date_format(apnt_ymd,"%Y-%m-%d") = '2022-04-13' and apnt_cncl_yn = 'N'
and a.pt_no = b.pt_no and a.mddr_id = c.dr_id
order by 6