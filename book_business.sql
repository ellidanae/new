DROP DATABASE IF EXISTS `book industry`;
CREATE DATABASE IF NOT EXISTS `book industry`; 
USE `book industry`;

-- --------------------------------------
--  TABLE AUTHORS
-- --------------------------------------
CREATE TABLE `Authors` (
	`AuthorID` 			int NOT NULL AUTO_INCREMENT,
	`FirstName` 		varchar (20) NOT NULL ,
	`LastName` 			varchar (20) NOT NULL ,		
	`Address` 			varchar (45) NULL ,
	`Phone` 		    varchar (24) NULL ,
  	PRIMARY KEY (`AuthorID`),	
	INDEX `AuthorID` (`AuthorID` ASC),
	INDEX `LastName` (`LastName` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;


-- --------------------------------------
--  TABLE Publishers
-- --------------------------------------
CREATE TABLE `Publishers` (
	`PublisherID` 			int NOT NULL AUTO_INCREMENT,
	`Name` 					varchar (45) NOT NULL ,
	`Address` 			varchar (45) NULL ,
	`Phone` 		    varchar (24) NULL ,
  	PRIMARY KEY (`PublisherID`),	
	INDEX `PublisherID` (`PublisherID` ASC),
	INDEX `Name` (`Name` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;


-- --------------------------------------
--  TABLE Editors
-- --------------------------------------
CREATE TABLE `Editors` (
	`EditorID` 			int NOT NULL AUTO_INCREMENT,
    `BookID`            int NOT NULL,
	`FirstName` 		varchar (20) NOT NULL ,
	`LastName` 			varchar (20) NOT NULL ,		
	`Address` 			varchar (45) NULL ,
	`Phone` 		    varchar (24) NULL ,
  	PRIMARY KEY (`EditorID`),	
	INDEX `EditorID` (`EditorID` ASC),
	INDEX `LastName` (`LastName` ASC)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;





-- --------------------------------------
--  TABLE BOOKS
-- --------------------------------------
CREATE TABLE `Books` (
    `BookID`            int NOT NULL AUTO_INCREMENT,
	`AuthorID` 			int NOT NULL,
    `PublisherID`		int NOT NULL,
    `EditorID`			int NOT NULL,
	-- `FirstName` 		varchar (20) NOT NULL ,
-- 	`LastName` 			varchar (20) NOT NULL ,	
    `Prise`	        	decimal(13,2),
    `Title`             varchar (60) NULL,
    `Genre`             varchar (60) NULL,
    `PubDate`   		date NULL,
    `Order`   			int,
    PRIMARY KEY (`BookID`), 
	INDEX `BookID` (`BookID` ASC),
    FOREIGN KEY (`PublisherID`) REFERENCES `Publishers` (`PublisherID`)
         ON DELETE NO ACTION
         ON UPDATE NO ACTION,   
    FOREIGN KEY (`EditorID`) REFERENCES `Editors` (`EditorID`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION, 
    FOREIGN KEY (`AuthorID`) REFERENCES `Authors` (`AuthorID`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION 

) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

