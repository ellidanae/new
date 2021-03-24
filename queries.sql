USE `book industry`;

-- 7.1 
SELECT * FROM Books 
WHERE AuthorID = 1

-- 7.2
-- SELECT *
-- FROM Authors 
-- WHERE BookID = 1

-- 7.5
-- SELECT *  FirstName, LastName,
-- 	CONCAT(FirstName,' ',LastName) AS FullName
-- FROM Books 
-- WHERE Genre = 'Fiction'

-- 7.6
-- SELECT * FROM Books 
-- WHERE PublisherID = 1

-- 7.7
-- SELECT * FROM Books 
-- WHERE EditorID = 2

-- 7.8
SELECT *
FROM Editors
WHERE LastName = 'Johnson' AND FirstName = 'Mike'


