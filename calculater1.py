from tkinter import *
from tkinter import ttk
root = Tk()
root.option_add("*TCombobox*Listbox.font", ("Arial", 12,"bold"))
root.option_add("*TCombobox*Listbox.background", "#7097b6")
root.option_add("*TCombobox*Listbox.foreground", "white")
root.option_add("*TCombobox*Listbox.selectBackground", "#142f44")
root.title("Simple calculater")
root.geometry("696x525")
root.maxsize(696,525)
root.minsize(696,525)
root.config(bg="#373737")
exp = StringVar()
history = []
history_index = -1
entry = ttk.Combobox(root ,textvariable= exp , background = "blue",justify=RIGHT , font = ("Arial" , 35 , "bold"))
entry.place(x=10 , y=10 , width = 674 , height = 190)
entry["values"] = history
entry.focus()
frame = Frame(root, width = 676 , height = 303 , bg = "#171717")
frame.place(x=10 , y=210)
def press(key):
    exp.set(exp.get() + key)
    entry.icursor(END)
    adjust_font()
def backspace():
    exp.set(exp.get()[:-1])
    entry.icursor(END)
    adjust_font()
def clear():
    exp.set("")
    adjust_font()
def calculate():
    try:
        expr = exp.get()               
        result = eval(expr)   
        adjust_font()           
        exp.set(str(result))  
        entry.icursor(END)           
        full_calc = expr + " = " + str(result)
        add_to_history(full_calc)
        save_to_file(full_calc)
    except:
        exp.set("ERROR")

def add_to_history(text):
    if text not in history:
        history.append(text)
        entry['values'] = history 
def history_up(event=None):
    global history_index
    if not history:
        return "break"

    if history_index == -1:
        
        history_index = len(history) - 1
    elif history_index > 0:
        history_index -= 1

    exp.set(history[history_index])
    adjust_font()
    return "break"

def history_down(event=None):
    global history_index
    if not history:
        return "break"

    if history_index < len(history) - 1:
        history_index += 1
        
        exp.set(history[history_index])
        adjust_font()
    else:
        history_index = -1
        exp.set("")

    return "break"
entry.bind("<Up>", history_up)
entry.bind("<Down>", history_down)


def adjust_font():
    length = len(exp.get())

    if length < 15:
        entry.config(font=("Arial", 35, "bold"))
    elif length < 25:
        entry.config(font=("Arial", 29, "bold"))
    elif length < 35:
        entry.config(font=("Arial", 23, "bold"))
    else:
        entry.config(font=("Arial", 19, "bold"))


def save_to_file(text):
    with open("calculator_history.txt", "a") as f:
        f.write(text + "\n")
def key_handler(event):
    if event.char in "0123456789.-+*/%":
        press(event.char)
        return "break"
    elif event.keysym=="Return":
        calculate()
        return "break"
    elif event.keysym=="Backspace":
        backspace()
        return "break"
b1 = Button(frame , text = "1" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command=lambda:press("1"))
b1.place(x=3 , y=3 , height = 73 , width = 148 ,)
b3 = Button(frame , text = "3" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("3")).place(x=303 , y=3,height = 73, width = 148,)
b4 = Button(frame , text = "4" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("4")).place(x=3 , y=78,height = 73, width = 148,)
b6 = Button(frame , text = "6" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("6")).place(x=303 , y=78,height = 73, width = 148,)
b9 = Button(frame , text = "9" , font = ("Arial" ,30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("9")).place(x=303 , y=153,height = 73, width = 148,)
b0 = Button(frame , text = "0" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("0")).place(x=153 , y=228,height = 73, width = 148,)
b15 = Button(frame , text = "." , font = ("Arial" , 35 , "bold"),bg="#5f6368",borderwidth=5,relief="raised",command =lambda:press(".")).place(x=3 , y=228,height = 73, width = 148,)
b8 = Button(frame , text = "8" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("8")).place(x=153 , y=153,height = 73, width = 148,)
b11 = Button(frame , text = "%" , font = ("Arial" , 27 , "bold"),bg="#5f6368",borderwidth=5,relief="raised",command= lambda : press("%")).place(x=303 , y=228,height = 73, width = 148)
b7 = Button(frame , text = "7" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("7")).place(x=3 , y=153,height = 73, width = 148,)
b12 = Button(frame , text = "+" , font = ("Arial" , 40 ),bg="#5f6368",borderwidth=5,relief="raised",command= lambda : press("+")).place(x=453 , y=3,height = 73, width = 109)
b2 = Button(frame , text = "2" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("2")).place(x=153 , y=3,height = 73, width = 148,)
b13 = Button(frame , text = "-" , font = ("Arial" , 45 ),bg="#5f6368",borderwidth=5,relief="raised",command= lambda : press("-")).place(x=453 , y=78,height = 73, width = 109)
b14 = Button(frame , text = "x" , font = ("Arial" , 32 ),bg="#5f6368",borderwidth=5,relief="raised",command= lambda : press("*")).place(x=453 , y=153,height = 73, width = 109)
b5 = Button(frame , text = "5" , font = ("Arial" , 30 , "bold"),bg="#80868b",borderwidth=5,relief="raised",command = lambda:press("5")).place(x=153 , y=78,height = 73, width = 148,)
b17 = Button(frame , text = "/" , font = ("Arial" , 30 ,"bold"),bg="#5f6368",borderwidth=5,relief="raised",command= lambda : press("/")).place(x=453 , y=228,height = 73, width = 109)
bac=Button(frame, text="AC", font=("Arial", 25, "bold"),bg="#f0dc9c",borderwidth=5,relief="raised", command=clear).place(x=564, y=78, height=73, width=109)
b16 = Button(frame , text = "⌫" , font = ("Arial" , 17 , "bold"),bg="#f0dc9c",borderwidth=5,relief="raised",command= backspace).place(x=564 , y=3,height = 73, width = 109)
b1156 = Button(frame , text = "=" , font = ("Arial" , 35 ),bg="#ff9500",borderwidth=5,relief="raised",command= calculate).place(x=564 , y=153,height = 148, width = 109)
entry.bind("<Key>",key_handler)
root.mainloop()
