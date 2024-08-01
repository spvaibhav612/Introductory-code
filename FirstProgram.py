from tkinter import *
import tkinter.font as font
window = Tk()
window.title("This is my first GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


def button_series():
    global ind
    global count
    count = 0
    ind = 1
    helv36 = font.Font(family='Helvetica', size=15, weight=font.BOLD)
    global button1
    button1 = Button(text="Block 1", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button1))
    button1.grid(row=0, column=0)

    global button2
    button2 = Button(text="Block 2", bd=5, height=3, width=10, font=helv36,command=lambda: button_click(button2))
    button2.grid(row=0, column=1)

    global button3
    button3 = Button(text="Block 3", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button3))
    button3.grid(row=0, column=2)

    global button4
    button4 = Button(text="Block 4", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button4))
    button4.grid(row=1, column=0)

    global button5
    button5 = Button(text="Block 5", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button5))
    button5.grid(row=1, column=1)

    global button6
    button6 = Button(text="Block 6", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button6))
    button6.grid(row=1, column=2)

    global button7
    button7 = Button(text="Block 7", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button7))
    button7.grid(row=2, column=0)

    global button8
    button8 = Button(text="Block 8", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button8))
    button8.grid(row=2, column=1)

    global button9
    button9 = Button(text="Block 9", bd=5, height=3, width=10, font=helv36, command=lambda: button_click(button9))
    button9.grid(row=2, column=2)

    global display
    display = Label(text='TIC TAC TOE', bd=5, height=3, width=10, font=helv36)
    display.grid(row=3, column=1)

    global reset
    reset = Button(text="Reset", bd=5, height=1, width=10, font=helv36, command=button_series)
    reset.grid(row=4, column=1)

def button_click(button):
    global ind
    if ind == 1:
        ind = 0
        button["text"] = ("x")
    else:
        ind = 1
        button["text"] = ("o")
    logic(ind)


def logic(ident):
    global count
    count += 1
    if count == 9:
        display["text"] = "Draw match"
    button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    for i in (0, 6, 3):
        if button_list[i]["text"] == button_list[i+1]["text"] and button_list[i+1]["text"] == button_list[i+2]["text"]:
            if ident == 0:
                display["text"] = "x win"
            else:
                display["text"] = "o win"
    for j in (0, 2):
        if button_list[j]["text"] == button_list[j+3]["text"] and button_list[j+3]["text"] == button_list[j+6]["text"]:
            if ident == 0:
                display["text"] = "x win"
            else:
                display["text"] = "o win"
    if button_list[0]["text"] == button_list[4]["text"] and button_list[4]["text"] == button_list[8][
            "text"]:
        if ident == 0:
            display["text"] = "x win"
        else:
            display["text"] = "o win"
    if button_list[2]["text"] == button_list[4]["text"] and button_list[4]["text"] == button_list[6][
            "text"]:
        if ident == 0:
            display["text"] = "x win"
        else:
            display["text"] = "o win"

button_series()

window.mainloop()