
# 8 Királynő probléma
**Időkorlát:** 1.00 s  
**Memóriakorlát:** 512 MB


## Link
https://cses.fi/problemset/task/1624/

## Feladatleírás

A sakk klasszikus 8 királynő feladatában az a cél, hogy elhelyezzünk nyolc királynőt egy 8x8-as táblán úgy, hogy azok ne üssék egymást. Ez azt jelenti, hogy nem lehet két királynő ugyanabban a sorban, oszlopban vagy átlóban.

Ebben a változatban a tábla bizonyos mezői akadályozottak lehetnek, amelyeket királynők nem foglalhatnak el. Az akadályozott mezőket egy `*` karakter jelöli.

A feladat az, hogy határozzuk meg, hány lehetséges módja van a nyolc királynő elhelyezésének a táblán, hogy azok ne üssék egymást, és ne kerüljenek akadályozott mezőkre.

## Bemenet

A bemenet nyolc sort tartalmaz, mindegyik sorban nyolc karaktert (`.` vagy `*`). A `.` karakter egy üres mezőt jelöl, ahová királynőt helyezhetünk, míg a `*` karakter egy akadályozott mezőt jelöl, ahová nem helyezhetünk királynőt.

## Kimenet

A programnak egyetlen egész számot kell kiírnia: az érvényes királynő-elhelyezések számát, ahol a királynők nem ütik egymást és nem helyezkednek el akadályozott mezőkön.

## Példa

### Bemenet
```
........
........
..*.....
........
........
.....*..
...*....
........
```

### Kimenet
```
65
```

Ebben a példában 65 különböző módja van a nyolc királynő elhelyezésének úgy, hogy azok ne üssék egymást, és ne álljanak akadályozott mezőkön.

## Megjegyzés

Az 8 királynő feladat hagyományos változatában, ahol nincs akadályozott mező, összesen 92 megoldás létezik. Azonban a feladat nehezítése miatt, hogy bizonyos mezők akadályozottak, a lehetséges megoldások száma változhat.

