--48. The Report
SELECT (CASE WHEN B.GRADE<8 THEN NULL ELSE A.NAME END), B.GRADE, A.MARKS
FROM STUDENTS A, GRADES B
WHERE A.MARKS BETWEEN B.MIN_MARK AND B.MAX_MARK
ORDER BY B.GRADE DESC, A.NAME


--49. Top Competitors
SELECT H.HACKER_ID, H.NAME
FROM SUBMISSIONS S
    JOIN CHALLENGES C
    ON S.CHALLENGE_ID = C.CHALLENGE_ID
    JOIN DIFFICULTY D
    ON C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL 
    JOIN HACKERS H
    ON S.HACKER_ID = H.HACKER_ID
WHERE S.SCORE = D.SCORE
GROUP BY H.HACKER_ID, H.NAME
  HAVING COUNT(H.HACKER_ID) > 1
ORDER BY COUNT(H.HACKER_ID) DESC, H.HACKER_ID ASC


--50. Print Prime Numbers
DELIMITER $$
CREATE PROCEDURE getPrime(IN n int, OUT result varchar(16383))
BEGIN
DECLARE j, i, isPrime int;
SET j := 2; 
SET result := ' '; 
WHILE(j < n) DO
    SET i := 2;
    SET isPrime := 0;

    WHILE(i <= j) DO
        IF(j%i = 0)THEN
            SET isPrime := isPrime + 1;
        END if;
    SET i := i + 1; /* Increment i */
    END WHILE;

    IF (isPrime = 1) THEN
        SET result:=concat(result, j, '&'); 
    END IF;

    SET j := j + 1;
end while;
End $$

call getPrime(1000, @result);
select substr(@result, 1, length(@result)-1);


--51. Ollivander's Inventory
SELECT W.ID, P.AGE, W.COINS_NEEDED, W.POWER
FROM WANDS W JOIN WANDS_PROPERTY P 
    ON W.CODE = P.CODE
WHERE P.IS_EVIL = 0 
  AND W.COINS_NEEDED = (
      SELECT MIN(COINS_NEEDED) 
      FROM WANDS 
      WHERE CODE = W.CODE
        AND POWER = W.POWER)
ORDER BY W.POWER DESC, P.AGE DESC


--52. Challenges
SELECT C.HACKER_ID, H.NAME, COUNT(C.HACKER_ID) as CNT
FROM HACKERS H JOIN CHALLENGES C
    ON H.HACKER_ID = C.HACKER_ID
GROUP BY C.HACKER_ID, H.NAME
HAVING CNT = (SELECT MAX(TMP.C_CNT) 
                   FROM (SELECT COUNT(HACKER_ID) AS C_CNT
                         FROM CHALLENGES
                        GROUP BY HACKER_ID
                        ORDER BY HACKER_ID)TMP)
       OR CNT IN (SELECT TMP2.CNT
             FROM (SELECT COUNT(*) AS CNT 
                   FROM CHALLENGES
                   GROUP BY HACKER_ID) TMP2
             GROUP BY TMP2.CNT
             HAVING COUNT(TMP2.CNT) = 1)
ORDER BY CNT DESC, C.HACKER_ID

--53. Contest Leaderboard
SELECT S.HACKER_ID, H.NAME, SUM(S.SCORE) AS TOTAL_SCORE
FROM HACKERS H JOIN (SELECT HACKER_ID, MAX(SCORE) AS SCORE
                     FROM SUBMISSIONS 
                     GROUP BY CHALLENGE_ID, HACKER_ID) S
    ON H.HACKER_ID = S.HACKER_ID
GROUP BY H.HACKER_ID, H.NAME
    HAVING TOTAL_SCORE != 0
ORDER BY TOTAL_SCORE DESC, S.HACKER_ID

--54. SQL Project Planning
SET sql_mode = '';
SELECT START_DATE, END_DATE
FROM 
    (SELECT START_DATE FROM PROJECTS WHERE START_DATE NOT IN (SELECT END_DATE FROM PROJECTS)) A,
    (SELECT END_DATE FROM PROJECTS WHERE END_DATE NOT IN (SELECT START_DATE FROM PROJECTS)) B 
WHERE START_DATE < END_DATE
GROUP BY START_DATE 
ORDER BY DATEDIFF(END_DATE, START_DATE), START_DATE

--55. Placements
Select S.NAME
FROM ( STUDENTS S join FRIENDS F Using(ID)
       join PACKAGES P1 on S.ID=P1.ID
       join PACKAGES P2 on F.FRIEND_ID=P2.ID)
Where P2.SALARY > P1.SALARY
Order By P2.SALARY

--56. Symmetric Pairs
SELECT f1.x, f1.y
FROM FUNCTIONS f1 INNER JOIN FUNCTIONS f2 ON f1.y = f2.x
WHERE f1.x = f2.y
GROUP BY f1.x, f1.y
HAVING COUNT(f1.x) > 1 OR f1.x < f1.y
ORDER BY f1.x

--57. Interviews
SELECT A.contest_id, A.hacker_id, A.name, SUM(tb1.ts), SUM(tb1.tas), SUM(tb2.tv), SUM(tb2.tuv)
FROM Contests A 
JOIN Colleges B ON A.contest_id = B.contest_id
JOIN (
		SELECT C.college_id, SUM(S.total_submissions) AS ts, SUM(S.total_accepted_submissions) AS tas
		FROM Challenges C JOIN Submission_Stats S ON C.challenge_id = S.challenge_id
		GROUP BY C.college_id) tb1 
	ON B.college_id = tb1.college_id
JOIN (
		SELECT C.college_id, SUM(V.total_views) AS tv, SUM(V.total_unique_views) AS tuv
		FROM Challenges C 
		JOIN View_Stats V 
		ON C.challenge_id = V.challenge_id
		GROUP BY C.college_id) tb2 
	ON tb2.college_id = B.college_id
GROUP BY A.contest_id, A.hacker_id, A.name
HAVING SUM(tb1.ts)!=0 or SUM(tb1.tas)!=0 or SUM(tb2.tv)!=0 or SUM(tb2.tuv)!=0
ORDER BY A.contest_id

--58. 15 Days of Learning SQL
SELECT submission_date,
(SELECT COUNT(DISTINCT hacker_id)  
 FROM Submissions s2  
 WHERE s2.submission_date = s1.submission_date 
   AND (
       SELECT COUNT(DISTINCT s3.submission_date) 
       FROM Submissions s3 
       WHERE s3.hacker_id = s2.hacker_id 
         AND s3.submission_date < s1.submission_date) = dateDIFF(s1.submission_date,'2016-03-01')),
(SELECT hacker_id  
 FROM submissions s2 
 WHERE s2.submission_date = s1.submission_date 
 GROUP BY hacker_id 
 ORDER BY COUNT(submission_id) DESC, hacker_id 
 LIMIT 1) AS shit,
(SELECT name 
 FROM hackers 
 WHERE hacker_id = shit)
FROM (SELECT DISTINCT submission_date from submissions) s1
GROUP BY submission_date
