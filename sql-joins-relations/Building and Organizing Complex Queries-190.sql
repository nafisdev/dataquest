## 3. The With Clause ##

WITH playlist_info AS
    (                
     SELECT
        p.playlist_id,
        p.name,
        t.name as tname,
        CAST(t.milliseconds AS FLOAT)/1000 as milliseconds    
     FROM playlist p 
     LEFT JOIN playlist_track pt ON p.playlist_id= pt.playlist_id 
     LEFT JOIN track t ON pt.track_id= t.track_id
    )

SELECT playlist_id,max(name) as playlist_name, count(tname) as number_of_tracks ,sum(milliseconds) as length_seconds  FROM playlist_info 
GROUP BY playlist_id
ORDER BY playlist_id

## 4. Creating Views ##

DROP VIEW IF EXISTS chinook.customer_gt_90_dollars;

CREATE VIEW chinook.customer_gt_90_dollars AS
SELECT c.* from customer c 
LEFT JOIN invoice i on c.customer_id = i.customer_id
LEFT JOIN invoice_line il on i.invoice_id = il.invoice_id
GROUP BY c.customer_id
HAVING SUM(il.unit_price*il.quantity) > 90;


select * from chinook.customer_gt_90_dollars;

## 5. Combining Rows With Union ##

select * from customer_usa
UNION
select * from customer_gt_90_dollars

## 6. Combining Rows Using Intersect and Except ##

WITH cus as (
select * from customer_usa
INTERSECT
select * from customer_gt_90_dollars
    )
select e.first_name||' '||e.last_name as employee_name, 
count(c.support_rep_id) as customers_usa_gt_90
from employee e
LEFT JOIN cus c on c.support_rep_id = e.employee_id where e.title like 'Sales Support Agent'
GROUP BY c.support_rep_id
ORDER by employee_name;

## 7. Multiple Named Subqueries ##

WITH
    customers_india AS
        (
        SELECT * FROM customer
        WHERE country = "India"
        ),
    sales_per_customer AS
        (
         SELECT
             customer_id,
             SUM(total) total
         FROM invoice
         GROUP BY 1
        )

SELECT
    ci.first_name || " " || ci.last_name customer_name,
    spc.total total_purchases
FROM customers_india ci
INNER JOIN sales_per_customer spc ON ci.customer_id = spc.customer_id
ORDER BY 1;
--     WITH
    
--     customers_india AS(
--     select * FROM
--     customer where country = 'India'
--     )
--     ,
--     customer_sums AS (
--     SELECT c.customer_id,SUM(t.unit_price*il.quantity) as sumtotal from customer c 
--     LEFT JOIN invoice i on c.customer_id = i.customer_id
--     LEFT JOIN invoice_line il on i.invoice_id = il.invoice_id
--      LEFT JOIN track t on t.track_id = il.track_id
--     GROUP BY c.customer_id)
    
--     SELECT c.first_name||' '||c.last_name as customer_name, cs.sumtotal as total_purchases
--     FROM
--     customers_india c 
--     LEFT JOIN customer_sums cs on c.customer_id=cs.customer_id
--     order by customer_name

## 8. Challenge: Each Country's Best Customer ##

WITH
    customer_country_purchases AS
        (
         SELECT
             i.customer_id,
             c.country,
             SUM(i.total) total_purchases
         FROM invoice i
         INNER JOIN customer c ON i.customer_id = c.customer_id
         GROUP BY 1, 2
        ),
    country_max_purchase AS
        (
         SELECT
             country,
             MAX(total_purchases) max_purchase
         FROM customer_country_purchases
         GROUP BY 1
        ),
    country_best_customer AS
        (
         SELECT
            cmp.country,
            cmp.max_purchase,
            (
             SELECT ccp.customer_id
             FROM customer_country_purchases ccp
             WHERE ccp.country = cmp.country AND cmp.max_purchase = ccp.total_purchases
            ) customer_id
         FROM country_max_purchase cmp
        )
SELECT
    cbc.country country,
    c.first_name || " " || c.last_name customer_name,
    cbc.max_purchase total_purchased
FROM customer c
INNER JOIN country_best_customer cbc ON cbc.customer_id = c.customer_id
ORDER BY 1 ASC


-- WITH

-- customer_sums AS (
--     SELECT c.customer_id,c.first_name||' '||c.last_name as customer_name, SUM(t.unit_price*il.quantity) as sumtotal,c.country 
--     from customer c

--     LEFT JOIN invoice i on c.customer_id = i.customer_id
--     LEFT JOIN invoice_line il on i.invoice_id = il.invoice_id
--      LEFT JOIN track t on t.track_id = il.track_id
--     GROUP BY c.customer_id)
    
--     select country , customer_name , MAX(sumtotal) as total_purchased
--     from customer_sums
--     group by country 
--     order by country