
import random 


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
    play_again()



def play_again():
    again = input("Would you like to play again?\nEnter Y or N: ")
    again = again.upper()   
    if again == "Y":
        new_game()
    
    
    elif again == "N":
        print("Thanks for playing!")
        
    else:
        error_message_play_again()



def check_for_close(list_of_winning_directions, list_of_user_directions):#method that prints how many of the choices are correct 
	
    for item in list_of_user_directions:
        
        if item[:] == item[:] in list_of_winning_directions:
            print(f"You got one of the chocies correct: {item}")
            break
        else:
            pass



def check_winning_conditions(list_of_winning_directions, list_of_user_directions): #check if user won by comparing the two lists.
	
    print(f"You chose: {list_of_user_directions}" )
    
    if list_of_winning_directions == list_of_user_directions:
        print(f"Winning directions were: {list_of_winning_directions}")
        print("You win! You make it to the end of the Labrynth and hear it changing behind you.") 
        play_again()
        
    elif list_of_winning_directions != list_of_user_directions:
	    
        print("You made a wrong turn! But you can still try again!")
        check_for_close(list_of_winning_directions, list_of_user_directions)
        #function here the compares the two lists and displays which guesses were correct 
        yes_no = input("Would you like to try again?\nY or N: ")
        yes_no = yes_no.upper()
        if yes_no == "Y":
            old_game(list_of_winning_directions)
        elif yes_no == "N":
            print("Thanks for playing!")
        else:
            error_message_play_again()
        
    


def play_round(): #main body of game where user inputs their decisions. 

    user_list = []
    while len(user_list) <= 2:
        user_direction = input("Left or right? \nEnter L or R: ") 
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
    print("You enter the labrynth. Ahead of you are three decisions.\nIf you get them all correct, you have beaten the labrynth.")
    new_game()



def new_game(): #only runs at first or if winning conditions are met. 
    
    winning_key = make_winning_list()
    check_winning_conditions(winning_key, play_round())




def old_game(key_list):
    old_winning_key = key_list #is passed old winning key from last round
    new_guesses = play_round() #creates new list of guesses from this new round
    check_winning_conditions(old_winning_key, new_guesses)
    




introduction()
 


