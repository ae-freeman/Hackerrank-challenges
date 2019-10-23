n = input()
phoneBook = {}

for i in range(int(n)):
    entry = input()
    splitEntry = entry.split()
    phoneBook[splitEntry[0]] = splitEntry[1]



lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')
