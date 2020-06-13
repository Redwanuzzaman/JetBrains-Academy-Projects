import math
principal = int(input("Enter the credit principal:"))

print("""What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment""")

choice = input()
if choice == "m":
    monthly_payment = int(input("Enter monthly payment:"))
    required_months = math.ceil(principal / monthly_payment)
    if required_months > 1:
        print("It takes {} months to repay the credit".format(required_months))
    else:
        print("It takes {} month to repay the credit".format(required_months))
else:
    periods = int(input("Enter count of months:"))
    payment = math.ceil(principal / periods)
    if principal % periods == 0:
        print("Your monthly payment = {}".format(payment))
    else:
        last_payment = principal - (periods - 1) * payment
        print("Your monthly payment = {} with last month payment = {}.".format(payment, last_payment))
