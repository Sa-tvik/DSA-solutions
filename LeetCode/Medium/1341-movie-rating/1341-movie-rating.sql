# Write your MySQL query statement below
SELECT name as results
FROM Users WHERE user_id = (
    SELECT mr.user_id FROM MovieRating mr JOIN Users USING(user_id)
    GROUP BY mr.user_id ORDER BY COUNT(mr.user_id) DESC,name ASC LIMIT 1
    
)
UNION ALL
SELECT title as results
FROM Movies WHERE movie_id = (
    SELECT mr.movie_id
    FROM MovieRating mr JOIN Movies m USING(movie_id) 
    WHERE mr.created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY mr.movie_id ORDER BY AVG(mr.rating) DESC, m.title ASC LIMIT 1
)
