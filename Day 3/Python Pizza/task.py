print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
sum = 0

if size == "S":
    sum += 15
elif size == "M":
    sum += 20
elif size == "L":
    sum += 25
if pepperoni == "Y" and size == "S":
    sum += 2
elif pepperoni == "Y" and size == "M":
    sum += 3
elif pepperoni == "Y" and size == "L":
    sum += 3
else:
    sum += 0
if extra_cheese == "Y":
    sum += 1
else:
    sum += 0
print(f"Your final bill is: ${sum}.")
