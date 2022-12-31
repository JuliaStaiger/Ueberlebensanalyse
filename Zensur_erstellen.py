# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:09:55 2022

@author: julia
"""


def Zensur_erstellen_def(df):
    #Abfrage, ob Zensur verfügbar ist
    a = input('Ist die Variable Zensur verfügbar? (Mit Ja oder Nein antworten): ')
    #Wenn die Antwort Ja ist, dann wird der Text ausgegeben
    if a == 'Ja':
        print('Zensur ist verfügbar')
    #Ist die Antwort Nein, so wird eine Variable erzeugt, anhand von Werten und einem Grenzwert
    elif a=='Nein':
        print('Zensur ist nicht verfügbar')
        #Abfrage nach der Variable
        c= input('Name der Variable, mit den Werten für die Variable Zensur?')
        b = input('Grenze?')
        print('Zensur wurde erstellt')
        #Unterhalb dem Wert b hat die Zensur den Wert 0 und überhalb 1
        df.loc[df[c] > int(b), 'Zensur'] = 1 # oberhalb der Grenze 1
        df.loc[df[c] < int(b), 'Zensur'] = 0 # unterhalb der Grenze 0
        print('Zensur wurde erstellt')
    else: 
        print('Fehler: Keine gültige Antwort')
        #Die ersten 5 Zeilen der Tabelle wird angezeigt, um zu überprüfen, ob alles funktioniert hat 
  