# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random
def game():
    score=random.randint(1,70)

    with open("Hi-score.txt") as f:
        hscore=f.read()
        if(hscore!=""):
            hscore=int(hscore)
        else:
            hscore=0

    print(f"Ur score is {score}")
    if(score>hscore):
        with open("Hi-score.txt","w") as f:
            f.write(str(hscore))
    
    return score

game()