import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel("data.xlsx", sheet_name = 'dane')
y = data['Y']
X = data[['X1','X2']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

residuals = y - y_predicted


to_sort = pd.DataFrame({"X1": X['X1'], "Reszty": residuals})
sorted_data = to_sort.sort_values(by="X1")
sorted_data = sorted_data.reset_index(drop = True)

# Oblicz liczbę serii
def count_runs(data):
    runs_count = 1
    for i in range(1, len(data)):
        if data[i] * data[i - 1] < 0:
            runs_count += 1
    return runs_count

observed_runs = count_runs(sorted_data['Reszty'])
n1 = len(sorted_data[sorted_data['Reszty'] > 0])
n2 = len(sorted_data[sorted_data['Reszty'] < 0])
print("Liczba serii: ", observed_runs)
print("Liczba '+': ", n1)
print("Liczba '-': ", n2)

# Wartości S1* i S2* odczytane z tablic na podstawie n1 oraz n2
n = len(sorted_data)
s1_star = 4
s2_star = 13

print("S1*: ",s1_star)
print("S2*: ",s2_star)

# Sprawdź warunek
alpha = 0.05
if s1_star < observed_runs < s2_star:
    print("Nie mamy podstaw do odrzucenia hipotezy zerowej: Reszty mają rozkład losowy.")
else:
    print("Odrzucamy hipotezę zerową: Reszty nie mają rozkładu losowego.")