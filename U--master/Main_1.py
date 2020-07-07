from tkinter import *

import os 
import time

def call_bro():
        os.system("python3 Get_Answers.py")
tk=Tk()
tk.title("Uniqus biss")
button_1=Button(tk, 
                text="KILL UNIQUS",
                command=call_bro)#响应botton
button_1.pack()

        
tk.mainloop()