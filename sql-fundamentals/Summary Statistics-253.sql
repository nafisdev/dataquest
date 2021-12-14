## 2. A Simple Question ##

SELECT MIN(Unemployment_rate) from recent_grads 

## 3. Aggregate Functions ##

SELECT SUM(Total) from recent_grads 

## 4. Order of Execution ##

SELECT COUNT(Major)
  FROM recent_grads
 WHERE ShareWomen < 0.5;

## 5. Missing Values ##

SELECT COUNT(Rank), COUNT(Major_code), COUNT(Major), COUNT(Major_category), COUNT(Total), COUNT(Sample_size), COUNT(Men), COUNT(Women), COUNT(ShareWomen), COUNT(Employed), COUNT(Full_time_year_round), COUNT(Unemployed), COUNT(Unemployment_rate), COUNT(Median), COUNT(P25th), COUNT(P75th), COUNT(College_jobs), COUNT(Non_college_jobs), COUNT(Low_wage_jobs)
  FROM recent_grads;
  SELECT COUNT(*),
COUNT(Unemployment_rate)
  FROM recent_grads

## 6. Combining Multiple Aggregation Functions ##

SELECT AVG(Total), MIN(Men), MAX(Women)
  FROM recent_grads;

## 7. Customizing the Results ##

  SELECT COUNT(*) as 'Number of Majors',
MAX(Unemployment_rate) as 'Highest Unemployment Rate'
  FROM recent_grads

## 8. Counting Unique Values ##

SELECT COUNT(DISTINCT Major) AS unique_majors,
COUNT(DISTINCT Major_category) AS unique_major_categories,
COUNT(DISTINCT Major_code) AS unique_major_codes
  FROM recent_grads;

## 10. String Functions and Operations ##

SELECT 'Major: '||LOWER(Major) as Major,
       Total, Men, Women, Unemployment_rate,
       LENGTH(Major) AS Length_of_name
  FROM recent_grads
 ORDER BY Unemployment_rate DESC
 -- LIMIT 3;

## 11. Performing Arithmetic in SQL ##

SELECT Major,Major_category, P75th - P25th AS quartile_spread
  FROM recent_grads
  order by quartile_spread
 LIMIT 20;