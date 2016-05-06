from collections import Counter
import lcs

def longest_common_substring(a):
    times=3
    for n in range(1,int(len(a)/times+1))[::-1]:
        substrings=[a[i:i+n] for i in range(len(a)-n+1)]
        freqs=Counter(substrings)
        if freqs.most_common(1)[0][1]>=3:
            seq=freqs.most_common(1)[0][0]
            # print("sequence '{}' of length {} occurs {} or more times".format(seq,n,times))
            return seq

def checkAllEqual(iterator):
    try:
        iterator = iter(iterator)
        first = next(iterator)
        return all(first == rest for rest in iterator)
    except StopIteration:
        return True

# Python program to find the length of the longest substring
# without repeating characters
NO_OF_CHARS = 256

def longestUniqueSubsttr(string):
    n = len(string)
    cur_len = 1  # To store the lenght of current substring
    max_len = 1  # To store the result
    prev_index = 0  # To store the previous index
    i = 0

    # Initialize the visited array as -1, -1 is used to indicate
    # that character has not been visited yet.
    visited = [-1] * NO_OF_CHARS

    # Mark first character as visited by storing the index of
    # first character in visited array.
    visited[ord(string[0])] = 0

    # Start from the second character. First character is already
    # processed (cur_len and max_len are initialized as 1, and
    # visited[str[0]] is set
    for i in range(1, n):
        prev_index = visited[ord(string[i])]

        # If the currentt character is not present in the already
        # processed substring or it is not part of the current NRCS,
        # then do cur_len++
        if prev_index == -1 or (i - cur_len > prev_index):
            cur_len += 1

        # If the current character is present in currently considered
        # NRCS, then update NRCS to start from the next character of
        # previous instance.
        else:
            # Also, when we are changing the NRCS, we should also
            # check whether length of the previous NRCS was greater
            # than max_len or not.
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - prev_index

        # update the index of current character
        visited[ord(string[i])] = i

    # Compare the length of last NRCS with max_len and update
    # max_len if needed
    if cur_len > max_len:
        max_len = cur_len

    return max_len


def longest_unique_substr(S):
    # This should be replaced by an array (size = alphabet size).
    last_occurrence = {}
    longest_len_so_far = 0
    longest_pos_so_far = 0
    curr_starting_pos = 0
    curr_length = 0

    for k, c in enumerate(S):
        l = last_occurrence.get(c, -1)
        # If no repetition within window, no problems.
        if l < curr_starting_pos:
            curr_length += 1
        else:
            # Check if it is the longest so far
            if curr_length > longest_len_so_far:
                longest_pos_so_far = curr_starting_pos
                longest_len_so_far = curr_length
            # Cut the prefix that has repetition
            curr_length -= l - curr_starting_pos
            curr_starting_pos = l + 1
        # In any case, update last_occurrence
        last_occurrence[c] = k

    # Maybe the longest substring is a suffix
    if curr_length > longest_len_so_far:
        longest_pos_so_far = curr_starting_pos
        longest_len_so_far = curr_length

    return S[longest_pos_so_far:longest_pos_so_far + longest_len_so_far]



a='fdwaw4helloworldvcdv1c3xcv3xcz1sda21f2sd1ahelloworldgafgfa4564534321fadghelloworld'
# lcs = longest_common_substring(a)
# print("The longest common substring is " + str(lcs))
# print("The length of the longest non-repeating character substring is " + str(len(lcs)))
#
# print("The input string is " + str(a))
# sstr = longest_unique_substr(a)
# print("The longest substring is "+ sstr)
# print ("The length of the longest non-repeating character substring is " + str(len(sstr)))

maxLenLcs = 0
bigPowerOf10 = 10**100

# a simple example
#lcsStr = lcs.LCS('abcbdab', 'bdcaba')
lcsStr = lcs.LCS(a,a)
#assert len(lcsStr) == lcs.LCSLength('abcbdab', 'bdcaba')
print('Length of Longest common subsequence: %d' %(len(lcsStr),))
print('Longest common subsequence: %s' % (lcsStr,))

# a complex example:
strA = '''abcdefgabcdefgaabcdefgabcdefgabcdesdqfgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg'''
strB = '''gdebcdehhglkjlkabvhgdebcdehhgdebcdehhgdebcdeoshhgdebcdehhgdebcdehhgdebcdehhgdebcdehh'''
lcsStr = lcs.LCS(strA, strB)
assert len(lcsStr) == lcs.LCSLength(strA, strB)
print('Length of Longest common subsequence: %d' %(len(lcsStr),))
print('Longest common subsequence: ')
print (lcsStr)

for i in range(2,1000):
    v = bigPowerOf10//i
    strv = str(v)
    lenv = len(strv)
    leftv = strv[0:lenv//2]
    rightv = strv[lenv//2+1:]
    lcsStr = lcs.LCS(leftv, rightv)

    lenLongestNonRepeating = longestUniqueSubsttr(lcsStr)
    #if not((lenLongestNonRepeating ==1) and (longestNonRepeating[0]=='0')):
    if (lenLongestNonRepeating > maxLenLcs):
        maxLenLcs = lenLongestNonRepeating
        print("Length of largest recurring cycle is {} for {}".format(lenLongestNonRepeating, i))
        print(str(v))
        print(str(1/i))


# for i in range(2,1000):
#     v = bigPowerOf10//i
#     # print(v)
#     lcs = longest_common_substring(str(v))
#     # lenLcs = len(lcs)
#     #print("Length of largest recurring cycle is {} for {} with cycle {}".format(lenLongestNonRepeating, i, longestNonRepeating))
#     if not(checkAllEqual(lcs)):
#         longestNonRepeating =longest_unique_substr(lcs)
#         lenLongestNonRepeating = len(longestNonRepeating)
#         lenLongestNonRepeating = longestUniqueSubsttr(lcs)
#         #if not((lenLongestNonRepeating ==1) and (longestNonRepeating[0]=='0')):
#         if (lenLongestNonRepeating > maxLenLcs):
#             maxLenLcs = lenLongestNonRepeating
#             print("Length of largest recurring cycle is {} for {} with cycle {}".format(lenLongestNonRepeating, i, longestNonRepeating))
#             print(str(v))
#             print(str(1/i))
#
