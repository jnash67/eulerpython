import eulerutils as eu
import itertools
import csv

# testString = "The quick brown fox"
# testList = eu.encrypt.convert_to_list_of_ascii_int(testString)
# encryptedList = eu.encrypt.encrypt_ascii_list(testList, "abc")
# encryptedString = eu.encrypt.convert_to_str(encryptedList)
# print("Encrypted is:'" + encryptedString + "'")
# decryptedList = eu.encrypt.decrypt_ascii_list(encryptedList, "abc")
# decryptedString = eu.encrypt.convert_to_str(decryptedList)
# print("Decrypted is:'" + decryptedString + "'")
#
# testString = "A"
# testList = eu.encrypt.convert_to_list_of_ascii_int(testString)
# encryptedList = eu.encrypt.encrypt_ascii_list(testList, "*")
# encryptedString = eu.encrypt.convert_to_str(encryptedList)
# print("Encrypted is:'" + encryptedString + "'")
# decryptedList = eu.encrypt.decrypt_ascii_list(encryptedList, "*")
# decryptedString = eu.encrypt.convert_to_str(decryptedList)
# print("Decrypted is:'" + decryptedString + "'")


file = "p059_cipher.txt"
asciiCharList = []
with open(file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print(row)
        charAsciiAsStrings = list(row)
asciiList = []
for i in charAsciiAsStrings:
    asciiList.append(int(i))

print("There are {} chars in file".format(len(asciiList)))
lower_case_letters = map(chr, range(97, 123))
common_words = ['and','the']

strpwd = ""
for i in itertools.product(lower_case_letters,repeat=3):
    strpwd = i[0]+i[1]+i[2]
    decryptedList = eu.encrypt.decrypt_ascii_list(asciiList, strpwd)
    decryptedString = eu.encrypt.convert_to_str(decryptedList).lower()
    if "and" in decryptedString and "the" in decryptedString and "beginning" in decryptedString:
        print("with password "+strpwd+ "==> " + decryptedString)
        sumOfAscii=0
        for s in decryptedList:
            sumOfAscii+=s
        print("The sum of the ascii is {}".format(sumOfAscii))
        break

    # if "if" in decryptedString and "or" in decryptedString:
    #     print("with password "+strpwd+ "==> " + decryptedString)

