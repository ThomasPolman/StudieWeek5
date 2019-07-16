import random
from colorama import Fore # Font colors for clearer presentation

# A warm welcome
print("\033[H\033[J") # Clear screen to avoid clutter
input(Fore.MAGENTA + "welcome to thomas' casino extravaganza!\n\n".upper())
print(Fore.BLACK + "We'll start you off with a 100 computermoneys. \nUse at your discretion.")
input("\nIf you get up to a 1000, you win.")
input("\nPlease don't.")
input("\nThank you.\n")

# Keeping track of plays and credit
class ScoreBoard:
    wins = 0
    losses = 0
    ties = 0
    money = 100
    money_lost = 0
    money_gained = 0
    
    def get_total(self, wins, losses, ties):
        return wins + losses + ties
    
    def __repr__(self):
        return Fore.BLACK + "You have played a total of " + str(self.get_total(self.wins, self.losses, self.ties)) + " games and are in possession of " + Fore.GREEN + str(ScoreBoard.money) + Fore.BLACK + " computermoneys.\n\n" + Fore.MAGENTA + "Wins: " + str(self.wins) + "\nComputermoneys gained: " + str(self.money_gained) + Fore.RED + "\n\nLosses: " + str(self.losses) + "\nComputermoneys lost: " + str(self.money_lost) + Fore.CYAN + "\n\nTies: " + str(self.ties)

score_repr = ScoreBoard()

# Main menu
def main_menu():
  print("\033[H\033[J") 
  choice = input(Fore.BLACK + "\nAt present we have five games available for you.\nPlease press the corresponding number to start your exciting journey to bankruptcy!\n\n1 - Flip a coin\n\n2 - Chõ-Han - Odd or even numbers\n\n3 - Boxing day - Highest card wins\n\n4 - Roullette.\n\n5 - Blackjack\n\n6 - Check how you're currently doing\n\n7 - Quit\n\nMake your choice here:  ")
  while choice != str(1) and choice != str(2) and choice != str(3) and choice != str(4) and choice != str(5) and choice != str(6) and choice != str(7):
    choice = input("Please choose from the provided list. ")

  if choice == str(1):
    return coinflip()
  elif choice == str(2):
    return cho_han()
  elif choice == str(3):
    return boxing_day()
  elif choice == str(4):
    return roullette()
  elif choice == str(5):
    return blackjack()
  elif choice == str(6):
    print("\033[H\033[J")
    input(score_repr)
    return main_menu()
  elif choice == str(7):
    return print("\nYou've still got " + str(ScoreBoard.money) + " computermoneys left! We were supposed to have that.")
      
# Repeated functions: end of game functionality and bets
def again():
  print("\033[H\033[J") 
  
  if ScoreBoard.money == 0:
    return print(Fore.BLACK + "\nByebye and thank you for the computermoneys.")

  print(Fore.BLACK + "\nYou have %s computermoneys left."%(ScoreBoard.money))

  if ScoreBoard.money >= 1000:
    input("\nJust grand.\n")
    input("Cheater.\n")
    input("Take the dirty computermoneys.\n")
    input("You'll probably spend it to fuel an alcohol addiction.\n")
    return input("Shame on you.")

  one_more_time = input("Would you like to play again?\nPress 1 to restart, 2 to quit or 3 to play another game. ")
  while one_more_time != str(1) and one_more_time != str(2) and one_more_time != str(3):
    one_more_time = input("Please choose 1 to restart, 2 to quit or 3 for the main menu.")
  if one_more_time == str(1):
    return True
  elif one_more_time == str(2):
    print("\nYou quit the game with %s computermoneys left. We were supposed to have that!"%(ScoreBoard.money))
    return False
  elif one_more_time == str(3):
    return main_menu()
  
def bet():
  bet = input(Fore.BLACK + "How much money would you like to bet? ")
  while int(bet) > ScoreBoard.money:
      bet = input("\nYou don't have that kind of dough, my optimistic friend. Please choose again. ")
  return int(bet)

# Games

#Flip a coin
def coinflip():
  print("\033[H\033[J")
  input(Fore.MAGENTA + "\nFlip a coin, win a prize!\n")
  
  try:
    bet_value = bet()
  except ValueError:
    input(Fore.BLACK + "\nPlease enter a valid number for betting.\nRestarting...")
    return coinflip()
    
  choice = input(Fore.BLACK + "\nPress 1 for heads, 2 for tails. ")
  while choice != str(1) and choice != str(2):
      choice = input("\nPlease press 1 or 2. ")
  
  flip = random.randint(1,2)
  if flip == 1:
      input(Fore.BLUE + "\nIt fell to heads!")
  else:
      input(Fore.BLUE + "\nIt fell to tails!")
      
  if int(choice) != flip:
    input(Fore.RED + "\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
    ScoreBoard.money = ScoreBoard.money - bet_value
    ScoreBoard.losses += 1  
    ScoreBoard.money_lost += bet_value
  else:
    input(Fore.MAGENTA + "\nYay! You've won %s computermoneys!\n"%(bet_value))
    ScoreBoard.money = ScoreBoard.money + bet_value
    ScoreBoard.wins += 1
    ScoreBoard.money_gained += bet_value
    
  if again():
    return coinflip()
  return

# Cho han: even/odd numbers with two dice
def cho_han():
    
  print("\033[H\033[J")
  input(Fore.MAGENTA + "\nRoll the dice, get the prize!\n")
  print(Fore.BLACK + "Bet on an even or odd number.\n")
  
  try:
    bet_value = bet()
  except ValueError:
    input("\nPlease enter a valid number for betting.\nRestarting...")
    return cho_han()

  choice = input(Fore.BLACK + "\nPress 1 for even, 2 for odds. ")
  while choice != str(1) and choice != str(2):
      choice = input("\nPlease press 1 or 2. ")

  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  roll_total = roll1 + roll2

  input(Fore.GREEN + "\nThe first dice rolled %s."%(roll1))
  input(Fore.BLUE + "\nThe second dice rolled %s."%(roll2))
    
  if roll_total % 2 == 0:
    input(Fore.BLACK + "\nA total of %s. It rolled an even number!"%(roll_total))
  else:
    input(Fore.BLACK + "\nA total of %s. It rolled an odd number!"%(roll_total))

  if choice == str(1) and roll_total % 2 == 0:
    input(Fore.MAGENTA + "\nYou've won %s computermoneys!"%(bet_value))
    ScoreBoard.money = ScoreBoard.money + bet_value
    ScoreBoard.wins += 1
    ScoreBoard.money_gained += bet_value
  elif choice == str(2) and roll_total % 2 == 1:
    input(Fore.MAGENTA + "\nYou've won %s computermoneys!"%(bet_value))
    ScoreBoard.money = ScoreBoard.money + bet_value
    ScoreBoard.wins += 1
    ScoreBoard.money_gained += bet_value
  else:
    input(Fore.RED + "\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
    ScoreBoard.money = ScoreBoard.money - bet_value
    ScoreBoard.losses += 1
    ScoreBoard.money_lost += bet_value

  if again():
    return cho_han()
  return

# Highest card wins
def boxing_day():
    
  print("\033[H\033[J")
  input(Fore.MAGENTA + "\nGet ready for some old skool paperfights!")
  input(Fore.BLACK + "\nTwo cards will be drawn. One for you, one for the dealer.\nThe highest card wins the bet.\n")
  input(Fore.RED + "Just don't let the king hit the queen. That's very rude.")
  
  try:
    bet_value = bet()
  except ValueError:
    input(Fore.BLACK + "\nPlease enter a valid number for betting.\nRestarting...")
    return boxing_day()

  #Deck creation
  deck_values = [i for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
  deck_signs = ['Hearts', 'Tiles', 'Pikes', 'Clovers']
  deck = [[value, sign] for value in deck_values for sign in deck_signs]

  #Draws
  random.shuffle(deck)
  random_pick1 = deck.pop()
  random_pick2 = deck.pop()
  value1 = random_pick1[0]
  value2 = random_pick2[0]
  
  #Values for facecards
  if value1 == 'Jack':
    value1 = int(11)
  elif value1 == 'Queen':
    value1 = int(12)
  elif value1 == 'King':
    value1 = int(13)
  elif value1 == 'Ace':
    value1 = int(14)
  else:
    value1 = random_pick1[0]

  if value2 == 'Jack':
    value2 = int(11)
  elif value2 == 'Queen':
    value2 = int(12)
  elif value2 == 'King':
    value2 = int(13)
  elif value2 == 'Ace':
    value2 = int(14)
  else:
    value2 = random_pick2[0]

  input("\nYou drew: %s"%(random_pick1))
  input(Fore.BLACK + "The dealer drew: %s"%(random_pick2))
  
  if random_pick1[0] == 'King' and random_pick2[0] == 'Queen':
      input(Fore.RED + "\nYou disgust me. Kings don't hit queens. I'm taking your money and kicking you out.")
      return
  if random_pick2[0] == 'King' and random_pick1[0] == 'Queen':
      input(Fore.MAGENTA + "\nWho does this dealer think he is? Hitting queens with kings. Highly inappropriate. Have some money my friend.")
      ScoreBoard.money = ScoreBoard.money + 900
      ScoreBoard.money_gained += 900
      ScoreBoard.wins += 1000000
      return main_menu()
  
  if value1 > value2:
    input(Fore.MAGENTA + "\nYou won! You get %s computermoneys!"%(bet_value))
    ScoreBoard.money = ScoreBoard.money + bet_value
    ScoreBoard.wins += 1
    ScoreBoard.money_gained += bet_value
  elif value2 > value1:
    input(Fore.RED + "\nYou lost! You lose %s computermoneys!"%(bet_value))
    ScoreBoard.money = ScoreBoard.money - bet_value
    ScoreBoard.losses += 1
    ScoreBoard.money_lost += bet_value
  else:
    input(Fore.CYAN + "\nIt's a tie! Lose nothing, gain nothing.")
    ScoreBoard.ties += 1
  
  if again():
    return boxing_day()
  return
  
#Roullette  
def roullette():

  print("\033[H\033[J")
  print(Fore.BLACK + "\nGet ready for some roulette!\nYou can choose an odd or even number, and double your return on a win.")
  input("You can also bet on any number between 1 and 36.\nYou'll return 35 times your bet on a win!")
  
  choice = input("\nPress 1 to bet on odd/even or 2 to bet on a number. ")
  while choice != str(1) and choice != str(2):
    choice = input("\nPlease press 1 for odd/even or 2 to bet on a number. ")

  #Odd or even numbers
  if choice == str(1):
    
    try:
      bet_value = bet()
    except ValueError:
      input(Fore.BLACK + "\nPlease enter a valid number for betting.\nRestarting...")
      return roullette()
    
    odd_even = input("\nPlease press 1 for even or 2 for odd. ")
    while odd_even != str(1) and odd_even != str(2):
      odd_even = input("Please press 1 or 2. ")
      
    roll_odd_even = random.randint(1,36)
    if roll_odd_even % 2 == 0:
      input(Fore.GREEN + "\n%s! It hit an even number!"%(roll_odd_even))
    else:
      input(Fore.BLUE + "\n%s! It hit an odd number!"%(roll_odd_even))

    if odd_even == str(1) and roll_odd_even % 2 == 0:
      input(Fore.MAGENTA + "\nYou've won %s computermoneys!"%(bet_value))
      ScoreBoard.money = ScoreBoard.money + bet_value
      ScoreBoard.wins += 1
      ScoreBoard.money_gained += bet_value
    elif odd_even == str(2) and roll_odd_even % 2 == 1:
      input(Fore.MAGENTA + "\nYou've won %s computermoneys!"%(bet_value))
      ScoreBoard.money = ScoreBoard.money + bet_value
      ScoreBoard.wins += 1
      ScoreBoard.money_gained += bet_value
    else:
      input(Fore.RED + "\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
      ScoreBoard.money = ScoreBoard.money - bet_value
      ScoreBoard.losses += 1
      ScoreBoard.money_lost += bet_value
      
    if again():
      return roullette()
    return

  # 1 to 36
  elif choice == str(2):
    
    try:
      bet_value = bet()
    except ValueError:
      input(Fore.BLACK + "\nPlease enter a valid number for betting.\nRestarting...")
      return roullette()
          
    number = input("\nWhich number would you like to bet on? ")
    while int(number) < 1 or int(number) > 36:
      number = input("\nPlease choose between 1 and 36. ")

    roll_number = random.randint(1,36)
    input(Fore.BLUE + "\nIt rolled %s!"%(roll_number))
    if roll_number == int(number):
      ScoreBoard.money = ScoreBoard.money + (bet_value * 35)
      input(Fore.MAGENTA + "\nAmazing!!! You've won %s computermoneys. You're rich, baby."%(str(bet_value*35)))
      ScoreBoard.wins += 1
      ScoreBoard.money_gained += bet_value * 35
    else:
      ScoreBoard.money = ScoreBoard.money - bet_value
      input(Fore.RED + "\nToo bad. What were you expecting though? ")
      ScoreBoard.losses += 1
      ScoreBoard.money_lost += bet_value

    if again():
      return roullette()
    return

# Blackjack
def blackjack():

  print("\033[H\033[J")
  input(Fore.MAGENTA + "\nWelcome to Blackjack!\n\n")
  input(Fore.BLACK + "Pass 21, you're done.\nChoose carefully.")
  
  try:
    bet_value = bet()
  except ValueError:
    input(Fore.BLACK + "\nPlease enter a valid number for betting.\nRestarting...")
    return blackjack()

  # Deck creation
  deck_values = [i for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
  deck_signs = ['Hearts', 'Tiles', 'Pikes', 'Clovers']
  deck = [[value, sign] for value in deck_values for sign in deck_signs]

  random.shuffle(deck)
              
  # Opening hands      
  player_hand = [deck.pop(), deck.pop()]
  dealer_hand = [deck.pop(), deck.pop()]
  # Player and dealer hand values: separated so player can choose ace value
  def player_hand_value(*cards):
      value = 0
      for flattened_list in cards:
          for card in flattened_list:
              if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
                  card[0] = int(10)
              elif card[0] == 'Ace':
                  ace_value = input("\nWould you like this Ace to be 1 or 11? ")
                  while ace_value != str(1) and ace_value != str(11):
                      ace_value = input("\nPlease choose between 1 or 11. ")
                  if ace_value == str(1):
                      card[0] = int(1)
                  elif ace_value == str(11):
                      card[0] = int(11)
              value += card[0]
      return value

  def dealer_hand_value(*cards):
      value = 0
      for flattened_list in cards:
          for card in flattened_list:
              if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King':
                  card[0] = int(10)
              elif card[0] == 'Ace':
                  card[0] = int(11)
              value += card[0]           
      return value

  # Function to simulate dealer play
  def dealer_play(hand_value):
      global money
      while hand_value < 16 or hand_value < player_end_value:
          input(Fore.BLUE + "Dealer hits and picks up...")
          card = [deck.pop()]
          hand = dealer_hand + card
          input(card)
          card_value = dealer_hand_value(card)
          hand_value += card_value
      # Checking for aces. Depending on the stage of the game, an ace can be named int(11) or 'Ace'. Room for improvement here.
      if hand_value > 21:
          for crd in hand:
              if crd[0] == int(11):
                  crd[0] = int(1)
                  hand_value = hand_value - 10
                  return dealer_play(hand_value)
              elif crd[0] == 'Ace': 
                  crd[0] = int(1)
                  hand_value = hand_value - 10
                  return dealer_play(hand_value)
          # Continue as normal    
          if hand_value > 21:
              input(Fore.MAGENTA + "Dealer bust! You win %s computermoneys."%(bet_value))
              ScoreBoard.money = ScoreBoard.money + bet_value
              ScoreBoard.wins += 1
              ScoreBoard.money_gained += bet_value
              return hand_value
      elif hand_value <= 21 and hand_value < player_end_value:
          return dealer_play(hand_value)
      else:
          return hand_value

  # Function to simulate player play
  def hit_or_stay(hand):
      global money
      input(Fore.BLACK + "\nYour current hand is: " + str(hand))
      choice = input("Please press 1 to draw another card, or 2 to stay your hand. ")
      while choice != str(1) and choice != str(2):
          choice = input("Please choose either 1 to hit or 2 to stay. ")
      if choice == str(2):
          print("\nDealer will play next.")
          return player_hand_value(hand)
        
      elif choice == str(1):
          card = [deck.pop()]
          input("You drew " + str(card))
          hand = hand + card
          if player_hand_value(hand) > 21:
              input(Fore.RED + "Bust! You lose %s computermoneys."%(bet_value))
              ScoreBoard.money = ScoreBoard.money - bet_value
              ScoreBoard.losses += 1
              ScoreBoard.money_lost += bet_value
              return player_hand_value(hand)
          elif player_hand_value(hand) <= 21:
              return hit_or_stay(hand)

  # Immediate win condition: blackjack
  if player_hand_value(player_hand) == 21 and dealer_hand_value(dealer_hand) == 21:
      input(Fore.BLUE + "\nWait, what? Oh. Two blackjacks. It's a tie.")
      ScoreBoard.ties += 1
      if again():
        return blackjack()
      return
  elif player_hand_value(player_hand) == 21:
      input(Fore.MAGENTA + "\nBlackjack! You win.")
      ScoreBoard.money = ScoreBoard.money + bet_value
      ScoreBoard.wins += 1
      ScoreBoard.money_gained += bet_value
      if again():
        return blackjack()
      return
  elif dealer_hand_value(dealer_hand) == 21:
      input(Fore.RED + "\nDealer has a blackjack! You lose.")
      ScoreBoard.money = ScoreBoard.money - bet_value
      ScoreBoard.losses += 1
      ScoreBoard.money_lost += bet_value
      if again():
        return blackjack()
      return

  # Player play
  player_end_value = hit_or_stay(player_hand)
  if player_end_value > 21: #Player bust
      if again():
          return blackjack()
      return
  elif player_end_value <= 21: #Dealer play
      input("Dealer drew " + str(dealer_hand))
      input("Playing the hand...")
      dealer_end_value = dealer_play(dealer_hand_value(dealer_hand))
      if dealer_end_value <= 21:
          if player_end_value > dealer_end_value:
              input(Fore.MAGENTA + "\nIt's %s for you, %s for the dealer. You win!"%(player_end_value, dealer_end_value))
              ScoreBoard.money = ScoreBoard.money + bet_value
              ScoreBoard.wins += 1
              ScoreBoard.money_gained += bet_value
          elif dealer_end_value > player_end_value:
              input(Fore.RED + "\nIt's %s for you, %s for the dealer. Dealer wins."%(player_end_value, dealer_end_value))
              ScoreBoard.money = ScoreBoard.money - bet_value
              ScoreBoard.losses += 1
              ScoreBoard.money_lost += bet_value
          elif dealer_end_value == player_end_value:
              input(Fore.CYAN + "\nIt's %s for you, %s for the dealer. It's a tie."%(player_end_value, dealer_end_value))
              ScoreBoard.ties += 1
          if again():
              return blackjack()
          return
  if again():
      return blackjack()
  return
      

        
# Approximation of an executable    
main_menu()

