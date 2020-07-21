import random

print("Welcome to number guesser") 

comp_num = random.randint(0, 10)
tries = 3
won = False
play = True

while play == True:
  while tries > 0:
    print()
    player_num = input("Enter a number between 0-10:")
    player_num = float(player_num)
    if player_num < 0 or player_num > 10:
      print("number is not between 1-10")
      break
    else:
      if player_num > comp_num:
        print("number is too big")
        tries -= 1
        print("you have " + str(tries) + " tries left")
      elif player_num < comp_num:
        print("number is too small")
        tries -= 1
        print("you have " + str(tries) + " tries left")
      else:
        print("Correct")
        won = True
        break