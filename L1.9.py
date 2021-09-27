import random
moves = ['r','p','s']

player_wins = ['pr','sp','rs']
while True:
    player_move = input("your move:")
    if player_move == 'q':
        break
    computer_move = random.choice(moves)
    print("You: ",player_move)
    print("Me: ", computer_move)
    if player_move == computer_move:
        print("Tie")
    elif player_move + computer_move in player_wins:
        print("You win!")
    else:
        print("You lose!")