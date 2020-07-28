
# In[220]:

# This is making of BlackJack by ard using concpets of OOP
# Multiple Classes: Deck, Player's hand, Money_Track


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank +" of "+ self.suit


# In[223]:


# card = Deck(suits[0],ranks[0])
# print(card)


# In[224]:


class Deck:
    
    def __init__(self):
        self.all_cards = []
        #print("inside __init__ of Deck")
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        #print("inside shuffle")
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        #print("inside deal_one")
        #print(len(self.all_cards))
        return self.all_cards.pop(0)
    


# In[225]:


# all_cards
# all_c = Deck()

# for x in all_c.all_cards:
#     print(x)
    
# print(all_c.all_cards[0])


# In[226]:


class Player:
    
    def __init__(self,name,initial_amount):
        self.name = name
        self.initial_amount = initial_amount
        self.total_sum = initial_amount
        self.all_cards = []
        
    def add_card(self,provided_card):
        return self.all_cards.append(provided_card)
    
    def return_single_card(self):
        return self.all_cards.pop(0)
    
    def return_all_cards(self):
        return self.all_cards
    
    def remove_all_cards(self):
        self.all_cards = []
        return self.all_cards
    
    def player_pay(self,bet_amount,game_state):
            
        if game_state == "Tie":
            self.total_sum += 0
        elif game_state == "Lose" or game_state == "Bust":
            self.total_sum -= bet_amount
        elif game_state == "Win":
            self.total_sum += bet_amount
        elif game_state == "BlackJack":
            self.total_sum += 1.5 * bet_amount
        elif game_state == "U_BlackJack":
            self.total_sum -= 1.5 * bet_amount
        elif game_state == "House_Bust":
            self.total_sum += 2 * bet_amount
        elif game_state == "U_House_Bust":
            self.total_sum -= 2 * bet_amount
        else:
            pass
        
        #print(f"{self.name} your money has gone from {self.initial_amount} to {self.total_sum}")


# In[227]:


def deal_cards(player_object,number_of_cards,list_name):
    player_object.remove_all_cards()
    for iteration in range(number_of_cards):
            player_object.add_card(new_deck.deal_one())
    for card in player_object.return_all_cards():
        list_name.append(card.value)
    return list_name
        
def game_logic(player_object,list_name,lower):
    # needs to be recursive 
    
    sum_elements = 0
    #print("printing list_name at the start of game_logic",player_object.name,list_name)

    if 21 < sum(list_name) and 11 in list_name:
        sum_elements = handle_ace(list_name)
        if lower <= sum_elements and sum_elements <= 21:
            return sum_elements
        elif sum_elements > 21:
            return sum_elements
        else:
            list_name_new = deal_cards(player_object,1,list_name)
            return game_logic(player_object,list_name_new,lower_threshold)

    elif lower <= sum(list_name) and sum(list_name) <= 21:
        return sum(list_name)
       
    
    elif 21 < sum(list_name) and 11 not in list_name:
        return sum(list_name)
        

    else:
        list_name_new = deal_cards(player_object,1,list_name)
        return game_logic(player_object,list_name_new,lower_threshold)
      
def handle_ace(list_name):
    return sum(list_name) - 10 * list_name.count(11)
        
def return_check(player_one,player_one_return,player_two,player_two_return):
    if player_one_return == player_two_return:
        print("Its a tie, bet is neither lost nor won ")
        player_one.player_pay(bet_amount,"Tie")
        player_two.player_pay(bet_amount,"Tie")
    
    elif player_two_return > 21:
        print("House Bust! you are getting paid twice your bet !")
        player_one.player_pay(bet_amount,"House_Bust")
        player_two.player_pay(bet_amount,"U_House_Bust")
        
    elif player_one_return > player_two_return:
        print("You have won this round, your cards sum is greater than sum of house's card")
        player_one.player_pay(bet_amount,"Win")
        player_two.player_pay(bet_amount,"Lose")
    
    elif player_one_return < player_two_return:
        print("You have lost this round, your cards sum is less than sum of house's card")
        player_one.player_pay(bet_amount,"Lose")
        player_two.player_pay(bet_amount,"Win")
    
    else:
        pass 

def check_funds(player_one_money,player_two_money,bet_amount):
    if player_one_money < bet_amount or player_two_money < bet_amount:
        print("Insufficient Funds! Game Over!")
        return True


# In[228]:

import random 

suits = ("Clubs","Spades","Diamonds","Hearts")
ranks = ("Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
              "Jack":10,"Queen":10,"King":10,"Ace":11}

player_one = Player("Arjun",200)
player_two = Player("House",300)
bet_amount = 50
lower = 18
lower_threshold = 17

#print("before calling game logic")

while True:
    
    new_deck = Deck()
    new_deck.shuffle()
    player_one_cards_list = []
    player_two_cards_list = []
    
    if check_funds(player_one.total_sum,player_two.total_sum,bet_amount):
        break
    
    player_one_cards = deal_cards(player_one,2,player_one_cards_list)
    player_two_cards = deal_cards(player_two,2,player_two_cards_list)

    player_one_return = game_logic(player_one,player_one_cards,lower)

    if player_one_return > 21:
        print("You have lost this round, your cards sum is greater than 21")
        player_one.player_pay(bet_amount,"Bust")
        player_two.player_pay(bet_amount,"Win")
    
    elif player_one_return == 21:
        print("You have won, BlackJack")
        player_one.player_pay(bet_amount,"BlackJack")
        player_two.player_pay(bet_amount,"U_BlackJack")
    
    else:
        player_two_return = game_logic(player_two,player_two_cards,lower_threshold)
        return_check(player_one,player_one_return,player_two,player_two_return)

if (player_one.total_sum > player_two.total_sum):
    print(f"{player_one.name} wins the game, has ${player_one.total_sum}, but how much money is enough money?")
else:
    print(f"{player_two.name} wins the game, has ${player_two.total_sum}, better luck next time {player_one.name}")

#return_check(player_one,player_one_check)
