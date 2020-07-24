
def missing_char(word, n):
    for i in word:
        if i == word[n]:
            text = word.replace(word[n], "")
            return text
            

print(missing_char("kitschen", 2))