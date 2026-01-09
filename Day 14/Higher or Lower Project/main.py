import random

import art
print(art.logo)
famous_people = [
    {"name":"Cristiano ronaldo","followers": 20000},
    {"name": "Kylie Jenner", "followers": 380},
    {"name": "Dwayne Johnson", "followers": 350},
    {"name": "Selena Gomez", "followers": 360},
    {"name": "Kim Kardashian", "followers": 330},
    {"name": "Ariana Grande", "followers": 330},
    {"name": "Beyoncé", "followers": 310},
    {"name": "Taylor Swift", "followers": 300},
    {"name": "Justin Bieber", "followers": 290}
]
def higer_or_lower():
    score = 0
    game_over = False
    person1 = random.choice(famous_people)
    person2 = random.choice(famous_people)
    while person1["followers"] == person2["followers"]:
        person2 = random.choice(famous_people)
    while not game_over:
        print(f"Compare {person1['name']} vs {person2['name']}")
        guess = input("Guess a for the first one and b for the second: ").upper()
        a_followers = person1['followers']
        b_followers = person2['followers']
        correct = "A" if a_followers > b_followers else "B"
        if guess == correct:
            score += 1
            print(f"Correct! Your current score: {score}")
            person1 = person2
            person2 = random.choice(famous_people)
        else:
            print(f"Wrong! Final score: {score}")
            game_over = True

higer_or_lower()


