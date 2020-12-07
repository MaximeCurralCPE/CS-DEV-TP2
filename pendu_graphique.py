'''
Sujet : CS-DEV TP 2 : pendu (interface graphique)
Auteur : Maxime Curral
Date de creation : 01/12/2020
'''

from tkinter import Tk, Label, Button, Frame, PhotoImage, Canvas


mw = Tk()
mw.title('Pendu')
mw.geometry('1000x300+100+200')
mw['bg'] = 'mediumaquamarine'

image_pendu = PhotoImage(file = 'bonhomme1.gif')

canvas = Canvas(mw, width = 100, height = 100)
item = canvas.create_image(0,0, anchor = 'center', image = image_pendu)
canvas.pack(side = 'right', padx = 10, pady = 10)

frame1 = Frame(mw, relief = 'groove')
frame1.pack(side = 'left', padx = 10, pady = 10)
frame1['bg'] = 'red'

frame2 = Frame(mw, relief = 'groove')
frame2.pack(side = 'left')


bouton = Button(frame1, text = "Quitter", fg = 'red', command = mw.destroy)
bouton.pack()

texte = Label(frame1, text = 'Hello World !')
texte.pack()



mw.mainloop()