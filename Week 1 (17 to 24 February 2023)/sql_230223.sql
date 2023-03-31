USE `classicmodels`;

SHOW TABLES; # Shows all tables in database

DESCRIBE employees; # Shows details for specific tables. In this case, its the 'employees' table.

/*
Selecting columns to display from data table with specific requirements. 
Using AND, OR, BETWEEN operators. 
*/

SELECT firstname, lastname, jobtitle, officecode FROM employees
	WHERE jobtitle = 'Sales Rep' AND officecode = 1;
    
SELECT firstname, lastname, jobtitle, officecode FROM employees
	WHERE jobtitle = 'Sales Rep' OR officecode = 1
		ORDER BY officecode, lastname;

SELECT firstName, lastName, officeCode FROM employees
	WHERE officeCode BETWEEN 1 AND 3
		ORDER BY officeCode;
        
# SELECT CASE, CASE X is evaluated
SELECT CASE 3
	WHEN 1 THEN 'one'
	WHEN 2 THEN 'two'
	WHEN 3 THEN 'three'
	ELSE 'more' 
  END;

SELECT CASE BINARY'B' 
	WHEN 'A' THEN 1 
    WHEN 'B'THEN 2 
    ELSE 'ENJOY' 
END;

SELECT firstname, lastname, email, officecode, CASE
	WHEN officecode  > 3 THEN 'Shut Down'
	WHEN officecode BETWEEN 1 AND 2 THEN 'Stay Open'
	ELSE 'No changes'
END AS office_status # create a column for output as office_status
FROM employees
ORDER BY office_status;

/*
Working with JOINS (INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, UNION). 
General syntax used for LEFT joins:

SELECT select_list FROM table1
	LEFT JOIN table2 
		ON join_condition;
        
Note: table1 is the left table and table2 is the right table.

The LEFT JOIN clause selects data starting from the left table (table1). 
It matches each row from the left table (table1) with every row from the right table (table2) based on the join_condition.
*/   
     
select * from customers;
# This query uses the LEFT JOIN clause to find all customers and their orders:

SELECT customers.customerNumber, customerName, orderNumber, status FROM customers
	LEFT JOIN orders 
		ON orders.customerNumber = customers.customerNumber
        ORDER BY status;
# Exactly the same query as above in Lines 61 to 63, but using aliases: 
SELECT c.customerNumber, customerName, orderNumber, status FROM customers c
	LEFT JOIN orders o 
		ON c.customerNumber = o.customerNumber
        ORDER BY status;
/*
customers is the left table and orders is the right table.
The LEFT JOIN clause returns all customers including the customers who have no order. 
If a customer has no order, the values in the column orderNumber and status are NULL.

Because both table customers and orders have the same column name ( customerNumber) in the join condition with the equal operator, 
the USING syntax can be used:
*/
SELECT customerNumber, customerName, orderNumber, status FROM customers
	LEFT JOIN orders USING (customerNumber);
 
# LEFT JOIN and LEFT OUTER JOIN are completely the same.
SELECT customerNumber, customerName, orderNumber, status FROM customers
	LEFT OUTER JOIN orders USING (customerNumber);
    
# Using LEFT join to find unmatched rows: We can find customers who have no order using WHERE.
SELECT c.customerNumber, customerName, orderNumber, status FROM customers c
	LEFT JOIN orders o 
		ON c.customerNumber = o.customerNumber
        WHERE orderNumber IS NULL; # Output shows 24 customers who do not have any orders.
        
# Using LEFT join to join three tables: customer, order, and payments
SELECT * FROM payments; #has customerNumber
SELECT * FROM employees; # has employeeNumber
SELECT * FROM customers; # has customerNumber

# employees is the left table, while customers and payments are the right tables.
SELECT firstName AS employee_firstname, lastName AS employee_lastname, customer.customerName, payments.checkNumber, payments.amount from employees #left table
	LEFT JOIN customers 
		ON employeeNumber = salesRepEmployeeNumber # This first LEFT JOIN returns all employees and customers who represented each employee.
    LEFT JOIN payments 
		ON payments.customerNumber = customers.customerNumber # This second LEFT JOIN returns payments of each customer represented by an employee.
    ORDER BY customerName, checkNumber;
/* 
UNION joins two tables with identical columns on top of one another.
The UNION operator selects only distinct values by default. To allow duplicate values, use UNION ALL.
*/
SELECT customers.customername, customers.customernumber, orders.ordernumber FROM orders
	INNER JOIN customers ON orders.customernumber = customers.customernumber
UNION ALL
SELECT customers.customername, customers.customernumber, orders.ordernumber from orders
	INNER JOIN customers USING (customernumber);

# Using NATURAL JOIN. Faster when one key is present. 
SELECT c.customers.customername, customers.customernumber, orders.ordernumber FROM orders
	NATURAL JOIN customers;

# DELETE clause deletes all joins. If alias is used, then aliases must be used with DELETE clause. 
delete o,c from order_new o
	inner join customer_new c on o.customer_id=c.customer_id
	where o.order_id IS NULL;
 
# ORDER BY statements

SELECT firstname, lastname, jobtitle, officecode FROM employees
	WHERE jobtitle = 'Sales Rep' OR officecode = 1
		ORDER BY officecode asc, lastname desc;
        
# Using aggregate functions (e.g. min, max, sum, avg, count, first, last).
SELECT salesRepEmployeeNumber FROM customers; # 122 rows in total, including NULL
SELECT distinct salesRepEmployeeNumber FROM customers; #16 distinct sales rep numbers, including NULL
SELECT salesRepEmployeeNumber, count(*) from customers; 

SELECT max(creditlimit) as "Maximum credit limit" from customers;
SELECT avg(creditlimit) as "Average credit limit" from customers;


# HAVING applies conditions to aggregate functions and works only with GROUP BY statements.  
SELECT country, min(creditlimit) AS "Minimum credit limit" FROM customers
    GROUP BY country
    HAVING min(creditlimit) > 56000
    ORDER BY creditlimit;

# Returns any rows which exceed the average credit limit of 20000.
SELECT *, AVG(creditlimit) AS "averageCreditLimit" FROM customers
    GROUP BY country
    HAVING averageCreditLimit >= 20000 
    ORDER BY averagecreditlimit;
    
# Returns customer numbers > 125 having average payments of more than 24,000. 
SELECT *, AVG(amount) AS 'avg' FROM payments
	WHERE customerNumber > 125
	GROUP BY customerNumber
	HAVING avg > 24000
	ORDER BY customerNumber;