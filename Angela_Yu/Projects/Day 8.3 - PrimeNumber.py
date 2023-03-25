def prime_checker(number):
    is_prime = True
    for n in range(2,number): 
        if number % n == 0:
            print(f"It's not a Prime number{n}")
            is_prime = False
    if is_prime:
        print("It's Prime Number")
    else:
        print("Not a prime number")

n = int(input("Enter your prime number"))
prime_checker(number=n)







