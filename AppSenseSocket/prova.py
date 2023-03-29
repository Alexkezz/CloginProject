from tkinter import *
master = Tk()
buttons = []
n = 9

def prova(boto_clicat):
    print("S'clicat el numero {}".format(boto_clicat))
for z in range(n):
    button = Button(master, text = str(z), command=lambda z=z:prova(str(z)))
    button.pack()
    buttons.append(button)
master.mainloop()