SELECT requester_id as id,
(SELECT count(*) FROM RequestAccepted
WHERE id=requester_id OR id = accepter_id) AS num
FROM RequestAccepted
GROUP BY requester_id
UNION
SELECT accepter_id as id,
(SELECT count(*) FROM RequestAccepted
WHERE id=requester_id OR id = accepter_id) AS num
FROM RequestAccepted
GROUP BY accepter_id
ORDER BY num DESC LIMIT 1;