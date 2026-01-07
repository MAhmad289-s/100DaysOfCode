import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


humaninput = int(input("What do you choose 0 for rock, 1 for scissors, 2 for paper?"))
print(f"Your choice: {humaninput}")
if humaninput == 0:
    print(rock)
    print(f"your choice: {rock}")
elif humaninput == 1:
    print(scissors)
    print(f"your choice: {scissors}")
elif humaninput == 2:
    print(paper)
    print(f"your choice: {paper}")

computerchoice = random.randint(0, 2)
if computerchoice == 0:
    print(rock)
elif computerchoice == 1:
    print(scissors)
elif computerchoice == 2:
    print(paper)

if humaninput >= 3 or humaninput < 0:
    print("Sorry, that's not a valid choice.")
elif computerchoice == 0 and humaninput == 2:
    print("You win!")
elif computerchoice == 2 and humaninput == 0:
    print("You lose!")
elif computerchoice < humaninput:
    print("You win!")
elif computerchoice > humaninput:
    print("You lose!")
elif computerchoice == computerchoice:
    print("It's a tie!")



