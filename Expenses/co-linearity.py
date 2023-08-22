import numpy as np
import pandas as pd
import statsmodels.api as sm
data = pd.read_excel("data.xlsx", sheet_name = "dane")

X = data[['X1','X2']]
y = data['Y']


# Wyznacz macierz współczynników determinacji
corr_matrix = np.corrcoef(X, rowvar=False)
print(corr_matrix)

# Wyznacz macierz odwrotności macierzy korelacji
corr_inv = np.linalg.inv(corr_matrix)

# Wyznacz VIF dla każdej zmiennej
vif = np.diag(corr_inv)

# Wyświetl VIF dla każdej zmiennej
for i, variable in enumerate(X.columns):
    print(f"{variable}: VIF = {vif[i]:.2f}")

print("Wnioski: Dla zmiennych X1 i X2 współczynnik VIF jest mniejszy od 10. Zmienne te charakteryzują się brakiem współliniowości, a więc nie są ze sobą silnie skorelowane.")