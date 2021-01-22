--1. Revising the Select Query I
SELECT *
FROM CITY A
WHERE A.POPULATION > 100000
AND A.COUNTRYCODE = 'USA'

--2. Revising the Select Query II
SELECT A.NAME
FROM CITY A
WHERE A.POPULATION > 120000
AND A.COUNTRYCODE = 'USA'

--3. Select All
SELECT *
FROM CITY A

--4. Select By ID
SELECT *
FROM CITY A 
WHERE ID = 1661

--5. Japanese Cities' Attributes
SELECT *
FROM CITY A 
WHERE COUNTRYCODE = 'JPN'

--6. Japanese Cities' Names
SELECT A.NAME
FROM CITY A 
WHERE COUNTRYCODE = 'JPN'

--7. Weather Observation Station 1
SELECT A.CITY, A.STATE
FROM STATION A

--8. Weather Observation Station 2
SELECT ROUND(SUM(A.LAT_N),2), ROUND(SUM(A.LONG_W), 2)
FROM STATION A

--9. Weather Observation Station 3
SELECT DISTINCT(A.CITY)
FROM STATION A
WHERE A.ID%2 = 0

--10. Weather Observation Station 4
SELECT COUNT(A.CITY) - COUNT(DISTINCT(CITY))
FROM STATION A

--11. Weather Observation Station 5
SELECT CITY, LENGTH(CITY)
  FROM STATION
  ORDER BY LENGTH(CITY), CITY
  LIMIT 1;

SELECT CITY, LENGTH(CITY)
  FROM STATION
  ORDER BY LENGTH(CITY) DESC, CITY
  LIMIT 1;
  
--12. Weather Observation Station 6
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) IN ('a','i','e','o','u')
  
--13. Weather Observation Station 7
SELECT DISTINCT CITY 
FROM STATION 
WHERE RIGHT(CITY,1) IN ('a','i','e','o','u')

--14. Weather Observation Station 8
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) IN ('a','i','e','o','u')
AND RIGHT(CITY,1) IN ('a','i','e','o','u')

--15. Weather Observation Station 9
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u')

--16. Weather Observation Station 10 
SELECT DISTINCT CITY 
FROM STATION 
WHERE RIGHT(CITY,1) NOT IN ('a','i','e','o','u')

--17. Weather Observation Station 11
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u')
OR RIGHT(CITY,1) NOT IN ('a','i','e','o','u');

--18. Weather Observation Station 12 
SELECT DISTINCT CITY 
FROM STATION 
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u')
AND RIGHT(CITY,1) NOT IN ('a','i','e','o','u');
