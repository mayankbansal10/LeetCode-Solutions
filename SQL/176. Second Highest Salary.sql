SELECT MAX(salary) AS SecondHighestSalary
FROM(SELECT salary FROM Employee
MINUS
SELECT MAX(salary)
FROM Employee);