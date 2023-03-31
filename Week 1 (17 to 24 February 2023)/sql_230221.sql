/*
SQL class - February 21, 2023.
*/

USE linalau;

CREATE TABLE vehicle(
	vehicle_no VARCHAR(20) PRIMARY KEY,
	model_name VARCHAR (45),
	price DECIMAL (10,2),
	sell_price DECIMAL (10,2));

INSERT INTO vehicle(vehicle_no, model_name, price, sell_price)
	VALUES
    ('ABC123', 'BMW', 54203.67, 18797),
	('DEF456','Audi', 64778.34, 48797),
	('GHI789','Opel',67647.23, 98797);

SELECT * FROM vehicle;

SHOW ENGINES;

USE mysql;
SELECT TABLE_NAME, ENGINE FROM information_schema.tables
	WHERE TABLE_NAME = 'vehicle';
REPAIR TABLE vehicle;

REPAIR TABLE vehicle QUICK EXTENDED; # quick extended will repair all tables related to vehicle, not just vehicle.

USE linalau;
ALTER TABLE vehicle ENGINE = 'MyISAM'; # MyISAM uses less disk space, good for inserts and select statements.
ALTER TABLE vehicle ENGINE = 'InnoDB';

SHOW TABLE STATUS; # shows the tables created in database along with all information

/*
How to add columns into existing table.
*/


ALTER TABLE vehicle 
	ADD COLUMN vehicle_lr_number VARCHAR (100) NOT NULL FIRST; # adds vehicle_lr_number as first column
    
ALTER TABLE vehicle 
	ADD COLUMN vehicle_colour VARCHAR (100) NOT NULL AFTER sell_price; # adds vehicle_colour as a column after sell_price
    
ALTER TABLE vehicle 
	ADD COLUMN tyre_type VARCHAR (100) NOT NULL AFTER sell_price; 

ALTER TABLE vehicle 
	ALTER model_name SET DEFAULT 'The car is very nice';
    
ALTER TABLE vehicle
	DROP COLUMN vehicle_lr_number; # drops column
    
#ALTER TABLE vehicle
#	ALTER vehicle_no SET DEFAULT ' ';
#
#INSERT INTO vehicle(tyre_type, vehicle_colour)
#	VALUES
#    ('winter', 'red'),
#	('summer', 'black'),
#	('winter', 'green');
/*
How to view columns that satisfy certain requirements
*/

SHOW COLUMNS FROM vehicle LIKE  'v%'; # returns columns starting with the alphabet 'v'
SHOW COLUMNS FROM vehicle LIKE  '%r'; # returns columns ending with the alphabet 'r'
SHOW FULL COLUMNS FROM vehicle LIKE 'v%';

/*
How to view columns that satisfy certain requirements
*/
SELECT * FROM vehicle;

ALTER TABLE vehicle
	RENAME COLUMN old_column_name TO new_column_name; # changing only column name without affecting rows.
    
ALTER TABLE vehicle 
	CHANGE COLUMN DESCRIPTION model_name VARCHAR (400); # more powerful 
	
/*
How to view columns that satisfy certain requirements
*/

SELECT * FROM vehicle;
CREATE VIEW vehicle_info 
	as select vehicle_no, car_price, vehicle_colour where model_name = 'Audi';
DROP VIEW vehicle_info;

/*
Restricting/enabling tables for other users by using LOCK TABLES and UNLOCK TABLES
*/
LOCK TABLES vehicles READ; # locks tables from editting, but reading remains possible
UNLOCK TABLES;

SELECT connection_id() # command to check connection ID

