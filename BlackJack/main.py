import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(player_list, comp_list):    
    player_list.append(random.choice(cards))
    comp_list.append(random.choice(cards))


def display_cards(player_list, comp_list):
    print("Your card draws are:")
    print(player_list)
    rand_num_comp = random.choice(comp_list)

    print("The computers card draws:")
    if len(player_list) == 2:
        print([" ", rand_num_comp])
    else:
        print([" "]* (len(player_list)-1) + [rand_num_comp])

def hit_or_stand():
    choice = ""

    while choice not in ["h", "s"]:
        choice = input("Would you like to hit or stand?:" )
        if choice not in ["h", "s"]:
            print("Please enter valid choice: ")

    return choice

def draw_card_after_hit(player_list, comp_list):
    player_list.append(random.choice(cards))
    comp_list.append(random.choice(cards))

def win_dec(player_list, comp_list):
    if sum(player_list) > 21 and sum(comp_list) > 21:
        print("Draw")
    
    elif sum(player_list) > 21 and sum(comp_list) <= 21:
        print("You lose!")

    elif sum(player_list) < 21 and sum(comp_list) < 21:
        if sum(player_list) > sum(comp_list):
            print("You win!")
        elif sum(player_list) == sum(comp_list):
            print("Its a draw!")
        else:
            print('Your lose!')
        
    elif sum(player_list) == sum(comp_list) and sum(player_list) == 21:
        print("You lose!")

    else:
        print("You win!")

def replay():
    return input("Do you want to replay the game? (y/n) ").lower().startswith("y")


while True:
    user_list = []
    computer_list = []
    gameon =  True

    while gameon:
        while sum(user_list) < 16 and sum(computer_list) < 16:
            draw_card(user_list, computer_list)
        
        display_cards(user_list, computer_list)

        if sum(user_list) > 21 or sum(computer_list) > 21:
            win_dec(user_list, computer_list)
            break
        
        game_choice = hit_or_stand()

        if game_choice == "h":
            draw_card_after_hit(user_list, computer_list)
            win_dec(user_list, computer_list)
            print(user_list, computer_list)
            gameon = False
        
        else:
            win_dec(user_list, computer_list)
            print(user_list, computer_list)
            gameon = False

    if not replay():
        break

            






        