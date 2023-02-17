# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:18:24 2022

@author: julia
"""


from lifelines import KaplanMeierFitter     #für die Kaplanmeier-Verteilung    
import seaborn as sns                       #Statistische Darstellung
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung
kmf = KaplanMeierFitter()

    
def Kaplan_Meier_def(df):
    #Durchführung einer Kaplan-Meier Schätzung
    kmf = KaplanMeierFitter()
    #durations = Lebensdauer; event_observed = Zensur
    kmf.fit(durations =  df["Lebensdauer"], event_observed = df["Zensur"],label = 'Kaplan-Meier-Verteilung')
    #Grafik plotten
    sns.set(rc={'figure.figsize':(8,8)})
    plt.figure()
    kmf.plot()
    #Überschrift
    plt.title("Kaplan-Meier-Schätzung",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Überlebenswahrscheinlichkeit",fontsize=20, labelpad=50)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=20, labelpad=20)
    plt.show() 
    return

def Kaplan_def(df):
    #Kaplan-Meier Schätzung ohne Konfidenzintervalle    
    sns.set(rc={'figure.figsize':(8,8)})
    kmf.fit(durations =  df["Lebensdauer"], event_observed = df["Zensur"],label = 'Kaplan-Meier-Verteilung')
    plt.figure()
    kmf.survival_function_.plot()
    #Überschrift
    plt.title("Kaplan-Meier-Schätzung",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Überlebenswahrscheinlichkeit",fontsize=20, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=20, labelpad=20)
    plt.show()
    return
