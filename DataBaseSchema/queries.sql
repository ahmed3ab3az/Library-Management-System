--Retrieve All Books
SELECT 
    b.Book_ID,
    b.Book_Title,
    b.Book_Price,
    b.Publication_Year,
    b.ISBN,
    a.[Name] AS Author_Name
FROM 
    Book b
LEFT JOIN 
    Author a ON b.Author_ID = a.Author_ID


--Retrieve Student Information
SELECT 
    s.Student_ID,
    s.FName,
    s.LName,
    s.UserName,
    s.Email,
    s.[Address],
    s.PhoneNumber
FROM 
    Student s
--Retrieve Book Orders
SELECT 
    o.Order_ID,
    o.Borrow_Date,
    o.Return_Date,
    o.Due_Date,
    s.FName AS Student_FName,
    s.LName AS Student_LName,
    b.Book_Title
FROM 
    [Order] o
LEFT JOIN 
    Student s ON o.Student_ID = s.Student_ID
LEFT JOIN 
    BookOrder bo ON o.Order_ID = bo.Order_ID
LEFT JOIN 
    Book b ON bo.Book_ID = b.Book_ID;
 --Count of Books by Author
SELECT 
    a.[Name] AS Author_Name,
    COUNT(b.Book_ID) AS Total_Books
FROM 
    Author a
LEFT JOIN 
    Book b ON a.Author_ID = b.Author_ID
GROUP BY 
    a.[Name];

	-- Retrieve Admin Information
SELECT 
    Admin_ID,
    FName,
    LName,
    Username,
    Email
FROM 
    Admin;
