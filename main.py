import sqlite3

# Creates an empty database
connection = sqlite3.connect("gta.db")

# Cursor Object is needed to use SQL commands
# This is needed for communication with the database
cursor = connection.cursor()

# Use Cursor Object to create a table with SQL within the gta database
cursor.execute("CREATE TABLE gta (release_year integer, release_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

# Method Executemany is necessary for inserting multiple rows into a table
cursor.executemany("INSERT INTO gta VALUES (?, ?, ?)", release_list)

# Reads from table and prints every row in the table
for row in cursor.execute("SELECT * FROM gta"):
    print(row)

# Selects specific rows from gta table
# Set 'c' to be represented as a key where its value is 'Liberty City'
print("******************************************")
cursor.execute("SELECT * FROM gta WHERE city=:c", {"c": "Liberty City"})
gta_search = cursor.fetchall()
print(gta_search)

cursor.execute("CREATE TABLE cities (gta_city text, real_city text)")
cursor.execute("INSERT INTO cities VALUES (?, ?)", ("Liberty City", "New York"))
cursor.execute("SELECT * FROM cities WHERE gta_city=:c", {"c": "Liberty City"})
cities_search = cursor.fetchall()

print(cities_search)

# Closed connection to database
connection.close()