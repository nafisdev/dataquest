## 1. Writing More Complex Queries ##

SELECT Major , ShareWomen
  FROM recent_grads
 WHERE ShareWomen > (
SELECT AVG(ShareWomen)
  FROM recent_grads);

## 2. Subqueries ##

SELECT Major , Unemployment_rate
  FROM recent_grads
 WHERE Unemployment_rate < (
SELECT AVG(Unemployment_rate)
  FROM recent_grads);

## 3. Subquery in SELECT ##

SELECT (CAST(COUNT(*) as Float)/
       CAST((SELECT COUNT(*)
          FROM recent_grads)
        as Float)
       ) 
       
       as proportion_abv_avg
  FROM recent_grads
 WHERE ShareWomen > (SELECT AVG(ShareWomen)
                       FROM recent_grads
                    );

## 4. The IN Operator ##

select Major_category,Major from recent_grads
where Major_category in ('Business',
'Humanities & Liberal Arts',
'Education')

## 5. Returning Multiple Results in Subqueries ##

SELECT Major_category, Major
  FROM recent_grads
 WHERE Major_category IN (SELECT Major_category
  FROM recent_grads
 GROUP BY Major_category
 ORDER BY SUM(TOTAL) DESC LIMIT 3);

## 6. Building Complex Subqueries ##

select AVG(CAST(Sample_size as FLOAT)
/
CAST(Total as FLOAT))  as avg_ratio from recent_grads

## 7. Practice Integrating A Subquery With The Outer Query ##

SELECT Major,Major_category,CAST(Sample_size as FLOAT)
/
CAST(Total as FLOAT)  as ratio from recent_grads
WHERE ratio > (select AVG(CAST(Sample_size as FLOAT)
/
CAST(Total as FLOAT))  as avg_ratio from recent_grads)