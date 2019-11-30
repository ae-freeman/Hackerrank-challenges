actual_date = input()
expected_date = input()

list_actual_date = actual_date.split()
list_expected_date = expected_date.split()

list_actual_date = list(map(int, list_actual_date))
list_expected_date = list(map(int, list_expected_date))


if list_actual_date[2] > list_expected_date[2]:
    print("10000")

elif list_actual_date[2] == list_expected_date[2] and list_actual_date[1] > list_expected_date[1]:
    fine = 500 * (list_actual_date[1] - list_expected_date[1])
    print(fine)

elif list_actual_date[2] == list_expected_date[2] and list_actual_date[1] == list_expected_date[1] and list_actual_date[0] > list_expected_date[0]:
    fine = 15 * (list_actual_date[0] - list_expected_date[0])
    print(fine)

else:
    print("0")
