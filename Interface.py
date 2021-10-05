import dbase
#-----------------------Warning---------------------------. 
def databaseCreation():
    #use this code only for creating and then comment it. 
    dbase.createdb()
#----------------------Warning----------------------------.
def addingMulRecord():
    MovieList = []
    n = int(input("PLEASE ENTER NUMBER OF ENTRIES: "))
    print("PLESE ENTER THE DETAILS IN MOVIE_NAME, ACTOR_NAME, ACTRESS NAME, YEAR, DIRECTOR_NAME")
    for i in range(n):
        k = tuple(input().split())
        MovieList.append(k)
    dbase.addMany_record(MovieList)



def addingSingleRecord():
    movie = input("Please Enter Movie Name: ")
    actor = input("Please Enter Actor Name: ")
    actress = input("Please Enter Actress Name: ")
    year = input("Please Enter Year: ")
    director = input("Please Enter Director Name: ")
    dbase.add_record(movie, actor, actress, year, director)

def deletingOneRecord():
    Dactor = input("Please Enter the Actor name to delete the record: ")
    dbase.delete_record(Dactor)

def ActorLookup():
    Factor = input("Please Enter The Actor Name for his movie details:  ")
    dbase.Lookup(Factor)

def ShowDB():
    print("THE MOVIE DATABASE IS: ")
    dbase.showall()

print("""1.Create DataBase(!NOTE: USE THIS FUNCTION ONLU ONCE!)
2. Add Multiple Records.
3. Add Single Record.
4. Delete Single Record.
5. Find Actor Details.
6. Show DATABASE.
""")
Data = int(input())
if Data == 1:
    databaseCreation()
elif Data == 2:
    addingMulRecord()
    dbase.showall()
elif Data == 3:
    addingSingleRecord()
    dbase.showall()
elif Data == 4:
    deletingOneRecord()
    dbase.showall()
elif Data == 5:
    ActorLookup()
elif Data == 6:
    ShowDB()
else:
    print("PLEASE ENTER VALID NUMBER")



