# Followed along from documentation
# [https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial]

# Import sqlite3 package
import sqlite3

# Choose the database to connect to
# Will create database of the name if it cannot be found
con = sqlite3.connect('./backend/tutorial.db') # Path based on where the file was executed FROM (running from root)

# Create a cursor
# Connects to the database, is what we will use to execute statements
cur = con.cursor()

# Create a table using raw SQL
cur.execute('CREATE TABLE movie(title, year, score)')
