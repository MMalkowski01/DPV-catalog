#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*-

from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def otw_wynik(nazwa_pliku):
        plik = open(nazwa_pliku,"r")
        lista_rek=[]
        lista_dek=[]
        lista_P_orb=[]
        lista_P_long = []
        for linia in plik:
                kolumna = linia.split()
                lista_rek.append(kolumna[0])
                lista_dek.append(kolumna[1])
                lista_P_orb.append(float(kolumna[2]))
                lista_P_long.append(float(kolumna[3]))
        plik.close()
        return (lista_rek,lista_dek,np.array(lista_P_orb),np.array(lista_P_long))
        
rek, dek, P_orb, P_long = otw_wynik("wynik")
catalog = SkyCoord(rek, dek, unit=(u.hourangle, u.deg))
MWB = SkyCoord("17:45:40.036", "-29:00:28.17",unit=(u.hourangle, u.deg))
LMC = SkyCoord("05:23:34.0", "-69:45:24",unit=(u.hourangle, u.deg))
SMC = SkyCoord("00:52:44.8", "-72:49:43",unit=(u.hourangle, u.deg))

d_LMC = catalog.separation(LMC).degree
d_SMC = catalog.separation(SMC).degree
d_MWB = catalog.separation(MWB).degree
plt.figure(figsize=(10,7))
maska_LMC = (d_LMC<15)
maska_SMC = (d_SMC<5)
maska_MWB = (d_MWB<15)
plt.scatter(P_orb[maska_LMC],P_long[maska_LMC],c="firebrick",marker="v")  
plt.scatter(P_orb[maska_SMC],P_long[maska_SMC],c="navy",marker="P")
plt.scatter(P_orb[maska_MWB],P_long[maska_MWB],c="forestgreen",marker=".")
plt.xlabel("P orb[d]")
plt.ylabel("P long[d]")
plt.title("P-P plot")
plt.gca().set_xscale("log")
plt.gca().set_yscale("log")
plt.gca().tick_params(right=True, top=True,which ="both",direction="in", labelright=True, labeltop=True)
plt.show()
