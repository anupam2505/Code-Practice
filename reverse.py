__Author__ = "Anupam Panwar"

__Date__ = 10 / 2 / 16

# Complete the function below.


def  rearrangeWord(word):
    word = list(word)
    length = len(word)
    i = length - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1

    ####if next alphabetical large string not possible
    if i <= 0:
        return "no answer"

    j = length - 1

    ## find swap element
    while word[j] <= word[i - 1]:
        j -= 1
    swap1 = word[i-1]
    swap2 = word[j]
    word[j] = swap1
    word[i-1] = swap2

    # Reverse the rest of the string
    word[i : ] = word[len(word) - 1 : i - 1 : -1]
    return ''.join(word)

word = "pp"
a = rearrangeWord(word)
print a