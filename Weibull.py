# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 20:21:12 2023

@author: julia
"""
import seaborn as sns                       #Statistische Darstellung
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung
from scipy.stats import weibull_min
import numpy as np
from lifelines import WeibullFitter
    
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
    wbf = WeibullFitter()
    r = df.Lebensdauer
    r = np.array(r)
    #Daten sortieren
    r.sort()
    wbf.fit(r)
    #Schätzung der Parameter
    print('Rho entspricht:','%.2f ' %wbf.rho_)
    print('Lamda entspricht:','%.2f' %wbf.lambda_)
    #Graphik erstellen 
    fig, ax = plt.subplots(1, 1)
    sns.set(rc={'figure.figsize':(8,8)})
    #Überschrift
    plt.title("Dichtefunktion",fontsize=15)
    #Benennung der y-Achse
    plt.ylabel("Dichte",fontsize=15, labelpad=50)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=15, labelpad=20)
    ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
    est_Ll_Fit,=ax.plot(r, weibull_min.pdf(r,wbf.rho_, 0 ,wbf.lambda_), linestyle=':',label='Lifelines Fitter')
    