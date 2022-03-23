# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

dtst = pd.read_csv('graph_1.csv') 
#Réparer les 2 colonnes pour mieux visualiser les données
#Stocker la 1ere colonne dans axe
axe_ordonnee = dtst.iloc[:,0]
#Stocker la derniere colonne dans axe
axe_abscisse = dtst.iloc[:,-1]

#Mise en place de graphe simple
plt.plot(axe_abscisse, axe_ordonnee)

#Labeliser l'Axes et titre
plt.title("évolution de portefeuille")
plt.xlabel("Temps")
plt.ylabel("Montant du capitale")

#Déterminer le couleur de droit
plt.plot(axe_abscisse, axe_ordonnee, 'green')

#Sauvegarder le graphique en format pdf
plt.savefig('graphe.pdf', format='pdf')