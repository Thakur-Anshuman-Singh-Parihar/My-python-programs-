from tkinter import *
import os 
st = Tk()
def shutdown():
    os.system("shutdown /s /t 1")
def restart():
    os.system("shutdown /r /t 1")
def restart_t():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")

st.title("SHUTDOWN APP")
st.geometry("500x370")
st.config(bg="light green",border="5")
rb = Button(st,text="RESTART",font=("libresian serif",20,"bold"),cursor="plus",command=restart)
rb.place(x=100,y=20,height=50,width=250)
rtb = Button(st,text="RESTART TIME",font=("libresian serif",20,"bold"),cursor="plus",command=restart_t)
rtb.place(x=160,y=100,height=50,width=250)
lsb = Button(st,text="LOGOUT",font=("libresian serif",20,"bold"),cursor="plus",command=logout)
lsb.place(x=100,y=180,height=50,width=250)
sdb = Button(st,text="SHUTDOWN",font=("libresian serif",20,"bold"),cursor="plus",command=shutdown)
sdb.place(x=160,y=260,height=50,width=250)


st.mainloop()