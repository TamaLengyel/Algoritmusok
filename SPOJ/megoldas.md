
# Megoldás - Trip
(kollokvium)

## Kódfelépítés és magyarázat

A kód célja, hogy két karakterlánc (Alice és Bob városlistája) közös részszekvenciáit megtalálja, figyelembe véve az eredeti sorrend megtartását. A megoldás dinamikus programozáson és rekurzív keresésen alapul.

### Importálás

```python
from functools import lru_cache
```

Az `lru_cache` egy Python dekorátor, amely cache-elést biztosít a rekurzív függvények számára. Ez segít abban, hogy a `collect_all_lcs` függvény gyorsabb legyen, mivel ugyanazokat a számításokat nem kell többször elvégezni.

### 1. Lépés: Dinamikus programozási tábla létrehozása

```python
def longest_common_subsequence_length(alice, bob):
    n, m = len(alice), len(bob)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
```

Létrehozunk egy `dp` mátrixot, amely `(n+1) x (m+1)` méretű, ahol `n` és `m` az `alice` és `bob` karakterláncok hossza. A mátrix minden eleme kezdetben 0, és ez lesz a dinamikus programozási táblánk, amely tárolja a leghosszabb közös részszekvencia (LCS) hosszát.

#### DP tábla feltöltése

```python
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if alice[i - 1] == bob[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

Egy kétirányú ciklusban feltöltjük a `dp` táblát:
- Ha az `alice[i-1]` és `bob[j-1]` karakterek egyeznek, akkor `dp[i][j]` értékét az `dp[i-1][j-1] + 1` értékkel növeljük.
- Ha nem egyeznek, akkor a `dp[i][j]` a `dp[i-1][j]` és `dp[i][j-1]` értékek maximuma lesz.

Végül a `dp[len(alice)][len(bob)]` tartalmazza a leghosszabb közös részszekvencia hosszát.

### 2. Lépés: Az összes leghosszabb közös részszekvencia gyűjtése

```python
@lru_cache(None)
def collect_all_lcs(dp, alice, bob, i, j, lcs_length, current_path):
```

Ez a függvény rekurzívan keresi az összes leghosszabb közös részszekvenciát. Az `@lru_cache` dekorátor használata lehetővé teszi, hogy az ismétlődő számításokat elkerüljük.

#### Alapesetek

```python
    if lcs_length == 0:
        return {current_path}
    if i == 0 or j == 0:
        return set()
```

Ha az `lcs_length` 0, az azt jelenti, hogy elértük a leghosszabb közös részszekvencia végét, ezért visszaadjuk a `current_path` útvonalat egy halmazban. Ha `i` vagy `j` 0, akkor elérjük a táblázat szélét, és egy üres halmazt adunk vissza.

#### Rekurzív keresés

```python
    result = set()
    if alice[i - 1] == bob[j - 1]:
        result.update(collect_all_lcs(dp, alice, bob, i - 1, j - 1, lcs_length - 1, alice[i - 1] + current_path))
    else:
        if dp[i - 1][j] == dp[i][j]:
            result.update(collect_all_lcs(dp, alice, bob, i - 1, j, lcs_length, current_path))
        if dp[i][j - 1] == dp[i][j]:
            result.update(collect_all_lcs(dp, alice, bob, i, j - 1, lcs_length, current_path))
```

- Ha az `alice[i-1]` és `bob[j-1]` karakterek megegyeznek, akkor az `i-1`, `j-1` pozícióra megyünk vissza, és a karaktert hozzáadjuk a `current_path`-hoz.
- Ha nem egyeznek, akkor azon ágon haladunk, amely megtartja az aktuális LCS hosszát.

### 3. Lépés: Eredmények gyűjtése és rendezése

```python
def trip_dynamic_programming(test_cases):
    results = []
    for alice, bob in test_cases:
        dp = longest_common_subsequence_length(alice, bob)
        lcs_length = dp[len(alice)][len(bob)]

        dp_tuple = tuple(tuple(row) for row in dp)
        all_lcs = collect_all_lcs(dp_tuple, alice, bob, len(alice), len(bob), lcs_length, "")

        sorted_lcs = sorted(all_lcs)[:1000]
        results.append(sorted_lcs)

    return results
```

A `trip_dynamic_programming` függvény:
1. Létrehozza a DP táblát.
2. Megkeresi az összes leghosszabb közös részszekvenciát.
3. Lexikografikus sorrendbe rendezi a találatokat, és korlátozza az eredményeket 1000 különböző elemre.

### Bemenet és kimenet kezelése

A végén a kód kezeli a bemenetet és kimenetet:

```python
# Input 
t = int(input())
test_cases = [(input().strip(), input().strip()) for _ in range(t)]
results = trip_dynamic_programming(test_cases)

# Output 
for i, result in enumerate(results):
    for trip in result:
        print(trip)
    if i < len(results) - 1:
        print()
```

- A bemeneti adatokat beolvassuk, és minden tesztesethez meghívjuk a `trip_dynamic_programming` függvényt.
- Az eredményeket kinyomtatjuk, minden teszteset között egy üres sort hagyva.

---

Ez a megoldás hatékonyan megtalálja és rendezi az összes lehetséges közös útvonalat két városlista között, figyelembe véve a problémában leírt feltételeket.
