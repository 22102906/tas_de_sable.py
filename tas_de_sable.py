############################################
#GROUPE LDDMP2
#CHASSOT Elise
#REYSSET Hugo
#ASADUZZAMAN Sihad
#RIZK Karen
#https://github.com/22102906/tas_de_sable.py
############################################

###import des modules#####
import tkinter as tk

#####variables globales########
height=500
width=500




racine=tk.Tk()
racine.title("tas_de_sable")
canvas=tk.Canvas(racine,height=height, width=width)
config_aleatoire=tk.Button(racine, text="Configuration aléatoire")

canvas.pack()
config_aleatoire.pack()


racine.mainloop()


















