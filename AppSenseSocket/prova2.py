from tkinter import *
from tkinter import ttk



root = Tk()
root.geometry("500x500")

frame = Frame(root)
frame.place(x=0)

main_frame = Frame(frame, bg="red")
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame, bg="blue", width=300, height=600)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scroll = ttk.Scrollbar(main_frame, orient=VERTICAL,command=canvas.yview)
scroll.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scroll.set)
canvas.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

sframe = Frame(canvas, bg="yellow")
canvas.create_window((0, 0), window=sframe, anchor="nw")

for i in range(100):
    Button(sframe, text=i, width=30).grid(row=i, column=0, pady=10)

root.mainloop()