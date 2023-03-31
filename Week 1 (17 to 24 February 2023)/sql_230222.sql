/*
SQL class - February 22, 2023.
*/
USE linalau;

select * from vehicle where (price > 47647 and model_name like 'mercedes%' ) or (sell_price > 18000);

CREATE TABLE food(
	food_id int PRIMARY KEY, 
    food_name VARCHAR (100),
    food_price DECIMAL (3,2),
    spicy BOOLEAN,
    sour BOOLEAN,
    bitter BOOLEAN,
    sweet BOOLEAN);
 
/*
Boolean terms (i.e. true or false)
*/ 
 
INSERT INTO food(food_id, food_name, food_price, spicy, sour, bitter, sweet)
	VALUES
    ('1', 'chicken curry', 5.65, true, false, false, false),
	('2','cherry', 6.50, false, true, false, true),
	('3','chips', 3.57, true, false, false, false),
    ('4', 'ham', 9.45, false, false, false, false),
    ('5', 'noodle', 7.34, true, true, false, true);

SELECT * FROM food;    
DESCRIBE food;
SHOW FULL COLUMNS FROM food;

SELECT * FROM food WHERE sweet IS TRUE;

SELECT * FROM food WHERE pass != TRUE; # != denotes 'is not'. it is the same as the 'is not' statement.

#% wild card of any number
# _ only on one unknown character

/*
ANY clause
*/ 

CREATE TABLE customer(
	customer_id INT PRIMARY KEY, 
    username VARCHAR (100),
    first_name VARCHAR (100),
    last_name VARCHAR (100),
    email VARCHAR (100),
    phone_number INT (20));
 
 INSERT INTO customer
	VALUES
		('1', 'lina.lau', 'Lina', 'Lau', 'lina.lau@company.com', '0145948329'),
		('2','fried.chicken', 'Fried', 'Chicken', 'fried.chicken@company.com', '0149382085'),
		('3','big.potato', 'Big', 'Potato', 'big.potato@company.com', '0145820649'),
		('4', 'ham.burger', 'Ham', 'Burger', 'ham.burger@company.com', '0140478239'),
		('5', 'apple.tree', 'Apple', 'Tree', 'apple.tree@company.com', '0145328402'); 
SELECT * FROM customer;

CREATE TABLE order_table(
	order_id INT PRIMARY KEY,
    customer VARCHAR (100),
    order_date DATE,
    order_value DECIMAL (10,2));
INSERT INTO order_table
	VALUES 
		('1', 'lina.lau','2019-08-30', 745456.23), 
		('2', 'fried.chicken', '2022-09-13', 824052.56), 
        ('3', 'big.potato', '2022-04-23', 373623.28),
        ('4', 'ham.burger', '2022-04-23', 694835.28),
        ('5', 'apple.tree', '2022-04-23', 96482.28);
SELECT * FROM order_table;

#To find all info on orders that were more than the average order.
SELECT * FROM order_table
	WHERE order_value > ANY(SELECT AVG(order_value) FROM order_table); 

#To find all info on orders that were less than the average order.
SELECT * FROM order_table
	WHERE order_value < ANY(SELECT AVG(order_value) FROM order_table); 

#To find all info on orders that were not equal to the average order.
SELECT * FROM order_table
	WHERE order_value <> ANY(SELECT AVG(order_value) FROM order_table); 
    
#SELECT first_name, last_name, customer_id FROM customer 
#	WHERE (customer_id = any(select customer_id from order_table));

#	select * from order_table where customer_id = order_table.customer_id);

select * from customer where username is not NULL; #returns customers where their username is not null
select * from customer where username is NULL;
select * from customer where customer_id between 2 and 4;

select * from order_table
	where order_date between cast('2018-01-01' as date) and cast('2022-04-30' as date);
    
/*
String comparison using strcmp() function
*/ 
select if('A' > 'B','yes','no');
select strcmp('aaaa', 'lina'); #returns -1
select if(strcmp('Lina','coconut') = 0,'equal','not equal');
select if(251 = 251,'correct','wrong');

SELECT STRCMP("lina", "lina");  # 0
SELECT STRCMP("linaaaa", "lina"); # 1 
SELECT STRCMP("lina", "linaaaa"); #-1

SELECT "lina"="lina";  #1
SELECT "linaaaa"="lina"; #0
SELECT "lina"="linaaaa"; #0

#If first expression is not NULL, IFNULL() returns first expression; otherwise it returns second expression.
SELECT ifnull('potato', 'chips');
SELECT ifnull(null, 'chips');

# The NULLIF() function returns NULL if two expressions are equal, otherwise it returns the first expression.
SELECT nullif('potato', 'potato'); 
SELECT nullif('potato', 'chips');

