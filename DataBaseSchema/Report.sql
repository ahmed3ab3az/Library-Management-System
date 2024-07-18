--List all books and their authors

SELECT b.Book_Title, a.Name AS Author_Name
FROM Book b
JOIN Author a ON b.Author_ID = a.Author_ID
ORDER BY b.Book_Title;


--Count the total number of books in the library

SELECT COUNT(*) AS Total_Books
FROM Book;

--Get the list of students who have borrowed books and the titles they borrowed

SELECT s.FName, s.LName, b.Book_Title, o.Borrow_Date, o.Due_Date
FROM Student s
JOIN [Order] o ON s.Student_ID = o.Student_ID
JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
JOIN Book b ON bo.Book_ID = b.Book_ID
ORDER BY s.LName, s.FName, o.Borrow_Date;


--Find the number of books each student has borrowed

SELECT s.Student_ID, s.FName, s.LName, COUNT(*) AS Books_Borrowed
FROM Student s
JOIN [Order] o ON s.Student_ID = o.Student_ID
JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
GROUP BY s.Student_ID, s.FName, s.LName
ORDER BY Books_Borrowed DESC;

--List all books that are currently available (not borrowed)

SELECT b.Book_Title, b.No_copies - ISNULL(bo.Borrowed_Copies, 0) AS Available_Copies
FROM Book b
LEFT JOIN (
    SELECT Book_ID, COUNT(*) AS Borrowed_Copies
    FROM BookOrder bo
    JOIN [Order] o ON bo.Order_ID = o.Order_ID
    WHERE o.Return_Date IS NULL
    GROUP BY bo.Book_ID
) bo ON b.Book_ID = bo.Book_ID
WHERE b.No_copies - ISNULL(bo.Borrowed_Copies, 0) > 0
ORDER BY b.Book_Title;

--Get the most borrowed books

SELECT b.Book_Title, COUNT(*) AS Times_Borrowed
FROM Book b
JOIN BookOrder bo ON b.Book_ID = bo.Book_ID
JOIN [Order] o ON bo.Order_ID = o.Order_ID
GROUP BY b.Book_Title
ORDER BY Times_Borrowed DESC;


--Find all overdue books and the students who borrowed them

SELECT s.FName, s.LName, b.Book_Title, o.Borrow_Date, o.Due_Date, DATEDIFF(DAY, o.Due_Date, GETDATE()) AS Days_Overdue
FROM Student s
JOIN [Order] o ON s.Student_ID = o.Student_ID
JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
JOIN Book b ON bo.Book_ID = b.Book_ID
WHERE o.Return_Date IS NULL AND o.Due_Date < GETDATE()
ORDER BY Days_Overdue DESC;


--Get the total number of authors in the library database

SELECT COUNT(*) AS Total_Authors
FROM Author;


--List of books published before the year 2000

SELECT Book_Title, Publication_Year, Author_ID
FROM Book
WHERE Publication_Year < 2000
ORDER BY Publication_Year;


--Find students who have never borrowed a book

SELECT s.Student_ID, s.FName, s.LName
FROM Student s
LEFT JOIN [Order] o ON s.Student_ID = o.Student_ID
WHERE o.Order_ID IS NULL
ORDER BY s.LName, s.FName;
