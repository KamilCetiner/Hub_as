
def front_back(word):
    if len(word) == 1:
        return word
    else:
        Long = len(word) - 1
        x = word[0]
        y = word[Long]
        z = word[1:-1]
        return y + z + x
print(front_back('a'))