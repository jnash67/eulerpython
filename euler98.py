import eulerutils as eu
import sortedcontainers as sc
import csv
import itertools

def wordVal(word, translateDict):
    wordStrNum = ''
    firstChar = True
    for ch in word:
        strdig = translateDict[ch]
        if firstChar:
            if strdig == '0':
                # no leading zeros
                return -1
        wordStrNum += translateDict[ch]
    return int(wordStrNum)


def check(anagram1, anagram2, uniquecharset, code):
    global largestSquare
    global squares
    translateDict = {}
    i = 0
    for ch in uniquecharset:
        translateDict[ch] = code[i]
        i+=1
    val1 = wordVal(anagram1, translateDict)
    val2 = wordVal(anagram2, translateDict)
    if (val1 in squares) and (val2 in squares):
        print("{} and {} are square pairs with val {} and {}".format(anagram1, anagram2, val1, val2))
        if val1 > largestSquare:
            largestSquare = val1
        if val2> largestSquare:
            largestSquare = val2


largestSquare = 0
file = "p098_words.txt"
wordsList = []
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        wordsList = list(row)


AllCharDict = sc.SortedDict()
UniqueCharDict = sc.SortedDict()
AnagramsDict = sc.SortedDict()
squares = sc.SortedList()

maxn = 9876543210
i = 1
while True:
    square = eu.square_number(i)
    squares.append(square);
    i+=1
    if square > maxn:
        break

maxwordlen = 0
maxuniquechars = 0
wordwithmaxuniquechars = ''
minlen = 1000
for word in wordsList:
    l = len(word)
    uniquecharset = sorted(''.join(set(word)))
    charstring = ''.join(sorted((list(word))))
    uniquechars = len(uniquecharset)
    AllCharDict[word] = charstring
    UniqueCharDict[charstring] = uniquecharset
    AnagramsDict.setdefault(charstring, []).append(word)
    if uniquechars >= maxuniquechars:
        print(word + "  " + str(uniquechars) + "   " + str(uniquecharset))
    if uniquechars > maxuniquechars:
        maxuniquechars = uniquechars
        wordwithmaxuniquechars= word
    if (l > maxwordlen):
        maxwordlen = l
    if l < minlen:
        minlen = l


digits =['0','1','2','3','4','5','6','7','8','9']

for chars in AnagramsDict.keys():
    anagramsList = AnagramsDict[chars];
    uniquecharset = UniqueCharDict[chars]
    uniquechars = len(uniquecharset)
    numanagrams =len(anagramsList)
    if numanagrams > 2:
        print("More than 2 in a pair {}".format(anagramsList))
    if numanagrams > 1:
        wordlen = len(anagramsList[0])
        for numcode in itertools.permutations(digits, uniquechars):
            check(anagramsList[0], anagramsList[1], uniquecharset, numcode)

print("Largest square is {}".format(largestSquare))
