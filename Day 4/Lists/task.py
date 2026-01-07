import random
provinces_of_Canada = ["Quebec","Ontario","Alberta","BC"]

provinces_of_Canada.append("Brokebyo")
print(random.choice(provinces_of_Canada))

x = random.randint(0,4)
if x == 1:
    print("Quebec")
