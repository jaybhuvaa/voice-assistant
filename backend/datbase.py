import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="jay81",
    database="voice_assistant"
)

# Create a cursor object
cursor = conn.cursor()

# SQL query to insert data
sql = "INSERT INTO demo (ID, Name) VALUES (2, 'John C martin')"
values = (1, "John")

# Execute the query
cursor.execute(sql, values)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
