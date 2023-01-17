# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:46:13 2023

@author: julia
"""
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung
from lifelines import WeibullFitter
import seaborn as sns
def Weibull_def(df):
    #Überprüfen, ob es einen Null-Wert gibt
    a = 0 in df.Lebensdauer 
    #Wenn diese Aussage wahr ist, dann wird ein kleiner Wert dazu addiert
    if a == True:
        print('Der Wert Null kommt vor.\nUm die Weibull-Verteilung durchzuführen, wird zu den Werten der Lebensdauer 1E-15 hinzuaddiert.')
        df.Lebensdauer = df.Lebensdauer + 1e-15
        #Wenn diese Aussage falsch ist, dann kommt eine Meldung
    else:
        print('Der Wert Null kommt NICHT vor')
    
    #Weibull-Verteilung
    wbf = WeibullFitter().fit(df["Lebensdauer"], df["Zensur"], label='Weibull')
    #Grafik plotten
    sns.set(rc={'figure.figsize':(8,8)})
    plt.figure()
    wbf.plot_density()
    #Überschrift
    plt.title("Weibull",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Überlebenswahrscheinlichkeit",fontsize=15, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=20, labelpad=20)
    plt.show()
    #wbf.params_ Befehl, um die Parameter µ und sigma auszugeben
    l=wbf.lambda_
    r=wbf.rho_
    print('Für diese Weibullverteilung ergibt sich ein Lamda-Wert von',"%.3f" %l,'\nFür diese Weibullverteilung ergibt sich ein Rho-Wert von ',"%.3f" %r)
