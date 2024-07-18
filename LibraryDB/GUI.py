import customtkinter as ctk
from customtkinter import E, END, INSERT, LEFT, N, NS, S, SE, SEL, TOP, W, X, Y
import tkinter as tk
from tkinter import messagebox
import datetime
from Queries import *

class LibraryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Library Management System')
        self.geometry('800x600')  # Set the initial window size

        container = ctk.CTkFrame(self)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky='nsew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, SignInPage, SignUpPage, AdminPage, StudentPage, EditBookPage, DeleteBookPage, DisplayBooksPage, BorrowBookPage, AddBookPage, UpdateDetailsPage,SearchBooksPage , ReturnBookPage ,DeleteStudentPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('HomePage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user_type = tk.StringVar(value='admin')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text='Library Management System', font=('Arial', 24))
        label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        button_login = ctk.CTkButton(self, text='Login', command=lambda: controller.show_frame('SignInPage'))
        button_login.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        button_signup = ctk.CTkButton(self, text='Sign Up', command=lambda: controller.show_frame('SignUpPage'))
        button_signup.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')

    def go_back(self):
        if self.user_type.get() == 'admin':
            self.controller.show_frame('AdminPage')
        else:
            self.controller.show_frame('StudentPage')

class SignInPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Log in', font=('Arial', 18)).pack(pady=10)
        username_frame = ctk.CTkFrame(self)
        username_frame.pack(pady=5)
        ctk.CTkLabel(username_frame, text='Username').pack(side=tk.LEFT)
        self.entry_username = ctk.CTkEntry(username_frame)
        self.entry_username.pack(side=tk.LEFT)
        password_frame = ctk.CTkFrame(self)
        password_frame.pack(pady=5)
        ctk.CTkLabel(password_frame, text='Password').pack(side=tk.LEFT)
        self.entry_password = ctk.CTkEntry(password_frame, show='*')
        self.entry_password.pack(side=tk.LEFT)
        ctk.CTkLabel(self, text='User Type').pack(pady=5)
        self.user_type = tk.StringVar(value='admin')
        user_type_frame = ctk.CTkFrame(self)
        user_type_frame.pack(pady=5)
        ctk.CTkRadioButton(user_type_frame, text='Admin', variable=self.user_type, value='admin').pack(side=tk.LEFT)
        ctk.CTkRadioButton(user_type_frame, text='Student', variable=self.user_type, value='student').pack(side=tk.LEFT)
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text='Login', command=self.submit_sign_in).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text='Back', command=self.go_back).pack(side=tk.LEFT, padx=5)

    def submit_sign_in(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        user_type = self.user_type.get()
        if sign_in(username, password, user_type):
            home_page = self.controller.frames['HomePage']
            home_page.user_type.set(user_type)
            if user_type == 'admin':
                self.controller.show_frame('AdminPage')
            else:
                self.controller.show_frame('StudentPage')
        else:
            messagebox.showerror('Error', 'Invalid username or password')

    def go_back(self):
        self.controller.show_frame('HomePage')

class SignUpPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Sign Up', font=('Arial', 18)).pack(pady=10)
        ctk.CTkLabel(self, text='First Name *').pack()
        self.entry_first_name = ctk.CTkEntry(self)
        self.entry_first_name.pack()
        ctk.CTkLabel(self, text='Last Name *').pack()
        self.entry_last_name = ctk.CTkEntry(self)
        self.entry_last_name.pack()
        ctk.CTkLabel(self, text='Username *').pack()
        self.entry_username = ctk.CTkEntry(self)
        self.entry_username.pack()
        ctk.CTkLabel(self, text='Password *').pack()
        self.entry_password = ctk.CTkEntry(self, show='*')
        self.entry_password.pack()
        ctk.CTkLabel(self, text='Email *').pack()
        self.entry_email = ctk.CTkEntry(self)
        self.entry_email.pack()
        ctk.CTkLabel(self, text='Phone Number (for Students)').pack()
        self.entry_phone_number = ctk.CTkEntry(self)
        self.entry_phone_number.pack()
        ctk.CTkLabel(self, text='Address').pack()
        self.entry_address = ctk.CTkEntry(self)
        self.entry_address.pack()
        ctk.CTkLabel(self, text='User Type').pack()
        self.user_type = tk.StringVar(value='admin')
        ctk.CTkRadioButton(self, text='Admin', variable=self.user_type, value='admin').pack()
        ctk.CTkRadioButton(self, text='Student', variable=self.user_type, value='student').pack()
        ctk.CTkButton(self, text='Sign Up', command=self.submit_sign_up).pack(pady=10)
        ctk.CTkButton(self, text='Back', command=lambda: controller.show_frame('HomePage')).pack(pady=10)

    def submit_sign_up(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()
        phone_number = self.entry_phone_number.get()
        address = self.entry_address.get()
        user_type = self.user_type.get()
        if not all([first_name, last_name, username, password, email]):
            messagebox.showerror('Error', 'Please fill in all required fields .')
            return
        if sign_up(username, password, user_type, first_name, last_name, email, address, phone_number):
            messagebox.showinfo('Success', 'Sign up successful!')
            self.controller.show_frame('SignInPage')
        else:
            messagebox.showerror('Error', 'Sign up failed. Please try again.')

class AdminPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Admin Dashboard', font=('Arial', 18)).pack(pady=10)
        ctk.CTkButton(self, text='Search Books', command=lambda: controller.show_frame('SearchBooksPage')).pack(pady=10)
        ctk.CTkButton(self, text='Add Book', command=lambda: controller.show_frame('AddBookPage')).pack(pady=10)
        ctk.CTkButton(self, text='Edit Book', command=lambda: controller.show_frame('EditBookPage')).pack(pady=10)
        ctk.CTkButton(self, text='Delete Book', command=lambda: controller.show_frame('DeleteBookPage')).pack(pady=10)
        ctk.CTkButton(self, text='View Book List', command=lambda: controller.show_frame('DisplayBooksPage')).pack(pady=10)
        ctk.CTkButton(self, text='Update Details', command=lambda: controller.show_frame('UpdateDetailsPage')).pack(pady=10)
        ctk.CTkButton(self, text='Delete Student', command=lambda: controller.show_frame('DeleteStudentPage')).pack(pady=10)

        ctk.CTkButton(self, text='Log Out', command=lambda: controller.show_frame('HomePage')).pack(pady=10)

class StudentPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Student Dashboard', font=('Arial', 18)).pack(pady=10)
        ctk.CTkButton(self, text='Search Books', command=lambda: controller.show_frame('SearchBooksPage')).pack(pady=10)
        ctk.CTkButton(self, text='View Book List', command=lambda: controller.show_frame('DisplayBooksPage')).pack(pady=10)
        ctk.CTkButton(self, text='Borrow Book', command=lambda: controller.show_frame('BorrowBookPage')).pack(pady=10)
        ctk.CTkButton(self, text='Return Book', command=lambda: controller.show_frame('ReturnBookPage')).pack(pady=10)
        ctk.CTkButton(self, text='Update Details', command=lambda: controller.show_frame('UpdateDetailsPage')).pack(pady=10)
        ctk.CTkButton(self, text='Log Out', command=lambda: controller.show_frame('HomePage')).pack(pady=10)

class AddBookPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Add Book', font=('Arial', 18)).pack(pady=10)
        frame_add_book = ctk.CTkFrame(self)
        frame_add_book.pack(pady=10)
        ctk.CTkLabel(frame_add_book, text='Book ID').grid(row=0, column=0)
        self.entry_book_id = ctk.CTkEntry(frame_add_book)
        self.entry_book_id.grid(row=0, column=1)
        ctk.CTkLabel(frame_add_book, text='Title').grid(row=1, column=0)
        self.entry_title = ctk.CTkEntry(frame_add_book)
        self.entry_title.grid(row=1, column=1)
        ctk.CTkLabel(frame_add_book, text='Price').grid(row=2, column=0)
        self.entry_price = ctk.CTkEntry(frame_add_book)
        self.entry_price.grid(row=2, column=1)
        ctk.CTkLabel(frame_add_book, text='Publication Year').grid(row=3, column=0)
        self.entry_year = ctk.CTkEntry(frame_add_book)
        self.entry_year.grid(row=3, column=1)
        ctk.CTkLabel(frame_add_book, text='Availability').grid(row=4, column=0)
        self.entry_availability = ctk.CTkEntry(frame_add_book)
        self.entry_availability.grid(row=4, column=1)
        ctk.CTkLabel(frame_add_book, text='Number of Copies').grid(row=5, column=0)
        self.entry_copies = ctk.CTkEntry(frame_add_book)
        self.entry_copies.grid(row=5, column=1)
        ctk.CTkLabel(frame_add_book, text='ISBN').grid(row=6, column=0)
        self.entry_isbn = ctk.CTkEntry(frame_add_book)
        self.entry_isbn.grid(row=6, column=1)
        ctk.CTkLabel(frame_add_book, text='Category').grid(row=7, column=0)
        self.entry_category = ctk.CTkEntry(frame_add_book)
        self.entry_category.grid(row=7, column=1)
        ctk.CTkLabel(frame_add_book, text='Publisher').grid(row=8, column=0)
        self.entry_publisher = ctk.CTkEntry(frame_add_book)
        self.entry_publisher.grid(row=8, column=1)
        ctk.CTkLabel(frame_add_book, text='Edition').grid(row=9, column=0)
        self.entry_edition = ctk.CTkEntry(frame_add_book)
        self.entry_edition.grid(row=9, column=1)
        ctk.CTkLabel(frame_add_book, text='Author ID').grid(row=10, column=0)
        self.entry_author_id = ctk.CTkEntry(frame_add_book)
        self.entry_author_id.grid(row=10, column=1)
        ctk.CTkButton(frame_add_book, text='Add Book', command=self.submit_add_book).grid(row=11, columnspan=2, pady=10)
        ctk.CTkButton(frame_add_book, text='Back', command=lambda: controller.show_frame('AdminPage')).grid(row=12, columnspan=2, pady=10)

    def submit_add_book(self):
        try:
            book_id = int(self.entry_book_id.get())
            title = self.entry_title.get()
            price = float(self.entry_price.get())
            year = int(self.entry_year.get())
            availability = int(self.entry_availability.get())
            copies = int(self.entry_copies.get())
            isbn = self.entry_isbn.get()
            category = self.entry_category.get()
            publisher = self.entry_publisher.get()
            edition = self.entry_edition.get()
            author_id = int(self.entry_author_id.get())
            add_book(book_id, title, price, year, availability, copies, isbn, category, publisher, edition, author_id)
            messagebox.showinfo('Add Book', 'Book added successfully!')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numeric values for Book ID, Price, Publication Year, Availability, Number of Copies, Author ID, and Admin ID.')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')


class EditBookPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Edit Book', font=('Arial', 18)).pack(pady=10)
        frame_edit_book = ctk.CTkFrame(self)
        frame_edit_book.pack(pady=10)
        ctk.CTkLabel(frame_edit_book, text='Book ID').grid(row=0, column=0)
        self.entry_book_id = ctk.CTkEntry(frame_edit_book)
        self.entry_book_id.grid(row=0, column=1)
        ctk.CTkLabel(frame_edit_book, text='Title').grid(row=1, column=0)
        self.entry_title = ctk.CTkEntry(frame_edit_book)
        self.entry_title.grid(row=1, column=1)
        ctk.CTkLabel(frame_edit_book, text='Price').grid(row=2, column=0)
        self.entry_price = ctk.CTkEntry(frame_edit_book)
        self.entry_price.grid(row=2, column=1)
        ctk.CTkLabel(frame_edit_book, text='Publication Year').grid(row=3, column=0)
        self.entry_year = ctk.CTkEntry(frame_edit_book)
        self.entry_year.grid(row=3, column=1)
        ctk.CTkLabel(frame_edit_book, text='Availability').grid(row=4, column=0)
        self.entry_availability = ctk.CTkEntry(frame_edit_book)
        self.entry_availability.grid(row=4, column=1)
        ctk.CTkLabel(frame_edit_book, text='Number of Copies').grid(row=5, column=0)
        self.entry_copies = ctk.CTkEntry(frame_edit_book)
        self.entry_copies.grid(row=5, column=1)
        ctk.CTkLabel(frame_edit_book, text='ISBN').grid(row=6, column=0)
        self.entry_isbn = ctk.CTkEntry(frame_edit_book)
        self.entry_isbn.grid(row=6, column=1)
        ctk.CTkLabel(frame_edit_book, text='Category').grid(row=7, column=0)
        self.entry_category = ctk.CTkEntry(frame_edit_book)
        self.entry_category.grid(row=7, column=1)
        ctk.CTkLabel(frame_edit_book, text='Publisher').grid(row=8, column=0)
        self.entry_publisher = ctk.CTkEntry(frame_edit_book)
        self.entry_publisher.grid(row=8, column=1)
        ctk.CTkLabel(frame_edit_book, text='Edition').grid(row=9, column=0)
        self.entry_edition = ctk.CTkEntry(frame_edit_book)
        self.entry_edition.grid(row=9, column=1)
        ctk.CTkLabel(frame_edit_book, text='Author ID').grid(row=10, column=0)
        self.entry_author_id = ctk.CTkEntry(frame_edit_book)
        self.entry_author_id.grid(row=10, column=1)
        ctk.CTkButton(frame_edit_book, text='Edit Book', command=self.submit_edit_book).grid(row=11, columnspan=2, pady=10)
        ctk.CTkButton(frame_edit_book, text='Back', command=lambda: controller.show_frame('AdminPage')).grid(row=12,  columnspan=2,  pady=10)

    def submit_edit_book(self):
        book_id = self.entry_book_id.get()
        title = self.entry_title.get() or None
        price = self.entry_price.get() or None
        year = self.entry_year.get() or None
        availability = self.entry_availability.get() or None
        copies = self.entry_copies.get() or None
        isbn = self.entry_isbn.get() or None
        category = self.entry_category.get() or None
        publisher = self.entry_publisher.get() or None
        edition = self.entry_edition.get() or None
        author_id = self.entry_author_id.get() or None

        if not any([title, price, year, availability, copies, isbn, category, publisher, edition, author_id]):
            messagebox.showerror('Error', 'Please provide at least one value to update.')
            return

        edit_book(book_id, title=title, price=price, year=year, availability=availability, copies=copies, isbn=isbn,  category=category, publisher=publisher, edition=edition, author_id=author_id)
        messagebox.showinfo('Edit Book', 'Book details updated successfully!')
class DeleteBookPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Delete Book', font=('Arial', 18)).pack(pady=10)
        frame_delete_book = ctk.CTkFrame(self)
        frame_delete_book.pack(pady=10)
        ctk.CTkLabel(frame_delete_book, text='Book ID').grid(row=0, column=0)
        self.entry_book_id = ctk.CTkEntry(frame_delete_book)
        self.entry_book_id.grid(row=0, column=1)
        ctk.CTkButton(frame_delete_book, text='Delete Book', command=self.submit_delete_book).grid(row=1, columnspan=2, pady=10)
        ctk.CTkButton(frame_delete_book, text='Back', command=lambda: controller.show_frame('AdminPage')).grid(row=2, columnspan=2, pady=10)

    def submit_delete_book(self):
        book_id = int(self.entry_book_id.get())
        try:
            delete_book(book_id)
            messagebox.showinfo('Delete Book', 'Book deleted successfully!')
        except Exception as e:
            messagebox.showerror('Delete Book', 'Error: This book cannot be deleted because it is referenced by other records.')



class BorrowBookPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text='Borrow Book', font=('Arial', 18)).pack(pady=(20, 10))

        frame_borrow_book = ctk.CTkFrame(self)
        frame_borrow_book.pack(pady=10)

        ctk.CTkLabel(frame_borrow_book, text='Student Username:').grid(row=0, column=0, sticky=E, padx=(0, 10))
        self.entry_username = ctk.CTkEntry(frame_borrow_book)
        self.entry_username.grid(row=0, column=1, sticky=W)

        ctk.CTkLabel(frame_borrow_book, text='Book ID:').grid(row=1, column=0, sticky=E, padx=(0, 10))
        self.entry_book_id = ctk.CTkEntry(frame_borrow_book)
        self.entry_book_id.grid(row=1, column=1, sticky=W)

        ctk.CTkButton(frame_borrow_book, text='Borrow Book', command=self.submit_borrow_book).grid(row=2, columnspan=2, pady=10)
        ctk.CTkButton(frame_borrow_book, text='Back', command=lambda: controller.show_frame('StudentPage')).grid(row=3, columnspan=2, pady=10)

    def submit_borrow_book(self):
        username = self.entry_username.get()
        book_id = self.entry_book_id.get()

        # Check if username or book_id are empty
        if not username.strip() or not book_id.strip():
            messagebox.showerror('Error', 'Please enter both the username and book ID.')
            return

        # Convert book_id to integer
        try:
            book_id = int(book_id)
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid book ID.')
            return

        # Call the borrow_book function
        success = borrow_book(username, book_id)

        if success:
            messagebox.showinfo('Borrow Book', 'Book borrowed successfully!')
        else:
            messagebox.showerror('Error', 'Failed to borrow book.')

class DisplayBooksPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Books List', font=('Arial', 18)).pack(pady=10)
        self.text_display_books = ctk.CTkTextbox(self, width=600, height=400)
        self.text_display_books.pack(pady=10)
        ctk.CTkButton(self, text='Refresh', command=self.display_books).pack(pady=10)
        ctk.CTkButton(self, text='Back', command=self.go_back).pack(pady=10)
        self.display_books()

    def display_books(self):
        books = display_books()
        self.text_display_books.delete(1.0, tk.END)
        self.text_display_books.insert(tk.END, books)

    def go_back(self):
        current_page = self.controller.frames['HomePage']
        if current_page.user_type.get() == 'admin':
            self.controller.show_frame('AdminPage')
        else:
            self.controller.show_frame('StudentPage')

class UpdateDetailsPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Update Details', font=('Arial', 18)).pack(pady=10)
        frame_update_details = ctk.CTkFrame(self)
        frame_update_details.pack(pady=10)
        ctk.CTkLabel(frame_update_details, text='Username to be Updated').grid(row=0, column=0)
        self.entry_username = ctk.CTkEntry(frame_update_details)
        self.entry_username.grid(row=0, column=1)
        ctk.CTkLabel(frame_update_details, text='First Name').grid(row=1, column=0)
        self.entry_first_name = ctk.CTkEntry(frame_update_details)
        self.entry_first_name.grid(row=1, column=1)
        ctk.CTkLabel(frame_update_details, text='Last Name').grid(row=2, column=0)
        self.entry_last_name = ctk.CTkEntry(frame_update_details)
        self.entry_last_name.grid(row=2, column=1)
        ctk.CTkLabel(frame_update_details, text='Address').grid(row=3, column=0)
        self.entry_address = ctk.CTkEntry(frame_update_details)
        self.entry_address.grid(row=3, column=1)
        ctk.CTkLabel(frame_update_details, text='Password').grid(row=4, column=0)
        self.entry_password = ctk.CTkEntry(frame_update_details, show='*')
        self.entry_password.grid(row=4, column=1)
        ctk.CTkButton(frame_update_details, text='Update Details', command=self.submit_update_details).grid(row=5, columnspan=2, pady=10)
        ctk.CTkButton(self, text='Back', command=self.go_back).pack(pady=10)

    def submit_update_details(self):
        username = self.entry_username.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        address = self.entry_address.get()
        password = self.entry_password.get()
        if not any([first_name, last_name, address, password]):
            messagebox.showerror('Error', 'Please provide at least one value to update.')
            return
        update_user_details(username, first_name=first_name, last_name=last_name, address=address, password=password)
        messagebox.showinfo('Update Details', 'Details updated successfully!')

    def go_back(self):
            current_page = self.controller.frames['HomePage']
            if current_page.user_type.get() == 'admin':
                self.controller.show_frame('AdminPage')
            else:
                self.controller.show_frame('StudentPage')

class SearchBooksPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Search Books', font=('Arial', 18)).pack(pady=10)
        frame_search = ctk.CTkFrame(self)
        frame_search.pack(pady=10)
        ctk.CTkLabel(frame_search, text='ISBN:').grid(row=0, column=0)
        self.entry_isbn = ctk.CTkEntry(frame_search)
        self.entry_isbn.grid(row=0, column=1)
        ctk.CTkLabel(frame_search, text='Publication Year:').grid(row=1, column=0)
        self.entry_year = ctk.CTkEntry(frame_search)
        self.entry_year.grid(row=1, column=1)
        ctk.CTkLabel(frame_search, text='Author:').grid(row=2, column=0)
        self.entry_author = ctk.CTkEntry(frame_search)
        self.entry_author.grid(row=2, column=1)
        ctk.CTkButton(frame_search, text='Search', command=self.search_books).grid(row=3, columnspan=2, pady=10)
        self.text_search_results = ctk.CTkTextbox(self, width=400, height=200)
        self.text_search_results.pack(pady=10)
        ctk.CTkButton(self, text='Back', command=self.go_back).pack(pady=10)

    def search_books(self):
        isbn = self.entry_isbn.get()
        year = self.entry_year.get()
        author = self.entry_author.get()

        query = '''
            SELECT 
                b.Book_ID,
                b.Book_Title,
                b.Book_Price,
                b.Publication_Year,
                b.Availability,
                b.No_copies,
                b.ISBN,
                b.Category,
                b.Publisher,
                b.Edition,
                a.Name AS Author_Name
            FROM 
                Book b
            LEFT JOIN 
                Author a ON b.Author_ID = a.Author_ID
            WHERE 1=1
        '''

        if isbn:
            query += f" AND b.ISBN = '{isbn}'"
        if year:
            query += f" AND b.Publication_Year = {year}"
        if author:
            query += f" AND a.Name LIKE '%{author}%'"

        books = execute_search_query(query)

        if books:
            self.text_search_results.delete(1.0, tk.END)
            for book in books:
                book_details = f"Book ID: {book[0]}\nTitle: {book[1]}\nPrice: {book[2]}\nPublication Year: {book[3]}\nAvailability: {book[4]}\nNumber of Copies: {book[5]}\nISBN: {book[6]}\nCategory: {book[7]}\nPublisher: {book[8]}\nEdition: {book[9]}\nAuthor: {book[10]}\n\n"

                self.text_search_results.insert(tk.END, book_details)
        else:
            self.text_search_results.delete(1.0, tk.END)
            self.text_search_results.insert(tk.END, 'No books found matching the criteria.')

    def go_back(self):
        current_page = self.controller.frames['HomePage']
        if current_page.user_type.get() == 'admin':
            self.controller.show_frame('AdminPage')
        else:
            self.controller.show_frame('StudentPage')

class ReturnBookPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Return Book', font=('Arial', 18)).pack(pady=10)
        frame_return_book = ctk.CTkFrame(self)
        frame_return_book.pack(pady=10)
        ctk.CTkLabel(frame_return_book, text='Student Username').grid(row=0, column=0)
        self.entry_username = ctk.CTkEntry(frame_return_book)
        self.entry_username.grid(row=0, column=1)
        ctk.CTkLabel(frame_return_book, text='Book ID').grid(row=1, column=0)
        self.entry_book_id = ctk.CTkEntry(frame_return_book)
        self.entry_book_id.grid(row=1, column=1)
        ctk.CTkButton(frame_return_book, text='Return Book', command=self.submit_return_book).grid(row=2, columnspan=2, pady=10)
        ctk.CTkButton(frame_return_book, text='Back', command=lambda: controller.show_frame('StudentPage')).grid(row=3, columnspan=2, pady=10)

    def submit_return_book(self):
        username = self.entry_username.get()
        book_id = int(self.entry_book_id.get())
        return_date = datetime.date.today()

        if return_book(username, book_id, return_date):
            messagebox.showinfo('Return Book', 'Book returned successfully!')
        else:
            messagebox.showerror('Error', 'Failed to return book. Please check the details.')
class DeleteStudentPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ctk.CTkLabel(self, text='Delete Student', font=('Arial', 18)).pack(pady=10)
        frame_delete_student = ctk.CTkFrame(self)
        frame_delete_student.pack(pady=10)
        ctk.CTkLabel(frame_delete_student, text='Student username').grid(row=0, column=0)
        self.entry_username = ctk.CTkEntry(frame_delete_student)
        self.entry_username.grid(row=0, column=1)
        ctk.CTkButton(frame_delete_student, text='Delete Student', command=self.submit_delete_student).grid(row=1, columnspan=2, pady=10)
        ctk.CTkButton(frame_delete_student, text='Back', command=lambda: controller.show_frame('AdminPage')).grid(row=2, columnspan=2, pady=10)


    def submit_delete_student(self):
        username = self.entry_username.get()
        # Call the delete_student function passing the student_id
        if delete_student(username):
            messagebox.showinfo('Delete Student', 'Student deleted successfully!')
        else:
            messagebox.showerror('Error', 'Failed to delete student. Please try again.')

