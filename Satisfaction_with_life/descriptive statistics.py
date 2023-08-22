import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx", sheet_name = "dane")
print(data)
print()
y = data['Y']
X = data[['X1','X2','X3','X4','X5','X6']]

basic_stats = data.describe()
print(basic_stats)
#print(f"Vs: {data[['Y','X1','X2','X3']].std()/data[['Y','X1','X2','X3']].mean()}", end = " ")

numeric_columns = data.select_dtypes(include=['number'])
mean_values = numeric_columns.mean()
std_deviation = numeric_columns.std()
coefficient_of_variation = (std_deviation / mean_values) * 100

print()
print("Współczynnik zmienności [%]:")
print(coefficient_of_variation)

v_critical = 10
for column, cv in coefficient_of_variation.items():
    if cv < v_critical:
        print(f"Zmienna {column} jest zmienną quasi stałą (współczynnik zmienności: {cv:.2f}%)")

#Macierz korelacji
print()
correlation_matrix = numeric_columns.corr()
print("Macierz korelacji: ")
print(correlation_matrix)

## Analiza wniosków
conclusions = []
for col1 in correlation_matrix.columns:
    for col2 in correlation_matrix.columns:
        if col1 != col2:
            corr_value = correlation_matrix.loc[col1, col2]
            conclusion = f"Korelacja między {col1} a {col2}: {corr_value:.2f}"
            if abs(corr_value) > 0.7:
                conclusion += " - Silna korelacja"
            elif abs(corr_value) > 0.3:
                conclusion += " - Średnia korelacja"
            else:
                conclusion += " - Słaba korelacja"
            conclusions.append(conclusion)

print("\nWnioski:")
for conclusion in conclusions:
    print(conclusion)



plt.figure(figsize = (10,6))
plt.scatter(X['X1'], y)
plt.xlabel('X1')
plt.ylabel('Y')
plt.title('Wykres Y od X1')
plt.text(0.5, 0.9, "Wniosek: Słaba korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()

plt.figure(figsize = (10,6))
plt.scatter(X['X2'], y)
plt.xlabel('X2')
plt.ylabel('Y')
plt.title('Wykres Y od X2')
plt.text(0.5, 0.9, "Wniosek: Słaba korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()

plt.figure(figsize = (10,6))
plt.scatter(X['X3'], y)
plt.xlabel('X3')
plt.ylabel('Y')
plt.title('Wykres Y od X3')
plt.text(0.5, 0.9, "Wniosek: Umarkowana korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()
plt.figure(figsize = (10,6))
plt.scatter(X['X4'], y)
plt.xlabel('X4')
plt.ylabel('Y')
plt.title('Wykres Y od X4')
plt.text(0.5, 0.9, "Wniosek: Umarkowana korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()

plt.figure(figsize = (10,6))
plt.scatter(X['X5'], y)
plt.xlabel('X5')
plt.ylabel('Y')
plt.title('Wykres Y od X5')
plt.text(0.5, 0.9, "Wniosek: Dobra korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()

plt.figure(figsize = (10,6))
plt.scatter(X['X6'], y)
plt.xlabel('X6')
plt.ylabel('Y')
plt.title('Wykres Y od X6')
plt.text(0.5, 0.9, "Wniosek: Słabe korelacja między zmiennymi",
         horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
plt.show()