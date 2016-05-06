import roman


def convert_bad_roman(r):
    global roman_dict
    roman_string = r
    val = 0
    while len(roman_string) > 1:
        char1 = roman_string[0]
        char2 = roman_string[1]
        if char1 == 'M' or char1 == 'D' or char1 == 'L' or char1 == 'V':
            val = val + roman_dict[char1]
            roman_string = roman_string[1:len(roman_string)]
        elif char1 == 'C':
            if char2 == 'D' or char2 == 'M':
                val = val + roman_dict[char1 + char2]
                roman_string = roman_string[2:len(roman_string)]
            else:
                val = val + roman_dict[char1]
                roman_string = roman_string[1:len(roman_string)]
        elif char1 == 'X':
            if char2 == 'L' or char2 == 'C':
                val = val + roman_dict[char1 + char2]
                roman_string = roman_string[2:len(roman_string)]
            else:
                val = val + roman_dict[char1]
                roman_string = roman_string[1:len(roman_string)]
        elif char1 == 'I':
            if char2 == 'V' or char2 == 'X':
                val = val + roman_dict[char1 + char2]
                roman_string = roman_string[2:len(roman_string)]
            else:
                val = val + roman_dict[char1]
                roman_string = roman_string[1:len(roman_string)]
        else:
            print("Should never be here {}".format(roman_string))

    if len(roman_string)==1:
        val = val + roman_dict[roman_string[0]]
    return val


roman_dict = dict()
roman_dict['I'] = 1
roman_dict['V'] = 5
roman_dict['X'] = 10
roman_dict['L'] = 50
roman_dict['C'] = 100
roman_dict['D'] = 500
roman_dict['M'] = 1000
roman_dict['IV'] = 4
roman_dict['IX'] = 9
roman_dict['XL'] = 40
roman_dict['XC'] = 90
roman_dict['CD'] = 400
roman_dict['CM'] = 900

file = "p089_roman.txt"

lineCount = 0
chars_saved = 0
for line in list(open(file)):
    line = line.strip()
    orig_len = len(line)
    intval = convert_bad_roman(line)
    correctRoman = roman.toRoman(intval)
    new_len = len(correctRoman)
    if new_len > orig_len:
        print("Shouldn't happen {} is longer than {} for intval {}".format(line, correctRoman, intval))
    chars_saved += orig_len - new_len

print("Total chars saved is {}".format(chars_saved))
