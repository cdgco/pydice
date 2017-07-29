from random import randint
import tkinter

top = tkinter.Tk()
top.title("Dice")
top.geometry("700x720")
top.configure(background="white")
img2 = tkinter.PhotoImage(file='ico.gif')
top.call('wm', 'iconphoto', top._w, img2)

img_path = "start.gif"
photo = tkinter.PhotoImage(file=img_path)
global label
label = tkinter.Label(top, image=photo)
label.photo = photo
label.pack(padx="100", pady="50", side="top")
label.configure(bg="white")


def dice():
    global label
    label.pack_forget()
    dicenum = randint(1, 6)
    dicestr = str(dicenum)
    img_path = dicestr + ".gif"
    photo = tkinter.PhotoImage(file=img_path)
    label = tkinter.Label(top, image=photo)
    label.photo = photo
    label.pack(padx="100", pady="50", side="top")
    label.configure(bg="white")


B = tkinter.Button(top, text="Roll Dice", command=dice)
B.pack(side="bottom", pady="30", ipadx="10")

top.mainloop()