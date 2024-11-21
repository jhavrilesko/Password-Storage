# Password Manager

 ## A simple password management system built using Python, SQLite3, and Argon2 for secure password hashing. This application allows users to:

 
 
 - Register new accounts

 - Log in with secure credentials

 - Add and store generated passwords for various services

 - Display stored passwords

 - Delete accounts

 
### Features

 - Password Generation: Automatically generates secure passwords for users.
 
 - User Authentication: Uses Argon2 for hashing and verifying passwords.
 
 - SQLite3 Database: Stores user credentials and service passwords securely.
 
 - User-Friendly Interface: Command-line interaction for easy usage.

### Table of Contents

 1. Installation
	
 2. Usage
		
 3. File Structure

 4. Technologies Used

 5. Future Improvements

 6. Installation


### Installation


Clone the Repository:

	git clone https://github.com/your-username/password-manager.git
	cd password-manager

	1. Install Required Packages: Ensure you have Python installed. Then, install the required dependencies:

		pip install -r requirements.txt
 
Add the following dependencies to requirements.txt if needed:

	argon2-cffi
Run the Application: Start the program with:

	python main.py
 
### Usage

Initial Setup

   1. On first run, the application initializes the database (passwords.db) with the required tables.
  
   2. Register a new user or log in with existing credentials.

After Logging In

   - Add a Password: Save generated passwords for different services.
  
   - View Stored Passwords: Display all saved passwords associated with your account.
  
  - Delete Account: Remove your account and associated data.
  
 -  Log Out: Exit the session.

### File Structure

 - main.py: The main script that handles user interaction and program flow.
 
 - database_manager.py: Manages SQLite database operations such as registration, login, password storage, and retrieval.
 
 - password_generator.py: Generates secure random passwords for user accounts.
 
Technologies Used

 - Python: Programming language for building the application.

- SQLite3: Embedded database for storing user data.

- Argon2: Secure password hashing algorithm for user authentication.

### Future Improvements

- Add an option to customize generated password length.

- Implement encryption for stored passwords using a library like cryptography.

- Create a graphical user interface (GUI) for improved usability.
  
- Add multi-user support for accessing shared credentials.
  
### Contribution
  Contributions are welcome! To contribute:

  - Fork the repository.

  - Create a new branch for your feature (git checkout -b feature-name).

  - Commit your changes (git commit -m "Add new feature").

  - Push to your branch (git push origin feature-name).

  - Open a pull request.

### License

This project is licensed under the MIT License.

### Contact

For questions or feedback, reach out to:

Name: Jake Havrilesko

Email: havrileskojake@gmail.com

GitHub: jhavrilesko



<!-- sqlite operational error = reset tables.
  1. open shell 
    python

    import sqlite3
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS passwords;")
cursor.execute("DROP TABLE IF EXISTS users;")
conn.commit()
print("Tables dropped successfully.")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        service TEXT NOT NULL,
        password TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
""")
conn.commit()
print("Tables recreated successfully.")


cursor.execute("PRAGMA table_info(users);")
print("Users Table Schema:", cursor.fetchall())

cursor.execute("PRAGMA table_info(passwords);")
print("Passwords Table Schema:", cursor.fetchall())


conn.close()
exit()
-->


    
