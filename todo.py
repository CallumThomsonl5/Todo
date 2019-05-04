#!/usr/bin/python3
import json, sys, os
 
def main(isfirstrun):
    def getHomeDir():
        homedir = os.environ['HOME']
        return homedir

    template = {
        '1': 'First Todo'
    }

    help = """add Adds todo entries
remove, delete Removes todo entries
list Lists entries
clear Clears screen 
help, ? Shows this help menu
exit Exits program
wipeall Wipes all entries"""

    try:
        os.mkdir("{}/.todo".format(getHomeDir()))
        os.system("rm -r {}/.todo".format(getHomeDir()))
        database = open("{}/.todo".format(getHomeDir()), 'w+')
        database.write(json.dumps(template))
        database.close()
        print("Created {}/.todo".format(getHomeDir()))
        print("Reading todo database from {}/.todo".format(getHomeDir()))
    except:
        if isfirstrun:
            print("Reading todo database from {}/.todo".format(getHomeDir()))
    try:
        while True:
            input1 = input("> ").lower().strip()
            database = open("{}/.todo".format(getHomeDir()), 'r')
            readData = json.load(database)
            
            if input1 in "exit quit".split():
                sys.exit()
            elif input1 == "list" or input1 == "ls":
                for x in readData:
                    print("["+x+"]", readData[x])
            elif input1 == "help" or input1 == "?":
                print(help)
            elif input1 == "clear":
                for x in range(50):
                    print(">\n>")
            elif input1 == "delete" or input1 == "remove":
                input2 = input("Which entry would you like to delete?: ")

                try:
                    del readData[input2]
                    writeData = open("{}/.todo".format(getHomeDir()), 'w')
                    json.dump(readData, writeData)
                    print("Removed todo", input2)
                    writeData.close()
                    database.close()
                except:
                    print("This todo does not exist")
            elif input1 == "add":
                #Input
                add = input("What would you like to add to todo list?: ")
                
                #Notify user that todo is added
                print("Added {} to your todo list.".format(add))
                
                #Get data to put in file
                for x in readData:
                    i = x
                
                try:
                    checkhasvalue = i
                except UnboundLocalError:
                    i = 0

                i = int(i)
                i += 1
                i = str(i)
                newList = {
                    i:add
                }

                #Update file
                readData.update(newList)
                dataFile = open('{}/.todo'.format(getHomeDir()), 'w')
                json.dump(readData, dataFile)
                dataFile.close()
                database.close()
            elif input1 == "":
                pass
            elif input1 == "wipeall":
                areyousure = input("Are you sure you want to delete all entries? [Y][N]: ").lower().strip()
                if areyousure == "y":
                    os.system("rm {}/.todo".format(getHomeDir()))
                    print("Deleted all entries")
                    print("Restarting...")
                    program = sys.executable
                    os.execl(program, program, * sys.argv)
                elif areyousure == "n":
                    print("Cancelled")
                else:
                    print("You didn't enter y or n")
            else:
                print("{}: command not found".format(input1))
                print("Type ? to see list of commands")
    except KeyboardInterrupt:
        print("To exit, type exit or quit")
        main(False)

if sys.platform == "linux" or sys.platform == "linux2":
    main(True)
else:
    print("This program only works on linux, if you really want to use an inferior OS then the code can be easily modified to work on other systems.")
