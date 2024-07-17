# Followed along from documentation
# [https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial]

# Import sqlite3 package
import sqlite3

# Let's make a string that represents our path
dbPath = './backend/tutorial.db'

# Choose the database to connect to
# Will create database of the name if it cannot be found
con = sqlite3.connect(dbPath) # Path based on where the file was executed FROM (running from root)

# Create a cursor
# Connects to the database, is what we will use to execute statements
cur = con.cursor()

# THis file creates a table, so delete it to run multiple times
cur.execute('DROP TABLE IF EXISTS movie')

# Create a table using raw SQL
cur.execute('CREATE TABLE movie(title, year, score)')

# Query a table's name from the master schema
# result is a sqlite object
res = cur.execute('SELECT name FROM sqlite_master')

# Use a fetch function to pull a single result as a tuple
print(res.fetchone())

# Query a nonexistant table
nores = cur.execute('SELECT name FROM sqlite_master WHERE name="noexist"')
print(nores.fetchone() is None) # Returns a None result

# Use python literals to run an insert statement to the movie table
cur.execute("""
INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
""")

# An insert statement opens a transaction
# A transaction is not saved into the database until commited
# Run to save changes
con.commit()

# Check to see data was added properly by fetching all scores
res = cur.execute('SELECT score FROM movie')
print(res.fetchall())

# We can insert more data more easily using collections and placeholders
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

# .executemany() will iterate through each item in the collection
# The ? placeholder is best practice, and safeguards against sql injection that happens with string formatting
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)

# Remember to commit after inserting
con.commit()

# Check data was added by iterating over result directly
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

# We can now close the connection
con.close()

# Check everything saved by reopening a new connection and querying again
new_con = sqlite3.connect(dbPath)
new_cur = new_con.cursor()

res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")

title, year = res.fetchone() # returns one result as a tuple, we can immediately destructure/assign to variables

print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

new_con.close()
