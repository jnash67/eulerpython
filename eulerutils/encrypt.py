import itertools

def encrypt_ascii_list(asciiList, pwd):
    pwdAsciiList = convert_to_list_of_ascii_int(pwd)
    pwdlen = len(pwdAsciiList)
    count = 0
    encrypted_list = []
    for asciiVal in asciiList:
        m = count % pwdlen
        count += 1
        result = asciiVal ^ pwdAsciiList[m]
        encrypted_list.append(result)
    return encrypted_list


def decrypt_ascii_list(encryptedAsciiList, pwd):
    pwdAsciiList = convert_to_list_of_ascii_int(pwd)
    pwdlen = len(pwdAsciiList)
    count = 0
    decrypted_list = []
    for asciiVal in encryptedAsciiList:
        m = count % pwdlen
        count += 1
        result = asciiVal ^ pwdAsciiList[m]
        decrypted_list.append(result)

    return decrypted_list


def convert_to_list_of_ascii_int(str):
    asciiList = []
    for char in str:
        asciiList.append(ord(char))
    return asciiList


def convert_to_str(asciiList):
    str = ""
    for i in asciiList:
        str = str + chr(i)
    return str