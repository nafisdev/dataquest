## 1. Introducing Joins ##

select * from facts inner JOIN cities on facts.id=cities.facts_id 
limit 10 

## 2. Understanding Inner Joins ##

select c.*,f.name as country_name  from facts as f INNER JOIN cities c on f.id=c.facts_id 
limit 5

## 3. Practicing Inner Joins ##

SELECT f.name as country,c.name as capital_city FROM cities c
INNER JOIN facts f ON f.id = c.facts_id and c.capital=1

## 4. Left Joins ##

SELECT f.name as country, f.population FROM facts f
LEFT JOIN cities c ON f.id = c.facts_id
where c.id is  null

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name as capital_city,f.name as country,c.population  FROM cities c
left join facts f on c.facts_id=f.id
where c.capital=1

order by c.population desc limit 10

## 7. Combining Joins with Subqueries ##

SELECT c.name as capital_city,f.name as country,c.population  FROM (select * from cities
                                                                   where capital=1
                                                                   ) c
left join facts f on c.facts_id=f.id
where c.population >10000000
 
order by c.population desc

## 8. Challenge: Complex Query with Joins and Subqueries ##

select name as country, CAST(pop as FLOAT) as urban_pop,
CAST(population as FLOAT) as total_pop, CAST(pop/population as FLOAT) as urban_pct from 
(Select CAST(SUM(sc.population) as FLOAT) as pop,sf.id,max(sf.name) as name ,CAST(max(sf.population) as FLOAT) as population  from facts sf 
 inner join cities  sc on sf.id = sc.facts_id 
 group by sf.id)
 where urban_pct  > 0.5
order by urban_pct