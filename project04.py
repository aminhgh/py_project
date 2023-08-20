#Rock - Paper - scissor
#import lib
import random 
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock-Paper-Scissor")

USER_SCORE = 0
COMPUTER_SCORE = 0
USER_CHOICE = " "
COMPUTER_CHOICE = " "

def choice_to_number(choice):
    response = {"rock":0,"paper":1,"scissor":2}
    return response[choice]
def number_to_choice(number):
    response = {0:"Rock",1:"paper",2:"scissor"}
    return response[number]
#computer def choice
def random_computer_choice():
    return random.choice(["rock","paper","scissor"])
# def result
def result(human_choice,ai_choice):
    global USER_SCORE
    global COMPUTER_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(ai_choice)
    if (user == comp):
        print("You both are Equal :/ ")
    elif ((user-comp)%3==1):
        print("Dear User you are the Winner :) ")
        USER_SCORE += 1
    else:
        print("Computer is Winner :( ")
        COMPUTER_SCORE += 1
#text_area
    text_area = tk.Text(master=window,height=12,width=30,background="#ffff80")
    text_area.grid(column=0,row=4)
    answer = "your choice : {uc} \n computer choice : {cc} \n your Score : {u} \n computer Score : {c} ".format(uc=USER_CHOICE,cc=COMPUTER_CHOICE,u=USER_SCORE,c=COMPUTER_SCORE)
    text_area.insert(tk.END,answer)

def Rock():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = "rock"
    COMPUTER_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)
def paper():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = "paper"
    COMPUTER_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)
def scissor():
    global USER_CHOICE
    global COMPUTER_CHOICE
    USER_CHOICE = "scissor"
    COMPUTER_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMPUTER_CHOICE)
#Button
button1 = tk.Button(text="Rock",bg="gray",command=Rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="Paper",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="scissor",bg="skyblue",command=scissor)
button3.grid(column=0,row=3)
# execute program
window.mainloop()