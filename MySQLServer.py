import MySQLdb
from MySQLdb import OperationalError

def create_database():
    try:
        # Connect to MySQL without using SELECT or SHOW queries
        connection = MySQLdb.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL user
            password='password'  # Replace with your MySQL password
        )

        cursor = connection.cursor()

        # Create the database if it doesn't exist (no SELECT or SHOW used)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except OperationalError as e:  # Catch specific errors for MySQL
        print(f"Error: {e}")

# Execute the function to create the database
create_database()
