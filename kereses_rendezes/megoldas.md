# Megoldás Magyarázata

## Feladat Áttekintése
A feladat célja meghatározni a legkisebb pozitív egész számot, amely nem állítható elő egy adott pénzérme lista részhalmazainak összegéből. Minden pénzérme pozitív egész értékkel rendelkezik, és ennek a "legkisebb elérhetetlen összegnek" a megtalálása a cél.

## Megoldás Lépései

### Bemenet
1. Az `n` egész szám jelzi a pénzérmék számát.
2. A `coins` lista tartalmazza ezeknek a pénzérméknek az értékeit.

### Lépések

1. **Pénzérmék Rendezése**:  
   A kód először rendezi a pénzérmék listáját növekvő sorrendbe. A rendezés segít abban, hogy a legkisebb értékekkel kezdjük a feldolgozást, biztosítva, hogy mindig a lehető legkisebb összegeket próbáljuk meg előállítani a rendelkezésre álló pénzérmékkel.

   ```python
   coins.sort()
   ```

2. **Legkisebb Összeg Kezdeti Értéke**:  
   Inicializáljuk a `smallest_sum` változót 1-re. Ez a változó azt az elérhetetlen legkisebb pozitív egész számot jelöli, amelyet nem lehet előállítani az eddig feldolgozott pénzérmék részhalmazával.

   ```python
   smallest_sum = 1
   ```

3. **Iterálás a Pénzérmék Felett**:  
   A kód ezután végigmegy az egyes érméken a rendezett listában.
   - Minden érme esetén ellenőrzi, hogy az érme értéke nagyobb-e, mint a `smallest_sum`. 
     - Ha `coin > smallest_sum`, az azt jelenti, hogy nem tudjuk előállítani a `smallest_sum` értéket az eddig látott érmékkel, így kilépünk a ciklusból.
     - Ellenkező esetben hozzáadjuk a jelenlegi `coin` értékét a `smallest_sum`-hoz, ezzel frissítve azt a következő elérhetetlen összegre.

   ```python
   for coin in coins:
       if coin > smallest_sum:
           break
       smallest_sum += coin
   ```

4. **Eredmény Kiírása**:  
   A ciklus után a `smallest_sum` tartalmazza a legkisebb pozitív egész számot, amely nem állítható elő a megadott érmékkel, amit végül kiírunk eredményként.

   ```python
   print(smallest_sum)
   ```

### Példa

Adott érmék esetén `[1, 1, 3, 4]`:
1. Rendezett érmék: `[1, 1, 3, 4]`
2. Inicializálás: `smallest_sum = 1`
3. Érmék feldolgozása:
   - Első `1`: `smallest_sum = 1 + 1 = 2`
   - Második `1`: `smallest_sum = 2 + 1 = 3`
   - `3`: `smallest_sum = 3 + 3 = 6`
   - `4`: Mivel `4 > 6`, kilépünk a ciklusból.
4. A kimenet `smallest_sum = 6`, mivel 6 a legkisebb elérhetetlen összeg.

### Bonyolultság
- **Időbonyolultság**: \(O(n \log n)\), főként a lista rendezése miatt.
- **Tárbonyolultság**: \(O(1)\), mivel csak néhány extra változót használunk.

## Összegzés
Ez az algoritmus hatékonyan megtalálja a legkisebb pozitív egész számot, amely nem állítható elő a megadott pénzérmék összegével, kihasználva a rendezést és egy egyszerű lineáris bejárást a rendezett érmék listáján.
