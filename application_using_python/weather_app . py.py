from tkinter import *
import requests
import json
win = Tk()
win.geometry("300x400")
win.resizable(False , False)
City_name = StringVar()
disp_msg = StringVar()

def get_details():
	Name = City_name.get()
	
	apikey = "125527c209392a558655eb67c62a193f"
	try:
		url = f"http://api.openweathermap.org/data/2.5/weather?q={Name}&appid="+apikey
		response = requests.get(url)
		try:
			temp = str(response.json()['main']['temp'] - 273)[:5]
			degree = u"\N{DEGREE SIGN}"
			string = "Temperature : " + temp + degree+"C"
		except:
			string = "City not found \n Try again"
	except:
		string = "Check your \n internet connection"
	disp_msg.set(string)


Label(win , text = "" , font = ("tahoma" , 15)).grid(row = 1 , columnspan = 4)
Label(win , text = "  Enter your City Name ", font = ("courier" , 15)).grid(row = 3 , columnspan = 4)
Label(win , text = "" , font = ("tahoma",15)).grid(row = 4 , columnspan = 4)
Entry(win , textvariable = City_name).grid(row = 5 , columnspan = 4)
Label(win , text = "" , font = ("tahoma" , 15)).grid(row = 6 , columnspan = 4)
Button(win , text = "Get Temperature" , command = get_details).grid(row=7 , columnspan = 4)

Label(win , text = "" , font = ("tahoma" , 15)).grid(row = 8 , columnspan = 4)
Label(win , textvariable = disp_msg , font = ("tahoma",15)).grid(row = 9 , columnspan = 4)


win.mainloop()