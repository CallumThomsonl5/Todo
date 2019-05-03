#!/usr/bin/python3
import json, sys, os

print(sys.platform)    

def getHomeDir():
    homedir = os.environ['HOME']
    return homedir

template = {
    '1': 'First Todo'
}

help = """add: adds todo
exit: exits program
list: lists todos
delete: deletes todo"""

try:
    os.mkdir("{}/.todo".format(getHomeDir()))
    os.system("rm -r {}/.todo".format(getHomeDir()))
    database = open("{}/.todo".format(getHomeDir()), 'w+')
    database.write(json.dumps(template))
    database.close()
    print("Created {}/.todo".format(getHomeDir()))
    print("Reading todo database from {}/.todo".format(getHomeDir()))
except:
    print("Reading todo database from {}/.todo".format(getHomeDir()))

while True:
    input1 = input("> ").lower().strip()
    database = open("{}/.todo".format(getHomeDir()), 'r')
    readData = json.load(database)
    
    if input1 == "exit":
        sys.exit()
    elif input1 == "add":
        add = input("What would you like to add to todo list?: ")
        print("Added {} to your todo list.".format(add))
        i = 0
        for x in readData:
            i = i + 1
        x = i+1
        newList = {
            x:add
        }
        readData.update(newList)

        dataFile = open('{}/.todo'.format(getHomeDir()), 'w')
        json.dump(readData, dataFile)
        dataFile.close()
        database.close()


        
    elif input1 == "list":
        for x in readData:
            print(x, readData[x])
    elif input1 == "help":
        print(help)
    elif input1 == "clear":
        for x in range(50):
            print(">\n>")
    elif input1 == "delete":
        input2 = input("Which entry would you like to delete?: ")

        readDataDelEhh = open("{}/.todo".format(getHomeDir()), 'w')
        del readData[input2]
        json.dump(readData, readDataDelEhh)
        print("Removed todo", input2)
        readDataDelEhh.close()
        database.close()
    else:
        print("Unknown command")
        print(help)

