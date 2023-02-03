from tkinter import *
from tkinter import messagebox
machine = Tk() 
machine.title("Convertisseur de monnaie")
machine.geometry("300x300")
machine.config(bg="#202630")
my_font = ('Arial', 16, 'bold')


#EN-TÊTE DE LA MACHINE
Mylabel=Label(machine, text="Convertisseur de monnaie", pady=20,fg='orange', bg="#202630", font=my_font)
Mylabel.pack()

#LABEL
Mylabel1=Label(machine, text="Montant à convertir :",fg='white', bg="#202630", font=('Times', 13, 'bold'))
Mylabel1.pack()

#BARRE DE CALCUL
entry1 = Entry(machine, width=18, font=('Times', 12))
entry1.pack()


#FONCTION DU BOUTON1
def euro_to_dirham():
    d = 11.04   # 11.04 dirham
    # 1 euro équivaut à 11.04 dirham marocain
    somme = float(entry1.get())

    if somme == float(entry1.get()):
        resultat1 = somme*d
        Label(machine, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None


#FONCTION DU BOUTON2
def dirham_to_euro():
    d = 11.04
    somme = float(entry1.get())


    if somme == float(entry1.get()):
        resultat1 = somme/d
        Label(machine, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None


#FONCTION DU BOUTON3 historique






#BOUTON QUI PERMET DE CONVERTIR LES EUROS EN DIRHAMS
bouton1 = Button(machine , text = "Euro → Dirham", bg = "orange" , fg = "white", height=1, width=15, command=euro_to_dirham)
bouton1.pack()

#BOUTON QUI PERMET DE CONVERTIR LES DIRHAMS EN EUROS
bouton2 = Button(machine , text = "Dirham → Euro", bg = "orange" , fg = "white", height=1, width=15, command=dirham_to_euro)
bouton2.pack()

#LABEL "RESULTAT"
Mylabel2=Label(machine, text="Résultat :", font=('Times', 13, 'bold'), pady=10,fg='white', bg="#202630")
Mylabel2.pack()

#BOUTON QUI PERMET DE VOIR L'HISTORIQUE DES CALCULS
#bouton3 = Button(machine , text = "Historique", bg = "orange" , fg = "white", width=5, padx=10, command=historique)
#bouton3.pack(side=BOTTOM)


machine.mainloop()