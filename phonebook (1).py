from Tkinter import *
import sqlite3
from Phonebook_007 import *
root = Tk()
root.geometry("10000x10000")
root.configure(background='black')
Label(root, text='Welcome to THE PHONEBOOK DIRECTORY ',bg="black",fg ='Green',font="Javanese 27 italic bold").grid(row=0,column=0)
Label(root, text='Project of Python And Database',bg="black",fg ='yellow',font="Javanese 30 bold underline").grid(row=5,column=2)
Label(root, text='Devloped By :- ADITI NEGI',fg ='#f4f5e2',font="Javanese 25 italic",bg="black").grid(row=6,column=2)
Label(root, text='reference taken from GEEKS FOR GEEKS ',fg ='#f4f5e2',font="Javanese 25 italic",bg="black").grid(row=7,column=2)
Label(root, text='DONE under the guidance of my mentor MR MAHESH KUMAR ',fg ='#f4f5e2',font="Times 25 italic",bg="black").grid(row=8,column=2)
Label(root, text='thank you for seeing my project',fg ='#f4f5e2',font="Times 25 italic",bg="black").grid(row=10,column=2)

def change(e=1):
    root.destroy()
    new_window()
root.bind('<Motion>',change)
root.mainloop()

