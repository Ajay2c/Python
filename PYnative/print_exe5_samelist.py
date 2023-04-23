# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then
# return False.


def checklist(numbers):
    print(print("Given list:", numbers))
    fst_num = numbers[0]
    lst_num = numbers[-1]

    if fst_num == lst_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is: ", checklist(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is: ", checklist(numbers_y))
