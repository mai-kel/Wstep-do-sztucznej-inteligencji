# Opis programu
Program ma na celu skonstruować maszynę wektorów nośnych, która będzie w stanie sklasyfikować zdjęcia odręcznie pisanych cyfr na podstawie zbioru danych MNIST. Porgram ponadto pokazuje dane dotyczące skuteczności maszyny wektorów nośnych.

## Moduł support_vector_machine.py
Moduł zawiera klasy odpowiedzialne za tworzenie maszyny wektorów nośnych.

## Moduł main.py
Moduł umożliwia zobaczenie danych na temat skuteczności SVM.
Przy uruchamianiu modułu należy podać dwa parametry:
- `to_train`: ilość obrazów na podstawie których SVM będzie się uczyć klasyfikacji
- `to_test` ilość obrazów na podstawie których SVM będzie testowany pod względem skuteczności

Przykładowe wywołanie modułu dla 1000 obrazów służących do nauki i 100 obrazów służąych do testowania.
```
python main.py 1000 100
```
Uwaga, wywołanie modułu main dla parametrów 10000 i 1000 tak jak zostało to zrobione w celu pozyskania danych do sprawozdania powoduje, że program będzie się wykonywać przez długi czas (około 10-15 minut)

## Instalacja wymaganych bibliotek
Aby zainstalować wymagane przez program biblioteki należy wykonać komendę poniżej
```
pip install -r requirements.txt
```