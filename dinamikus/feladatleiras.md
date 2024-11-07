
# Kingdom Division - Feladatleírás

## Link
https://www.hackerrank.com/challenges/kingdom-division/problem?isFullScreen=true


Egy királyságban vagyunk, ahol a király eldöntötte, hogy felosztja a területét két különálló régióra. A királyság egy faként van modellezve, amelynek csúcsai a városokat jelölik, és az élei a városokat összekötő utakat.

A cél az, hogy minden várost pontosan egy régióhoz rendeljünk hozzá, úgy, hogy a következő feltételek teljesüljenek:
1. Minden szomszédos város különböző régióba kerüljön, vagy mindkettő ugyanabba.
2. Legalább két módon kell felosztani a városokat, amelyek megfelelnek az első feltételnek.

Írj egy programot, amely kiszámolja, hányféleképpen lehet felosztani a városokat az adott szabályok szerint. Mivel az eredmény nagy lehet, add meg a választ a 10^9 + 7 (1000000007) modulo szerint.

## Bemenet

Az első sor tartalmaz egy egész számot, `n`-t, amely a városok számát jelöli (1 ≤ n ≤ 10^5).

A következő `n-1` sor mindegyike két egész számot tartalmaz, `u` és `v` (1 ≤ u, v ≤ n), amelyek azt jelentik, hogy van egy út `u` és `v` városok között.

## Kimenet

Egyetlen egész számot adj vissza, amely a városok felosztásának lehetséges módjainak számát jelöli, a 10^9 + 7 modulo szerint.

## Példa

### Bemenet
```
3
1 2
1 3
```

### Kimenet
```
2
```

### Magyarázat

Az alábbiak szerint lehet a városokat két régióra osztani:

1. Az 1-es város az egyik régióhoz tartozik, a 2-es és 3-as város pedig a másikhoz.
2. Az 1-es város a másik régióhoz tartozik, míg a 2-es és 3-as város az elsőhöz.

Ezek a megoldások megfelelnek a szabályoknak.

## Megjegyzés

- A feladat célja, hogy a fán alapuló felosztások minden lehetséges érvényes kombinációját kiszámoljuk, amely kielégíti a megadott feltételeket.
- Mivel `n` nagy lehet, az algoritmus hatékonyságára kell figyelni.
