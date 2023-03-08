import tkinter
import random

colour = ["red", "blue", "green", "black", "pink", "yellow", "orange", "purple", "brown"]

timeleft = 60

point = 0

def startGame(event):
    if timeleft == 60:
      countdown()
    nextcolour()
      
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft = timeleft - 1
        timeText.config(text="Time Left: "+ str(timeleft))
        timeText.after(1000,countdown)

def nextcolour():
    global point
    global timeleft
    if timeleft > 0:
        answer.focus_set()
        if answer.get().lower() == colour[1].lower():
            point = point + 1
        answer.delete(0,tkinter.END)
        random.shuffle(colour)
        label.config(fg = str(colour[1]), text=str(colour[0]))


        score.config(text="Score: "+ str(point))

        
        
window = tkinter.Tk()

window.title("colour game")

window.geometry("400x200")

instructions = tkinter.Label(window, text="type in the colour of the word")
instructions.pack()

score = tkinter.Label(window, text="press enter to start")
score.pack()

timeText = tkinter.Label(text="time left: "+ str(timeleft))
timeText.pack()

label = tkinter.Label(text="",font=('Helvetica',60))
label.pack()

answer = tkinter.Entry(window)
window.bind('<Return>',startGame)
answer.pack()

timetext = tkinter.Label(window, text="Time Left: "+str(timeleft))

window.mainloop()



