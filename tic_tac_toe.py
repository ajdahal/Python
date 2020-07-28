#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Usage: python3 tic_tac_toe.py
#Making code more robust: pylint tic_tac_toe.py -r y
#Author: @arjun


# In[2]:


def display_static_board():
     #static_lister = [1,2,3,4,5,6,7,8,9]
     print("  1 | 2 | 3 ")
     print("------------")
     print("  4 | 5 | 6 ")
     print("------------")
     print("  7 | 8 | 9 ")
    


# In[3]:


#display_static_board()


# In[4]:


def dynamic_display(lst):
    print(f" {lst[0]}    |   {lst[1]}   |   {lst[2]} ")
    print("-------------------------")
    print(f" {lst[3]}    |   {lst[4]}   |   {lst[5]} ")
    print("-------------------------")
    print(f" {lst[6]}    |   {lst[7]}   |   {lst[8]} ")
    


# In[ ]:





# In[5]:


def player_selector():
    print("Hi, Welcome to the tic_tac_toe by ard ")
    print("\n")
    #print("Please input your name and hit enter: ")
    global player_one, player_two
    player_one = input("Please input your name and hit enter: ")
    print(f"Hi {player_one}, you have been assigned the symbol 'X' for the game play")
    print("please pass the control to the next player")
    player_two = input("please input your name and hit enter: ")
    print(f"Hi {player_two}, you have been assigned the symbol '0' for the game play")
    
    print("Good Luck for the game !")
    


# In[6]:


# player_selector()


# In[7]:


def start_game():
    #this can be reduced by creating a function for taking player_one and player_two's input along with checks
    print("\n")
    print("\n")
    print("Rule_X: ")
    print("Player one starts the game, please press keys alternatively")
    print("Please press numbers from 1 to 9 to fill the corresponding cells: ")
    print("\n")
    print("Please review the static board cells and numbers assigned to them: ")
    # display_static_board()
    print("\n")
    start_stop = input ("Start the game, press y: ")
    if start_stop.lower() == "y":
        start_stop = True
    else:
        start_stop = False
    play_list = [""]*9
    
    while start_stop:
        
        print("\n")
        display_static_board()
        
        print("\n")
        print(f"Turn of {player_one}:")
        take_and_validate_player_input(play_list,"player_one")
                
            
        dynamic_display(play_list)
        
        print("\n")
        
        if pre_check_game_logic(play_list) == False:
            break
                 
        
        print("\n")
        print(f"Turn of {player_two}:")
        
        take_and_validate_player_input(play_list,"player_two")
        
        print("\n")
        dynamic_display(play_list)
        print("\n")

        if pre_check_game_logic(play_list) == False:
            break
        
        
    return True


# In[8]:


def pre_check_game_logic(play_list):
        if play_list.count("0") > 2 or play_list.count("X") > 2:
            if game_end(check_game_logic(play_list)) == False:
                start_stop = False
                return start_stop
            else:
                pass   


# In[9]:


def take_and_validate_player_input(play_list, player_number):
        
        while True:
            
            try:
                player_input = int(input("Please put the number between [1-9]: "))   
            except:
                print("Enter a string that can be converted to integer: ")
                continue
    
            if 1 <= player_input <= 9:
                pass
            else:
                print("please input integer in between 1 and 9: ")
                continue
            
            if play_list[player_input - 1] == "":    
                if player_number == "player_one":
                    play_list[player_input - 1] = "X"
                elif player_number == "player_two":
                    play_list[player_input - 1] = "0"
                else:
                    pass
                
                break;
            else:
                print("Illegal Operation, Cannot overwrite current value")
                continue


# In[10]:


def check_game_logic(play_list):
    
    # print("check_game_logic_called")
    # This can be reduced by creating a list of lists with the numbers in each if condition and checking them in while loop 
    
    if play_list[1] == play_list[4] and play_list[4] == play_list[7]:
        if play_list[7] == "X":
            return "1"
        elif play_list[7] == "0":
            return "2"
        else:
            pass
        
    if play_list[3] == play_list[4] and play_list[4] == play_list[5]:
        if play_list[5] == 'X':
            return "1"
        elif play_list[5] == "0":
            return "2"
        else:
            pass
        
    if play_list[6] == play_list[7] and play_list[7] == play_list[8]:
        if play_list[8] == "X":
            return "1"
        elif play_list[8] == "0":
            return "2"
        else:
            pass
        
    if play_list[2] == play_list[5] and play_list[5] == play_list[8]:
        if play_list[8] == "X":
            return "1"
        elif play_list[8] == "0":
            return "2"
        else:
            pass

        
    if play_list[2] == play_list[4] and play_list[4] == play_list[6]:
        if play_list[6] == "X":
            return "1"
        elif play_list[6] == "0":
            return "2"
        else:
            pass

    
    
    if play_list[0] == play_list[1] and play_list[1] == play_list[2]:
        if play_list[2] == "X":
            return "1"
        elif play_list[2] == "0":
            return "2"
        else:
            pass

    
    if play_list[0] == play_list[4] and play_list[4] == play_list[8]:
        if play_list[8] == "X":
            return "1"
        elif play_list[8] == "0":
            return "2"
        else:
            pass

    
    if play_list[0] == play_list[3] and play_list[3] == play_list[6]:
        if play_list[6] == "X":
            return "1"
        elif play_list[6] == "0":
            return "2"
        else:
            pass
    
    if play_list.count("X") == 5 and play_list.count("0") == 4:
        return "9"
    
    # print("check_game_logic_call_ended")


# In[11]:


def game_end(game_variable):
    # print(game_variable)
    
    if game_variable == "1":
        print (f"{player_one} wins the game, {player_two} better luck next time")
        print("Game Over!")
        return False
        
    elif game_variable == "2":
        print (f"{player_two} wins the game, {player_one} better luck next time")
        print("Game Over!")
        return False 
      
    elif game_variable == "9":
        print("All the cells have been filled up")
        print("Game Over!")
        return False
    
    else:
        return True


# In[12]:


import sys

def main():
    
    while True:
        player_selector()
        game_over_check = start_game()
        
        if game_over_check:
            print("The game has ended :( ")
            
        want_to_play = input("press q to quit game else it will continue: ")
        if want_to_play == "q":
            sys.exit()
        else:
            continue    
if __name__=="__main__":main()


# In[ ]:




