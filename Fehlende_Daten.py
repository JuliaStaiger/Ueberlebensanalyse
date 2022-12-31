# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:15:12 2022

@author: julia
"""

def Fehlende_Daten_def(df):
    Null= df.isnull().sum()
    #Einstellung der Größe für die nächste Grafik
    import seaborn as sns    
    sns.set(rc={'figure.figsize':(8,8)})
    b =sum(Null)
    if b == 0:
        print('Es fehlen keine Werte.')
    elif b >0:
        print('Es fehlen Werte.\nDie Anzahl der fehlenden Werte entspricht: '"%.0f" %b)
        Null_1=Null>0
        Null_1=Null[Null_1]
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
        while a> 0:
            a= df.iloc[Zahl_Zeile,].isnull().sum()
            Zahl_Zeile= Zahl_Zeile+1
            if a == 0:
                break
        for d in range(0,e):
            h =df[Null_1.index[d]]
            f= h.iloc[Zahl_Zeile-1,]
            if type(f) == str:
                print ('Die folgende Variable ist ein string: ' + Null_1.index[d] )
            else:
                print('Die folgende Variable ist ein float: ' + Null_1.index[d])
                #Fehlen Daten, so wird der Mittelwert aller Daten aus der Spalte ermittelt und diesen für die fehlenden Zahlen übernommen.
                df[Null_1.index[d]].fillna(df[Null_1.index[d]].mean(), inplace = True)
                print('Fehlende Daten wurden ersetzt.')
                