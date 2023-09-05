from data import data
import random

vs = """
██╗░░░██╗░██████╗
██║░░░██║██╔════╝
╚██╗░██╔╝╚█████╗░
░╚████╔╝░░╚═══██╗
░░╚██╔╝░░██████╔╝
░░░╚═╝░░░╚═════╝░

"""
def print_art():
    print("""
██╗░░██╗██╗░██████╗░██╗░░██╗███████╗██████╗░  ░█████╗░██████╗░
██║░░██║██║██╔════╝░██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗
███████║██║██║░░██╗░███████║█████╗░░██████╔╝  ██║░░██║██████╔╝
██╔══██║██║██║░░╚██╗██╔══██║██╔══╝░░██╔══██╗  ██║░░██║██╔══██╗
██║░░██║██║╚██████╔╝██║░░██║███████╗██║░░██║  ╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝

██╗░░░░░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░░█████╗░
██║░░░░░██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗██╔══██╗
██║░░░░░██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝╚═╝███╔╝
██║░░░░░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗░░░╚══╝░
███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║░░░██╗░░
╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░
          """)
    

def get_random_search():

    return random.choice(data)

def return_search(account):
    name = account['name']
    follower = account['follower_count']
    desc = account['description']
    country = account['country']

    return f"{name}, a {desc}, from {country}"

def compare_followers(guess, a_followers, b_followers):
    if a_followers['follower_count'] > b_followers['follower_count']:
        return "a"
    
    else:
        return "b"
    


def replay():
    return input("Do you want to replay the game? (y/n) ").lower().startswith("y")


while True:
    print_art()
    a_account = get_random_search()
    b_account = get_random_search()
    gameon = True
    points = 0
    while gameon:
        a_account = b_account
        b_account = get_random_search()
        print(return_search(a_account))
        print(vs)
        print(return_search(b_account))

        guess = input("Who do you think has more followers?: ")

        if compare_followers(guess, a_account, b_account) == guess:
            print("You got it correctly!")
            points += 1
            print("Your score is:" + str(points))
        else:
            print("Sorry, game over!")
            print("Your score is {point}".format(point = points))
            gameon = False

    if not replay():
        break

            

        
        







