import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL user
            password='password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            # Create a cursor object to interact with the MySQL server
            cursor = connection.cursor()

            # SQL query to create database (without using SELECT or SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Close the cursor and connection
            cursor.close()
            connection.close()

    except Error as e:
        print(f"Error: {e}")

# Run the function to create the database
create_database()
