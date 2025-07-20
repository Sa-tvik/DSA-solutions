# Write your MySQL query statement below
SELECT p.product_id,
     IFNULL(ROUND(SUM(u.units * p.price) / SUM(u.units), 2),0) AS average_price
From Prices p  LEFT JOIN UnitsSold u
ON u.purchase_date BETWEEN p.start_date AND p.end_date AND p.product_id = u.product_id
GROUP BY p.product_id;