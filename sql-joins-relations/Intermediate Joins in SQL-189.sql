## 2. Joining Three Tables ##

SELECT il.track_id,t.name as track_name, mt.name as track_type,t.unit_price,quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE invoice_id = 4;

## 3. Joining More Than Three Tables ##

SELECT il.track_id,t.name as track_name,at.name as artist_name, mt.name as track_type,t.unit_price,quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album ab ON t.album_id=ab.album_id
INNER JOIN artist at ON at.artist_id=ab.artist_id
WHERE invoice_id = 4;

## 4. Combining Multiple Joins with Subqueries ##

SELECT
    ta.album_name album,
    ta.artist_name artist
    ,COUNT(*) tracks_purchased
FROM invoice_line il
INNER JOIN (
            SELECT
                t.track_id,
                al.title album_name,
                ar.name as artist_name
            FROM track t
            INNER JOIN album al ON al.album_id = t.album_id
            INNER JOIN artist ar ON ar.artist_id = al.artist_id
           ) ta
           ON ta.track_id = il.track_id
GROUP BY 1
ORDER BY 3 DESC LIMIT 5;

## 5. Recursive Joins ##

SELECT
    e1.first_name||' '||e1.last_name employee_name,
    e1.title employee_title,
    e2.first_name||' '||e2.last_name supervisor_name,
    e2.title supervisor_title
FROM employee e1
LEFT JOIN employee e2 on e1.reports_to = e2.employee_id
order by 1 asc

## 6. Pattern Matching Using Like ##

SELECT
    first_name,
    last_name,
    phone
FROM customer
WHERE first_name LIKE "%Belle%";

## 7. Revisiting CASE ##

SELECT c.first_name||' '||c.last_name customer_name,
count(c.customer_id) number_of_purchases,
SUM(i.total) total_spent,
CASE WHEN SUM(i.total)<40 THEN 'small spender'
WHEN SUM(i.total) > 100 THEN 'big spender'
ELSE 'regular'
END
customer_category
FROM customer c
INNER JOIN invoice i ON c.customer_id=i.customer_id 
group by c.customer_id
order by 1