USE `book industry`;


INSERT INTO `Authors` VALUES(1,1,'Publo','Neruda', 'NULL');
INSERT INTO `Authors` VALUES(2,2,'Ernest ','Hemingway', 'NULL');
INSERT INTO `Authors` VALUES(3,3,'Ernest ','Hemingway', 'NULL');
INSERT INTO `Authors` VALUES(4,4,'Edgard Allan','Poe', 'NULL');
INSERT INTO `Authors` VALUES(5,5,'Jane','Austen', 'NULL');


INSERT INTO `Publishers` VALUES(1,'Dover Publications', '31 2nd St, Mineola, NY 11501','(516) 294-7000'); -- Pride and Prejudice
INSERT INTO `Publishers` VALUES(2,'Scribner Book Company', '597 5th Ave, New York, NY 10017','NULL'); -- The Snows of Kilimanjaro
INSERT INTO `Publishers` VALUES(3,'CreateSpace Independent Publishing Platform', 'South Carolina','(843) 992-7458');


INSERT INTO `Editors` VALUES(1,1,'Mike','Johnson', '31 Memorial St, Cambridge, MA 02138','(857) 286-8589'); -- Pride and Prejudice
INSERT INTO `Editors` VALUES(2,5,'Mike','Johnson', '31 Memorial St, Cambridge, MA 02138','(857) 286-8589'); -- Pride and Prejudice
INSERT INTO `Editors` VALUES(3,2,'Jane','Johnson', '597 Madison Ave, New York, NY 10017','(718) 987-2135'); -- The Snows of Kilimanjaro
INSERT INTO `Editors` VALUES(4,3,'Helena', 'Gaffin','5905 Wilshire Blvd, Los Angeles, CA 90036','(213) 002-1658');
INSERT INTO `Editors` VALUES(5,4,'Helena', 'Gaffin','5905 Wilshire Blvd, Los Angeles, CA 90036','(213) 002-1658');



INSERT INTO `Books` VALUES(1,1,3,1,12.99,'Love: poems','Poetry', '1995-06-21',55);
INSERT INTO `Books` VALUES(2,2,1,3,6.36,'The Snows of Kilimanjaro','Fiction', '1906-08-02',2);
INSERT INTO `Books` VALUES(3,3,2,4,9.80,'The Old Man And The Sea','Fiction', '1952-09-22',23);
INSERT INTO `Books` VALUES(4,4,2,5,19.80,'The Raven','Fantacy Novel', '1945-01-10',1);
INSERT INTO `Books` VALUES(5,5,3,2,7.99,'Pride and Prejudice ', 'Romantic novel', '1813-01-28',13);


