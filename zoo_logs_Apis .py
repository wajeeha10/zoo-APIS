# Define all connection functions.
# import connection , execute, read query, and date function fron their  respective libraries.
#Import flask and required functions.
import mysql.connector
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import flask
from flask import jsonify
from flask import request


# creating connection to mysql database.
# provide  compleate database address, username, id , passward  to connection function and access database. 
conn = create_connection('test1.cukicjxpnl1a.us-east-2.rds.amazonaws.com', 'admin', '12345free', 'test1db')


# setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser


# CREATE AN API FOR ZOO
@app.route('/', methods=['GET']) # default url without any routing as GET request ,a route is created http://127.0.0.1:5000/
def zoo():
    return "<h1> WELCOME TO THE ZOO /n nihal padora </h1>"

#get route http://127.0.0.1:5000/


# Create an API to get all data from zoo table

# CREATE CRUD APIS FOR ZOO TABLE. 

# 1. SET READ ZOO TABLE FROM DATA BASE (test1db).
@app.route('/api/animal/all', methods=['GET']) #endpoint to get all the animals:  http://127.0.0.1:5000/api/animal/all
def all_animals():
    sql = "SELECT * FROM zoo"   #pointer to select zoo table.
    users = execute_read_query(conn, sql) # read gata from zoo table. run querry
    return jsonify(users)                # returns list of all data from zoo table.


# 2. SET API TO ENTER NEW ANIMAL IN ZOO TABLE ON DATA BASE (test1db) .

@app.route('/api/animal', methods=['POST']) # add animal as POST:  http://127.0.0.1:5000/api/animal
def new_animal():          
    request_data = request.get_json() 
    # get new animal information to add on zoo table       
    newname = request_data['animal']
    newgender = request_data['gender']
    newsubtype = request_data['subtype']
    newage = request_data['age']
    newcolor = request_data['color']  
    # insert  new information into trip.                     
    insertn = "INSERT INTO zoo(animal, gender, subtype, age, color) VALUES ('%s' ,'%s' ,'%s' ,'%s' ,'%s')"  %(newname, newgender,newsubtype, newage, newcolor) 
    try: #check for error.
        execute_query(conn, insertn) #run querry
        # give update to  log table, saying that an animal was added.
        #APPLY SELECT QUERY THAT FATCH NEWANIMAL ID FROM ZOO TABLE ( ON DATA BASE (test1db)) TO INSERT IT INTO LOG TABLE.
        newid = "Select id from zoo where animal='%s' AND gender='%s' AND subtype='%s' AND age ='%s' AND color ='%s'" %(newname, newgender,newsubtype, newage, newcolor)
        addid = execute_read_query(conn, newid) #run querry
        animal_id = addid[0]["id"] #Get in from addid_list where id is stored in a json object
        comment = "A %s was added to zoo" % (newname) #insert updated comment.
        insertlog = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), %s , '%s')" %(animal_id, comment) #Apply sysdate() function to get current date on batabase.
        execute_query(conn, insertlog) #run querry
        return 'Add request auccessful'
    except Error as e:
        return f"the error {e} occured "

# 3. SET API TO UPDATE DESIRED ANIMAL FROM ZOO  (ON DATA BASE (test1db).
@app.route('/api/animal', methods=['PUT']) #endppoint to update a single animal by id: http://127.0.0.1:5000/api/animal?id=1 (let update id = 1)
def api_id():
    if 'id' in request.args: #only if an id is provided as an argument, proceed
        id = int(request.args['id'])
        request_data = request.get_json()
        # get updated for all colunm of zoo table.
        new_name = request_data["animal"]
        new_gender = request_data["gender"]
        new_subtype = request_data["subtype"]
        new_age =  request_data["age"] 
        new_color = request_data["color"]
        # use Update command to update desired animal.
        query = """UPDATE zoo SET animal = '%s' ,gender = '%s' , subtype = '%s' ,  age = '%s' , color = '%s' WHERE id = '%s'"""  %(new_name, new_gender, new_subtype, new_age, new_color, id)                            
        try:
            execute_query(conn, query) #run querry
        # set querry to provide updated animal id and comment to  log table.
            ucomment = "A %s was update to zoo on  %s id " % (new_name, id)
            insertlog = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), %s , '%s')" %(id, ucomment) #Apply sysdate() function to get current date on batabase.
            execute_query(conn, insertlog) #run querry
            return f"updated id {id} entry"
        except Error as e:
            return f"the error {e} occured"

    else:
        return 'ERROR: No ID provided!'
    

# 4. SET API TO DELETE ANIMAL FROM ZOO TABLE ON DATA BASE (test1db).

@app.route('/api/animal', methods=['DELETE']) # #endppoint to update a single animal by id: http://127.0.0.1:5000/api/animal?id=1 (let delete id = 1)
def delete_animal():       
    request_data = request.get_json()  
    idToDelete = request_data['id']                       
    delete_statement = "DELETE FROM zoo WHERE id = '%s'" % (idToDelete)  #set delete querry to delete animal from zoo table.
    execute_query(conn, delete_statement) #run querry
    delcomment = "A %s was deleted from zoo" % (newname)
    #set querry to provide deleted animal id and comment to  log table. 
    insertlog = "INSERT INTO logs(date, animalid, comment) VALUES (sysdate(), %s , '%s')" %(idToDelete, delcomment) #Apply sysdate() function to get current date on batabase.
    execute_query(conn, insertlog) #run querry
    return "delete request successful"


# For logs table

#5. CREAT API TO READ LOGS TABLE FROM DATA BASE (test1db).
@app.route('/api/logs/all', methods=['GET']) # returns all logs:  http://127.0.0.1:5000/api/logs/all
def all_logs():
    sqlogs = "SELECT * FROM logs"
    readlogs = execute_read_query(conn, sqlogs) #run querry

    return jsonify(readlogs)

#6. CREAT API TO RESET LOGS TABLE FROM DATA BASE (test1db).
@app.route('/api/logs', methods=['DELETE']) #API to get a user reset command  http://127.0.0.1:5000/api/logs?reset=true
def clear():
    reset =  request.args["reset"]

    if reset == "true":                        
       cleartable = "DELETE FROM logs "
       execute_query(conn,  cleartable) #run querry

       return "reset all successful"

app.run()