import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):  # Create a function to connect to  mysq- database. 
    connection = None
    try:                                                               # May be my connection work or not just try.
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:                                                # if connection not work or any other thing just say e.
        print(f"The error '{e}' occurred")

    return connection                                                # get an active connection to operate database.


def execute_query(connection, query):
    cursor = connection.cursor()                                    # creat cursor -a pointer to endpoint that talk to database.
    try:
        cursor.execute(query)                                       # execute sql statment
        connection.commit()
        print("Query executed successfully")                         # Message if conncetion created and quert executed successfully.
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


