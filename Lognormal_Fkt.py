# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:32:15 2022

@author: julia

"""
import numpy as np                          #Wissenschaftliches Rechnen und numerische Berechnungen
from scipy import stats                     #Wahrscheinlichekeitsverteilungen
import seaborn as sns                       #Statistische Darstellung
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung

def Lognormal_def(df):
    #Minimalwert der Lebensdauer bestimmen
    value_min = min(df.Lebensdauer)
    #Maximalwert der Lebensdauer bestimmen
    value_max = max(df.Lebensdauer)
    print('Der Minimal-Wert der Lebensdauer beträgt', '%.0f'%value_min)
    print('Der Minimal-Wert der Lebensdauer beträgt', '%.0f'%value_max)
    #µ und sigma schätzen
    s, loc, scale = stats.lognorm.fit(df.Lebensdauer, floc=0) #x0 is rawdata x-axis
    mu = np.log(scale)
    sigma = s
    print('Sigma entspricht:','%.2f'%s,'\nµ entspricht:','%.2f'%mu)
    #n ist die hälfe aller Werte
    n = df.shape[0]/2  
    #n wird zu einem integer
    n =int(n)
    #n Zahlen zwischen dem maximal und minimal-Wert der Lebensdauer
    z = np.linspace(value_min,value_max,n)
    #Grafik plotten
    sns.set(rc={'figure.figsize':(8,8)})
    plt.figure()
    a = stats.lognorm.pdf(z,mu,sigma)
    #Überschrift
    plt.title("Lognormal Verteilung",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Überlebenswahrscheinlichkeit",fontsize=15, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=15, labelpad=20)
    sns.lineplot(x=z, y=a)
    plt.show()
    return
