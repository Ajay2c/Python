import math
def paint_calc(height,width,cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"the number of cans you need is: {number_of_cans}")

test_h = int(input("please enter the wall height: "))
test_w = int(input("please enter the wall width: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover =coverage)
