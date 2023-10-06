#NYAGA JOY CHRISTINE MUTHONI
#SCT211-0572/2022

print("This is a BMI calculator:")
height = float(input("Enter your height in metres>>"))
weight = float (input("Enter your weight in kgs>>"))
bmi = weight/ (height*height)

if (bmi < 18.5) :
    print(f"Your BMI is {bmi:.2f} and you are underweight")

elif (18.5<=bmi<=24.9):
    print(f"Your BMI is {bmi:.2f} and your weight is normal")

elif (bmi>24.9):
    print(f"Your BMI is {bmi:.2f} and you are overweight")
