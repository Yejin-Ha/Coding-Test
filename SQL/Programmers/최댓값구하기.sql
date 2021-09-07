-- 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.
SELECT * 
FROM (SELECT DATETIME 
     FROM ANIMAL_INS
     ORDER BY DATETIME DESC)
-- ROWNUM을 사용하여 상위의 1개의 데이터만 조회한다.
WHERE ROWNUM = 1;
