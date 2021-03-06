# -*- coding: utf-8 -*-

# Auteurs : Ricardo Ramos (traitement et affichage de la courbe) et
#           Alexandre l'Heritier (fenètre de configuration).

# 2eme fichier pour le fonctionnement de PyCalc.

# Importation des modules nécessaires.
from tkinter import *
import turtle
import math

def erreur():
	# A faire !
	pass

def repère(t):
	t.width(3)
	t.setposition(-300,0)
	t.fd(600)
	t.right(90)
	t.fd(5)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(5)
	t.penup()
	t.setposition(0, -300)
	t.pendown()
	t.setheading(90)
	t.fd(600)
	t.right(90)
	t.fd(5)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(10)
	t.left(120)
	t.fd(5)
	t.color('grey')
	t.width(1)


	for i in range(1, 20):
		if i == 10:
			continue
		t.penup()
		t.setposition(-300, i*30-300)
		t.pendown()
		t.setheading(0)
		t.fd(600)


	for i in range(1, 20):
		if i ==10:
			continue
		t.penup()
		t.setposition(i*30-300, -300)
		t.pendown()
		t.setheading(90)
		t.fd(600)


	t.penup()
	t.setposition(0,0)
	t.pendown()
	t.color('black')

def fonction(t, f,c):
	t.color(c)
	ff = []


	for i in range(len(f)):
		if i < len(f)-1:

			if ord(f[i]) in range(48,58) and f[i-1] != ',' and ord(f[i+1]) not in\
			range(48,58) :
				elt = f[i]+'*30'
				ff.append(elt)
			else:
				ff.append(f[i])
		else:
			if ord(f[i]) in range(48,58) and f[i-1] != '*'and ord(f[i-1]) not\
			in range(48,58) and f[i-2] != '*':
				elt = f[i]+'*30'
				ff.append(elt)
			else:
				ff.append(f[i])


	f = ''
	for elt in ff:
		f += elt


	if f != 'x':
		if 'x' in f and 'x**2' not in f:
			f = f.replace('x','(x/30)')
		if 'x**2' or 'x^2' in f:
			f = f.replace('x**2','pow(x,2)/30')
			f = f.replace('x^2','pow(x,2)/30')
		if 'x+' in f:
			f = f.replace('x+','(x/30)+')
		if 'x-' in f:
			f = f.replace('x-','(x/30)-')
		if 'x*' in f:
			f = f.replace('x*','(x/30)*')


	x = -300
	y = eval(f)
	t.penup()
	t.setposition(x,y)
	t.pendown()


	for x in range (-300, 300):
		y = eval(f)
		t.setposition(x, y)
		#print(f,x, y)

def dessine(liste):
	"""
	Fonction qui ce charge de dessiner les courbes.
	"""
	# Si la liste reçu n'est pas vide.
	if liste != []:

		# Création de la fenètre turtle.
		t = turtle.Turtle()

		# On cache la tortue.
		t.hideturtle()

		# On met la vitesse max.
		t.speed(0)

		# On configure la taille de la fenètre.
		turtle.setup(width=650,height=650)

		# Création du repère.
		repère(t)

		# On compte le nombre de tour à faire.
		nb_tour = len(liste)

		# Boucle qui permet d'afficher les courbes.
		for n in range(nb_tour):
			e = liste[n]
			f = e[0]
			c = e[1]
			fonction(t,f,c)

		# Mainloop pour que la fenètre reste.
		turtle.mainloop()

def graf(b):
	"""
	Fonction qui se charge d'afficher la fenètre et de traiter les
	informations entrée pour retourner une liste.
	"""
	# Début : fenetre5.
	# On crée la fenetre.
	fenetre5 = Tk()

	# On lui donne un titre.
	fenetre5.title("f(x)")

	# On initialise les variables.
	y_1_v = StringVar()
	y_1_vo = IntVar()
	if b != "":
		y_1_v.set(b)
		y_1_vo.set(1)
	y_1_c1 = IntVar()
	y_1_c2 = IntVar()
	y_1_c3 = IntVar()
	y_1_c4 = IntVar()
	y_1_c5 = IntVar()
	y_1_c6 = IntVar()
	y_1_c7 = IntVar()
	y_1_c8 = IntVar()
	y_2_v = StringVar()
	y_2_vo = IntVar()
	y_2_c1 = IntVar()
	y_2_c2 = IntVar()
	y_2_c3 = IntVar()
	y_2_c4 = IntVar()
	y_2_c5 = IntVar()
	y_2_c6 = IntVar()
	y_2_c7 = IntVar()
	y_2_c8 = IntVar()
	y_3_v = StringVar()
	y_3_vo = IntVar()
	y_3_c1 = IntVar()
	y_3_c2 = IntVar()
	y_3_c3 = IntVar()
	y_3_c4 = IntVar()
	y_3_c5 = IntVar()
	y_3_c6 = IntVar()
	y_3_c7 = IntVar()
	y_3_c8 = IntVar()
	y_4_v = StringVar()
	y_4_vo = IntVar()
	y_4_c1 = IntVar()
	y_4_c2 = IntVar()
	y_4_c3 = IntVar()
	y_4_c4 = IntVar()
	y_4_c5 = IntVar()
	y_4_c6 = IntVar()
	y_4_c7 = IntVar()
	y_4_c8 = IntVar()
	y_5_v = StringVar()
	y_5_vo = IntVar()
	y_5_c1 = IntVar()
	y_5_c2 = IntVar()
	y_5_c3 = IntVar()
	y_5_c4 = IntVar()
	y_5_c5 = IntVar()
	y_5_c6 = IntVar()
	y_5_c7 = IntVar()
	y_5_c8 = IntVar()
	y_6_v = StringVar()
	y_6_vo = IntVar()
	y_6_c1 = IntVar()
	y_6_c2 = IntVar()
	y_6_c3 = IntVar()
	y_6_c4 = IntVar()
	y_6_c5 = IntVar()
	y_6_c6 = IntVar()
	y_6_c7 = IntVar()
	y_6_c8 = IntVar()
	y_7_v = StringVar()
	y_7_vo = IntVar()
	y_7_c1 = IntVar()
	y_7_c2 = IntVar()
	y_7_c3 = IntVar()
	y_7_c4 = IntVar()
	y_7_c5 = IntVar()
	y_7_c6 = IntVar()
	y_7_c7 = IntVar()
	y_7_c8 = IntVar()
	y_8_v = StringVar()
	y_8_vo = IntVar()
	y_8_c1 = IntVar()
	y_8_c2 = IntVar()
	y_8_c3 = IntVar()
	y_8_c4 = IntVar()
	y_8_c5 = IntVar()
	y_8_c6 = IntVar()
	y_8_c7 = IntVar()
	y_8_c8 = IntVar()

	# On crée les éléments...
	titre = Label(fenetre5, text="Graphique de fonction")

	y_1 = Label(fenetre5, text="y1 :")
	y_1_1 = Entry(fenetre5, textvariable=y_1_v)
	y_1_2 = Checkbutton(fenetre5, variable=y_1_vo)
	y_1_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_1_3.menu  = Menu(y_1_3, tearoff = 0)
	y_1_3["menu"]  =  y_1_3.menu
	y_1_3.menu.add_checkbutton (label="Bleu", variable=y_1_c1)
	y_1_3.menu.add_checkbutton (label="Rouge", variable=y_1_c2)
	y_1_3.menu.add_checkbutton (label="Vert", variable=y_1_c3)
	y_1_3.menu.add_checkbutton (label="Jaune", variable=y_1_c4)
	y_1_3.menu.add_checkbutton (label="Marron", variable=y_1_c5)
	y_1_3.menu.add_checkbutton (label="Rose", variable=y_1_c6)
	y_1_3.menu.add_checkbutton (label="Orange", variable=y_1_c7)
	y_1_3.menu.add_checkbutton (label="Noir", variable=y_1_c8)

	y_2 = Label(fenetre5, text="y2 :")
	y_2_1 = Entry(fenetre5, textvariable=y_2_v)
	y_2_2 = Checkbutton(fenetre5, variable=y_2_vo)
	y_2_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_2_3.menu  = Menu(y_2_3, tearoff = 0)
	y_2_3["menu"]  =  y_2_3.menu
	y_2_3.menu.add_checkbutton (label="Bleu", variable=y_2_c1)
	y_2_3.menu.add_checkbutton (label="Rouge", variable=y_2_c2)
	y_2_3.menu.add_checkbutton (label="Vert", variable=y_2_c3)
	y_2_3.menu.add_checkbutton (label="Jaune", variable=y_2_c4)
	y_2_3.menu.add_checkbutton (label="Marron", variable=y_2_c5)
	y_2_3.menu.add_checkbutton (label="Rose", variable=y_2_c6)
	y_2_3.menu.add_checkbutton (label="Orange", variable=y_2_c7)
	y_2_3.menu.add_checkbutton (label="Noir", variable=y_2_c8)

	y_3 = Label(fenetre5, text="y3 :")
	y_3_1 = Entry(fenetre5, textvariable=y_3_v)
	y_3_2 = Checkbutton(fenetre5, variable=y_3_vo)
	y_3_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_3_3.menu  =  Menu(y_3_3, tearoff = 0)
	y_3_3["menu"]  =  y_3_3.menu
	y_3_3.menu.add_checkbutton (label="Bleu", variable=y_3_c1)
	y_3_3.menu.add_checkbutton (label="Rouge", variable=y_3_c2)
	y_3_3.menu.add_checkbutton (label="Vert", variable=y_3_c3)
	y_3_3.menu.add_checkbutton (label="Jaune", variable=y_3_c4)
	y_3_3.menu.add_checkbutton (label="Marron", variable=y_3_c5)
	y_3_3.menu.add_checkbutton (label="Rose", variable=y_3_c6)
	y_3_3.menu.add_checkbutton (label="Orange", variable=y_3_c7)
	y_3_3.menu.add_checkbutton (label="Noir", variable=y_3_c8)

	y_4 = Label(fenetre5, text="y4 :")
	y_4_1 = Entry(fenetre5, textvariable=y_4_v)
	y_4_2 = Checkbutton(fenetre5, variable=y_4_vo)
	y_4_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_4_3.menu  =  Menu(y_4_3, tearoff = 0)
	y_4_3["menu"]  =  y_4_3.menu
	y_4_3.menu.add_checkbutton (label="Bleu", variable=y_4_c1)
	y_4_3.menu.add_checkbutton (label="Rouge", variable=y_4_c2)
	y_4_3.menu.add_checkbutton (label="Vert", variable=y_4_c3)
	y_4_3.menu.add_checkbutton (label="Jaune", variable=y_4_c4)
	y_4_3.menu.add_checkbutton (label="Marron", variable=y_4_c5)
	y_4_3.menu.add_checkbutton (label="Rose", variable=y_4_c6)
	y_4_3.menu.add_checkbutton (label="Orange", variable=y_4_c7)
	y_4_3.menu.add_checkbutton (label="Noir", variable=y_4_c8)

	y_5 = Label(fenetre5, text="y5 :")
	y_5_1 = Entry(fenetre5, textvariable=y_5_v)
	y_5_2 = Checkbutton(fenetre5, variable=y_5_vo)
	y_5_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_5_3.menu  =  Menu(y_5_3, tearoff = 0)
	y_5_3["menu"]  =  y_5_3.menu
	y_5_3.menu.add_checkbutton (label="Bleu", variable=y_5_c1)
	y_5_3.menu.add_checkbutton (label="Rouge", variable=y_5_c2)
	y_5_3.menu.add_checkbutton (label="Vert", variable=y_5_c3)
	y_5_3.menu.add_checkbutton (label="Jaune", variable=y_5_c4)
	y_5_3.menu.add_checkbutton (label="Marron", variable=y_5_c5)
	y_5_3.menu.add_checkbutton (label="Rose", variable=y_5_c6)
	y_5_3.menu.add_checkbutton (label="Orange", variable=y_5_c7)
	y_5_3.menu.add_checkbutton (label="Noir", variable=y_5_c8)

	y_6 = Label(fenetre5, text="y6 :")
	y_6_1 = Entry(fenetre5, textvariable=y_6_v)
	y_6_2 = Checkbutton(fenetre5, variable=y_6_vo)
	y_6_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_6_3.menu  =  Menu(y_6_3, tearoff = 0)
	y_6_3["menu"]  =  y_6_3.menu
	y_6_3.menu.add_checkbutton (label="Bleu", variable=y_6_c1)
	y_6_3.menu.add_checkbutton (label="Rouge", variable=y_6_c2)
	y_6_3.menu.add_checkbutton (label="Vert", variable=y_6_c3)
	y_6_3.menu.add_checkbutton (label="Jaune", variable=y_6_c4)
	y_6_3.menu.add_checkbutton (label="Marron", variable=y_6_c5)
	y_6_3.menu.add_checkbutton (label="Rose", variable=y_6_c6)
	y_6_3.menu.add_checkbutton (label="Orange", variable=y_6_c7)
	y_6_3.menu.add_checkbutton (label="Noir", variable=y_6_c8)

	y_7 = Label(fenetre5, text="y7 :")
	y_7_1 = Entry(fenetre5, textvariable=y_7_v)
	y_7_2 = Checkbutton(fenetre5, variable=y_7_vo)
	y_7_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_7_3.menu  =  Menu(y_7_3, tearoff = 0)
	y_7_3["menu"]  =  y_7_3.menu
	y_7_3.menu.add_checkbutton (label="Bleu", variable=y_7_c1)
	y_7_3.menu.add_checkbutton (label="Rouge", variable=y_7_c2)
	y_7_3.menu.add_checkbutton (label="Vert", variable=y_7_c3)
	y_7_3.menu.add_checkbutton (label="Jaune", variable=y_7_c4)
	y_7_3.menu.add_checkbutton (label="Marron", variable=y_7_c5)
	y_7_3.menu.add_checkbutton (label="Rose", variable=y_7_c6)
	y_7_3.menu.add_checkbutton (label="Orange", variable=y_7_c7)
	y_7_3.menu.add_checkbutton (label="Noir", variable=y_7_c8)

	y_8 = Label(fenetre5, text="y8 :")
	y_8_1 = Entry(fenetre5, textvariable=y_8_v)
	y_8_2 = Checkbutton(fenetre5, variable=y_8_vo)
	y_8_3 = Menubutton(fenetre5, text="Couleur", relief=RAISED)
	y_8_3.menu  =  Menu(y_8_3, tearoff = 0)
	y_8_3["menu"]  =  y_8_3.menu
	y_8_3.menu.add_checkbutton (label="Bleu", variable=y_8_c1)
	y_8_3.menu.add_checkbutton (label="Rouge", variable=y_8_c2)
	y_8_3.menu.add_checkbutton (label="Vert", variable=y_8_c3)
	y_8_3.menu.add_checkbutton (label="Jaune", variable=y_8_c4)
	y_8_3.menu.add_checkbutton (label="Marron", variable=y_8_c5)
	y_8_3.menu.add_checkbutton (label="Rose", variable=y_8_c6)
	y_8_3.menu.add_checkbutton (label="Orange", variable=y_8_c7)
	y_8_3.menu.add_checkbutton (label="Noir", variable=y_8_c8)

	bouton = Button(fenetre5, text="Afficher", command=fenetre5.destroy)


	# ...on leurs donnent les caractèristiques sur leurs polices...
	titre.config(font=('Arial', 14))
	y_1.config(font=('Arial', 14, 'bold'))
	y_1_1.config(font=('Arial', 14, 'bold'))
	y_2.config(font=('Arial', 14, 'bold'))
	y_2_1.config(font=('Arial', 14, 'bold'))
	y_3.config(font=('Arial', 14, 'bold'))
	y_3_1.config(font=('Arial', 14, 'bold'))
	y_4.config(font=('Arial', 14, 'bold'))
	y_4_1.config(font=('Arial', 14, 'bold'))
	y_5.config(font=('Arial', 14, 'bold'))
	y_5_1.config(font=('Arial', 14, 'bold'))
	y_6.config(font=('Arial', 14, 'bold'))
	y_6_1.config(font=('Arial', 14, 'bold'))
	y_7.config(font=('Arial', 14, 'bold'))
	y_7_1.config(font=('Arial', 14, 'bold'))
	y_8.config(font=('Arial', 14, 'bold'))
	y_8_1.config(font=('Arial', 14, 'bold'))
	bouton.config(font=('Arial', 14, 'bold'))


	# ...et on les placent dans la fenètre.
	titre.grid(row=1, column=1, columnspan=3)
	y_1.grid(row=2, column=2)
	y_1_1.grid(row=2, column=3)
	y_1_2.grid(row=2, column=4)
	y_1_3.grid(row=2, column=1)
	y_2.grid(row=3, column=2)
	y_2_1.grid(row=3, column=3)
	y_2_2.grid(row=3, column=4)
	y_2_3.grid(row=3, column=1)
	y_3.grid(row=4, column=2)
	y_3_1.grid(row=4, column=3)
	y_3_2.grid(row=4, column=4)
	y_3_3.grid(row=4, column=1)
	y_4.grid(row=5, column=2)
	y_4_1.grid(row=5, column=3)
	y_4_2.grid(row=5, column=4)
	y_4_3.grid(row=5, column=1)
	y_5.grid(row=6, column=2)
	y_5_1.grid(row=6, column=3)
	y_5_2.grid(row=6, column=4)
	y_5_3.grid(row=6, column=1)
	y_6.grid(row=7, column=2)
	y_6_1.grid(row=7, column=3)
	y_6_2.grid(row=7, column=4)
	y_6_3.grid(row=7, column=1)
	y_7.grid(row=8, column=2)
	y_7_1.grid(row=8, column=3)
	y_7_2.grid(row=8, column=4)
	y_7_3.grid(row=8, column=1)
	y_8.grid(row=9, column=2)
	y_8_1.grid(row=9, column=3)
	y_8_2.grid(row=9, column=4)
	y_8_3.grid(row=9, column=1)
	bouton.grid(row=10, column=2)


	# Mainloop pour que la fenètre reste ouverte.
	fenetre5.mainloop()

	# Fin : fenetre5.

	# Récuperation des valeurs pour les remettrent dans leurs variables
	# associées.
	y_1_v = y_1_v.get()
	y_1_vo = y_1_vo.get()
	y_2_v = y_2_v.get()
	y_2_vo = y_2_vo.get()
	y_3_v = y_3_v.get()
	y_3_vo = y_3_vo.get()
	y_4_v = y_4_v.get()
	y_4_vo = y_4_vo.get()
	y_5_v = y_5_v.get()
	y_5_vo = y_5_vo.get()
	y_6_v = y_6_v.get()
	y_6_vo = y_6_vo.get()
	y_7_v = y_7_v.get()
	y_7_vo = y_7_vo.get()
	y_8_v = y_8_v.get()
	y_8_vo = y_8_vo.get()
	y_1_c1 = y_1_c1.get()
	y_1_c2 = y_1_c2.get()
	y_1_c3 = y_1_c3.get()
	y_1_c4 = y_1_c4.get()
	y_1_c5 = y_1_c5.get()
	y_1_c6 = y_1_c6.get()
	y_1_c7 = y_1_c7.get()
	y_1_c8 = y_1_c8.get()
	y_2_c1 = y_2_c1.get()
	y_2_c2 = y_2_c2.get()
	y_2_c3 = y_2_c3.get()
	y_2_c4 = y_2_c4.get()
	y_2_c5 = y_2_c5.get()
	y_2_c6 = y_2_c6.get()
	y_2_c7 = y_2_c7.get()
	y_2_c8 = y_2_c8.get()
	y_3_c1 = y_3_c1.get()
	y_3_c2 = y_3_c2.get()
	y_3_c3 = y_3_c3.get()
	y_3_c4 = y_3_c4.get()
	y_3_c5 = y_3_c5.get()
	y_3_c6 = y_3_c6.get()
	y_3_c7 = y_3_c7.get()
	y_3_c8 = y_3_c8.get()
	y_4_c1 = y_4_c1.get()
	y_4_c2 = y_4_c2.get()
	y_4_c3 = y_4_c3.get()
	y_4_c4 = y_4_c4.get()
	y_4_c5 = y_4_c5.get()
	y_4_c6 = y_4_c6.get()
	y_4_c7 = y_4_c7.get()
	y_4_c8 = y_4_c8.get()
	y_5_c1 = y_5_c1.get()
	y_5_c2 = y_5_c2.get()
	y_5_c3 = y_5_c3.get()
	y_5_c4 = y_5_c4.get()
	y_5_c5 = y_5_c5.get()
	y_5_c6 = y_5_c6.get()
	y_5_c7 = y_5_c7.get()
	y_5_c8 = y_5_c8.get()
	y_6_c1 = y_6_c1.get()
	y_6_c2 = y_6_c2.get()
	y_6_c3 = y_6_c3.get()
	y_6_c4 = y_6_c4.get()
	y_6_c5 = y_6_c5.get()
	y_6_c6 = y_6_c6.get()
	y_6_c7 = y_6_c7.get()
	y_6_c8 = y_6_c8.get()
	y_7_c1 = y_7_c1.get()
	y_7_c2 = y_7_c2.get()
	y_7_c3 = y_7_c3.get()
	y_7_c4 = y_7_c4.get()
	y_7_c5 = y_7_c5.get()
	y_7_c6 = y_7_c6.get()
	y_7_c7 = y_7_c7.get()
	y_7_c8 = y_7_c8.get()
	y_8_c1 = y_8_c1.get()
	y_8_c2 = y_8_c2.get()
	y_8_c3 = y_8_c3.get()
	y_8_c4 = y_8_c4.get()
	y_8_c5 = y_8_c5.get()
	y_8_c6 = y_8_c6.get()
	y_8_c7 = y_8_c7.get()
	y_8_c8 = y_8_c8.get()

	# Configuration des couleurs des courbes.
	if y_1_c1 == 1:
		y_1_c = "blue"
	elif y_1_c2 == 1:
		y_1_c = "red"
	elif y_1_c3 == 1:
		y_1_c = "green"
	elif y_1_c4 == 1:
		y_1_c = "yellow"
	elif y_1_c5 == 1:
		y_1_c = "brown"
	elif y_1_c6 == 1:
		y_1_c = "pink"
	elif y_1_c7 == 1:
		y_1_c = "orange"
	elif y_1_c8 == 1:
		y_1_c = "black"
	else:
		y_1_c = "black"
	if y_2_c1 == 1:
		y_2_c = "blue"
	elif y_2_c2 == 1:
		y_2_c = "red"
	elif y_2_c3 == 1:
		y_2_c = "green"
	elif y_2_c4 == 1:
		y_2_c = "yellow"
	elif y_2_c5 == 1:
		y_2_c = "brown"
	elif y_2_c6 == 1:
		y_2_c = "pink"
	elif y_2_c7 == 1:
		y_2_c = "orange"
	elif y_2_c8 == 1:
		y_2_c = "black"
	else:
		y_2_c = "black"
	if y_3_c1 == 1:
		y_3_c = "blue"
	elif y_3_c2 == 1:
		y_3_c = "red"
	elif y_3_c3 == 1:
		y_3_c = "green"
	elif y_3_c4 == 1:
		y_3_c = "yellow"
	elif y_3_c5 == 1:
		y_3_c = "brown"
	elif y_3_c6 == 1:
		y_3_c = "pink"
	elif y_3_c7 == 1:
		y_3_c = "orange"
	elif y_3_c8 == 1:
		y_3_c = "black"
	else:
		y_3_c = "black"
	if y_4_c1 == 1:
		y_4_c = "blue"
	elif y_4_c2 == 1:
		y_4_c = "red"
	elif y_4_c3 == 1:
		y_4_c = "green"
	elif y_4_c4 == 1:
		y_4_c = "yellow"
	elif y_4_c5 == 1:
		y_4_c = "brown"
	elif y_4_c6 == 1:
		y_4_c = "pink"
	elif y_4_c7 == 1:
		y_4_c = "orange"
	elif y_4_c8 == 1:
		y_4_c = "black"
	else:
		y_4_c = "black"
	if y_5_c1 == 1:
		y_5_c = "blue"
	elif y_5_c2 == 1:
		y_5_c = "red"
	elif y_5_c3 == 1:
		y_5_c = "green"
	elif y_5_c4 == 1:
		y_5_c = "yellow"
	elif y_5_c5 == 1:
		y_5_c = "brown"
	elif y_5_c6 == 1:
		y_5_c = "pink"
	elif y_5_c7 == 1:
		y_5_c = "orange"
	elif y_5_c8 == 1:
		y_5_c = "black"
	else:
		y_5_c = "black"
	if y_6_c1 == 1:
		y_6_c = "blue"
	elif y_6_c2 == 1:
		y_6_c = "red"
	elif y_6_c3 == 1:
		y_6_c = "green"
	elif y_6_c4 == 1:
		y_6_c = "yellow"
	elif y_6_c5 == 1:
		y_6_c = "brown"
	elif y_6_c6 == 1:
		y_6_c = "pink"
	elif y_6_c7 == 1:
		y_6_c = "orange"
	elif y_6_c8 == 1:
		y_6_c = "black"
	else:
		y_6_c = "black"
	if y_7_c1 == 1:
		y_7_c = "blue"
	elif y_7_c2 == 1:
		y_7_c = "red"
	elif y_7_c3 == 1:
		y_7_c = "green"
	elif y_7_c4 == 1:
		y_7_c = "yellow"
	elif y_7_c5 == 1:
		y_7_c = "brown"
	elif y_7_c6 == 1:
		y_7_c = "pink"
	elif y_7_c7 == 1:
		y_7_c = "orange"
	elif y_7_c8 == 1:
		y_7_c = "black"
	else:
		y_7_c = "black"
	if y_8_c1 == 1:
		y_8_c = "blue"
	elif y_8_c2 == 1:
		y_8_c = "red"
	elif y_8_c3 == 1:
		y_8_c = "green"
	elif y_8_c4 == 1:
		y_8_c = "yellow"
	elif y_8_c5 == 1:
		y_8_c = "brown"
	elif y_8_c6 == 1:
		y_8_c = "pink"
	elif y_8_c7 == 1:
		y_8_c = "orange"
	elif y_8_c8 == 1:
		y_8_c = "black"
	else:
		y_8_c = "black"

	# Création d'une liste dans a.
	a = []

	# Tests pour créer la liste final à envoyer à la fonction dessine.
	if y_1_vo == 1:
		c = []
		c.append(y_1_v)
		c.append(y_1_c)
		a.append(c)
	if y_2_vo == 1:
		c = []
		c.append(y_2_v)
		c.append(y_2_c)
		a.append(c)
	if y_3_vo == 1:
		c = []
		c.append(y_3_v)
		c.append(y_3_c)
		a.append(c)
	if y_4_vo == 1:
		c = []
		c.append(y_4_v)
		c.append(y_4_c)
		a.append(c)
	if y_5_vo == 1:
		c = []
		c.append(y_5_v)
		c.append(y_5_c)
		a.append(c)
	if y_6_vo == 1:
		c = []
		c.append(y_6_v)
		c.append(y_6_c)
		a.append(c)
	if y_7_vo == 1:
		c = []
		c.append(y_7_v)
		c.append(y_7_c)
		a.append(c)
	if y_8_vo == 1:
		c = []
		c.append(y_8_v)
		c.append(y_8_c)
		a.append(c)

	# Retourne a.
	return a


def mainfx(b):
	"""
	Fonction principal.
	"""
	a = graf(b)
	#print(a)
	dessine(a)
