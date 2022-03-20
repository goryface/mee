#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:42:26 2022

@author: rais
"""
import numpy as np
g = 10.
L = 1.
lamb=20
omega0 = np.sqrt(g/L)
# fonctions de base
def F(Y,t):
    """second membre de l'EDO"""
    global omega0
    dY = np.array([Y[1],-2*lamb*omega0-omega0**2*np.sin(Y[0])])
    return dY


from scipy.integrate import odeint
def solution(theta0):
    T = np.linspace(0.,2*(2*np.pi)/omega0,101)
    # condition initiale
    Y0 = np.array([theta0,0.])
    # integration
    Y = odeint(F, Y0, T)
    return T,Y

import matplotlib.pyplot as plt
def trace(T,Y):
    Theta=Y[:,0]
    
    plt.figure(figsize=(14,7))
    # trace theta(t)
    plt.subplot(1,2,1)
    plt.plot(T,(Theta*180/3.14),'x',label="$\\theta$",lw=2)
    plt.title('Angle $\\theta(t)$')
    plt.xlabel('t')
    plt.legend()