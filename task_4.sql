-- Use the provided database
USE alx_book_store;

-- Query the information_schema to get the details of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' 
AND TABLE_NAME = 'Books';
