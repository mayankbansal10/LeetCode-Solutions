SELECT d.name AS Department, e1.name AS Employee, e1.salary as Salary
FROM Employee e1
JOIN Department d 
ON e1.Departmentid = d.Id
WHERE 3 > (SELECT COUNT(DISTINCT e2.Salary)
          FROM Employee e2
          WHERE e2.salary > e1.salary
          AND e1.DepartmentId = e2.DepartmentId)