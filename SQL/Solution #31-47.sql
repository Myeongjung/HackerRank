--31. Revising Aggregations - The Count Function
SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000

--32. Revising Aggregations - The Sum Function
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'

--33. Revising Aggregations - Averages
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'

--34. Average Population
SELECT FLOOR(AVG(POPULATION))
FROM CITY

--35. Japan Population
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN'

--36. Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY

--37. The Blunder
SELECT CEIL(AVG(SALARY)-AVG(REPLACE(SALARY,'0',''))) 
FROM EMPLOYEES

--38. Top Earners
SELECT (SALARY * MONTHS) AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY 1
ORDER BY EARNINGS DESC
LIMIT 1

--39. Asian Population
SELECT SUM(A.POPULATION)
FROM CITY A 
    JOIN COUNTRY B
    ON A.COUNTRYCODE = B.CODE
WHERE B.CONTINENT = 'ASIA'

--40. African Cities
SELECT A.NAME
FROM CITY A 
    JOIN COUNTRY B
    ON A.COUNTRYCODE = B.CODE
WHERE B.CONTINENT = 'AFRICA'

--41. Average Population of Each Continent
SELECT B.CONTINENT, FLOOR(AVG(A.POPULATION))
FROM CITY A 
    JOIN COUNTRY B
    ON A.COUNTRYCODE = B.CODE
GROUP BY CONTINENT

--42. Draw The Triangle 1
SET @i := 21;
SELECT REPEAT('* ', @i := @i - 1)
FROM INFORMATION_SCHEMA.TABLES;

--43. Draw The Triangle 2
SET @i := 0;
SELECT REPEAT('* ', @i := @i + 1)
FROM INFORMATION_SCHEMA.TABLES;
WHERE @i < 20;

--44. The PADS
SELECT CONCAT(NAME, '(', SUBSTR(OCCUPATION, 1,1), ')')
FROM OCCUPATIONS
ORDER BY NAME;

SELECT CONCAT('There are a total of', ' ', COUNT(*), ' ', LOWER(OCCUPATION), 's.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(*), OCCUPATION

--45. Occupations
set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
) temp
group by RowNumber;

SELECT
    GROUP_CONCAT(if(Occupation = 'Doctor', Name, NULL)) AS 'Doctor', 
    GROUP_CONCAT(if(Occupation = 'Professor', Name, NULL)) AS 'Professor', 
    GROUP_CONCAT(if(Occupation = 'Singer', Name, NULL)) AS 'Singer', 
    GROUP_CONCAT(if(Occupation = 'Actor', Name, NULL)) AS 'Actor'
FROM
(
    SELECT a.*,
        (CASE @vOccup WHEN a.OCCUPATION THEN @rownum:=@rownum+1 ELSE @rownum:=1 END) rnum,
        (@vOccup:=a.OCCUPATION) vOccup
    FROM OCCUPATIONS a,(SELECT @vOccup:='', @rownum:=0 FROM DUAL) b
    ORDER BY OCCUPATION, NAME ) c
GROUP BY c.rnum

--46. Binary Tree Nodes
SELECT
    CASE WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
    END
FROM BST
ORDER BY N

--47. New Companies
SELECT  c.company_code, 
    c.founder,
    COUNT(DISTINCT l.lead_manager_code),
    COUNT(DISTINCT s.senior_manager_code),
    COUNT(DISTINCT m.manager_code),
    COUNT(DISTINCT e.employee_code)
FROM  Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e 
WHERE c.company_code = l.company_code 
    AND l.lead_manager_code=s.lead_manager_code 
    AND s.senior_manager_code=m.senior_manager_code 
    AND m.manager_code=e.manager_code 
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;