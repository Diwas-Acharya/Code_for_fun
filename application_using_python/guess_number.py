from tkinter import *
import random
  
top = Tk()  
 
top.geometry("300x450")  
top.resizable(False , False)

	
msg = StringVar()
disp_msg = StringVar()

def generate_number(start , end):
	global number
	number = random.randint(start,end)

def reset():
	T.delete("1.0","end")
	generate_number(1,100)

def place_it(event):
	try:
		guess_number = int(msg.get())
	except:
		T.insert(INSERT,"\n        please enter number")
		text.delete(0,END)
		return 
	text.delete(0,END)
	left_message = "\n\n   "+str(guess_number)
	if number != guess_number:
		T.insert(INSERT,left_message + "           Wrong Guess")
		if guess_number < number:
			print("think higher")
		else:
			print("think lower")
	else:
		T.insert(INSERT,left_message + "\t\tRight Guess\n\t\tWant to play again\n\t\tRestart the game")

	
#creating a simple canvas  
c = Canvas(top,height = "450")  
T = Text(top , bg = "lavender" , fg = "green")
T.pack()

text = Entry(top , font= (70) , textvariable = msg , justify = "center")
text.place(height = 40 , x =20 , y = 398)
send = Button(top , font = (70) , text = "Reset" , command = reset)
send.place(height = 35 , x = 230 , y = 400)
top.bind("<Return>", place_it)
c.pack() 

generate_number(1,100)
  
top.mainloop()  
