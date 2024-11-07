
# Megoldás Menete

Ez a megoldás a giant pizza problémát, mint 2-sat problémát old meg a Tarjan algoritmus alkalmazásával, amely erősen összefüggő komponensek (SCC) meghatározására szolgál irányított gráfban. A kód két fő funkcióra épül: `tarjan_scc` és `solve_2sat`.

## 1. Tarjan algoritmus (tarjan_scc függvény)

A `tarjan_scc` függvény célja az erősen összefüggő komponensek megtalálása a gráfban. Az SCC-k olyan részei a gráfnak, ahol minden csúcs elérhető a többi csúcstól, és vissza is. A `tarjan_scc` algoritmus egy mélységi bejárásos (DFS) módszert használ a következő lépésekkel:

1. **Indexek és Lowlinkek beállítása**: Minden csúcsot ellátunk egy egyedi indexszel, és egy úgynevezett "lowlink" értékkel, ami a csúcs minimális elérési pontját mutatja.
2. **Stack és SCC lista kezelése**: A gráf bejárása során a csúcsokat egy stack-ben tároljuk, hogy megőrizzük az éppen vizsgált SCC csúcsait.
3. **Erősen összefüggő komponensek összegyűjtése**: Amikor egy SCC-t találunk (azaz amikor egy csúcs lowlink értéke megegyezik az indexével), a csúcsokat kivesszük a stack-ből, és elmentjük őket egy listában.

A `tarjan_scc` kimenete a gráf összes SCC-je egy listában.

## 2. 2-sat probléma megoldása (solve_2sat függvény)

A `solve_2sat` függvény a 2-sat probléma megoldására készült, amely egy speciális Boole-függvény kielégíthetőségi probléma, ahol a feltételek (klauzulák) legfeljebb két literálból állnak.

1. **Implikációs gráf felépítése**: Minden változó két állapottal rendelkezhet (igaz vagy hamis), és az implikációs gráfot ennek megfelelően építjük fel. Például, ha `(A vagy B)` van a feltételek között, akkor `!A -> B` és `!B -> A` implikációkat adunk hozzá a gráfhoz.
2. **Erősen összefüggő komponensek keresése**: Az `tarjan_scc` segítségével megtaláljuk a gráf SCC-it.
3. **Változók hozzárendelése**: Ha egy változó és annak negáltja ugyanabban az SCC-ben található, a probléma nem oldható meg, és az eredmény `IMPOSSIBLE`. Ha külön SCC-kben vannak, hozzárendeljük az igaz vagy hamis értéket a változókhoz.

## 3. main

A `main` függvény a bemeneti adatokat olvassa be, majd a `solve_2sat` függvénnyel oldja meg a problémát. A bemenet a következő formátumú:

- Első szám: klauzulák száma (`m`)
- Második szám: változók száma (`n`)
- Ezután minden sorban két feltétel található, pl. `+ 1 - 2`, ahol `+` vagy `-` jelöli az állítást vagy a tagadást.

A `solve_2sat` eredményétől függően a program vagy kiírja, hogy `IMPOSSIBLE`, ha nincs megoldás, vagy a változók igaz/hamis hozzárendelését.

## Megjegyzések

- **Rekurziós limit növelése**: A program elején a rekurziós limitet 500000-re állítjuk (`sys.setrecursionlimit(500000)`), hogy támogassuk a mélyebb rekurziókat a nagy gráfokon.
- **Kód hatékonyság**: A Tarjan algoritmus időkomplexitása lineáris a csúcsok és élek számának függvényében, ami lehetővé teszi nagyobb gráfok kezelését is.

Ez a megoldás hatékony módot kínál a 2-sat probléma megoldására nagy bemeneti adatok mellett is.
