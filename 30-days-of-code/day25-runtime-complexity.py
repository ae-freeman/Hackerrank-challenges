import math

def isPrime(n):

    if n == 1:
        return False

    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        return False


    else:
        for j in range(2, int(sqrt) + 1):
            if n % j == 0:
                return False
                break
        else:
            return True


tests = int(input())

for i in range(tests):
    n = int(input())

    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
