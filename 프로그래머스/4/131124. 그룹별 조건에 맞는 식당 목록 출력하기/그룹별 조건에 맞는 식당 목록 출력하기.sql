-- 코드를 입력하세요
SELECT member_name, review_text, date_format(review_date,"%Y-%m-%d")
FROM member_profile AS m
JOIN rest_review AS r ON m.member_id = r.member_id
JOIN (
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) AS top_reviewers ON m.member_id = top_reviewers.member_id
ORDER BY 3,2
