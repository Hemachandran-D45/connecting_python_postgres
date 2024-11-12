import pg8000

# This block is used for database connection and executing commands

cur = None
conn = None

try:
     # Establishing the connection to the PostgreSQL database
    conn = pg8000.connect(
        host="localhost",  # The host where the database is running (localhost for local machine)
        database="postgres",  # The name of the database you're connecting to
        user="postgres",  # The database user 
        password="1234",  
        port="5432"  # The port the PostgreSQL service is listening on (default is 5432)
    )
# Creating a cursor object to interact with the database
    cur = conn.cursor()
        #cursor is an object that allows you to interact with the database by executing SQL commands and fetching results.
        # The cursor provides an interface between your Python code and the database to send SQL queries and retrieve data.



    #sql command to create table
    cur.execute(""" CREATE TABLE IF NOT EXISTS person(
                id int primary key,
                name varchar(30),
                age int,
                gender char
                );
    """) 

    # print("Table created successfully")

    #cur.execute() is used to send an SQL command to the database.
    #It takes an SQL statement as a string and executes it on the connected database.

    cur.execute("""INSERT INTO person(id,name,age,gender)
                VALUES(1,'Hemachandran',24,'m'),
                (2,'Hitesh',22,'m'),
                (3,'Ramachandran',33,'m'),
                (4,'Harichandran',17,'m'),
                (5,'Ravichandran',53,'m');

""")
    cur.execute("""select * from person where name = 'Hitesh';

""")
    result = cur.fetchone()
    print(result)

    cur.execute("""select * from person where age > 20
""")
    
    result1 = cur.fetchall()
    for row in result1:
        print(row)
    # print(result1)


     #Commit the transaction to save any changes made (inserting data, etc.)
    conn.commit()
    # print("changes commited")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cur:
        cur.close()  # Close the cursor (prevents memory leaks)
    if conn:
      conn.close()  # Close the connection to the database (releases resources)
    # print("Database connection closed.")


# Commonly Used execute() Methods:
# fetchone(): Retrieves the first row of the result .
# fetchall(): Retrieves all rows of the result.
# commit(): Used to save any changes made to the database (e.g., inserts, updates, or deletes). 
        # It is essential after running commands like INSERT, UPDATE, or DELETE.
