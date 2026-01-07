# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
from tkinter.font import names


# def greet_with_name(name,location):
#     print(f"Welcome {name}")
#     print(f"What is it like in {location}")
#
# greet_with_name(name ="Bob",location="San Francisco")

def calculate_love_score(name1, name2):
    love_score = 0
    true_score = 0
    true = "true"
    love = "love"
    combined_name = f"{name1} {name2}"
    for letter in combined_name:
        if letter in true:
            true_score += 1
        if letter in love:
            love_score += 1
    print(f"{true_score}{love_score}")

calculate_love_score("Angela Yu", "Jack Bauer")

