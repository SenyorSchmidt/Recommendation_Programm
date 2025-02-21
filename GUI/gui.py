from tkinter import *

root = Tk() 
root.geometry("300x200") 

w = Label(root, text ='GeeksForGeeks', font = "50") 
w.pack() 

menubutton = Menubutton(root, text = "Menu") 
	
menubutton.menu = Menu(menubutton) 
menubutton["menu"]= menubutton.menu 

var1 = IntVar() 
var2 = IntVar() 

menubutton.menu.add_checkbutton(label = "Genre", 
								variable = var1) 
menubutton.menu.add_checkbutton(label = "Actor", 
								variable = var2) 

	
menubutton.pack() 
root.mainloop() 
