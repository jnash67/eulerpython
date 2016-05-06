from collections import Counter

def longest_common_substring(a):
    times=3
    for n in range(1,int(len(a)/times+1))[::-1]:
        substrings=[a[i:i+n] for i in range(len(a)-n+1)]
        freqs=Counter(substrings)
        if freqs.most_common(1)[0][1]>=3:
            seq=freqs.most_common(1)[0][0]
            # print("sequence '{}' of length {} occurs {} or more times".format(seq,n,times))
            return seq

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


bigPowerOf10 = 10**500
# a='fdwaw4helloworldvcdv1c3xcv3xcz1sda21f2sd1ahelloworldgafgfa4564534321fadghelloworld'
# lcs = longest_common_substring(a)
# print("The longest common substring is " + str(lcs))
# print("The length of the longest non-repeating character substring is " + str(len(lcs)))
#
# print("len is " + str(len(a)))
# mid = len(a) //2
# print("mid is " + str(mid))
# lefta = a[:len(a)//2]
# righta = a[len(a)//2:]

# leftLcs = longest_common_substring(lefta)
# rightLcs = longest_common_substring(righta)
# print(leftLcs)
# print(rightLcs)

maxmax = 0
for i in range(2,1000):
    v = bigPowerOf10//i
    strv = str(v)
    mid = len(strv) //2
    max = 0
    leftalcs= None
    rightalcs = None
    for index in range(1,mid):
        lefta = strv[:index]
        righta = strv[-1*index:]
        leftalcs = longest_unique_substr(lefta)
        rightalcs = longest_unique_substr(righta)
        if not((leftalcs is None) or (rightalcs is None)):
            lenleftalcs = len(leftalcs)
            lenrightalcs =len(rightalcs)
            if (lenleftalcs==lenrightalcs):
                if (lenleftalcs>3):
                    if (lenleftalcs > max):
                        max = lenleftalcs
    if (max > 0):
        if (max > maxmax):
            maxmax = max
            print("i is {} and len is {}".format(i,max))
            print(leftalcs)
            print(rightalcs)
