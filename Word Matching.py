def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("Words with the first and last character the same \n", lst)
    return ctr
count = match_words(['abc', 'deg', 'aga', '345', '343'])
print("Number of words having the first and last character the same:", count)
