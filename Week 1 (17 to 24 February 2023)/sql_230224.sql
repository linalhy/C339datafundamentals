/*
February 24, 2023
Regular expressions
*/

# REGEXP = RLIKE
USE `classicmodels`;
SELECT * FROM employees;

# ^ I want carat to check either 'a', 'b', 'c' or 'd' to be the beginning of the string
SELECT employeeNumber, firstName, lastName FROM employees 
	WHERE firstName REGEXP '^[abcd]'
    ORDER BY firstName; 
    
# Returns all names ending with 'n'   
SELECT employeeNumber, firstName, lastName FROM employees 
	WHERE firstName REGEXP 'n$'
    ORDER BY firstName; 
    
# Returns all names ending with 1 letter where 'e', 'm', or 'i'.
SELECT employeeNumber, firstName FROM employees
	WHERE firstName REGEXP '^.*[emi]$'
    ORDER BY firstName;  
    
# Returns all names ending with the last two charcters (i.e. 'm' and 'i')     
SELECT employeeNumber, firstName FROM employees
	WHERE firstName REGEXP '^.*[emi]{2}$'
    ORDER BY firstName; 
    
# Returns all names NOT ending with 2 letters where 'e', 'm', or 'i'.     
SELECT employeeNumber, firstName, lastName FROM employees
	WHERE firstName REGEXP '^.*[^emi]{2}$'
    ORDER BY firstName; 
    
# Returns all names with 5 letters.    
SELECT employeeNumber, firstName, lastName FROM employees 
	WHERE firstName REGEXP '^\\w{5}$'
    ORDER BY firstName;
    
# Returns all names that contain the letter 'i'.    
SELECT employeeNumber, firstName, lastName FROM employees 
	WHERE firstName REGEXP 'i'
    ORDER BY firstName; 
 
# First parameter
SELECT REGEXP_LIKE('A', '[A-Z]', 'C') AS check_;

# In 'pink', replace 'pi' with 'X'. Output will be 'Xnk'
SELECT regexp_replace('pink', 'pi', 'X') AS renamed;

/*
REGEXP_SUBSTR (expression, pattern [, position[, occurrence[, match_type]]])  
Returns the substring of the string expr that matches the regular expression specified by the pattern pat, NULL if there is no match.
If expr or pat is NULL, the return value is NULL.
*/

SELECT regexp_substr('nice potato chip', '[a-z]+', 1, 3) AS renamed;

SELECT employeeNumber, firstName, lastName FROM employees 
	where firstName rlike 'r$|n$';

/*
INDEXING.
*/
select * from employees;

# Creating index
show index from employees where column_name = 'firstName'; # No index
create index firstName_index on employees(firstName); # Creates an index for firstName
SHOW INDEX FROM employees WHERE COLUMN_NAME = 'firstName'; # Now firstName has an index
SELECT * FROM employees WHERE firstName  = 'Jeff';

# Deleting index
ALTER TABLE employees
	DROP INDEX firstName_index;
DROP INDEX firstName_index ON employees; # Another way to delete an index
SHOW INDEX FROM employees WHERE COLUMN_NAME = 'firstName'; # Now there is no index again for firstName.


CREATE TABLE example_temp (
	id INT AUTO_INCREMENT PRIMARY KEY,
	firstName VARCHAR (250) NOT NULL,
	age INT NOT NULL);

INSERT INTO example_temp(firstName, age) VALUES ('John',25);
INSERT INTO example_temp(firstName, age) VALUES ('Jane',30);

SELECT * FROM example_temp;
SELECT last_insert_id(); # The last_insert_id() function returns the AUTO_INCREMENT id of the last row that has been inserted or updated in a table.

# Partitioning

SELECT * FROM orders;

CREATE TABLE orders_partition(
	orderNumber INT NOT NULL AUTO_INCREMENT,
	order_date DATE NOT NULL,
	PRIMARY KEY(orderNumber, order_date))
PARTITION BY RANGE(YEAR(order_date))(
		PARTITION p0 VALUES LESS THAN (2003),
		PARTITION p1 VALUES LESS THAN (2004),
		PARTITION p2 VALUES LESS THAN MAXVALUE);

INSERT INTO orders_partition (orderNumber, order_date)
	SELECT orderNumber, orderDate FROM orders;

SELECT * FROM orders_partition WHERE order_date ='2004-05-11';
EXPLAIN SELECT * FROM orders_partition WHERE order_date='2004-05-11'; 

SELECT *, ROW_NUMBER() OVER (PARTITION BY order_date) AS row_num 
	FROM orders_partition 
    ORDER BY order_date; 

# RANK() function
SELECT * FROM payments; #has customerNumber
SELECT * FROM customers; # has customerNUmber
SELECT * FROM orderDetails; # has customerNumber

CREATE TABLE customer_order 
SELECT customerNumber, customerName, sum(p.amount) AS totalAmount FROM customers c
		JOIN payments p USING (customerNumber)
        JOIN orders o USING (customerNumber)
        GROUP BY customerNumber;
SELECT * FROM customer_order;

# RANK() used to rank totalAmount of customers. DENSE_RANK() can be used when there are duplicate ranks (e.g. two position #2)
SELECT *, RANK() OVER (ORDER BY totalAmount DESC) AS amount_rank from customer_order;

# Find out which customer is at rank number 10 with the total amount.
SELECT customerName, totalAmount, amount_rank 
	FROM (SELECT *, RANK() OVER (ORDER BY totalAmount DESC) AS amount_rank from customer_order) AS ranked_amount 
    WHERE amount_rank = 10;

