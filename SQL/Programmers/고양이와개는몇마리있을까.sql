-- 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

SELECT ANIMAL_TYPE, COUNT(*)
FROM ANIMAL_INS
-- ANIMAL_TYPE이 Cat / Dog 인 데이터만 출력
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
-- Groupby를 통해 cat과 dog로 묶는다.
GROUP BY ANIMAL_TYPE
-- 정렬을 통해 cat이 dog보다 먼저 조회되도록 설정
ORDER BY ANIMAL_TYPE;
