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