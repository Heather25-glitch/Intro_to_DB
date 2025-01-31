import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL user
            password='password'  # Replace with your MySQL password
        )

        # Check if connection was successful
        if connection.is_connected():
            cursor = connection.cursor()

            # Attempt to create the database (no SELECT or SHOW commands involved)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Close the cursor and connection
            cursor.close()
            connection.close()

    except Error as e:  # Handle MySQL-specific errors
        print(f"Error: {e}")

# Execute the function to create the database
create_database()
