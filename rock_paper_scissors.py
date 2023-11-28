import random

print("Welcome to my game")

user = input("Please enter your choice Rock, Paper, or Scissors: ").capitalize()
while user not in ['Rock', 'Paper', 'Scissors']:
    print("Invalid choice. Please enter Rock, Paper, or Scissors.")
    user = input("Please enter your choice Rock, Paper, or Scissors: ").capitalize()

pc = random.choice(["Rock", "Paper", "Scissors"])

print("User played : " + user)
print("PC played : " + pc)

if user == pc:
    print("It's a tie")
elif (user == "Paper" and pc == "Rock") or (user == "Scissors" and pc == "Paper") or (user == "Rock" and pc == "Scissors"):
    print("You won!")
else:
    print("You lose")
