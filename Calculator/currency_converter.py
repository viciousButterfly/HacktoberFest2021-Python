from tkinter import *

import calendar

def showCal() :

	gui = Tk()
	gui.config(background = "white")
	gui.title("CALENDAR")
	gui.geometry("550x600")

	year = int(year_field.get())

	cal_content = calendar.calendar(year)
	cal_year = Label(gui, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 20)
	
	gui.mainloop()

	
if __name__ == "__main__" :

	gui = Tk()
	gui.config(background = "white")
	gui.title("CALENDAR")
	gui.geometry("250x140")

	cal = Label(gui, text = "CALENDAR", bg = "white",
							font = ("times", 30, 'bold'))

	year = Label(gui, text = "Enter Year :",bg='white')
	
	year_field = Entry(gui)
	Show = Button(gui, text = "Show Calendar -->", fg = "Black",bg = "lightblue", command = showCal)
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "red", command = exit)
	
	cal.grid(row = 1, column = 1)
	year.grid(row = 2, column = 1)
	year_field.grid(row = 3, column = 1)
	Show.grid(row = 4, column = 1)
	Exit.grid(row = 6, column = 1)
	
	gui.mainloop()