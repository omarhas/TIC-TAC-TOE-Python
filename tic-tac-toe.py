from helpers import draw_board,check_turn,check_for_wins
import os
spots={1:"1",2:"2",3:"3",4:"4",5:"5",
       6:"6",7:"7",8:"8",9:"9"}
playing= True 
complete = False 
turn=0
prev_turn = -1
while (playing):
    #reset the screen so the board can't repeated every time
    os.system('cls' if os.name =="nt" else clear)
    draw_board(spots)
    #if invalid turn occured , let the player know
    if prev_turn == turn:
        print('invalid spot selected , please pick another.')
    prev_turn = turn 
    print("player "+ str((turn % 2)+1) + "'s turn: pick your spot or press q to quit")
    choice=input()
    if choice == 'q':
        playing = False 
    #check if the player input a valid numb er 1-9
    elif str.isdigit(choice)  and int(choice) in spots:
        #check if the spot has already been taken
        if not spots[int(choice)] in {"X","O"}:
            #valid number => update the board
            turn +=1
            spots[int(choice)] = check_turn(turn) 
    #check if the game has ended or a player won
    if check_for_wins(spots): playing, complete = False , True
    if turn > 8: playing= False

#Draw the board for the last time
os.system('cls' if os.name=='nt' else 'clear')
draw_board(spots)

#display who win if there is a winner
if complete:
    if check_turn(turn) == 'X' : print('Player 1 Wins')
    else: print('Player 2 Wins')
else: 
    print("No Winner")

print("Thanks For Playing")
