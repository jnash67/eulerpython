def rotate_num(num, d):
    strval = str(num)
    rot = strval[d - 1] + strval[0:d - 1]
    return int(rot)

def reverse_num(num):
    strval = str(num)
    revstr = strval[::-1]
    return int(revstr)


def is_palindrome(s):
    return str(s) == str(s)[::-1]


def truncLeft(num, d):
    strval = str(num)
    trl = strval[0:d - 1]
    return int(trl)


def truncRight(num, d):
    strval = str(num)
    trr = strval[1:d]
    return int(trr)


def nth_pos_of_number(num, n):
    strval = str(num)
    strdig = strval[n]
    print(strdig)
    return int(strdig)


def char_position_in_alphabet(letter):
    return ord(letter.lower()) - 97 + 1


def val_of_word(w):
    val = 0
    for char in w:
        val += char_position_in_alphabet(char)
    return val


def same_digits_regardless_of_length(a, b):
    if sorted(set(str(a))) == sorted(set(str(b))):
        return True
    else:
        return False


# this finds anagrams
def same_digits_and_same_length(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False


def replace_one_digit(num, posdig, replacewith):
    strlist = list(str(num))
    strrepl = str(replacewith)
    strlist[posdig] = strrepl
    strval = ''.join(strlist)
    return int(strval)


def replace_two_digits(num, posdig1, posdig2, replacewith):
    strlist = list(str(num))
    strrepl = str(replacewith)
    strlist[posdig1] = strrepl
    strlist[posdig2] = strrepl
    strval = ''.join(strlist)
    return int(strval)


def replace_three_digits(num, posdig1, posdig2,posdig3, replacewith):
    strlist = list(str(num))
    strrepl = str(replacewith)
    strlist[posdig1] = strrepl
    strlist[posdig2] = strrepl
    strlist[posdig3] = strrepl
    strval = ''.join(strlist)
    return int(strval)
