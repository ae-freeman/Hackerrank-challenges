n = input()
phoneBook = {}

for i in range(int(n)):
    entry = input()
    splitEntry = entry.split()
    phoneBook[splitEntry[0]] = splitEntry[1]



for j in range(int(n)):
    name = str(input())
    if name in phoneBook:
        phone = phoneBook[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")
