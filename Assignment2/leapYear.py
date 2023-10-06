#NYAGA JOY CHRISTINE MUTHONI
#SCT211-0572/2022

print("This is a python program to check if year is a leap year or not")

year = int(input("Enter a year>>"))


if (year % 400 == 0) and (year % 100 == 0):
    print(year, " is a leap year")

 
elif (year % 4 ==0) and (year % 100 != 0):
    print(year, " is a leap year")


else:
    print(year, " is not a leap year")  