USE UniversityLibrary;

-- Insert into Admin Table
INSERT INTO [Admin] (Admin_ID, FName, LName, Username, [Password], Email, [Address])
VALUES 
(1, 'John', 'Doe', 'johndoe', 'password123', 'john.doe@example.com', '123 Main St'),
(2, 'Jane', 'Smith', 'janesmith', 'password456', 'jane.smith@example.com', '456 Elm St'),
(3, 'Michael', 'Johnson', 'michaelj', 'password789', 'michael.johnson@example.com', '789 Oak St'),
(4, 'Emily', 'Davis', 'emilyd', 'password101', 'emily.davis@example.com', '1010 Maple St'),
(5, 'David', 'Miller', 'davidm', 'password112', 'david.miller@example.com', '1212 Pine St'),
(6, 'Emma', 'Garcia', 'emmag', 'password131', 'emma.garcia@example.com', '1313 Birch St'),
(7, 'James', 'Martinez', 'jamesm', 'password415', 'james.martinez@example.com', '1414 Cedar St'),
(8, 'Olivia', 'Hernandez', 'oliviah', 'password161', 'olivia.hernandez@example.com', '1515 Oak St'),
(9, 'William', 'Lopez', 'williaml', 'password171', 'william.lopez@example.com', '1616 Elm St'),
(10, 'Sophia', 'Gonzalez', 'sophiag', 'password181', 'sophia.gonzalez@example.com', '1717 Maple St'),
(11, 'Alexander', 'Wilson', 'alexanderw', 'password191', 'alexander.wilson@example.com', '1818 Pine St'),
(12, 'Isabella', 'Anderson', 'isabellaa', 'password202', 'isabella.anderson@example.com', '1919 Birch St'),
(13, 'Jacob', 'Thomas', 'jacobt', 'password213', 'jacob.thomas@example.com', '2020 Cedar St'),
(14, 'Mia', 'Taylor', 'miat', 'password224', 'mia.taylor@example.com', '2121 Oak St'),
(15, 'Ethan', 'Moore', 'ethanm', 'password235', 'ethan.moore@example.com', '2222 Elm St'),
(16, 'Ava', 'Jackson', 'avaj', 'password246', 'ava.jackson@example.com', '2323 Maple St'),
(17, 'Michael', 'Lee', 'michaell', 'password257', 'michael.lee@example.com', '2424 Pine St'),
(18, 'Charlotte', 'Perez', 'charlottep', 'password268', 'charlotte.perez@example.com', '2525 Birch St'),
(19, 'Daniel', 'White', 'danielw', 'password279', 'daniel.white@example.com', '2626 Cedar St'),
(20, 'Amelia', 'Harris', 'ameliah', 'password280', 'amelia.harris@example.com', '2727 Oak St');

-- Insert into Author Table
INSERT INTO Author (Author_ID, [Name], Biography)
VALUES 
(1, 'J.K. Rowling', 'Author of the Harry Potter series'),
(2, 'George R.R. Martin', 'Author of A Song of Ice and Fire'),
(3, 'Agatha Christie', 'Known for her detective novels and short story collections.'),
(4, 'Stephen King', 'American author of horror, supernatural fiction, suspense, and fantasy novels.'),
(5, 'J.R.R. Tolkien', 'Author of The Lord of the Rings series.'),
(6, 'Isaac Asimov', 'Known for his works of science fiction and popular science.'),
(7, 'Ernest Hemingway', 'American novelist and short story writer.'),
(8, 'Mark Twain', 'Known for his novels The Adventures of Tom Sawyer and Adventures of Huckleberry Finn.'),
(9, 'F. Scott Fitzgerald', 'American novelist, known for The Great Gatsby.'),
(10, 'Jane Austen', 'Known for her novels on British landed gentry.'),
(11, 'Charles Dickens', 'English writer and social critic.'),
(12, 'Leo Tolstoy', 'Russian author, best known for War and Peace and Anna Karenina.'),
(13, 'Gabriel Garcia Marquez', 'Colombian novelist, known for One Hundred Years of Solitude.'),
(14, 'H.G. Wells', 'English writer, known for his works of science fiction.'),
(15, 'Arthur Conan Doyle', 'British writer, creator of Sherlock Holmes.'),
(16, 'Herman Melville', 'American novelist, best known for Moby-Dick.'),
(17, 'Oscar Wilde', 'Irish poet and playwright.'),
(18, 'Edgar Allan Poe', 'American writer, known for his poetry and macabre tales.'),
(19, 'Franz Kafka', 'German-speaking Bohemian writer.'),
(20, 'Virginia Woolf', 'English writer, known for her modernist classics.');

-- Insert into Book Table
INSERT INTO Book (Book_ID, Book_Title, Book_Price, Publication_Year, [Availability], No_copies, ISBN, Category, Publisher, Edition, Author_ID)
VALUES 
(1, 'Harry Potter and the Sorcerers Stone', 19.99, 1997, 1, 10, '9780439708180', 'Fantasy', 'Scholastic', '1st', 1),
(2, 'A Game of Thrones', 24.99, 1996, 1, 15, '9780553103540', 'Fantasy', 'Bantam Books', '1st', 2),
(3, 'Murder on the Orient Express', 15.99, 1934, 1, 7, '9780007119318', 'Mystery', 'Collins Crime Club', 'Reprint', 3),
(4, 'The Shining', 18.99, 1977, 1, 5, '9780307743657', 'Horror', 'Doubleday', '1st', 4),
(5, 'The Hobbit', 14.99, 1937, 1, 12, '9780345339683', 'Fantasy', 'George Allen & Unwin', 'Reprint', 5),
(6, 'Foundation', 17.99, 1951, 1, 8, '9780553293357', 'Science Fiction', 'Gnome Press', '1st', 6),
(7, 'The Old Man and the Sea', 13.99, 1952, 1, 11, '9780684830490', 'Fiction', 'Charles Scribner Sons', '1st', 7),
(8, 'The Adventures of Huckleberry Finn', 10.99, 1884, 1, 9, '9780486280615', 'Fiction', 'Chatto & Windus', 'Reprint', 8),
(9, 'The Great Gatsby', 14.99, 1925, 1, 6, '9780743273565', 'Fiction', 'Charles Scribner Sons', '1st', 9),
(10, 'Pride and Prejudice', 12.99, 1813, 1, 13, '9780141439518', 'Fiction', 'T. Egerton', 'Reprint', 10),
(11, 'Great Expectations', 16.99, 1861, 1, 7, '9780141439563', 'Fiction', 'Chapman & Hall', 'Reprint', 11),
(12, 'War and Peace', 22.99, 1869, 1, 10, '9780140447934', 'Fiction', 'The Russian Messenger', 'Reprint', 12),
(13, 'One Hundred Years of Solitude', 18.99, 1967, 1, 14, '9780060883287', 'Magic Realism', 'Harper & Row', '1st', 13),
(14, 'The Time Machine', 12.99, 1895, 1, 5, '9780553213513', 'Science Fiction', 'Heinemann', 'Reprint', 14),
(15, 'The Hound of the Baskervilles', 15.99, 1902, 1, 8, '9780141034323', 'Mystery', 'George Newnes', 'Reprint', 15),
(16, 'Moby-Dick', 19.99, 1851, 1, 6, '9781503280786', 'Adventure', 'Harper & Brothers', 'Reprint', 16),
(17, 'The Picture of Dorian Gray', 11.99, 1890, 1, 7, '9780141439570', 'Philosophical Fiction', 'Lippincott Monthly Magazine', 'Reprint', 17),
(18, 'The Tell-Tale Heart', 9.99, 1843, 1, 15, '9780141039915', 'Horror', 'The Pioneer', 'Reprint', 18),
(19, 'The Metamorphosis', 10.99, 1915, 1, 12, '9780553213698', 'Absurdist Fiction', 'Kurt Wolff Verlag', 'Reprint', 19),
(20, 'Mrs Dalloway', 13.99, 1925, 1, 10, '9780156628709', 'Modernist', 'Hogarth Press', 'Reprint', 20);

-- Insert into Student Table
INSERT INTO Student (Student_ID, FName, LName, UserName, [Password], Email, [Address],PhoneNumber)
VALUES 
(1, 'Alice', 'Johnson', 'alicej', 'password789', 'alice.johnson@example.com', '789 Oak St', '123-456-7890'),
(2, 'Bob', 'Williams', 'bobw', 'password012', 'bob.williams@example.com', '321 Pine St', '098-765-4321'),
(3, 'Charlie', 'Brown', 'charlieb', 'password345', 'charlie.brown@example.com', '1010 Maple St', '555-678-9012'),
(4, 'Lucy', 'Van Pelt', 'lucyvp', 'password678', 'lucy.vanpelt@example.com', '2020 Birch St', '555-123-4567'),
(5, 'Daisy', 'Miller', 'daisym', 'password7890', 'daisy.miller@example.com', '3030 Cedar St', '123-321-1234'),
(6, 'Edward', 'Green', 'edwardg', 'password111', 'edward.green@example.com', '3131 Pine St', '321-321-4321'),
(7, 'Grace', 'Kelly', 'gracek', 'password222', 'grace.kelly@example.com', '3232 Maple St', '555-987-6543'),
(8, 'Henry', 'Ford', 'henryf', 'password333', 'henry.ford@example.com', '3333 Oak St', '432-123-6789'),
(9, 'Ivy', 'White', 'ivyw', 'password444', 'ivy.white@example.com', '3434 Birch St', '555-234-5678'),
(10, 'Jack', 'Black', 'jackb', 'password555', 'jack.black@example.com', '3535 Elm St', '123-765-4321'),
(11, 'Kara', 'Brown', 'karab', 'password666', 'kara.brown@example.com', '3636 Cedar St', '555-876-5432'),
(12, 'Liam', 'Gray', 'liamg', 'password777', 'liam.gray@example.com', '3737 Pine St', '987-123-4567'),
(13, 'Mia', 'Jones', 'miaj', 'password888', 'mia.jones@example.com', '3838 Maple St', '555-345-6789'),
(14, 'Nathan', 'Hall', 'nathanh', 'password999', 'nathan.hall@example.com', '3939 Oak St', '123-567-8901'),
(15, 'Olivia', 'Moore', 'oliviam', 'password1010', 'olivia.moore@example.com', '4040 Birch St', '555-678-1234'),
(16, 'Peter', 'Parker', 'peterp', 'password1111', 'peter.parker@example.com', '4141 Elm St', '432-876-5432'),
(17, 'Quinn', 'Adams', 'quinna', 'password1212', 'quinn.adams@example.com', '4242 Cedar St', '987-654-3210'),
(18, 'Rose', 'Baker', 'roseb', 'password1313', 'rose.baker@example.com', '4343 Pine St', '555-567-8901'),
(19, 'Sam', 'Taylor', 'samt', 'password1414', 'sam.taylor@example.com', '4444 Maple St', '123-234-3456'),
(20, 'Tina', 'Clark', 'tinac', 'password1515', 'tina.clark@example.com', '4545 Oak St', '555-123-4567');

-- Insert into [Order] Table
INSERT INTO [Order] (Order_ID, Borrow_Date, Return_Date, Due_Date, Student_ID)
VALUES 
(1, '2024-04-01', '2024-04-15', '2024-04-20', 1),
(2, '2024-04-05', '2024-04-19', '2024-04-25', 2),
(3, '2024-05-10', '2024-05-24', '2024-05-30', 3),
(4, '2024-05-15', '2024-05-29', '2024-06-05', 4),
(5, '2024-05-20', '2024-06-03', '2024-06-10', 5),
(6, '2024-05-25', '2024-06-08', '2024-06-15', 6),
(7, '2024-05-30', '2024-06-13', '2024-06-20', 7),
(8, '2024-06-04', '2024-06-18', '2024-06-25', 8),
(9, '2024-06-09', '2024-06-23', '2024-06-30', 9),
(10, '2024-06-14', '2024-06-28', '2024-07-05', 10),
(11, '2024-06-19', '2024-07-03', '2024-07-10', 11),
(12, '2024-06-24', '2024-07-08', '2024-07-15', 12),
(13, '2024-06-29', '2024-07-13', '2024-07-20', 13),
(14, '2024-07-04', '2024-07-18', '2024-07-25', 14),
(15, '2024-07-09', '2024-07-23', '2024-07-30', 15),
(16, '2024-07-14', '2024-07-28', '2024-08-05', 16),
(17, '2024-07-19', '2024-08-02', '2024-08-10', 17),
(18, '2024-07-24', '2024-08-07', '2024-08-15', 18),
(19, '2024-07-29', '2024-08-12', '2024-08-20', 19),
(20, '2024-08-03', '2024-08-17', '2024-08-25', 20);

-- Insert into BookOrder Table
INSERT INTO BookOrder (Book_ID, Order_ID)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10),
(11, 11),
(12, 12),
(13, 13),
(14, 14),
(15, 15),
(16, 16),
(17, 17),
(18, 18),
(19, 19),
(20, 20);
