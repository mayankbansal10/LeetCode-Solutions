SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'
UNION
SELECT p.product_id,  p.new_price AS price
FROM Products p
INNER JOIN 
(SELECT product_id, MAX(change_date) AS max_date
FROM Products
WHERE change_date <='2019-08-16'
GROUP BY product_id) r
ON p.product_id = r.product_id AND p.change_date=r.max_date;