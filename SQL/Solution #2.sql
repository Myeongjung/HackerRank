--1. Weather Observation Station 13
SELECT TRUNCATE(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345

--2. Weather Observation Station 14
SELECT TRUNCATE(MAX(LAT_N),4) 
FROM STATION
WHERE LAT_N < 137.2345

--3. Weather Observation Station 15
SELECT ROUND(MAX(LONG_W), 4)
FROM STATION
WHERE LAT_N < 137.2345
GROUP BY LAT_N
ORDER BY LAT_N DESC
LIMIT 1

--4. Weather Observation Station 16
SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780

--5. Weather Observation Station 17
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (
    SELECT MIN(LAT_N) 
    FROM STATION 
    WHERE LAT_N>38.7780)
	
--6. Weather Observation Station 18

--7. Weather Observation Station 19

--8. Weather Observation Station 20