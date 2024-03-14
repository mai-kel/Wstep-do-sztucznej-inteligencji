# Opis programu
Program ma na celu umożliwić obserwację rozgrywki komputera korzystającego z algorytmu minimax z komputerem, który wykonuje ruchy losowe.
Ponadto umożliwia zobaczenie statystyki na temat ilości wygranych gier komputera korzystającego z algorytmu minimax w zależności od tego,
czy rozpoczynał rozgrywkę.

## Moduł get_statistics.py
Moduł umożliwia wyświetlenie statystki na temat ilości wygranych gier przez komputer korzystający z algorytmu minimax. Przy uruchamianiu moudułu należy podać jeden parametr:
- `n`: ilość analizowanych gier

Przykładowe wywołanie modułu dla 100 analizowanych gier.
```
python get_statistics.py 100
```

## Moduł show_game.py
Moduł umożliwia zobaczenie przykładowej rozgrywki komputera korzystającego z algorytmu minimax z komputerem, który wykonuje ruchy losowe.
Przy uruchamianiu modułu należy podać dwa parametry:
- `who_begins`: "znak" komputera który zaczyna rozgrywkę, może przyjmować X lub O
- `who_minimax` "znak" komputera który będzie grać z użyciem algorytmu minimax, może przyjmować X lub O

Przykładowe wywołanie modułu dla komputera zaczynającego ze znakiem X oraz dla komputera używającego algorytmu minimax ze znakiem O
```
python show_game.py X O
```

## Instalacja wymaganych bibliotek
Aby zainstalować wymagane przez program biblioteki należy komendy poniżej
```
pip install -r requirements.txt
```

