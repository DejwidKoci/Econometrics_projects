import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel("data.xlsx", sheet_name = 'dane')
y = data['Y']
X = data[['X1','X4','X7']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

residuals = y - y_predicted


to_sort = pd.DataFrame({"X1": X['X1'], "Reszty": residuals})
sorted_data = to_sort.sort_values(by = 'X1')
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

expect_value = (2 * n1 * n2)/(n1 + n2) + 1
standard_deviation = (2 * n1 * n2 * (2 * n1 * n2 - n1 - n2) / ((n1 + n2)**2 * (n1 + n2 - 1)))**(1/2)
z = (observed_runs - expect_value) / standard_deviation

alpha = 0.05
if z < 1.96:
    print("Nie mamy podstaw do odrzucenia hipotezy zerowej: Reszty mają rozkład losowy.")
else:
    print("Odrzucamy hipotezę zerową: Reszty nie mają rozkładu losowego.")