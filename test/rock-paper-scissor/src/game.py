from model import Hand
from service import get_random_hand, get_ai_hand

def play_game(get_opponent):
    print("")
    print("Now playing... (1)rock (2)paper (3)scissor")
    user_play = int(input("What is your move? "))
    
    user_hand = Hand(user_play) # bug! should be `Hand(user_play - 1)`
    opponent_hand = get_opponent()

    print(f"You played {user_hand} while the opponent played {opponent_hand}")

    if user_hand > opponent_hand:
        print("you win!!")
    elif user_hand == opponent_hand:
        print("draw")
    else:
        print("you lose??")
        

def main():
    print("Rock Paper Scissor:")
    print("--- (1) vs Random")
    print("--- (2) vs Smart AI")
    user_select = input("select your opponent: ").strip()

    if user_select == "1":
        play_game(get_random_hand)
    elif user_select == "2":
        play_game(get_ai_hand)
    else:
        print("wrong number. bye")


if __name__ == "__main__":
    main()
