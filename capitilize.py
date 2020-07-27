
name = input("Enter a name ")


First = name[0].upper()

for i in name:
    if i == " ":
        x = name.index(i)
        y =  name[x + 1]
        Second = y.upper()

print(First + name[1:x] + " " + Second + name[(x + 2) :])


