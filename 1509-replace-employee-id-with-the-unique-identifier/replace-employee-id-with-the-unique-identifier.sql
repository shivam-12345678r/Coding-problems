# Write your MySQL query statement below
select unique_id ,name
from employees as e1
left join employeeuni as e2
on e1.id = e2.id;