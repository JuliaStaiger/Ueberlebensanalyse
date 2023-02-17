# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:15:12 2022

@author: julia
"""
import seaborn as sns 

def Fehlende_Daten_def(df):
    #Erstellung einer Serie mit allen Variablen, sowie die Anzahl deren Null-Werte
    Null= df.isnull().sum()   
    sns.set(rc={'figure.figsize':(8,8)})
    #b gibt die Anzahl aller fehlenden Werte an
    b =sum(Null)
    #Ist b gleich Null, so fehlen keine Daten
    if b == 0:
        print('Es fehlen keine Werte.')
    #Ist b größer Null, gibt es fehlende Werte
    elif b >0:
        print('Es fehlen Werte.\nDie Anzahl der fehlenden Werte entspricht: '"%.0f" %b)
        #Neue Serie erstellen mit den Variablen, bei denen Werte fehlen
        Null_1=Null>0
        Null_1=Null[Null_1]
        #e gibt die Anzahl der Variablen an, bei denen Werte fehlen
        e= Null_1.shape[0]
        print('Bei den folgenden Variablen fehlen Daten: ')
        #Eine Schleife gibt die Namen der Variablen aus
        for i in range(0, e):
            a  =Null_1.index[i]
            print(a)
            if i== e:
                break
        Zahl_Zeile = 0
        a= df.iloc[0,].isnull().sum()
        #Zeile finde, in der keine Daten fehlen
        #Solange NaN-Werte in der Zeile vorhanden sind wird die nächste genommen
        while a> 0:
            a= df.iloc[Zahl_Zeile,].isnull().sum()
            Zahl_Zeile= Zahl_Zeile+1
            if a == 0:
                break
        #Datentypen der jeweiligen Variable untersuchen
        for d in range(0,e):
            h =df[Null_1.index[d]]
            f= h.iloc[Zahl_Zeile-1,]
            #Ist der Datentyp ein string, so können die Daten nicht ersetzt werden
            if type(f) == str:
                print ('Die folgende Variable ist ein string: ' + Null_1.index[d] )
            #Bei anderen Datentypen werden die Daten durch den Mittelwert ersetzt
            else:
                print('Die folgende Variable ist ein float: ' + Null_1.index[d])
                #Fehlen Daten, so wird der Mittelwert aller Daten aus der Spalte ermittelt und diesen für die fehlenden Zahlen übernommen.
                df[Null_1.index[d]].fillna(df[Null_1.index[d]].mean(), inplace = True)
                print('Fehlende Daten wurden ersetzt.')
                