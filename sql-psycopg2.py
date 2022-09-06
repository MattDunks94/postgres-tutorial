# Carry out the following, in the termianl, to run project:
# pip3 install psycopg2
# pip3 install SQLAlchemy
# set_pg
# psql
# CREATE DATABASE chinook;
# \c chinook (To switch to the chinook db)
# Within chinook db: \i Chinook_PostgreSql.sql 

import psycopg2


# Connect to 'chinook' database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database. (similar to an Array, List)
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table.
# (Use the cursor.fetchall())
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table.
# (Use the cursor.fetchall())
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only "Queen" from the "Artist" table.
# (Use the cursor.fetchone())
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select only "ArtistId" #51 from the "Artist" table.
# (Use the cursor.fetchone())
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
# (Use the cursor.fetchall())
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Select all tracks where the composer is "Queen" from 
# the "Track" table.
# (Use the cursor.fetchall())
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print results by iterating through them using a for loop.
for result in results:
    print(result)