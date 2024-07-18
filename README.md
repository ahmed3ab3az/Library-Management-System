
---

# Library Management System

## Overview

The Library Management System is designed to streamline and manage the various operations of a university library. This project provides functionalities to manage books, users, and transactions in a SQL Server database, along with a graphical user interface for ease of use.

## Features

- **Book Management**: Add, edit, delete, and display books in the library.
- **User Management**: Sign up, sign in, update user details, and delete users.
- **Transaction Management**: Borrow and return books, and manage due dates.
- **Database Connectivity**: Seamless connection to a SQL Server database using pyodbc.
- **Graphical User Interface**: User-friendly GUI for interacting with the library system.

## Getting Started

### Prerequisites

- Python 3.x
- pyodbc library
- customtkinter , tkinter for GUI libraries
- SQL Server with the `UniversityLibrary` database

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ahmed3ab3az/Library-Management-System.git
    cd Library-Management-System
    ```

2. Install the required Python packages:
    ```sh
    pip install pyodbc
    ```

3. Configure the SQL Server connection in `Queries.py`:
    ```python
    server = 'YOUR_SERVER_NAME'  # Replace with your server name
    database = 'UniversityLibrary'  # Database name
    driver = 'ODBC Driver 17 for SQL Server'  # ODBC driver
    ```

### Usage

1. **Running the GUI**:
    ```sh
    python GUI.py
    ```

2. **Interacting with the Library System**:
    - **Sign Up**: Create a new user account (admin or student).
    - **Sign In**: Log in with your credentials.
    - **Add/Edit/Delete Books**: Manage the book inventory.
    - **Borrow/Return Books**: Handle book borrowing and returning transactions.
    - **Update User Details**: Modify user information.
    - **Delete User**: Remove a user account from the system.
    - **Display Books**: View all available books in the library.

## File Descriptions

- `Queries.py`: Contains all the functions to interact with the SQL Server database, such as adding, editing, deleting books, and managing users and transactions.
- `GUI.py`: Implements the graphical user interface for the library management system, allowing users to interact with the system through a user-friendly interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact:

- Ahmed Abaza: [ahmed3ab3az@gmail.com](mailto:ahmed3ab3az@gmail.com)

---
