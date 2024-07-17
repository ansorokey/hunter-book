import sqlite3

# Establish the database we want to connect to
# (Assume we're running this from root directory)
db = sqlite3.connect('./backend/mhw.db')

# Create a cursor
# (this is our connection to the database/will execute sql statements)
curs = db.cursor()

# Save an executed query to a variable (is a sqlite3 cursor object)
all_mons = curs.execute("SELECT * FROM monsters")

# Iterate throught the data
for mon in all_mons:
    print(mon)
