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
#Hauteur du canvas
height=500
#Largeur du canvas
width=500
#taille de la grille
N=3

#######Listes###########
L_courant=[[]]

########fonction du boutton##########
def bt_aleatoire():
    pass

def conf_courante():
    pass




racine=tk.Tk()
racine.title("tas_de_sable")
canvas=tk.Canvas(racine,height=height, width=width)
config_aleatoire=tk.Button(racine, text="Configuration aléatoire",command=bt_aleatoire)

canvas.pack()
config_aleatoire.pack()


racine.mainloop()


















