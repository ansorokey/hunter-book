import sqlite3
from data import smallMonsters, largeMonsters, locales

# Establish the database we want to connect to
# (Assume we're running this from root directory)
dbPath = './backend/mhw.db'
db = sqlite3.connect(dbPath)

# Create a cursor
# (this is our connection to the database/will execute sql statements)
curs = db.cursor()

# DROP EXISTING DATA
curs.execute("""
DROP TABLE IF EXISTS large_monsters;
""")

curs.execute("""
DROP TABLE IF EXISTS small_monsters;
""")

curs.execute("""
DROP TABLE IF EXISTS locales;
""")

# Create tables
curs.execute("""
CREATE TABLE large_monsters (
    name varchar(20) PRIMARY KEY NOT NULL UNIQUE,
    type varchar(20),
    size varchar(5)
);
""")

curs.execute("""
CREATE TABLE small_monsters (
    name varchar(20) PRIMARY KEY NOT NULL UNIQUE,
    size varchar(5)
);
""")

curs.execute("""
CREATE TABLE locales (
    name varchar(20) PRIMARY KEY NOT NULL UNIQUE
)
""")

# Check tables were made
tableNames = curs.execute("SELECT name FROM sqlite_master;")
print(tableNames.fetchall())

curs.executemany("""
INSERT INTO large_monsters (name, type, size) VALUES (:name, :type, :size);
""", largeMonsters)

curs.executemany("""
INSERT INTO small_monsters (name, size) VALUES (:name, :size);
""", smallMonsters)

curs.executemany("""
INSERT INTO locales (name) VALUES (?);
""", locales)

print('Seed complete')
