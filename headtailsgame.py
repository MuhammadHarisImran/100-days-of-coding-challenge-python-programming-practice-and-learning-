import random
print("Welcome to the heads or tails game!")
print("You have 5 chances to guess the coin toss!")
print("Here we go!")

output = random.randint(0,1)
input  = input("Please pick heads (h) or tails (t): ")
if input == "h":
  if output == 0:
    print("You win! It was heads.")
  else:
    print("You lose! It was tails.")

elif input == "t":
  if output == 1:
    print("You win! It was tails.")
  else:
    print("You lose! It was heads.")