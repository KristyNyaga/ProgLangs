#NYAGA JOY CHRISTINE MUTHONI
#SCT211-0572/2022

print("Server to enter total bill>>")
totalBill = float(input("Bill:"))
print("Dear customer(s), your total bill is " + str(totalBill))
payers = int(input("How many people will be splitting the bill?"))
tipAmount = int(input("We(I) would like to give a tip of (10/12/15) percent of the bill>>" ))
amountPayable = (totalBill+(tipAmount*0.01*totalBill))/payers
print("The total amount to be paid by each person is ")
print("%.2f" %amountPayable)