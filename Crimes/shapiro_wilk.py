from scipy.stats import shapiro
from randomness_of_residuals import residuals

#print(residuals)

statistic, p_value = shapiro(residuals)
alfa = 0.05

print("Wynik testu Shapiro-Wilka:")
print(f"Statystyka testowa: {statistic}")
print(f"P-wartość: {p_value}")

if p_value > alfa:
    print("Nie ma podstaw do odrzucenia hipotezy zerowej: Dane pochodzą z rozkładu normalnego.")
else:
    print("Odrzucamy hipotezę zerową: Dane nie pochodzą z rozkładu normalnego.")