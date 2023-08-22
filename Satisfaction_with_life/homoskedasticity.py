from randomness_of_residuals import residuals
from statsmodels.stats.api import het_goldfeldquandt
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name = 'dane')
X = data[['X4', 'X5']]

test_result = het_goldfeldquandt(residuals, X)

# Wyświetl wynik testu Goldfelda-Quandta
print("Wynik testu Goldfelda-Quandta:")
print("Statystyka testowa:", test_result[0])
print("P-wartość:", test_result[1])

alpha = 0.05  # Poziom istotności

if test_result[1] > alpha:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej: Reszty są homoskedastyczne.")
else:
    print("Odrzucamy hipotezę zerową: Reszty nie są homoskedastyczne.")

