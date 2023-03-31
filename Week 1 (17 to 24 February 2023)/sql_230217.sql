CREATE DATABASE linalau;
SHOW DATABASES;
USE linalau;

#creating table named student
CREATE TABLE student(
id INT, 
username VARCHAR (100));
 
ALTER TABLE student RENAME COLUMN country to motherland;

SELECT * FROM student;
INSERT INTO student
	(id, username, motherland)
VALUES 
	(1 ,"lina.lau", "Malaysia"), 
	(2, "abc.def", "Germany"),
    (3, "john.doe", "Spain"),
    (4, "jane.right", "Japan");
ALTER TABLE student ADD PRIMARY KEY(id);
INSERT INTO student 
	(id, username, motherland)
VALUES
	(5, "fried.chicken", "Turkey"),
    (6, "baked.beans", "Australia");
DESCRIBE TABLE student;

#DELETE FROM student WHERE id="4"; #deleting rows

#creating table named personal_details
CREATE TABLE personal_details(
id INT,
username VARCHAR (100),
first_name VARCHAR (100),
last_name VARCHAR (100),
birth_date DATE,
postcode VARCHAR (100));

SELECT * FROM personal_details;
#DELETE FROM personal_details WHERE id=1;
#SELECT * FROM personal_details ORDER BY id;

INSERT INTO personal_details 
	(id, username, first_name, last_name, birth_date, postcode)
VALUES 
	(1, "lina.lau", "Lina", "Lau", "1992-03-04", "12345"),
	(2, "pepe.lol", "Pepe", "Lol", "1945-12-21", "13567"),
	(3, "abc.def", "Abc", "Def", "2003-01-22", "54378");
ALTER TABLE personal_details ADD PRIMARY KEY (id);
INSERT INTO personal_details 
	(id, username, first_name, last_name, birth_date, postcode)
VALUES
	(4, "fried.chicken", "Fried", "Chicken", "1945-04-03", "95832"),
    (5, "baked.beans", "Baked", "Beans", "2003-04-17", "46423");
    
ALTER TABLE personal_details ADD university VARCHAR (100); #adding new column named university to personal_details table
	
UPDATE personal_details 
	SET university = "University of Melon" WHERE id=1;


#INSERT INTO table_name1 (columns) SELECT columns FROM table_name2; copying row data from one sql table to another
#truncate table #deletes all rows in a table. returns a table without rows. 
#describe table personal_details; #describe table provides more information on the table itself. describe provides general information on the table.

SHOW TABLES; #shows tables in database

