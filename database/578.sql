# Write your MySQL query statement below
SELECT question_id AS survey_log
FROM (
        SELECT question_id, 
            SUM(CASE
                WHEN action = 'answer' THEN 1
                ELSE 0
            END) AS num_answer,
            SUM(CASE
                WHEN action = 'show' THEN 1
                ELSE 0
            END) AS num_show
        FROM survey_log
        GROUP BY question_id
            ) tb
ORDER BY num_answer / num_show DESC
LIMIT 1;
