#!/usr/bin/env python
# coding: utf-8

# In[4]:


def initialization_and_game_logic():
    
    import random

    # Card Types: Space, Diamond, Club, Heart

    cards_dict = {"H1":"Ace","H2":2,"H3":3,"H4":4,"H5":5,"H6":6,"H7":7,"H8":8,"H9":9,"H10":10,"H11":"Jack","H12":"Queen","H13":"King","D1":"Ace","D2":2,"D3":3,"D4":4,"D5":5,"D6":6,"D7":7,"D8":8,"D9":9,"D10":10,"D11":"Jack","D12":"Queen","D13":"King","C1":"Ace","C2":2,"C3":3,"C4":4,"C5":5,"C6":6,"C7":7,"C8":8,"C9":9,"C10":10,"C11":"Jack","C12":"Queen","C13":"King","S1":"Ace","S2":2,"S3":3,"S4":4,"S5":5,"S6":6,"S7":7,"S8":8,"S9":9,"S10":10,"S11":"Jack","S12":"Queen","S13":"King"}
    value_mapped_dict = {"Ace":14,"Jack":11,"Queen":12,"King":13}

    halving_point = len(cards_dict)//2

    for key,value in cards_dict.items():
        if value in value_mapped_dict.keys():
            cards_dict[key] = value_mapped_dict[value]

    #print(cards_dict)

    cards_item_list = list(cards_dict.items())
    random.shuffle(cards_item_list)
    cards_dict_shuffled = dict(cards_item_list)
    player_one_cards = dict(list(cards_dict_shuffled.items())[halving_point:])
    player_two_cards = dict(list(cards_dict_shuffled.items())[:halving_point])

    #print(player_one_cards)

    player_one_cards_list = []
    player_two_cards_list = []

    for keys in player_one_cards.keys():
        player_one_cards_list.append(keys)

    for keys in player_two_cards.keys():
        player_two_cards_list.append(keys)


    print("___Drawing a random card from both the players____")

    player_one_wins = []
    player_two_wins = []
    players_equal_one = []
    players_equal_two = []
    player_one = "ramesh"
    player_two = "arjun"

    card_dealt = 0
    while True:
        
        # print("value of card_dealt:",card_dealt)
        if player_one_cards[player_one_cards_list[card_dealt]] > player_two_cards[player_two_cards_list[card_dealt]]:
            player_one_wins.append(player_two_cards_list[card_dealt])
            game_check = add_or_delete_items(player_one_wins,player_two_wins,players_equal_one,players_equal_two,player_one_cards,player_two_cards,player_one_cards_list,player_two_cards_list,card_dealt,player_one,player_two)
            card_dealt = 0
            player_one_wins = []
            player_two_wins = []
            players_equal_one = []
            players_equal_two = []
            
        elif player_one_cards[player_one_cards_list[card_dealt]] < player_two_cards[player_two_cards_list[card_dealt]]:
            player_two_wins.append(player_one_cards_list[card_dealt])
            game_check = add_or_delete_items(player_one_wins,player_two_wins,players_equal_one,players_equal_two,player_one_cards,player_two_cards,player_one_cards_list,player_two_cards_list,card_dealt,player_one,player_two)
            card_dealt = 0
            player_one_wins = []
            player_two_wins = []
            players_equal_one = []
            players_equal_two = []
            
        elif player_one_cards[player_one_cards_list[card_dealt]] == player_two_cards[player_two_cards_list[card_dealt]]:
            print("It's War:")
            players_equal_one.append(player_one_cards_list[card_dealt])
            players_equal_two.append(player_two_cards_list[card_dealt])
            card_dealt += 1
            
        else:
            pass
            
        if game_check == False:
            break 


# In[5]:


def add_or_delete_items(player_one_wins,player_two_wins,players_equal_one,players_equal_two,player_one_cards,player_two_cards,player_one_cards_list,player_two_cards_list,card_dealt,player_one,player_two):
    
    
    '''
        print("Beginning of call to add_or_delete_items__ player_one_cards_list: ",player_one_cards_list)
        print("Beginning of call to add_or_delete_items__ player_two_cards_list: ",player_two_cards_list)
        print("Begin_list_player_one_wins: ", player_one_wins)
        print("Being_list_player_two_wins: ", player_two_wins)
        print("Being_list_player_equal_one: ",players_equal_one)
        print("Begin_list_player_equal_two: ",players_equal_two)
        print("\n")
    '''
    #print("Beginning of call to add_or_delete_items__ player_one_cards_list: ",player_one_cards_list)
    #print("Beginning of call to add_or_delete_items__ player_two_cards_list: ",player_two_cards_list)
    #print("\n")
    
    
    if len(player_one_wins) != 0:
        for item in player_one_wins:
            player_one_cards.update({item:player_two_cards[item]})
            player_one_cards_list.append(item)
            del player_two_cards[item]
            player_two_cards_list.remove(item)
            player_one_wins.remove(item)
        
        if len(players_equal_two) !=0:
            for item_y in players_equal_two:
                player_one_cards.update({item_y:player_two_cards[item_y]})
                player_one_cards_list.append(item_y)
                del player_two_cards[item_y]
                player_two_cards_list.remove(item_y)
                players_equal_two.remove(item_y)
    else:
        pass
    
    if len(player_two_wins) != 0:
        for item_z in player_two_wins:
            player_two_cards.update({item_z:player_one_cards[item_z]})
            player_two_cards_list.append(item_z)
            del player_one_cards[item_z]
            player_one_cards_list.remove(item_z)
            player_two_wins.remove(item_z)
           
            
        if len(players_equal_one) != 0:
            for item_x in players_equal_one:
                player_two_cards.update({item_x:player_one_cards[item_x]})
                player_two_cards_list.append(item_x)
                del player_one_cards[item_x]
                player_one_cards_list.remove(item_x) 
                players_equal_one.remove(item_x)
    else:
        pass
    
    
    
    #print("End of calling add_or_delete_items__ player_one_cards_list: ",player_one_cards_list)
    #print("End of calling add_or_delete_items__ player_two_cards_list: ",player_two_cards_list)
    #print("\n")
     
    
   
    if len(player_two_cards_list) == 0:
        print(f"{player_one} wins the war")
        return False
    elif len(player_one_cards_list) == 0:
        print(f"{player_two} wins the war")
        return False
    else:
        pass
        


# In[6]:


print("game_on")
initialization_and_game_logic()
print("\n")
print("game_over!")

