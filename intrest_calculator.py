principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest}")
