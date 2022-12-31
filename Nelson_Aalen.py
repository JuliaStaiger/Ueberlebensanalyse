# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:43:13 2022

@author: julia
"""
from lifelines import KaplanMeierFitter     #für die Kaplanmeier-Verteilung 
kmf = KaplanMeierFitter()
import seaborn as sns                       #Statistische Darstellung
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung
from lifelines import NelsonAalenFitter     #für die Nelson-Aalen-Schätzung

def Beide_Verteilungen_def(df):
    #Beide Verteilungen in eine Grafik
    sns.set(rc={'figure.figsize':(8,8)})
    plt.figure()
    #durations = Lebensdauer; event_observed = Zensur
    kmf.fit(durations =  df["Lebensdauer"], event_observed = df["Zensur"], label = 'Kaplan-Meier-Verteilung')
    ax = kmf.plot()
    naf = NelsonAalenFitter(nelson_aalen_smoothing=False)
    naf.fit(df["Lebensdauer"], event_observed = df["Zensur_2"], label = 'Nelson-Aalen-Verteilung')
    naf.cumulative_hazard_
    ax = naf.plot(ax=ax)
    #Überschrift
    plt.title("Kaplan-Meier und Nelson-Aalen-Schätzung",fontsize=15)
    #Benennung der y-Achse
    plt.ylabel("Wahrscheinlichkeit",fontsize=15, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=15, labelpad=20)
    #Legende plotten
    plt.legend()
    plt.show()
    return

def Nelson_Aalen_def(df):
    #Nelson-Aalen Schätzung durchführen
    naf = NelsonAalenFitter(nelson_aalen_smoothing=False)
    #durations = Lebensdauer; event_observed = Zensur
    naf.fit(durations = df["Lebensdauer"], event_observed = df["Zensur_2"],label = 'Nelson-Aalen-Verteilung')
    naf.cumulative_hazard_
    #Grafik plotten
    sns.set(rc={'figure.figsize':(8,8)})
    plt.figure()
    naf.plot_cumulative_hazard()
    #Überschrift
    plt.title("Nelson-Aalen-Schätzung",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Ausfallrate",fontsize=20, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=20, labelpad=20)
    plt.show()
    return
