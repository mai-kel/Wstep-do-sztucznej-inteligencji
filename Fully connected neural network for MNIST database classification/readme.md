# Opis programu
Program ma na celu skonstruować sieć neuronową, która będzie w stanie sklasyfikować zdjęcia odręcznie pisanych cyfr na podstawie zbioru danych MNIST. Program ponadto pokazuje dane dotyczące skuteczności sieci neuronowej.

## Moduł neural_network.py
Moduł zawiera klasy odpowiedzialne za tworzenie sieci neuronowej.

## Moduł loss_func.py
Moduł zawiera funkcję straty i jej pochodną wykorzystywane przez sieć neuronową w module main.py.

## Moduł activation_func.py
Moduł zawiera funkcję błędu średniokwadratowego i jej pochodną wykorzystywane przez sieć neuronową w module main.py.

## Moduł main.py
Moduł umożliwia zobaczenie danych na temat skuteczności sieci neuronowej.
Przy uruchamianiu modułu należy podać dwa parametry:
- `to_train`: ilość obrazów na podstawie których sieć neuronowa będzie się uczyć klasyfikacji
- `to_test` ilość obrazów na podstawie których sieć neuronowa będzie testowana pod względem skuteczności

Przykładowe wywołanie modułu dla 1000 obrazów służących do nauki i 100 obrazów służąych do testowania.
```
python main.py 1000 100
```
Uwaga, wywołanie modułu main dla parametrów 10000 i 1000 tak jak zostało to zrobione w celu pozyskania danych do sprawozdania powoduje, że program będzie się wykonywać przez dłuższy czas (około 5-10 minut).

## Instalacja wymaganych bibliotek
Aby zainstalować wymagane przez program biblioteki należy wykonać komendę poniżej
```
pip install -r requirements.txt
```