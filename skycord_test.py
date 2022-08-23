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
        for linia in plik:
                kolumna = linia.split()
                lista_id.append(kolumna[0])
                lista_rek.append(kolumna[1])
                lista_dek.append(kolumna[2])
        plik.close()
        return (lista_id,lista_rek,lista_dek)

plik_A=otw_A("2010AcA....60..179P")
plik_C=otw_C("2003A_26A...399L..47M")
c = SkyCoord(plik_A[1], plik_A[2],unit=(u.hourangle, u.deg))
catalog = SkyCoord(plik_C[1], plik_C[2],unit=(u.hourangle, u.deg))
idxc, idxcatalog, d2d, _ = catalog.search_around_sky(c, 2*u.arcsec)


out = open("wynik","w")
for numer,idc,idcatalog in zip(d2d,idxc,idxcatalog):
        if numer>0:
                print(plik_A[0][idc],plik_A[0][idcatalog],idc,idcatalog,numer.to(u.arcsec).value)
        if idc == idcatalog:
                continue
        print(plik_A[0][idc],plik_C[0][idcatalog],idc,idcatalog,numer.to(u.arcsec).value,file=out)
#for i,nazwa in enumerate(plik_A[0]):
        #tekst = plik_A[0][i]
#print(tekst)





exit()
