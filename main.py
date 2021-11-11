import random
from tkinter import *
import tkinter.font as tfont

win = Tk()
win.title("Rock Paper Scissors!")

# Defining fonts

font = tfont.Font(family="Lucida Grande", size=16)

################

# Functions

def check_highstreak(my_streak_score, comp_streak_score):
    my_highstreak_score = 0
    comp_highstreak_score = 0

    if my_streak_score > my_highstreak_score:
        my_highstreak_score += 1
    
    elif comp_streak_score > comp_highstreak_score:
        comp_highstreak_score += 1
    
    else:
        pass

    # Defining highscore

    my_high_streak = Label(win, text=f"My high streak: {str(my_highstreak_score)}", font=font)
    comp_high_streak = Label(win, text=f"Computer high streak: {str(comp_highstreak_score)}", font=font)

    # Displaying highscore

    my_high_streak.grid(row=2, column=1)
    comp_high_streak.grid(row=2, column=3)


def play(choice):
    cchoices = ("r", "p", "s")
    computer_choice = random.choice(cchoices)
    my_streak_score = 0
    comp_streak_score = 0



    if choice == "r" and computer_choice == "r":
        fin_label = Label(win, text="We both chose rock! Its a draw.", font=font, height=5)
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)

        
    elif choice == "p" and computer_choice == "p":
        fin_label = Label(win, text="We both chose paper! Its a draw.", font=font, height=5)
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)


    elif choice == "s" and computer_choice == "s":
        fin_label = Label(win, text="We both chose scissors! Its a draw.", font=font, height=5)
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)




    elif choice == "r" and computer_choice == "p":
        fin_label = Label(win, text="I win! I chose Paper and you chose Rock", font=font, height=10)
        comp_streak_score += 1
        my_streak_score = 0
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    elif choice == "p" and computer_choice == "r":
        fin_label = Label(win, text="You win! I chose Rock and you chose Paper", font=font, height=10)
        comp_streak_score = 0
        my_streak_score += 1
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    elif choice == "p" and computer_choice == "s":
        fin_label = Label(win, text="I win! I chose Scissors and you chose Paper", font=font, height=10)
        comp_streak_score += 1
        my_streak_score = 0
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    elif choice == "s" and computer_choice == "p":
        fin_label = Label(win, text="You win! I chose Paper and you chose Scissors", font=font, height=10)
        comp_streak_score = 0
        my_streak_score += 1
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    elif choice == "s" and computer_choice == "r":
        fin_label = Label(win, text="I win! I chose Rock and you chose Scissors", font=font, height=10)
        comp_streak_score += 1
        my_streak_score = 0
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    elif choice == "r" and computer_choice == "s":
        fin_label = Label(win, text="You win! I chose Scissors and you chose Rock", font=font, height=10)
        comp_streak_score = 0
        my_streak_score += 1
        my_streak = Label(win, text=f"My streak: {str(my_streak_score)}", font=font)
        comp_streak= Label(win, text=f"Computer streak: {str(comp_streak_score)}", font=font, height=5)
        check_highstreak(my_streak_score, comp_streak_score)
        

    else:
        pass




    fin_label.grid(row=4, column=2)
    my_streak.grid(row=1, column=1)
    comp_streak.grid(row=1, column=3)

############

# Defining stuff

info = Label(win, text="Choose one of the following buttons...\nTry and defeat the computer!", height=5, width=40, font=font)


## buttons
rock_button = Button(win, text="Rock", width=10, height=5, command=lambda: play("r"), font=font)
paper_button = Button(win, text="Paper", width=10, height=5, command=lambda: play("p"), font=font)
scissors_button = Button(win, text="Scissors", width=10, height=5, command=lambda: play("s"), font=font)



################

# Inputing stuff

info.grid(row=0, column=2)
rock_button.grid(row=3, column=1)
paper_button.grid(row=3, column=2)
scissors_button.grid(row=3, column=3)



win.mainloop()