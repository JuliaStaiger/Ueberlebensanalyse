# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:28:03 2023

@author: julia
"""
import numpy as np                          #Wissenschaftliches Rechnen und numerische Berechnungen
from scipy import stats                     #Wahrscheinlichekeitsverteilungen
import seaborn as sns                       #Statistische Darstellung
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung
from scipy.stats import lognorm

def Lognormal_def(df):
    s = df.Lebensdauer
    s = np.array(s)
    #Daten sortieren
    s.sort()
    # Schätzung von mu und sigma
    mu_est= np.mean(np.log(s))
    sigma_est = np.std(np.log(s))
    #Graphik erstellen
    fig, ax = plt.subplots(1, 1)
    sns.set(rc={'figure.figsize':(8,8)})
    #Überschrift
    plt.title("Dichtefunktion",fontsize=20)
    #Benennung der y-Achse
    plt.ylabel("Dichte",fontsize=15, labelpad=20)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=15, labelpad=20)
    #Erstellung der Graphik
    ax.hist(s, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
    est,=ax.plot(s, lognorm.pdf(s,sigma_est,mu_est,scale=np.exp(mu_est)),label='Direkte Schätzung')
    print('Sigma entspricht:','%.2f'%sigma_est,'\nµ entspricht:','%.2f'%mu_est)
    
