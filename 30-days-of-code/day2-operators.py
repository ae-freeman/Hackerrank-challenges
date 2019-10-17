# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    addTip = (tip_percent/100) * meal_cost
    addTax = (tax_percent/100) * meal_cost

    print(round(meal_cost + addTip + addTax))
