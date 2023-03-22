
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

#Hint 2: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


import random
from replit import clear
from art import logo

def deal_card():
  """returns a random card from the deck"""
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)
  


def calculate_score(card):
  """Takes a list of cards and return the score calculated from the cards."""
  if sum(card) == 21 and len(card) == 2:
      return 0

  if 11 in card and sum(card)> 21:
      card.remove(11)
      card.append(1)
  return sum(card)

def compare(user_scores,computer_scores):
    """compares both scores to give the winner or loser"""
    if user_scores ==computer_scores:
       return "draw."
    elif computer_scores ==0:
       return"You lost, opponent has black jack.😱"
      
    elif user_scores >21 and computer_scores > 21:
       return"You went over,you lose.😤"

    elif  user_scores > 21:
      return"You went over , you lose.😭"  
      
    elif user_scores == 0 :
      return"You win with a black jack.😎"

    elif computer_scores >21:
      return"Opponent went over, you win😃"

    else:
      return"You lose.😤"


  
def play_game():
  """recursion- function calling itself again."""
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over=False
  
  for cards in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
     
  while not is_game_over:
  
    user_scores = calculate_score(user_cards)
    computer_scores= calculate_score(computer_cards)
    print(f" Your cards:{user_cards} current score:{user_scores}")
    print(f"Computer first card:{computer_cards[0]}")
    
    if user_scores==0 or computer_scores==0 or user_scores >21:
          is_game_over= True
    else:
      
       user_should_deal= input("Type'y' to get another card, type 'n' to pass:")
       if user_should_deal =='y':
          user_cards.append(deal_card())
       else:
          is_game_over=True
  
  
  while computer_scores != 0 and computer_scores < 17:
    computer_cards.append(deal_card())
    computer_scores= calculate_score(computer_cards)
  
  
  print(f"Your final hand:{user_cards} , your score:{user_scores}")
  print(f"Computer final hand:{computer_cards} , computer score:{computer_scores}")
  print(compare(user_scores, computer_scores))

while input("Do you want to play a game of blackjack? Type'y' or'n':")=='y':
  clear()                                
  play_game()