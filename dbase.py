import sqlite3
def createdb():
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()   
    cur.execute(""" CREATE TABLE Movies(
    movie_name text,
    actor_name text,
    actress_name text,
    year_release integer,
    director_name text
   )""")
def showall():
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()


    #Quering the database
    cur.execute("SELECT * FROM Movies")
    items = cur.fetchall()
    print("Movie","\t\t ","ACTOR"," \t\t","ACTRESS","\t\t ", "YEAR","\t\t ","DIRECTOR")
    print("------","\t\t ","------"," \t\t","--------","\t\t", "-----","\t\t ","---------")
    for i in items:
        print(i[0], "\t \t",i[1],"\t \t", i[2],"\t\t",i[3],"\t \t",i[4])

    #comit and close
    con.commit()
    con.close()
    
def add_record(movies, actors, actress, year, director):
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()
    #adding data to db
    cur.execute("INSERT INTO Movies VALUES (?, ?, ?, ?, ?)",(movies, actors, actress, year, director))
    print("Record Inserted Sucessfully...")
    #comit and close
    con.commit()
    con.close()

def delete_record(id):
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor() 
    #deleting the record
    cur.execute("DELETE FROM Movies WHERE actor_name = (?)", (id,))
    print("Record Removed Sucessfully...")
    #comit and close
    con.commit()
    con.close()

def addMany_record(LIST):
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor()
    #adding multiple data items
    cur.executemany("INSERT INTO Movies VALUES (?, ?, ?, ?, ?)",(LIST))
    print("Record Inserted Sucessfully...")
    #comit and close
    con.commit()
    con.close()

def Lookup(actor_details):
    #connection to db and cursor
    con = sqlite3.connect('Movie.db')
    cur = con.cursor() 
    #searching the actors
    cur.execute("SELECT * FROM Movies WHERE actor_name = (?)", (actor_details,))
    items = cur.fetchall()
    print("ACTOR"," ", "MOVIE NAME")
    print("-----"," ", "---------")
    for i in items:
        print(i[1]," ", i[0])  
    #comit and close
    con.commit()
    con.close()    

