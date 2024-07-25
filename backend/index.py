
from data import largeMonsters, smallMonsters

for m in largeMonsters:
    m['locales'] = []

# Open the file - a flag to append (write to the end of the file)
# f = open('data.py', 'a')
# f.write('largeMonsters = [\n')
# for m in largeMonsters:
#     f.write(str(m) + ',\n')

# import sqlite3

# def pause():
#     res = input()

#     if res == "" or res != "":
#         return

# startProgram = False
# def menu():
#     print("""
#         1. View large monsters
#         2. View small monsters
#         3. View locales
#         Q. Quit program
#     """)

#     userInput = input()

#     if userInput == '1':
#         print('Gathering monster data...')
#         db = sqlite3.connect('./backend/mhw.db')
#         curs = db.cursor()
#         allMons = curs.execute('SELECT * FROM large_monsters;')
#         for mon in allMons:
#             print(mon)
#         db.close()
#         print('Press enter to continue')
#         pause()

#     elif userInput == 'q' or 'Q':
#         print('exiting')
#         global startProgram
#         startProgram = False
#     else:
#         print('No action for selected input')

# while startProgram:
#     menu()
