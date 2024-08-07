import sqlite3
from data import smallMonsters, largeMonsters, locales

# Establish the database we want to connect to
# (Assume we're running this from root directory)
dbPath = './backend/mhw.db'
db = sqlite3.connect(dbPath)

# Create a cursor
# (this is our connection to the database/will execute sql statements)
curs = db.cursor()

# Drop existing tables
curs.execute("""
DROP TABLE IF EXISTS large_monsters;
""")

curs.execute("""
DROP TABLE IF EXISTS small_monsters;
""")

curs.execute("""
DROP TABLE IF EXISTS locales;
""")

curs.execute("""
DROP TABLE IF EXISTS monster_locales;
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

# Polymorphic many to many table, foreign key points to two tables
curs.execute("""
CREATE TABLE monster_locales (
    monster_name varchar(20) NOT NULL,
    monster_size varchar(5) NOT NULL,
    locale_name varchar(20) NOT NULL,
    FOREIGN KEY (monster_name)
        references large_monsters (name)
            ON DELETE CASCADE
    FOREIGN KEY (monster_name)
        references small_monsters (name)
             ON DELETE CASCADE
    FOREIGN KEY (locale_name)
        references locales (name)
            ON DELETE CASCADE
);
""")

# Check tables were made
tableNames = curs.execute("SELECT name FROM sqlite_master;")
print(tableNames.fetchall())

# Insert data into tables
curs.executemany("""
INSERT INTO large_monsters (name, type, size) VALUES (:name, :type, :size);
""", largeMonsters)

curs.executemany("""
INSERT INTO small_monsters (name, size) VALUES (:name, :size);
""", smallMonsters)

curs.executemany("""
INSERT INTO locales (name) VALUES (?);
""", locales)

# Seed Monster_locations
for mon in largeMonsters:
    if 'locales' in mon:
        for l in mon['locales']:
            curs.execute("""
            INSERT INTO monster_locales (monster_name, monster_size, locale_name) VALUES (?,?,?)
            """, (mon['name'], mon['size'], l))

# Save actions to database
db.commit()
