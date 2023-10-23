"""
projekt_1.py: prvni projekt do Engeto Online Python Akademie
author: Patrik Bocek
email: patrik.bocek@tria-tr.cz
discord: Patrik B fallencz#2217
"""


import re
'''
author =
'''
texts = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

logins = [["bob", "123"], ["ann", "pass123"], ["mike", "password123"], ["liz", "pass123"]]



def login():
    username = input("username:")
    password = input("password:")
    x = 0
    for i in logins:
        if username == i[0] and password == i[1]:
            print(f'Welcome, {username}')
            chooseText()
            break
        test = len(logins) - 1
        if  x == len(logins) - 1:
            print("Incorrect username or password")
        x += 1
        

def chooseText():
    choice = input(f'Choose Text [1-{len(texts)}]:')

    try:    
        if int(choice) <= len(texts):
            analyzeText(int(choice))
        else:
            print(f'Please use a number from 1-{len(texts)}')
            
    except:
        print(f'Please use a number from 1-{len(texts)}')
        exit()


    

    
def analyzeText(choice):
    wordCount = 0
    numberCount = 0
    upperWords = 0
    lowerWords = 0
    titleWords = 0
    sumOfAllNum = 0
    arrOfWordLengths = []

    chosenText = texts[choice - 1].replace(".", "").replace(",", "")
    sectors = re.split(r' |\n', chosenText)

    for i in sectors:
            if i.isnumeric():
                numberCount += 1
                if isinstance(i, complex):
                    sumOfAllNum += complex(i)[:-1]
                else:
                    sumOfAllNum += int(i)
            else:
                wordCount += 1
                arrOfWordLengths = countLetters(arrOfWordLengths, i)

                if i.istitle():
                    titleWords += 1

                if i.isupper():
                    upperWords += 1

                if i.islower():
                    lowerWords += 1
    printGraph(wordCount, titleWords, upperWords, lowerWords, sumOfAllNum, numberCount, arrOfWordLengths)

def countLetters(arr: list, word):
    wordArr = list(word)
    if wordArr[len(wordArr) - 1] == ",":
        word = wordArr.pop()

    if len(arr) < len(word):
        for i in range(len(word) - len(arr)):
            arr.append(0)
    arr[len(word) - 1] += 1
    return arr

def printGraph(wordCount, titleWords, upperWords, lowerWords, sumOfAllNum, numberCount, arrOfWordLengths):
    print(f'''
There are {wordCount} words in the selected text.
There are {titleWords} titlecase words.
There are {upperWords} uppercase words.
There are {lowerWords} lowercase words.
There are {numberCount} numeric strings.
The sum of all the numbers {sumOfAllNum}''')
    max = arrOfWordLengths[0]
    print("""
----------------------------------------
LEN| OCCURRENCES |NR.
----------------------------------------""")
        
    for i in range(0, len(arrOfWordLengths)):      
        if(arrOfWordLengths[i] > max):    
            max = arrOfWordLengths[i]

    for i in range(len(arrOfWordLengths)):
        stars = "*" * arrOfWordLengths[i]
        spaces = " " * (max - arrOfWordLengths[i])

        if i < 9:
            currentLen = " " + str(i + 1)
        else:
            currentLen = str(i + 1)

        print(f'{currentLen}|{stars + spaces}|{arrOfWordLengths[i]}')
      
login()