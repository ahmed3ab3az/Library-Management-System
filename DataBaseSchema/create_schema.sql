-- create data base  if it doesn't exist
IF NOT EXISTS (
    SELECT * FROM sys.databases 
    WHERE name = 'UniversityLibrary' 
)
BEGIN
    CREATE DATABASE UniversityLibrary  
END

use UniversityLibrary ;
-- Drop tables if they already exist (to avoid conflicts)
DROP TABLE IF EXISTS BookOrder;
DROP TABLE IF EXISTS [Order];
DROP TABLE IF EXISTS PhoneNumber;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS [Admin]; 
-- Admin Table
CREATE TABLE [Admin] (
    Admin_ID INT PRIMARY KEY,
	FName VARCHAR(50)NOT NULL,
    LName VARCHAR(50) NOT NULL,
	Username VARCHAR(50) unique NOT NULL,
    [Password] VARCHAR(50)NOT NULL,
	 Email VARCHAR(100) unique NOT NULL,
    [Address] VARCHAR(200) ,
);

-- Author Table
CREATE TABLE Author (
    Author_ID INT PRIMARY KEY,
    [Name] VARCHAR(100),
    Biography TEXT
);

-- Book Table
CREATE TABLE Book (
    Book_ID INT PRIMARY KEY,
    Book_Title VARCHAR(100) NOT NULL,
    Book_Price DECIMAL(10, 2),
    Publication_Year INT,
    [Availability] BIT ,
    No_copies INT,
    ISBN VARCHAR(20) unique not null,
    Category VARCHAR(50),
    Publisher VARCHAR(100),
    Edition VARCHAR(50),
	Author_ID INT ,
	-- Relationship between Book and Author
	 FOREIGN KEY (Author_ID) REFERENCES Author(Author_ID),
	-- Relationship between Book and Admin
	


);


-- Student Table
CREATE TABLE Student (
    Student_ID INT PRIMARY KEY NOT NULL,
    FName VARCHAR(50)NOT NULL,
    LName VARCHAR(50) NOT NULL,
    UserName VARCHAR(50)unique NOT NULL,
    [Password] VARCHAR(50)NOT NULL,
    Email VARCHAR(100) unique NOT NULL,
    [Address] VARCHAR(200) ,
	PhoneNumber VARCHAR(20)

	
);

-- Order Table
CREATE TABLE [Order] (
    Order_ID INT PRIMARY KEY,
    Borrow_Date DATE,
    Return_Date DATE,
    Due_Date DATE,
	Student_ID INT,
	FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)


);
-- Relationship between order and Student


CREATE TABLE BookOrder (
    Book_ID INT,
    Order_ID INT,
    PRIMARY KEY (Book_ID, Order_ID),
    FOREIGN KEY (Book_ID) REFERENCES Book(Book_ID),
    FOREIGN KEY (Order_ID) REFERENCES [Order] (Order_ID)
);
