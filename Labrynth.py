
import random 
# make input in form LRL

#function that creates winning list
#!!!!!only call this function to make new list IF the user list is the same as the winning list!!!
def make_winning_list():#creates list of directions that computer will use as winning parameters
    
    options = ["L", "R"] #winning list is taken from these two directions
    winning_list = []

    for i in range(3):
    	winning_list.append(random.choice(options)) #creates random list with three values taken from options list
    
    return winning_list #returns a list as a variable




def error_message_play_again():
    print("I don't understand.")
    play_again_new()



def play_again_new():
    again = input("Would you like to re-enter the Labrynth?\nEnter Y or N: ")
    again = again.upper()   
    if again == "Y":
        new_game()
    
    
    elif again == "N":
        print("Thanks for playing!")
        
    else:
        error_message_play_again()



def show_hint(list_of_winning_directions, list_of_user_directions):#method that prints how many of the choices are correct 
	
    hint = 0

    
    if list_of_user_directions[0] == list_of_winning_directions[0]:
            hint += 1
            
    if list_of_user_directions[1] == list_of_winning_directions[1]:
            hint += 1
            
    if list_of_user_directions[2] == list_of_winning_directions[2]:
            hint += 1
            
        
    else:
        pass

    print(f"You got {hint} of the directions correct.")
    try_again(list_of_winning_directions)




def check_winning_conditions(list_of_winning_directions, list_of_user_directions): #check if user won by comparing the two lists.
	
    print(f"You chose: {list_of_user_directions}" )
    
    if list_of_winning_directions == list_of_user_directions:
        print(f"Winning directions were: {list_of_winning_directions}")
        print("You win! You escape the Labrynth and hear it changing behind you.") 
        play_again_new()
        
    elif list_of_winning_directions != list_of_user_directions:
	    
        print("You made a wrong turn somewhere!")
        
        show_hint(list_of_winning_directions, list_of_user_directions)#function here that compares the two lists 
            #and displays which guesses were correct                # 0 resets hint 
    
        try_again(list_of_winning_directions)
            

def try_again(list_of_winning_directions):      
        
        yes_no = input("Would you like to try again?\nY or N: ")
        yes_no = yes_no.upper()
        if yes_no == "Y":
            old_game(list_of_winning_directions)
        elif yes_no == "N":
            print("Thanks for playing!")
        elif yes_no == "H":
            print(list_of_winning_directions)
        else:
            error_message_play_again()
        
    


def play_round(): #main body of game where user inputs their decisions. 

    user_list = []
    while len(user_list) <= 2:
        user_direction = input("You walk for a bit, and then the path splits. Do you go left or right? \nEnter L or R: ") 
        user_direction = user_direction.upper()
        if user_direction == "L":
            user_list.append(user_direction)
            print("You go left.")
            

        elif user_direction == "R":
            user_list.append(user_direction)
            print("You go right.")
        
    
         
        
        else:
            print("Please enter L or R.")
    
    return user_list

def introduction():
    print("You approach the Labrynth. Ahead of you are three decisions.\nIf you get them all correct, you escape the Labrynth!\nIf you fail, you will remain in the Labrynth but you can keep trying until you escape.\nYou will be given a hint after every failed attempt. Good luck!")
    input("Press Enter when you are ready to enter the Labrynth. ")
    new_game()

def new_game(): #only runs at first or if winning conditions are met. 
    print("You enter the Labrynth...")
    winning_key = make_winning_list()
    check_winning_conditions(winning_key, play_round())




def old_game(key_list):
    old_winning_key = key_list #is passed old winning key from last round
    new_guesses = play_round() #creates new list of guesses from this new round
    check_winning_conditions(old_winning_key, new_guesses)
    




introduction()
 


