import sqlite3
from data import monsters

# Establish the database we want to connect to
# (Assume we're running this from root directory)
dbPath = './backend/mhw.db'
db = sqlite3.connect(dbPath)

# Create a cursor
# (this is our connection to the database/will execute sql statements)
curs = db.cursor()

# DROP EXISTING DATA
curs.execute("""
DROP TABLE IF EXISTS monsters;
""")

# Create tables
curs.execute("""
CREATE TABLE monsters (
    monsterId integer PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL UNIQUE,
    type varchar(20),
    size varchar(5)
);
""")

# Check tables were made
tableNames = curs.execute("SELECT name FROM sqlite_master;")
print(tableNames.fetchall())

curs.executemany("""
INSERT INTO monsters (name, size) VALUES (?, ?);
""", monsters)

checkMonsters = curs.execute("""
SELECT * from MONSTERS limit 5;
""");

print(checkMonsters.fetchall())
