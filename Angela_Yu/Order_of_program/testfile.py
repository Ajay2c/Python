def my_function():
    x = 5
    y = 10
    if x < y:
        z = x + y
        print(z)  # z is defined and can be accessed within this if block
    print(z)  # This will give an error because z is not defined outside of the if block

my_function()
