# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:35:50 2021

@author: Chloé
"""

#-------- interface
# creation de l'interface 
from tkinter import * 
#from main import *
from PIL import Image, ImageTk 
import os 


#Repertoire courant
import os
repertoire = os.getcwd()
os.chdir(repertoire)

#creer une premiere fenetre 
window = Tk()


# personnaliser la fenetre 
window.title("Projet Python")
window.geometry("1080x720")
window.minsize(1080,720)
window.config(background="#048B9A")


# creer une nouvelle fenetre 
def action1():
    win = Toplevel(window)
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Evolution du mot 'death' au cours de l'annee 2020",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    texteLabel2 = Label(win, text="L'evolution du mot 'death' semble fortement correlee avec les confinements que les Etats ont mis en place.""\n""On voit que le regain d'interet pour ce mot coincide avec les periodes de remise en confinement.""\n""Le rebond de 'death', en Janvier, indique un potentiel reconfinement...",bg="#048B9A")
    texteLabel2.pack() 
    image = PhotoImage(file=r"mort.png")
    canvas = Canvas(win,bg="#048B9A",width=360,height=300)
    canvas.create_image(image.width()/2,image.height()/2,image=image,anchor=CENTER)
    label1=Label(canvas, image=image,bg="#048B9A")
    canvas.pack()
    image.pack()

def action2():
    win = Toplevel(window)
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Evolution du mot 'vaccine' au cours de l'année 2020",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    texteLabel2 = Label(win,text="L'utilisation du mot 'vaccine' explose au cours du mois de Janvier 2021.""\n" "Il s'agit de la date a laquelle la plupart des pays occidentaux ont deploye leurs vaccins.""\n""Cette evolution n'est donc pas etonnante en raison de la polimique qu'ils suscitent. (#complotistesReddit)",bg="#048B9A")
    texteLabel2.pack() 
    image = PhotoImage(file=r"histo_vaccin.png")
    canvas = Canvas(win,bg="#048B9A",width=370,height=300)
    canvas.create_image(image.width()/2,image.height()/2,image=image,anchor=CENTER)
    label1=Label(canvas, image=image,bg="#048B9A")
    canvas.pack()
    image.pack()

def action3():
    win = Toplevel(window)
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Evolution du mot 'patients' au cours de l'année 2020",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    texteLabel2 = Label(win,text="On peut apercevoir sur ce graphique les 2 vagues de contamination.""\n""Et potentiellement une 3eme deja en cours...",bg="#048B9A")
    texteLabel2.pack() 
    image = PhotoImage(file=r"patient.png")
    canvas = Canvas(win,bg="#048B9A",width=360,height=300)
    canvas.create_image(image.width()/2,image.height()/2,image=image,anchor=CENTER)
    label1=Label(canvas, image=image,bg="#048B9A")
    canvas.pack()
    image.pack()
    
def create1():
    win = Toplevel(window)
    win.title("Projet Python")
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Description generale",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    texteLabel1 = Label(win ,text="1) Voici les mots les plus frequents dans le corpus : ",font=("Arial",10),bg="#048B9A")
    texteLabel1.pack()
  #  texteLabel2 = Label(win ,text=data_mot.head(10),font=("Arial",10),bg="#048B9A")
  #  texteLabel2.pack()
    texteLabel3 = Label(win ,text="2) Voici le nuage de mots : ",font=("Arial",10),bg="#048B9A")
    texteLabel3.pack()    
    image = PhotoImage(file=r"nuage_mot_all.png")
    canvas = Canvas(win,bg="#048B9A",width=345,height=180)
    canvas.create_image(image.width()/2,image.height()/2,image=image,anchor=CENTER)
    label1=Label(canvas, image=image,bg="#048B9A")
    canvas.pack()
    image.pack()
    
def create2():
    win = Toplevel(window)
    win.title("Projet Python")
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Nuages de mots Reddit&Arxiv",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    texteLabel4 = Label(win, text="On remarque que les deux nuages de mots possèdent des similitudes.""\n " "Cependant on observe également que Reddit contient des mots relatifs à l'opinion des utilisateurs""\n" "alors qu'Arxiv est davantage tourné vers la recherche scientifique (avec des mots comme data, machine learning...)",bg="#048B9A")
    texteLabel4.pack() 
    texteLabel2 = Label(win ,text="Nuage de mots Reddit ",font=("Arial",10),bg="#048B9A")
    texteLabel2.pack(anchor=W)    
    texteLabel3 = Label(win ,text="Nuage de mots Arxiv ",font=("Arial",10),bg="#048B9A")
    texteLabel3.pack(anchor=E)  
    image1 = PhotoImage(file=r"nuage_mot_reddit.png")
    image2 = PhotoImage(file=r"nuage_mot_arxiv.png")
    canvas = Canvas(win,bg="#048B9A",width=690,height=175)
    canvas.create_image(image1.width(),image1.height(),image=image1,anchor=SE)
    canvas.create_image(image2.width(),image2.height(),image=image2,anchor=SW)
    canvas.pack()
    image1.pack()
    image2.pack()
    
    
def create3():
    win = Toplevel(window)
    win.title("Projet Python")
    win.geometry("1080x720")
    win.minsize(1080,720)
    win.config(background="#048B9A")
    texteLabel = Label(win ,text="Evolution des mots",font=("Arial",40),bg="#048B9A")
    texteLabel.pack()
    button1 = Button(win,text="mot cle 'death'",bg="#FEE347",font=("Arial",20),command=action1)
    button2 = Button(win,text="mot cle 'vaccine'",bg="#FEE347",font=("Arial",20),command=action2)
    button3 = Button(win,text="mot cle 'patients'",bg="#FEE347",font=("Arial",20),command=action3)
    button1.pack(pady=1,fill=X)
    button2.pack(pady=1,fill=X)
    button3.pack(pady=1,fill=X)
    
    
#ajouter texte
label_title = Label(window ,text="Coronavirus",font=("Arial",40),bg="#048B9A")
label_title.pack()

#ajouter bouton
button1 = Button(window,text="Description generale",bg="#FEE347",font=("Arial",20),command = create1)
button2 = Button (window,text="Nuages de mots Reddit&Arxiv",bg="#FEE347",font=("Arial",20),command = create2)
button3 = Button (window,text="Evolution des mots",bg="#FEE347",font=("Arial",20),command = create3)

button1.pack(pady=1,fill=X)
button2.pack(pady=1,fill=X)
button3.pack(pady=1,fill=X)




#afficher la fenetre 
window.mainloop()
