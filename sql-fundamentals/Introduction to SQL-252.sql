## 3. Your First Query ##

SELECT *
  FROM recent_grads;

## 4. Understanding Your First Query ##

SELECT * 
  FROM recent_grads;select * from recent_grads;

  

## 6. The LIMIT Clause ##

SELECT  * from recent_grads LIMIT 5

## 7. Selecting Specific Columns ##

SELECT  Major , ShareWomen from recent_grads

## 8. Filtering Rows Using WHERE ##

SELECT  Major , ShareWomen FROM recent_grads WHERE ShareWomen<0.5

## 9. Expressing Multiple Filter Criteria Using 'AND' ##

SELECT Major,Major_category,Median,ShareWomen FROM recent_grads WHERE ShareWomen>0.5 and Median>50000

## 10. Returning One of Several Conditions With OR ##

SELECT Major,Median,Unemployed from recent_grads where Median>=10000 or ShareWomen<0.5 limit 20 

## 11. Grouping Operators with Parentheses ##

select Major,
Major_category,
ShareWomen,
Unemployment_rate from recent_grads where (Major_category = 'Engineering') and (sharewomen>0.5 or Unemployment_rate<0.051 )

## 12. Ordering Results Using ORDER BY ##

SELECT Major,
ShareWomen,
Unemployment_rate from recent_grads where ShareWomen > 0.3 and Unemployment_rate<0.1 order by ShareWomen desc

## 13. Practice Writing a Query ##

select Major_category, Major, Unemployment_rate
from recent_grads where Major_category='Engineering' or Major_category='Physical Sciences' order by Unemployment_rate asc