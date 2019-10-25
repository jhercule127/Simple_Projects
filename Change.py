import sys
while True:
    n =  input("Hello! How much change is owed? ")
    n = float(n)
    if n > 0:
        break

cents = int(round(n * 100))
amount_of_quarters=0
amount_of_dimes=0
amount_of_nickels=0
amount_of_pennies=0

while cents >= 25:
    amount_of_quarters = amount_of_quarters+1
    cents-=25
    
while cents >= 10:
    amount_of_dimes = amount_of_dimes +1
    cents-= 10
    
while cents >=5:
    amount_of_nickels = amount_of_nickels +1
    cents-= 5

while cents >=1:
    amount_of_pennies = amount_of_pennies +1
    cents -= 1
    
print("Change given back: {} quarter(s), {} dime(s), {} nickel(s), {} penny/pennies" 
.format(amount_of_quarters,amount_of_dimes, amount_of_nickels, amount_of_pennies))
