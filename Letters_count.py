
sentence = "ak akce, kara gun icindir."
dictionary = {}

for i in sentence:
    keys = dictionary.keys()
    if i in keys:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
print(dictionary)
    
            



