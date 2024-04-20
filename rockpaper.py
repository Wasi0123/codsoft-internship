import tkinter as tk
import random



def rps(num):
	if num == 0:
		print("Choose : rock")
	elif num == 1:
		print("Choose : paper")
	else:
		print("Choose: scissors")
	com = random.randint(0,2)
	print("player1:",com)
	if com == 0:
		comAns = "ROCK"
	elif com == 1:
		comAns = "PAPER"
	else:
		comAns = "SCISSORS"

	comp['text'] = comAns			
	label['text'] = result(num,com)		

	
def result(player,com):
	if player == com:			
		print("DRAW")
		result = "DRAW"
	elif player == 2 and com == 1:		
		print("WIN")
		result = " YOU WIN !"
	elif player == 1 and com == 0:		
		print("WIN")
		result = "YOU WIN !"
	elif player == 0 and com == 2:		
		print("WIN")
		result = "YOU WIN !"
	else:
		print("LOSE")
		result = "YOU LOSE !"

	return result


root = tk.Tk(className = ' RockPaperScissors')


canvas = tk.Canvas(root, bg ='#ccff99', width = 640, height = 690)
canvas.pack()


title = tk.Label(root, font = ('Bahnschrift',30,'bold'), text = 'ROCK - PAPER - SCISSORS', fg = 'black', bg ='#ccff99')
title.place(anchor = 'center', relx = 0.5, rely = 0.06)


frame3 = tk.Frame(root, bg = 'black', width = 300, height = 75)
frame3.place(anchor = 'center', relx = 0.5, rely = 0.18)
ccom = tk.Label(frame3, text = 'player1:', font = ('OCR A Extended',20,'bold'), fg = '#00ff00', bg = 'black')
ccom.place(relwidth = 1, relheight = 1)


frame1 = tk.Frame(root, bg = 'black', width = 300, height = 120)
frame1.place(anchor = 'center', relx = 0.5, rely = 0.3)
comp = tk.Label(frame1, font = ('OCR A Extended',34,'bold'), fg = '#00ff00', bg = 'black')
comp.place(relwidth=1, relheight=1)


frame2 = tk.Frame(root, bg = 'black', width = 300, height = 100)
frame2.place(anchor = 'center', relx = 0.5, rely = 0.5)
label = tk.Label(frame2, font = ('OCR A Extended',34,'bold'), fg = '#00ff00', bg = 'black')
label.place(relwidth=1, relheight=1)


choose = tk.Label(root, font = ('Bahnschrift',22,'bold'), text = 'make your choose', fg = 'brown', bg ='#ccff99')
choose.place(anchor = 'center', relx = 0.5, rely = 0.62)

button0 = tk.Button(root, text = 'rock', command =lambda: rps(0))

button0.place(relx = 0.08, rely = 0.68)

button1 = tk.Button(root, text = 'paper', command =lambda: rps(1))

button1.place(relx = 0.38, rely = 0.68)

button2 = tk.Button(root, text = 'scissors', command =lambda: rps(2))

button2.place(relx = 0.68, rely = 0.68)

root.resizable(False,False)

root.mainloop()

