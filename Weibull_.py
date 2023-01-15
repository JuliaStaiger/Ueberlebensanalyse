# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:00:25 2023

@author: julia
"""
import matplotlib.pyplot as plt             #ermöglicht graphische Dastellung

import seaborn as sns
import predictr
from predictr import Analysis, PlotAll
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
    
    a = Analysis(df=df.Lebensdauer, bounds='lrb', bounds_type='2s', show = False, unit= 'min')
    a.mle()
    sns.set(rc={'figure.figsize':(8,8)})
    # Use weibull_pdf method in PlotAll to plot the Weibull pdfs
    # beta contains the Weibull shape parameters, which were estimated using Analysis class.
    # Do the same for the Weibull scale parameter eta.
    # Cusomize the path directory in order to use this code
    value_max = max(df.Lebensdauer)
    plt.ylabel("Dichtefunktion",fontsize=15, labelpad=50)
    #Benennung der x-Achse
    plt.xlabel("Überlebenszeit",fontsize=15, labelpad=20)
    #PlotAll().weibull_pdf(beta = [a.beta], eta = [a.eta], linestyle=['-'], labels = ['A'], x_bounds=[0, value_max, 200], plot_title = 'Weibull-Verteilung', x_label='Überlebenszeit', y_label='Density Function', save=False)#, color=['black'])
    PlotAll().weibull_pdf(beta = [a.beta], eta = [a.eta], linestyle=['-'], labels = ['A'], x_bounds=[0, value_max, 200],plot_title = 'Weibull-Verteilung', save=False)#, color=['black'])
    
    print('Rho entspricht:','%.2f' %a.beta)
    print('Lamda entspricht:','%.2f' %a.eta)
    

