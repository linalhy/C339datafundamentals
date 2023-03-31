USE linalau;

CREATE TABLE student3(
	id  INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR (100) NOT NULL,
    first_name CHAR (100),
    last_name CHAR (100),
    gender CHAR (1) CHARACTER SET ASCII,
    birth_date DATE,
    todays_date DATE,
    age INT);
    
SHOW CHARACTER SET; #shows different character sets available
   
SELECT * FROM student3;

INSERT INTO student3
	(id, username, first_name, last_name, gender, birth_date)
VALUES 
	(1, "lina.lau", "Lina", "Lau", "F", "1992-03-04"),
	(2, "pepe.lol", "Pepe", "Lol", "M", "2004-05-12"),
	(3, "abc.def", "Abc", "Def", "F", "1997-12-14"),
    (4, "fried.chicken", "Fried", "Chicken", "M", "1934-07-15");
    
UPDATE student3 SET todays_date = current_date();  

#SELECT * FROM student3 WHERE birth_date LIKE '%%04%%';
#SELECT * FROM student3 WHERE (id between 2 and 4) AND (username LIKE '%%in%%';
#DATEDIFF?



SELECT student3.id, (TIMESTAMPDIFF(year, birth_date, NOW())) AS age FROM student3;
ALTER TABLE student3 MODIFY COLUMN age INT; # Change type of column

UPDATE student3 AS s3
	INNER JOIN( 
		SELECT student3.id, (TIMESTAMPDIFF(year, birth_date, NOW())) AS calculated_age FROM student3) AS r 
	ON s3.id = r.id 
	SET s3.age = r.calculated_age;

SELECT current_date() - birth_date AS age FROM student3;
#SELECT current_date(), birth_date, COALESCE(current_date() - birth_date) AS age FROM student3;

#ALTER TABLE student3 
#	MODIFY COLUMN age DECIMAL (2, 1);

#adding multiple new columns to student2    
#ALTER TABLE student2 
#	ADD date DATE,
#    ADD todays_date DATE,
#    ADD age INT;   

## Creating users and granting/revoking permissions ##
CREATE USER linalau@localhost IDENTIFIED BY 'linalau';
SELECT USER FROM mysql.user;
GRANT ALL PRIVILEGES ON *.* TO linalau@localhost; #*.* means on all schemas and all tables
GRANT CREATE, SELECT, INSERT ON *.* TO linalau@localhost;
FLUSH PRIVILEGES; #applies changes

SHOW GRANTS FOR linalau@localhost;
DROP USER jineshtest@localhost; #remove user from database
SELECT USER, HOST, account_locked, password_Expired FROM mysql.user;
SELECT USER, HOST, db, command FROM information_schema.processlist;

SELECT USER();

USE mysql;
UPDATE USER SET authentication_string = PASSWORD('XX') WHERE USER ='linalau' AND HOST = 'localhost'; #change password for user 'linalau'
FLUSH PRIVILEGES;

## Copying tables ##
SELECT * FROM student3;

CREATE TABLE student4
	SELECT id,username,gender FROM student3;
SELECT * FROM student4;

CREATE TABLE student12
	SELECT * FROM student10;

