
# Megoldás Magyarázata

## Feladat Áttekintése
Ez a program egy 8x8-as sakktábla királynő feladatának megoldására szolgál, ahol a cél az, hogy a táblán elhelyezett akadályok („*”-ok) mellett úgy helyezzük el a királynőket, hogy ne üssék egymást. Az algoritmus visszaszámlálja az összes lehetséges királynő-elhelyezést, amely megfelel ezeknek a követelményeknek.

## Megoldás Lépései

### Bemenet
1. A `board` lista 8 sorból áll, ahol minden sor egy 8 karakterből álló karakterlánc ('.' vagy '*'), amely megadja a tábla aktuális állapotát. A pont ('.') jelzi az üres mezőket, a '*' az akadályokat jelöli.

### Segédfüggvények

1. **is_safe(row, col, cols, diag1, diag2)**:
   - Ez a függvény ellenőrzi, hogy a `(row, col)` pozíció biztonságos-e, azaz egy királynőt el lehet-e helyezni ezen a mezőn úgy, hogy ne üssék egymást.
   - A `cols`, `diag1` és `diag2` listák a megfelelő oszlopokat és átlókat követik:
     - `cols[col]` igaz, ha az adott oszlopban már van királynő.
     - `diag1[row - col]` igaz, ha az adott főátlóban már van királynő.
     - `diag2[row + col]` igaz, ha az adott mellékátlóban már van királynő.

   ```python
   def is_safe(row, col, cols, diag1, diag2):
       return not (cols[col] or diag1[row - col] or diag2[row + col])
   ```

2. **solve(row, board, cols, diag1, diag2)**:
   - Ez a rekurzív függvény próbálja elhelyezni a királynőket minden sorban.
   - Ha a `row` eléri a 8-at, akkor megtaláltunk egy érvényes királynő-elhelyezést, ezért visszatérünk 1-gyel.
   - Az `is_safe` függvénnyel ellenőrzi, hogy az adott mező biztonságos-e:
     - Ha biztonságos, akkor elhelyez egy királynőt, frissíti az `cols`, `diag1`, és `diag2` listákat.
     - Rekurzívan meghívja a `solve` függvényt a következő sorra.
     - Végül visszaállítja a `cols`, `diag1`, és `diag2` állapotokat (visszalépés), hogy folytathassa a további lehetőségek keresését.
   
   ```python
   def solve(row, board, cols, diag1, diag2):
       if row == 8:
           return 1
       count = 0
       for col in range(8):
           if board[row][col] == '.' and is_safe(row, col, cols, diag1, diag2):
               cols[col] = diag1[row - col] = diag2[row + col] = True
               count += solve(row + 1, board, cols, diag1, diag2)
               cols[col] = diag1[row - col] = diag2[row + col] = False
       return count
   ```

### main

- A `main()` olvassa be a táblát, inicializálja a `cols`, `diag1`, és `diag2` listákat hamis értékekkel.
- Meghívja a `solve` függvényt az első sorral kezdve, és kiírja az összes lehetséges érvényes elhelyezés számát.

   ```python
   def main():
       board = [input().strip() for _ in range(8)]
       cols = [False] * 8
       diag1 = [False] * 15
       diag2 = [False] * 15
       print(solve(0, board, cols, diag1, diag2))
   ```

### Példa Működés
Ha a tábla üres (minden mező '.'), akkor a program megtalálja az összes lehetséges módot a királynők elhelyezésére úgy, hogy ne üssék egymást.

### Idő- és Tárbonyolultság
- **Időbonyolultság**: A rekurzív hívások száma exponenciális lehet a backtracking miatt, így a bonyolultság \(O(8!)\).
- **Tárbonyolultság**: \(O(8)\), mivel egyszerre csak egy sorban kell nyomon követni a királynők pozícióját.

Ez az algoritmus hatékonyan megoldja a problémát backtracking technikával, ami lehetővé teszi az összes lehetséges királynő-elhelyezés megtalálását.
