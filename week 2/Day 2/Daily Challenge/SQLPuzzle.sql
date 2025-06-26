/*
CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')


SELECT * FROM FirstTab
-- OUTPUT
5	"Pawan"
6	"Sharlee"
7	"Krish"
	"Avtaar"
	

CREATE TABLE SecondTab (
    id integer 
)


INSERT INTO SecondTab VALUES
-- OUTPUT
(5),
(NULL)


SELECT * FROM SecondTab
-- OUTPUT
"id"
5
null

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- OUTPUT
"count"
0

CREATE TABLE ThirdTab (
    id integer ,
	last_name varchar(25)
	
	
)

INSERT INTO ThirdTab VALUES
(5,
NULL),(1,
'salma'),(NULL,
'hafssa')

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM ThirdTab WHERE id IS NULL )
-- OUTPUT
0

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- OUTPUT
 2
 
SELECT COUNT(*) FROM FirstTab  WHERE id NOT IN ( SELECT id FROM SecondTab )
-- OUTPUT
0
*/
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- OUTPUT
2
