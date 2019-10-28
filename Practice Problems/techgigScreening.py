def recursiveFn(word):
    l = len(word)
    i = 0
    count = 0
    j = len(word) - 1
    while i < len(word):
        if i == j:
            break
        elif word[i] != word[j]:
            # print word[:j+1]+ word[i] + word[j+1:]
            # print word[:i]+ word[j] + word[i:]
            count = count + 1 + min(recursiveFn(word[:j + 1] + word[i] + word[j + 1:]),
                                    recursiveFn(word[:i] + word[j] + word[i:]))
            break
        elif word[i] == word[j]:
            i = i + 1
            j = j - 1
    return count
    # count = recursiveFn(word)


def main():
    n = int(raw_input())
    word = raw_input()
    if word[len(word) - 1] == '\n':
        word = word[: len(word)]
    if len(word) == 1:
        count = 0
    else:
        count = recursiveFn(word)
    print str(count)


# Write code here

main()
