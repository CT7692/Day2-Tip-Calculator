# 100 Days of Code: The Complete Python Pro Bootcamp
# Day 2 - Tip Calculator

functional = True
print("Welcome to the tip calculator.")
str_total = input("Bill total? $")

total = float(str_total)

if total <= 0:
    functional = False
    while functional == False:
        str_total = input("Please enter a valid bill total. $")
        total = float(str_total)
        if total > 0:
            functional = True

str_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

if str_percentage != "10" and str_percentage != "12" and str_percentage != "15":
    functional = False
    while functional == False:
        str_percentage = input("Please enter a listed percentage. 10, 12, or 15? ")
        if str_percentage == "10" or str_percentage == "12" or str_percentage == "15":
            functional = True

    
percentage = (float(str_percentage)/100)

str_ppl = input("How many people are paying the bill? ")
people = round(float(str_ppl))

payment = (total / people) * (1 + percentage)

print(f"Each person should pay: ${payment:.2f}.")