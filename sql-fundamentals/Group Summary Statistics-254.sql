## 2. If/Then in SQL ##

SELECT 
CASE 
WHEN Sample_size<200 THEN 'Small'
WHEN Sample_size<1000 and Sample_size>=200 THEN 'Medium'
ELSE 'Large'
END
as Sample_category FROM recent_grads 

## 3. Dissecting CASE ##

SELECT Major,Sample_size,
CASE 
WHEN Sample_size<200 THEN 'Small'
WHEN Sample_size<1000 and Sample_size>=200 THEN 'Medium'
ELSE 'Large'
END
as Sample_category FROM recent_grads 

## 4. Calculating Group-Level Summary Statistics ##

select Major_category ,SUM(Total)
as Total_graduates  from recent_grads GROUP by    Major_category 

## 5. GROUP BY Visual Breakdown ##

SELECT Major_category, AVG(ShareWomen) as Average_women
  FROM recent_grads
 GROUP BY Major_category;

## 6. Multiple Summary Statistics by Group ##

SELECT Major_category,
       SUM(Women) as Total_women, AVG(ShareWomen) as Mean_women, SUM(Total)*AVG(ShareWomen)as Estimate_women
  FROM recent_grads
 GROUP BY Major_category;

## 7. Multiple Group Columns ##

SELECT Major_category,Sample_category,
        AVG(ShareWomen) as Mean_women, SUM(Total) as Total_graduates
  FROM new_grads
 GROUP BY Major_category,Sample_category

## 8. Querying Virtual Columns With the HAVING Statement ##

SELECT Major_category,AVG(Low_wage_jobs) / AVG(Total) as Share_low_wage
  FROM new_grads
 GROUP BY Major_category
 HAVING Share_low_wage>0.1

## 10. Rounding Results With the ROUND() Function ##

SELECT 
       ROUND(ShareWomen, 4) AS Rounded_women ,
       Major_category
  FROM new_grads LIMIT 10

## 11. Nesting functions ##

SELECT Major_category,
       ROUND(AVG(College_jobs) / AVG(Total), 3) AS Share_degree_jobs
  FROM new_grads
 GROUP BY Major_category
HAVING Share_degree_jobs < 0.3

## 12. Casting ##

SELECT Major_category, CAST(CAST(SUM(Women) AS Float) / CAST(SUM(Total) AS Float) AS Float) AS SW
  FROM new_grads 
  
 GROUP by Major_category
 ORDER BY SW