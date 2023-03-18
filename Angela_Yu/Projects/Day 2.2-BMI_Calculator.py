height = input("What is your height in m: ")
weight = input("what is your weight in kg: ")

a = int(weight)
b = float(height)

# the formula for this BMI is
# BMI = weight / (height * height)

bmi = int(a / (b ** 2))

print(bmi)
