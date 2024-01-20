# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 22:44:26 2024

@author: Eshaan Gurjar
"""

from tkinter import *
import random

root = Tk()
root.title("Country City Capital")
root.geometry("600x600")



enter_country = Entry(root)
enter_country.place(relx = 0.5, rely = 0.1, anchor = CENTER)

enter_capital = Entry(root)
enter_capital.place(relx = 0.5, rely = 0.2, anchor = CENTER)



label_country_list = Label(root, text = "Countries : ")
label_country_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_capital_list = Label(root, text = "Capitals : ")
label_capital_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)



label_country = Label(root, text = "Country : ")
label_country.place(relx = 0.5, rely = 0.7, anchor = CENTER)

label_capital = Label(root, text = "Capital : ")
label_capital.place(relx = 0.5, rely = 0.8, anchor = CENTER)



country_list = []
capital_list = []

def takeText():
    country = enter_country.get()
    capital = enter_capital.get()
    
    country_list.append(country)
    capital_list.append(capital)
    
    label_country_list["text"] = str(country_list)
    label_capital_list["text"] = str(capital_list)
    
def chooseRandom():
    random1 = random.randint(0,len(country_list) - 1)
    random2 = random.randint(0,len(capital_list) - 1)
    
    random_country = country_list[random1]
    random_capital = capital_list[random2]
    
    label_country["text"] = str(random_country)
    label_capital["text"] = str(random_capital)
    
capture = Button(root, text = "Capture Text", command = takeText)
capture.place(relx = 0.5, rely = 0.3, anchor = CENTER)

make = Button(root, text = "Use Answer", command = chooseRandom)
make.place(relx = 0.5, rely = 0.6, anchor = CENTER) 

root.mainloop()   
    

