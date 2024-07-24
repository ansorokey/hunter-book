
# from data import largeMonsters, smallMonsters

# res = []
# for m in smallMonsters:
#     mon = {
#         'name': m[0],
#         'size': m[1]
#     }
#     res.append(mon)

# # Open the file - a flag to append (write to the end of the file)
# f = open('./data.py', 'a')
# f.write('smallMonsters = {0}'.format(res))
import sqlite3

def pause():
    res = input()

    if res == "":
        return

startProgram = True
def menu():
    print("""
        1. View large monsters
        2. View small monsters
        3. View locales
        Q. Quit program
    """)

    userInput = input()

    if userInput == '1':
        print('Gathering monster data...')
        db = sqlite3.connect('./backend/mhw.db')
        curs = db.cursor()
        allMons = curs.execute('SELECT * FROM large_monsters;')
        for mon in allMons:
            print(mon)
        print('Press enter to continue')
        pause()

    elif userInput == 'q' or 'Q':
        print('exiting')
        global startProgram
        startProgram = False
    else:
        print('No action for selected input')

while startProgram:
    menu()
