SELECT salary * months AS earnings, COUNT(*)
FROM EMPLOYEE
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1
