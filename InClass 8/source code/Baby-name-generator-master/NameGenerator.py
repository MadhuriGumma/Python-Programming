
import random

    #OccuranceMap is a map of map. Its keys are some chars based on the Markove order and its values are the map containing
    # characters following the keys and the number of times they occur
def buildMap(order,gender):
    listOfNames = []
    if gender.lstrip() == 'b':
        fileName = "namesBoys.txt"
    elif gender.lstrip() == 'g':
        fileName = "namesGirls.txt"
    else:
        exit("Please only enter b or g")
        #Building a list of names and append '_' to their beginning and end
    with open(fileName, 'r') as names:
        for name in names:
            listOfNames.append("_"*order + name.lower() + "_"*order)
    occuranceMap = {}
    #loop through every name in the list
    for n in listOfNames:
        #Loop through characters within a name to find the keys and their following chars
        for index in range(0, len(n) - order):
            key = n[index:order + index]
            nextChar = n[index + order:index + order + 1]
            #Check for existance of the key
            if key in occuranceMap:
                currentMap = occuranceMap[key]
                if nextChar in currentMap:
                    currentMap[nextChar] += 1
                else:
                    currentMap[nextChar] = 1
                occuranceMap[key] = currentMap
            else:
                newEntry = {}
                newEntry[nextChar] = 1
                occuranceMap[key] = newEntry
    return occuranceMap

# This is a simple method to retrieve the chars that follow a specific key. For example the chars that follow "FG"
def getCharsForKey(key, map):
    chars = map[key]
    return chars

#Based on what the is the currenr generated sequence of chars for the name, this method generates a new char
def generateNextChar(order,name, map):
    chars = getCharsForKey(name[len(name) - order:len(name)], map)
    #We build a list that contains every char that follows our key. The number of times they appear in the list
    # depends on the number of times they apprear after our key.
    listOfChars = []
    charsMap = list(chars.items())
    for (key, value) in charsMap:
        for i in range(0, value):
            listOfChars.append(key)
    # Now that we have a list of candidate chars, we generate a random index to pick up a char. It's obvious that
    #Chars with higher occurance have higher chance of being picked
    randomIndex = random.randint(0, len(listOfChars) - 1)
    selectedLetter = listOfChars[randomIndex]
    return selectedLetter



def generateNewNames(minLength, maxLlength, order,count, gender):
    print("**************************************")
    print("**************************************")
    print("Here are generated names. Hope you like them! :)")
    #OccuranceMap is a map of map. Its keys are some chars based on the Markove order and its values are the map containing
    # characters following the keys and the number of times they occur
    occuranceMap = buildMap(order, gender)
    c = 0
    # We iterate through the loop until we get the desired number of names
    while (c < count):
        #Initiate the name with the '_' character. the number this character should be repeated depends on the markove order
        name = "_" * order
        while len(name) < maxLlength + order:
            char = generateNextChar(order,name, occuranceMap)
            if char == '_':
                break
            name += char
        #Remome some unwanted characters
        generatedName = name.replace('\n', '').replace('\r', '')
        # WE only accept names that their length is bigger than minL
        if (len(generatedName[order:]) > minLength ):
            print(generatedName[order:])
            c += 1
