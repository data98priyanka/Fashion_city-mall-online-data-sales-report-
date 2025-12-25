CREATE database mou_sql;
use mou_sql
GO

CREATE TABLE me_class(
                NAMES VARCHAR(50) PRIMARY KEY,
                roll INT UNIQUE
) 
GO

INSERT into me_class(names,roll)
VALUES ('rani', 1),
        ('mohan',21)
GO

SELECT * from me_class
GO