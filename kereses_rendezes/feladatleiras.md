# Hiányzó Érme Összeg
**Időkorlát:** 1.00 s  
**Memóriakorlát:** 512 MB

## Link
https://cses.fi/problemset/task/2183/

## Feladat

Van *n* darab érméd, mindegyik pozitív egész értékkel.  
Mi a legkisebb olyan összeg, amelyet nem tudsz előállítani az érmék egy részhalmazának felhasználásával?

## Bemenet

Az első sor egy egész számot tartalmaz, *n*-t: az érmék számát.  
A második sor *n* darab egész számot tartalmaz: az egyes érmék értékeit.

## Kimenet

Egyetlen egész számot kell kiírni: a legkisebb olyan összeget, amelyet nem lehet előállítani az érmék egy részhalmazával.

## Korlátok

- 1 ≤ *n* ≤ 2 × 10⁵
- 1 ≤ *xᵢ* ≤ 10⁹

## Példa

**Bemenet:**
5 2 9 1 2 7


**Kimenet:**
64


## Megjegyzés

A feladat megoldásához érdemes az érméket növekvő sorrendbe rendezni, majd iteratívan meghatározni a legkisebb elő nem állítható összeget.
