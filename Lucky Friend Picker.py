# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 17:14:42 2022

@author: PC_RC
"""

from tkinter import *
import random

root = Tk()
root.title("Lucky Friend Picker")
root.geometry("400x400")
root.configure(background="lightblue")

enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.2, anchor = CENTER)

friend_list = Label(root)
random_number_label = Label(root)
lucky_friend = Label(root)

list1 = []
def addfriend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"]= "Your friend list: "+ str(list1)
    
def random_number():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    lucky_friend["text"] = "Your Lucky Friend Is, " + str(generated_random_number)
    
btn = Button(root, text="Add to friend list", command = addfriend)
btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)

friend_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn = Button(root, text="Who is your lucky friend?", command = random_number)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

random_number_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
lucky_friend.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()

