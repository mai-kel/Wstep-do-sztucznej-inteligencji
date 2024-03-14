# Opis programu
Program ma na celu wyznaczenie polityki decyzyjnej dla problemu FrozenLake8x8 z poślizgiem posługując się algorytmem Q-learning. Program ponadto pokazuje dane na temat skuteczności polityki oraz procesu uczenia.

## Moduł frozen_lake.py
Moduł zawiera klasę, która wyznacza politykę decyzyjną dla problemu FrozenLake8x8 korzystając z algorytmu Q-learning.

## Moduł main.py
Moduł umożliwia zobaczenie danych na temat skuteczności wyznaczonych polityk decyzyjnej oraz wykres przebiegu treningu.
Przy uruchamianiu modułu należy podać sześć parametrów:
- `alpha`: parametr szybkości uczenia, jego zakres to <0, 1>
- `gamma`: parametr odpowiedzialny za to, jak dużą wagę algorytm ma przywiązywać do nagród w przyszłości w stosunku do nagród natychmiastowych (im parametr większy tym większa waga dla nagród w przyszłości), jego zakres to <0, 1>
- `epsilon`: parametr określa początkową losowość podejmowanych akcji przez agenta w procesie uczenia, jego zakres to <0, 1>
- `epsilon_decay`: parametr określa jak szybko ma zmniejszać się parametr epsilon, jego zakres to <0, 1>
- `episodes`: parametr określa na jakiej liczbie epizodów algorytm będzie się uczyć
- `games_to_test`: parametr określa na jakiej liczbie gier będzie mierzony winrate

Przykładowe wywołanie modułu dla α=0.9, γ=0.9, ε=1, epsilon_decay=0.01, episodes=2000, games_to_test=200
```
python main.py 0.9 0.9 1 0.01 2000 200
```

## Instalacja wymaganych bibliotek
Aby zainstalować wymagane przez program biblioteki należy wykonać komendę poniżej
```
pip install -r requirements.txt
```