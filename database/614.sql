# Write your MySQL query statement below
SELECT f1.follower, COUNT(DISTINCT f2.follower) AS num
FROM follow f1 LEFT JOIN follow f2 ON f1.follower = f2.followee
-- GROUP BY f1.follower
WHERE f2.followee IS NOT NULL
GROUP BY f1.follower
