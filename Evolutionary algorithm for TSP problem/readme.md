# Opis programu
Program ma na celu rozwiązać problem komiwojażera. Współrzędne punktów do odwiedzenia należy podać w pliku tekstowym w konwencji
```
[[X1, Y1], [X2, Y2], ..., [Xn, Yn]]
```
gdzie Xn Yn to kolejne wsółrzędne punktu.
Ponadto program umożliwia wyświetlenie wykresu przykładowego rozwiązania oraz wyświetlenie przebiegu postępu algorytmu.

## Moduł solver.py
Moduł zawiera implementację algorytmu ewolucyjnego.

## Moduł plotter
Moduł po uruchomieniu wyświetla wykres z przykładowym rozwiązaniem oraz przebiegiem postępu algorytmu.
Moduł nie przyjmuje żadnych parametrów.
Przykładowe uruchomienie modułu:
```
python plotter.py
```

## Moduł main.py
Moduł umożliwia znalezienie rozwiązania dla i wyświetlenie go na wyjście dla wybranych parametrów algorytmu.
Moduł przyjmuje poniższe parametry:
- `rozmiar populacji`
- `ścieżka do pliku tekstowego z listą punktów`
- `szansa na mutację`
- `siła mutacji`
- `szansa na krzyżowanie`
- `ilość iteracji`

Przykładowe uruchomienie modułu:
```
python main.py 100 cities.txt 0.6 1 0.8 800
```

## Instalacja wymaganych bibliotek
Aby zainstalować wymagane przez program biblioteki należy wykonać komendę poniżej
```
pip install -r requirements.txt
```
