#   python platform where anyone can share /host their code for community pypi.org

#   pip , is a package manager we can install packages

from tkinter import *

UI = Tk()
UI.geometry("512x350")
UI.title("MyCustomNotepad")

input_text = ""

input_frame = Frame(UI,width=300 , height=50,bd = 0, highlightbackground="blue" , highlightcolor="red",highlightthickness=2)

input_frame.pack(side=TOP)

input_field = Entry(input_frame,font=('arial',18,'bold') , textvariable= input_text,bg = "#eee" ,width=50,justify=LEFT)
input_field.grid(row=0, column=0)

input_field.pack(ipady=10)

buttons = Frame(UI,width=300, height=250,bg="gray")
buttons.pack()

one = Button(buttons , text="1", fg = "red",width=10,height=3,bd = 0,bg="#eee",cursor="hand2", border= 10)

one.pack()


### Code


button_colors = ["red", "green", "blue", "orange", "purple"]

for i in range(1, 6):
    button = Button(UI, text=f"Button {i}",bg=button_colors[i-1])
    button.pack(pady=5)



UI.mainloop()


