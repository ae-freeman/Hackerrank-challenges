# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):

    candles = 0
    biggestNumber = max(ar)

    for i in range (len(ar)):
        if ar[i] == biggestNumber:
            candles += 1

    return candles
