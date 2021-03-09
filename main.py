# Lucky Unicorn Decomposition Step 4 Payment Mechanics Endgame
# create the payment mechanics for the end of the game

import random

how_much = 0.0

def start_up():
  print("Welcome to the Lucky Unicorn Game!")

# Integer checking funtion
def intcheck (question, num):
  valid = False
  while not valid:
    error = "Whoops! Please enter an integer over 0."
    
    try:
        response = int(input(question))
        
        if num <= response:
          return response
        else:
          print(error)
          print()
    except ValueError:
      print(error)

# Randomly generate a token
def play():
  # adjusted list to ensure that users don't get too many unicorns

  # Starting amount set up
  # Choose 100 tokens (i.e. play 100 rounds and ...)
  # HOW_MUCH = 100

  # List changed to ensure casino always wins (odds in their favour)
  tokens = ["horse", "zebra", "donkey", 
            "horse", "zebra", "donkey",
            "horse", "zebra", "donkey","unicorn"]

  # set up counters
  unicorns_count = 0
  zebhor_count = 0
  donkey_count = 0
  total = 0.0
  print("testing")
  # User inputs starting amount
  how_much = input(intcheck("How much would you like to play with? >>",0))

 
  for item in range(0,how_much):
    chosen = random.choice(tokens)
    # Adjust total correctly for a given token

    if chosen == "unicorn":
      # count # of unicorns and multiply by 5
      unicorns_count += 1 # unicorns_count = unicorns_count + 1
      total += 5
      feedback = "Congratulations you won $5.00"
    elif chosen == "donkey":
      donkey_count += 1 # count # of donkeys
      feedback = "Sorry, you did not win anything this round."
    else: # for zebra or horse
      zebhor_count += 1
      total -= 0.5 # subtract by 0.5
      feedback = "Congratulations you won $0.50"
    
    # print(chosen) # test in component 2
    print(feedback)
    print("You have in total ${}".format(total))

  # Working out total won / lost
  # Money Calculations
  winnings = how_much - total

  # Printing winnings
  print("*** Win / Loss Calculations ***")
  print("Unicorns: ", unicorns_count)
  print("Zebras / Horses: ", zebhor_count)
  print("Donkeys: ", donkey_count)
  print()
  print("You spent ${}".format(how_much))
  print("You go home with ${:.2f}".format(winnings)) #colon dot 2f shows 2 decimal places

def finish():
  print("Thank you for playing.")
  print("End of Process")

# main routine goes here
start_up()
play()
finish()
