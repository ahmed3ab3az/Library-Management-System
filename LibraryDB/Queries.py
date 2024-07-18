import pyodbc
import datetime


server = 'DESKTOP-GLJLREN\\MSSQLSERVER01'  ## YOU MUST PUT YOUR SERVER NAME --> You will find it at the begin of SSMS in server name or in the first line in Object Explorer
database = 'UniversityLibrary'             ##Database name DO NOT change it
driver = 'ODBC Driver 17 for SQL Server'   ## ODBC (Open Database Connectivity) driver to be used for connecting to the SQL Server database + driver version + SQL server
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes'

admin_username = None
def connect_to_database():
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except Exception as e:
        print(f'Error connecting to the database: {e}')
        return None

def execute_query(query):
    connection = None
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print('Query executed successfully.')
    except Exception as e:
        print(f'Error executing query: {e}')
    finally:
        if connection:
            connection.close()

def add_book(book_id, title, price, year, availability, copies, isbn, category, publisher, edition, author_id , admin_id = admin_username):
    query = f"\nINSERT INTO Book (Book_ID, Book_Title, Book_Price, Publication_Year, [Availability], No_copies, ISBN, Category, Publisher, Edition, Author_ID , Admin_ID)\n            VALUES ({book_id}, '{title}', {price}, {year}, {availability}, {copies}, '{isbn}', '{category}', '{publisher}', '{edition}', {author_id} , {admin_id})\n        "
    execute_query(query)


def edit_book(book_id, title=None, price=None, year=None, availability=None, copies=None, isbn=None, category=None,publisher=None, edition=None, author_id=None):
    if not any([title, price, year, availability, copies, isbn, category, publisher, edition, author_id]):
        print('No updates provided.')
        return

    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            update_query = 'UPDATE Book SET '
            update_values = []

            if title:
                update_values.append(f"Book_Title = '{title}'")
            if price:
                update_values.append(f"Book_Price = {price}")
            if year:
                update_values.append(f"Publication_Year = {year}")
            if availability is not None:
                update_values.append(f"[Availability] = {availability}")
            if copies:
                update_values.append(f"No_copies = {copies}")
            if isbn:
                update_values.append(f"ISBN = '{isbn}'")
            if category:
                update_values.append(f"Category = '{category}'")
            if publisher:
                update_values.append(f"Publisher = '{publisher}'")
            if edition:
                update_values.append(f"Edition = '{edition}'")
            if author_id:
                update_values.append(f"Author_ID = {author_id}")

            update_query += ', '.join(update_values)
            update_query += f" WHERE Book_ID = {book_id}"

            cursor.execute(update_query)
            connection.commit()
            print('Book details updated successfully.')
    except Exception as e:
        print(f'Error updating book details: {e}')
    finally:
        if connection:
            connection.close()

def return_book(username, book_id, return_date):
    update_order_query = """
        UPDATE [Order]
        SET Return_Date = ?
        WHERE Order_ID IN (
            SELECT o.Order_ID
            FROM [Order] o
            JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
            JOIN Student s ON o.Student_ID = s.Student_ID
            WHERE s.UserName = ? AND bo.Book_ID = ?
        )
        AND Return_Date IS NULL
    """
    delete_book_order_query = """
        DELETE FROM BookOrder
        WHERE Order_ID IN (
            SELECT o.Order_ID
            FROM [Order] o
            JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
            JOIN Student s ON o.Student_ID = s.Student_ID
            WHERE s.UserName = ? AND bo.Book_ID = ?
        )
        AND Order_ID NOT IN (
            SELECT Order_ID
            FROM [Order]
            WHERE Return_Date IS NULL
        )
    """
    update_book_query = """
        UPDATE Book
        SET No_copies = No_copies + 1,
            Availability = CASE WHEN No_copies + 1 > 0 THEN 1 ELSE Availability END
        WHERE Book_ID = ?
    """
    check_borrow_query = """
        SELECT o.Order_ID
        FROM [Order] o
        JOIN BookOrder bo ON o.Order_ID = bo.Order_ID
        JOIN Student s ON o.Student_ID = s.Student_ID
        WHERE s.UserName = ? AND bo.Book_ID = ? AND o.Return_Date IS NULL
    """
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            # Retrieve Student_ID based on the username
            cursor.execute("SELECT Student_ID FROM Student WHERE UserName = ?", (username,))
            row = cursor.fetchone()
            student_id = row[0] if row else None

            if student_id is None:
                print("Error: Student with the provided username does not exist.")
                return False

            # Check if the student has borrowed this book and hasn't returned it
            cursor.execute(check_borrow_query, (username, book_id))
            order_row = cursor.fetchone()

            if order_row is None:
                print("Error: This student did not borrow this book or the book has already been returned.")
                return False

            # Execute the update order query
            cursor.execute(update_order_query, (return_date, username, book_id))

            # Execute the delete book order query
            cursor.execute(delete_book_order_query, (username, book_id))

            # Execute the update book availability query
            cursor.execute(update_book_query, (book_id,))

            connection.commit()  # Commit changes to the database
            connection.close()
            return True
    except Exception as e:
        print(f'Error returning book: {e}')
        return False

def delete_book(book_id):
    query = f"DELETE FROM Books WHERE Book_ID = {book_id}"
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            connection.close()
    except Exception as e:
        print(f'Error executing query: {e}')
        raise


def display_books():
    query = """
    SELECT 
        b.Book_ID,
        b.Book_Title,
        b.Book_Price,
        b.Publication_Year,
        b.ISBN,
        a.[Name] AS Author_Name,
        b.Category
    FROM 
        Book b
    LEFT JOIN 
        Author a ON b.Author_ID = a.Author_ID
    """
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            books = cursor.fetchall()
            if books:
                result = 'Books available in the library:\n'
                for book in books:
                    result += f'Book ID: {book[0]}, Title: {book[1]}, Price: {book[2]}, Publication Year: {book[3]}, ISBN: {book[4]}, Author: {book[5]}, Category: {book[6]}\n'
                    result += '------------------------------\n'
                connection.close()
                return result
            else:
                connection.close()
                return 'No books found in the library.'
    except Exception as e:
        print(f'Error displaying books: {e}')
        return 'Error displaying books.'


def sign_in(username, password, user_type):
    global admin_username  # Declare the global variable

    table = 'Admin' if user_type == 'admin' else 'Student'
    query = f"SELECT * FROM {table} WHERE Username = '{username}' AND Password = '{password}'"
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            user = cursor.fetchone()
            connection.close()
            if user:
                if user_type == 'admin':
                    admin_username = username  # Store the admin username in the global variable
                return True
            else:
                return False
    except Exception as e:
        print(f'Error signing in: {e}')
        return False


def sign_up(username, password, user_type, first_name, last_name, email, address, phone_number):
    table = 'Admin' if user_type == 'admin' else 'Student'
    id_column = 'Admin_ID' if user_type == 'admin' else 'Student_ID'
    query_id = f'SELECT MAX({id_column}) FROM {table}'
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query_id)
            max_id = cursor.fetchone()[0]
            new_id = (max_id if max_id else 0) + 1
            if table == 'Student':
                query = f"\n INSERT INTO {table} ({id_column}, FName, LName, Username, Password, Email, Address,PhoneNumber)\n                VALUES ({new_id}, '{first_name}', '{last_name}', '{username}', '{password}', '{email}', '{address}','{phone_number}')\n            "
            else:
                query = f"\n INSERT INTO {table} ({id_column}, FName, LName, Username, Password, Email, Address)\n                VALUES ({new_id}, '{first_name}', '{last_name}', '{username}', '{password}', '{email}', '{address}')\n                "
            execute_query(query)
            return True
    except Exception as e:
        print(f'Error signing up: {e}')
        return False



def borrow_book(username, book_id):
    borrow_date = datetime.date.today()
    due_date = borrow_date + datetime.timedelta(days=14)  # Assuming a 2-week borrowing period

    # Retrieve Student_ID based on the username
    get_student_id_query = """
        SELECT Student_ID FROM Student WHERE UserName = ?
    """

    # First, update the book's number of copies and availability if needed
    update_book_query = """
        UPDATE Book
        SET No_copies = No_copies - 1,
            Availability = CASE WHEN No_copies - 1 = 0 THEN 0 ELSE Availability END
        WHERE Book_ID = ? AND No_copies > 0
    """

    # Second, insert a new order into the Order table
    insert_order_query = """
        INSERT INTO [Order] (Order_ID, Borrow_Date, Due_Date, Student_ID)
        VALUES (?, ?, ?, ?)
    """

    # Third, insert into the BookOrder table to link the book with the order
    insert_book_order_query = """
        INSERT INTO BookOrder (Book_ID, Order_ID)
        VALUES (?, ?)
    """

    try:
        connection = connect_to_database()  # Replace with your connection details
        cursor = connection.cursor()

        # Retrieve Student_ID based on the username
        cursor.execute(get_student_id_query, (username,))
        row = cursor.fetchone()
        student_id = row[0] if row else None

        if student_id is None:
            print("Error: Student with the provided username does not exist.")
            return False

        # Execute the update book query
        cursor.execute(update_book_query, (book_id,))

        if cursor.rowcount > 0:
            # Only proceed if the book's number of copies was successfully updated

            # Fetch the current maximum Order_ID and increment it by one
            cursor.execute("SELECT MAX(Order_ID) FROM [Order]")
            max_order_id = cursor.fetchone()[0]
            order_id = max_order_id + 1 if max_order_id is not None else 1

            # Execute insert order query
            cursor.execute(insert_order_query, (order_id, borrow_date, due_date, student_id))

            # Insert into BookOrder table to link the book with the order
            cursor.execute(insert_book_order_query, (book_id, order_id))

            connection.commit()
            connection.close()
            return True
        else:
            print("Error: The book is not available for borrowing.")
            connection.close()
            return False
    except Exception as e:
        print(f'Error borrowing book: {e}')
        return False

def update_user_details(username, first_name=None, last_name=None, address=None, password=None):
    if not any([first_name, last_name, address, password]):
        print('No updates provided.')
        return
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Admin WHERE Username = '{username}'")
            admin_user = cursor.fetchone()
            cursor.execute(f"SELECT * FROM Student WHERE Username = '{username}'")
            student_user = cursor.fetchone()
            if admin_user:
                update_query = 'UPDATE Admin SET'
                update_values = []
                if first_name:
                    update_values.append(f"FName = '{first_name}'")
                if last_name:
                    update_values.append(f"LName = '{last_name}'")
                if address:
                    update_values.append(f"Address = '{address}'")
                if password:
                    update_values.append(f"Password = '{password}'")
                update_query += ' ' + ', '.join(update_values)
                update_query += f" WHERE Username = '{username}'"
                cursor.execute(update_query)
                connection.commit()
                print('Admin details updated successfully.')
            elif student_user:
                update_query = 'UPDATE Student SET'
                update_values = []
                if first_name:
                    update_values.append(f"FName = '{first_name}'")
                if last_name:
                    update_values.append(f"LName = '{last_name}'")
                if address:
                    update_values.append(f"Address = '{address}'")
                if password:
                    update_values.append(f"Password = '{password}'")
                update_query += ' ' + ', '.join(update_values)
                update_query += f" WHERE Username = '{username}'"
                cursor.execute(update_query)
                connection.commit()
                print('Student details updated successfully.')
            else:
                print(f'No user found with username: {username}')
    except Exception as e:
        print(f'Error updating user details: {e}')
    finally:
        if connection:
            connection.close()

def execute_search_query(query):
    connection = None
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            books = cursor.fetchall()
            connection.close()
            return books
    except Exception as e:
        print(f"Error executing search query: {e}")
        return None
def delete_student(username):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Student WHERE username = '{username}'")
            student = cursor.fetchone()
            if student:
                cursor.execute(f"DELETE FROM Student WHERE username = '{username}'")
                connection.commit()
                return True
            else:
                print("Student does not exist.")
    except Exception as e:
        print(f"Error deleting student: {e}")
    finally:
        if connection:
            connection.close()
    return False
