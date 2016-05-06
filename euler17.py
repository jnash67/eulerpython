import num2words

def adjusted_word_length(n):
    word = num2words.num2words(n)
    l = len(word)
    spaces = word.count(' ')
    dashes = word.count('-')
    adjl = l -spaces - dashes
    print("Num is {} - as a word \"{}\" num spaces {} num dashes {} size {} adj size {}".format(n, word, spaces, dashes,l,adjl))
    return adjl


count = 0
for i in range(1,1001):
    count = count + adjusted_word_length(i)
print("Total count is " + str(count))