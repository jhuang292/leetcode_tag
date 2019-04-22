# Write your MySQL query statement below
SELECT ABS(p1.x - p2.x) AS shortest
FROM point p1, point p2
WHERE p1.x != p2.x 
ORDER BY ABS(p1.x - p2.x) 
LIMIT 1
