# Write your MySQL query statement below
SELECT tb.Request_at AS Day, ROUND(SUM(CASE
                                WHEN tb.Status != 'completed' THEN 1
                                ELSE 0
                             END) / COUNT(tb.Request_at),2) AS "Cancellation Rate"
FROM (
        SELECT *
        FROM Trips
        WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes') AND Driver_Id NOT IN (SELECT Users_Id FROM Users WHERE Banned = 'Yes') 
        ) tb
WHERE tb.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY tb.Request_at

