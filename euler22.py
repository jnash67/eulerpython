import csv
import string

def char_position(letter):
    return ord(letter.lower()) - 97 + 1

def valOfName(name):
    val = 0
    for char in name:
        val += char_position(char)
    return val

# text_file = open("triangle1.txt", "r")
# lines = text_file.readlines()
#file = "triangle1.txt"
file = "p022_names.txt"
# for line in open(file):
#     print(line)

namesList = []
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        namesList = list(row)
# for line in reversed(list(open(file))):
#     print(line)
#     line = line.strip()
#     listOfStr = line.split(" ")
#print(namesList[0])
#print(namesList[1])
if len(namesList)==len(set(namesList)):
    print("There are no duplicate names")
else:
    print("There ARE duplicate names")
namesList = sorted(namesList)
print(namesList)
print(len(namesList))
#print(char_position('z'))
#print(char_position('Z'))
#print(valOfName("COLIN"))
#print(namesList.index("COLIN"))

numNames = len(namesList)
tot = 0
for i in range(0,numNames):
    tot += (i + 1) * valOfName(namesList[i])
print("Total is " + str(tot))