import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import datetime
from datetime import date


conn = create_connection('test1.cukicjxpnl1a.us-east-2.rds.amazonaws.com', 'admin', '12345free', 'test1db')


def create_table():   #create table.

    create_zoo = """
    create table if not exists zoo  (
    id INT (6) unsigned auto_increment,  
    animal varchar(30) not null,
    gender varchar(30) not null,
    subtype varchar(30) not null,
    age  INT(6) unsigned,
    color varchar(30) not null,
    PRIMARY KEY (id)
    )
    """
    execute_query(conn, create_zoo ) # Call function to execute query.

    #create a table on mysql database with name destination. having column id, date, animalid, comment.
def create_logs_table():   #create table.

    create_logs = """
    create table if not exists logs(  
    id INT (6) unsigned auto_increment,
    date DATE,  
    animalid varchar(30) not null,
    comment MEDIUMTEXT NULL  ,
    PRIMARY KEY (id)
    )
    """
    print('table created')
    execute_query(conn, create_logs )

    

def zoo_insert():

   
    insert1 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES (' lion', 'male','Asiatic', '9_years','orange');"
    insert2 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES ('lion', 'female','Asiatic', '8_years','orange_black');"
    insert3 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES (' monkey', 'male','gorella', '7 years','gray');"
    insert4 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES (' squirrel', 'male','Mini' ,'3 years','black and white');"
    insert5 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES (' gorillas', 'male','lowland', '15 years','brown');"
    insert6 = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES (' gorillas', 'female','lowland' ,'5 years','black and brown');"

   
    execute_query(conn, insert1)
    execute_query(conn, insert2)
    execute_query(conn, insert3)
    execute_query(conn, insert4)
    execute_query(conn, insert5)
    execute_query(conn, insert6)
    print('Data inserted')


def logs_insert():

    qry1 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), '1' , ' old male lion in zoo);"
    qry2 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), '2' , ' old female lion in zoo);"
    qry3 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), '3' , ' old male monkey in zoo');"
    qry4 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), '4' , '' old male  squirrel in zoo ');"
    qry5 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(),  '5', '' old male gorillas in zoo ');"
    qry6 = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), '6' , '' old female gorillas in zoo ');"

    execute_query(conn, qry1)
    execute_query(conn, qry2)
    execute_query(conn, qry3)
    execute_query(conn, qry4)
    execute_query(conn, qry5)
    execute_query(conn, qry6)
    print('Logs Data inserted')

  



if __name__ == '__main__':
    create_table()
    create_logs_table()
    zoo_insert()
    logs_insert()


