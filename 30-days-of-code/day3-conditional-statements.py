if __name__ == '__main__':
    N = int(input())


weird = False
if (N % 2 == 1) or (N > 5 and N < 21):
    weird = True

if weird:
    print("Weird")
else:
    print("Not Weird")
