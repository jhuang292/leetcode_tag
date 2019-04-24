# Write your MySQL query statement below
SELECT tb1.pay_month, tb1.department_id, CASE 
                                            WHEN tb1.average_salary > tb2.average_salary THEN 'higher'
                                            WHEN tb1.average_salary = tb2.average_salary THEN 'same'
                                            ELSE 'lower'
                                         END AS comparison
FROM (
        SELECT DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month, e.department_id, AVG(amount) AS average_salary
        FROM salary s LEFT JOIN employee e ON s.employee_id = e.employee_id
        GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m'), e.department_id 
        ORDER BY DATE_FORMAT(s.pay_date, '%Y-%m') DESC, e.department_id
            ) tb1 LEFT JOIN (
                            SELECT DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month, AVG(amount) AS average_salary
                            FROM salary s LEFT JOIN employee e ON s.employee_id = e.employee_id 
                            GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m')
                                ) tb2 ON tb1.pay_month = tb2.pay_month;                             
