#NYAGA JOY CHRISTINE MUTHONI
#SCT211-0572/2022

def func_sum():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    sum = num1 + num2
    print("Sum is " + str(sum))

def func_ageCalculator():
    birthYear = int(input("Enter your birth year>>"))
    currentYear = int(input("Enter current year>>"))
    ageYears = currentYear - birthYear
    ageMonths = ageYears * 12
    ageDays = ageMonths * 30

    print(f"you are {ageYears} years old.")
    print(f"you are {ageMonths} months old.")
    print(f"you are {ageDays} days old.")

def all_Operations():
    func_sum()
    func_ageCalculator()

all_Operations()

