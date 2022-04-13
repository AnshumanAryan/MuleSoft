import sqlite3
try:
    sqliteConnection = sqlite3.connect('MSmovies.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

cursor.execute("""CREATE TABLE Movies_Table (
    Movie_Name     VARCHAR PRIMARY KEY,
    Movie_Actor    VARCHAR,
    Movie_Actress  VARCHAR,
    Movie_Year     INTEGER,
    Movie_director VARCHAR,
    Movie_lang     VARCHAR
)""")

# Inserting data into table
cursor.execute("INSERT INTO Movies_Table VALUES('Lord Of the Rings','Elijah Wood','Liv Tyler','2014','Peter Jackson','English')")
print("Command executed successfully")
cursor.execute("INSERT INTO Movies_Table VALUES('The Dark Knight','Aaron Eckhart','Anne Hathaway','2014','Christopher Nolan','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Inception','Leonardo Dicaprio','Marion','2010','Christopher Nolan','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Naruto','Sasuke','Sakura','2007','Hayato','Japanes')")
cursor.execute("INSERT INTO Movies_Table VALUES('Pirates of Caribbean','Johnny Depp','Keira Knightly','2003','Gore Verbinski','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Attack on Titans','Levi','Historia Reiss','2009','Shinji Higuchi','Korean')")
cursor.execute("INSERT INTO Movies_Table VALUES('Death Note ','Nat Wolff','Margaret Qualley','2017','Adam Wingard','Japneese')")
cursor.execute("INSERT INTO Movies_Table VALUES('Harry Porter ','Daniel Radcliffe','Ema Watson','2001','David Yates','English')")

cursor.execute("SELECT * FROM Movies_Table")
movie_list = cursor.fetchall()
for i in movie_list:
    print (i)
print("\n")

f=0
name = input("Enter the actor name to print his movie:")
name = name.upper()         #to convert every input character to uppercase 
for i in movie_list:
    t=i[1].upper()          #converted to uppercase to check with input name
    if(t==name):
        cursor.execute("SELECT * FROM Movies_Table WHERE Movie_Actor='i[1]'")
        mov_list = cursor.fetchall()
        print(i)
        f=1
if(f==0):
    print("Actor not found in the database!!")
    cursor.close()
    sqliteConnection.close()
    print("The SQLite connection is closed")