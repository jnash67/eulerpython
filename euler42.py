import csv
import string

def char_position(letter):
    return ord(letter.lower()) - 97 + 1

def valOfWord(w):
    val = 0
    for char in w:
        val += char_position(char)
    return val

# text_file = open("triangle1.txt", "r")
# lines = text_file.readlines()
#file = "triangle1.txt"
file = "p042_words.txt"
# for line in open(file):
#     print(line)

triangleList = []
# 20th triangle number is 210.  The maximum word value is 192.
for i in range(1,21):
    triangle = 1/2*(i)*(i+1)
    triangleList.append(triangle)

wordList = []
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        wordList = list(row)

max = 0
count=0
triangleWordsList = []
for w in wordList:
    val = valOfWord(w)
    if (val in triangleList):
        count+=1
        triangleWordsList.append(w)
    if (val>max):
        max = val

print("Triangle words are: {}".format(triangleWordsList))
print("Maximum word value is {}".format(max))
print("There are {} triangle words".format(count))
