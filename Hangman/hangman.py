import random
from random_word import RandomWords

# r = RandomWords()
# word = r.get_random_word()
# word_list = ["_"]*len(word)

life_diag = {

            6: """
                    +----+
                    |    |
                         |
                         |
                        _|

                    """


            ,5: """
                    +----+
                    |    |
                    O    |
                         |
                        _|

                    """
            ,4: """
                    +----+
                    |    |
                    O    |
                    |    |
                        _|

                    """
            ,3: """
                    +----+
                    |    |
                    O    |
                   /|    |
                        _|

                    """
            ,2:"""
                    +----+
                    |    |
                    O    |
                   /|\   |
                        _|

                    """
            ,1:"""
                    +----+
                    |    |
                    O    |
                   /|\   |
                   /    _|

                    """
            ,0:"""
                    +----+
                    |    |
                    O    |
                   /|\   |
                   / \  _|

                    """
        }

def display_lives(life_no):
    print(life_diag[life_no])

def display_word(list):
    print("".join(list))


# def ask_input():

#     letter = ""
#     while letter.upper()  not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         letter = input("Please enter your choice: ")
#         if letter.upper() not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             print("Please enter an alphabet")
    
#     return letter


def check_input(list, word, guess):
    for i in word:
        if i == guess:
            list[word.index(i)] = i

    return guess in list

def win_check(list):
    return list.count("_ ") == 0

def replay():
    return input("Do you want to replay the game? (y/n) ").lower().startswith("y")

while True:
    lives = 6
    r = RandomWords()
    final_word = r.get_random_word()
    print("""
            ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
            ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
            ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
            ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
            ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
            ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
        """)
    word_list = ["_ "]*len(final_word)
    gameon = True
    while gameon:
        if word_list.count("_ ") != 0 and lives <= 6 and lives > 0:
            guess = input("Please enter your guess(single letter from a-z):")
            if check_input(word_list, final_word, guess):
                display_lives(lives)
                display_word(word_list)
                print("You have : " + str(lives) + " lives.")
                if win_check(word_list):
                    print("You have won!")
                    gameon = False

            else:
                lives -= 1
                display_lives(lives)
                display_word(word_list)

        
        elif word_list.count("_ ") != 0 and lives <= 0:

            print("Game over!")
            print("The word was: "+ final_word)
            gameon = False

    if not replay():
        break

        

        




