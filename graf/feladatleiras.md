
# Óriás Pizza

**Időkorlát:** 1.00 s  
**Memóriakorlát:** 512 MB

## Link
https://cses.fi/problemset/task/1684/


Uolevi családja egy nagy pizzát szeretne rendelni és együtt elfogyasztani. Összesen n családtag csatlakozik a rendeléshez, és m lehetséges feltét van. A pizzára bármennyi feltét kerülhet.

Minden családtag két kívánságot ad meg a pizzafeltétekkel kapcsolatban. A kívánságok a következő formátumúak: "feltét x jó/rossz". A feladatod, hogy kiválaszd azokat a feltéteket, hogy mindenki legalább egy kívánsága teljesüljön (egy jó feltét rajta van a pizzán, vagy egy rossz feltét nincs rajta).

## Bemenet

Az első sorban két egész szám található, n és m: a családtagok és a feltétek száma. A feltéteket az 1, 2, ..., m számok jelölik.

Ezt követően n sor következik, amelyek a kívánságokat írják le. Minden sorban két kívánság található a következő formátumban: "+ x" (a x feltét jó) vagy "- x" (a x feltét rossz).

## Kimenet

Írj ki egy sort, amely m szimbólumból áll: minden feltét esetén "+" ha az szerepel a pizzán, és "-" ha nem szerepel rajta. Bármilyen érvényes megoldást elfogadunk.

Ha nincs érvényes megoldás, akkor írj ki "IMPOSSIBLE".

## Megkötések

- 1 ≤ n, m ≤ 10^5
- 1 ≤ x ≤ m

## Példa

**Bemenet:**
```
3 5
+ 1 + 2
- 1 + 3
+ 4 - 2
```

**Kimenet:**
```
- + + - +
```
