import mysql.connector

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='root',       # Replace with your MySQL user
            password='password'  # Replace with your MySQL password
        )

        # Create a cursor to execute the query
        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Print success message
        print("Database 'alx_book_store' created successfully!")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:  # Handle errors specifically related to MySQL
        print(f"Error: {e}")

# Execute the function to create the database
create_database()
