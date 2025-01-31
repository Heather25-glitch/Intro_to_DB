import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server (without SELECT or SHOW)
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL user
            password='password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor to execute SQL commands
            cursor = connection.cursor()

            # Create the database if it doesn't exist (no SELECT or SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Close the cursor and connection
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")

# Execute the function to create the database
create_database()
