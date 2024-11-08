# TRIP - Utazás
#dinamikus-programozás

## LINK
https://www.spoj.com/problems/TRIP/


Alice és Bob el szeretnének menni nyaralni. Mindketten készítettek egy listát az általuk meglátogatandó városokról, sorrendben. Egy város többször is szerepelhet egy listán. Mivel együtt szeretnének utazni, meg kell egyezniük egy közös útvonalban. Egyikük sem akarja megváltoztatni a saját listája városainak sorrendjét vagy új városokat hozzáadni. Ezért nincs más választásuk, mint hogy néhány várost eltávolítsanak a listájukról. Természetesen a közös útvonalnak a lehető legtöbb várost kell tartalmaznia, hogy minél több látnivalót láthassanak. Pontosan 26 város található a régióban. Ezért a városokat kisbetűkkel jelölik 'a'-tól 'z'-ig.

## Bemenet
A bemenet első sora tartalmaz egy T ≤ 10 számot, amely a következő tesztesetek számát jelzi. Minden teszteset két sorból áll; az első sor Alice listája, a második sor Bob listája. Minden lista 1 és 80 közötti kisbetűkből áll.

## Kimenet
A kimenetnek minden tesztesethez tartalmaznia kell az összes lehetséges közös útvonalat pontosan egyszer, amelyek megfelelnek a fenti feltételeknek. Legalább egy ilyen útvonal létezik, de soha nem több mint 1000 különböző útvonal. A kimenetet lexikografikus sorrendben kell megjeleníteni. Minden teszteset kimenetének végére egy üres sort kell illeszteni.

## Példa
### Bemenet
1  
abcabcaa  
acbacba


### Kimenet
ababa  
abaca  
abcba  
acaba   
acaca   
acbaa  
