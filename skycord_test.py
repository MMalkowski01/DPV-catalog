#!/usr/bin/env python                                                 
# -*- coding: utf-8 -*-
from astropy import units as u
from astropy.coordinates import SkyCoord
def otw_A(nazwa_pliku):
        plik = open(nazwa_pliku,"r")
        lista_id=[]
        lista_rek=[]
        lista_dek=[]
        for linia in plik:
                kolumna = linia.split()
                lista_id.append(kolumna[0])
                lista_rek.append(kolumna[3])
                lista_dek.append(kolumna[4])
        plik.close()
        return (lista_id,lista_rek,lista_dek)

def otw_C(nazwa_pliku):
        plik = open(nazwa_pliku,"r")
        lista_id=[]
        lista_rek=[]
        lista_dek=[]
        lista_per1=[]
        lista_per2=[]
        for linia in plik:
                kolumna = linia.split()
                lista_id.append(kolumna[0])
                lista_rek.append(kolumna[1])
                lista_dek.append(kolumna[2])
                lista_per1.append(kolumna[3])
                lista_per2.append(kolumna[4])
        plik.close()
        return (lista_id,lista_rek,lista_dek,lista_per1,lista_per2)

def otw_Period_A(nazwa_pliku):
        plik = open(nazwa_pliku,"r")
        lista_id=[]
        lista_per1=[]
        lista_per2=[]
        for linia in plik:
                kolumna = linia.split()
                lista_id.append(kolumna[0])
                lista_per1.append(kolumna[3])
                lista_per2.append(kolumna[7])
        plik.close()
        return (lista_id,lista_per1,lista_per2)

plik_A=otw_A("2010AcA....60..179P")
plik_C=otw_C("2003AA...399L..47M")
plik_Per=otw_Period_A("2010AcA....60..179P_Period.dat")
c = SkyCoord(plik_A[1], plik_A[2],unit=(u.hourangle, u.deg))
catalog = SkyCoord(plik_C[1], plik_C[2],unit=(u.hourangle, u.deg))
idxc, idxcatalog, d2d, _ = catalog.search_around_sky(c, 2*u.arcsec)

out = open("wynik","w")
numerek = 0
usuniete_C =[]
for i,linia in enumerate(plik_A[0]):
        tekst = plik_A[1][i]+" "+plik_A[2][i]+" "+plik_Per[1][i]+" "+plik_Per[2][i]+" "+plik_A[0][i]+" "
        if i in idxc:
                IDC = plik_C[0][idxcatalog[numerek]]
                tekst += IDC
                numerek+=1
                usuniete_C.append(IDC)
        else:
                tekst+="-"
        print(tekst,file=out)
for i,linia in enumerate(plik_C[0]):
        if plik_C[0][i] in usuniete_C:
                continue
        tekst = plik_C[1][i]+" "+plik_C[2][i]+" "+plik_C[3][i]+" "+plik_C[4][i]+" "+"-               "+" "+plik_C[0][i]
        print(tekst,file=out)        
out.close()






exit()
