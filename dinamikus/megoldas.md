
# Kingdom Division függvény részletes magyarázata

A `kingdomDivision` függvény célja, hogy kiszámolja, hányféleképpen lehet egy királyságot két régióra osztani egy fa struktúrában úgy, hogy teljesüljenek a feladatban megadott feltételek. Az alábbiakban részletesen bemutatjuk a függvény működését, beleértve az alkalmazott dinamikus programozási technikákat és a memoizálást.

## Függvény bemenetei és alapbeállításai

- **Bemenetek:**
  - `n`: A városok száma.
  - `roads`: Egy lista, amely az egyes városok közötti kapcsolatokat (utakat) tartalmazza.

- **Különleges értékek és beállítások:**
  - `MOD = 10 ** 9 + 7`: A válaszokat modulo `10^9 + 7` formában adjuk meg a túlcsordulás elkerülése érdekében.
  - `sys.setrecursionlimit(200000)`: A rekurzív hívások korlátját 200000-re állítjuk be, mivel mélyebb rekurziók is előfordulhatnak a nagy fa struktúráknál.

## Gráf felépítése

A `defaultdict` típusú `graph` szótárban tároljuk a gráfot (városok és utak kapcsolatait). Minden város egy listát kap, amely az adott városhoz csatlakozó többi várost tartalmazza:

```python
graph = defaultdict(list)
for u, v in roads:
    graph[u].append(v)
    graph[v].append(u)
```

## Dinamikus programozás és memoizálás

Két memoizált függvényt hozunk létre (`f` és `g`), amelyekben a részszámításokat tároljuk:
- `memo_f`: Az `f(node, parent)` értékek tárolására szolgál.
- `memo_g`: A `g(node, parent)` értékek tárolására szolgál.

## Függvények részletei

### `f(node, parent)` függvény

Ez a függvény azt számolja ki, hányféleképpen lehet a `node` várost régióhoz rendelni, ha a `parent` városhoz van kapcsolva. Lépései:

1. Ellenőrzi, hogy az eredmény már ki lett-e számítva a `memo_f` tárolóban. Ha igen, visszatér ezzel az értékkel.
2. Kezdetben `res = 1`.
3. Végigmegy a `node` gyermek városain, kivéve a `parent`-et.
   - A `res` értékét megszorozza a `child` városra vonatkozó számított értékekkel: `(2 * f(child, node) + g(child, node))`.
   - Ez azt jelenti, hogy a `child` város vagy különböző régióban van, vagy ugyanabban, mint `node`.
4. Levonja a `g(node, parent)` értéket, hogy biztosítsa a szabályok betartását, majd elmenti az eredményt a `memo_f` tárolóba és visszatér ezzel az értékkel.

### `g(node, parent)` függvény

Ez a függvény azt számolja ki, hogy hányféleképpen lehet a `node` várost és annak gyermekeit egy régióba sorolni.

1. Ha a számítás már szerepel a `memo_g` tárolóban, akkor az értékkel tér vissza.
2. Kezdetben `res = 1`.
3. Bejárja a `node` gyermek csúcsait, és minden gyermekre meghívja az `f(child, node)` függvényt, majd az eredményt megszorozza `res`-szel.
4. A végeredményt elmenti a `memo_g` tárolóba és visszatér ezzel az értékkel.

## A végső eredmény kiszámítása

A fő visszatérési érték a `2 * f(1, 0) % MOD`. Itt az `f(1, 0)` azt jelenti, hogy az 1-es várost, mint gyökeret vesszük, amelynek nincs szülője (`0`). Mivel két régióra kell felosztani a városokat, ezt a megoldást megszorozzuk kettővel.

## Összegzés

Ez a megoldás hatékony a dinamikus programozásnak köszönhetően, ami elkerüli a redundáns számításokat és gyorsabbá teszi a nagy fák bejárását. Az `f` és `g` függvények az összes lehetséges régiókba osztási kombinációt számolják ki, figyelembe véve a szomszédos városok elhelyezési szabályait.
