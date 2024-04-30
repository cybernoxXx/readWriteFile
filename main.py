def writeToFile(fileName, content):
    with open(fileName, "w") as myFile:
        myFile.write(content)


def appendToFile(fileName, content):
    with open(fileName, "a") as myFile:
        myFile.write(content)

def readFromFile(fileName):
    with open(fileName, "r") as myFile:
        content = myFile.read()
    return content

writeToFile("greet.txt", "Hello!\n")
appendToFile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"