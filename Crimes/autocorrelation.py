from randomness_of_residuals import residuals
from statsmodels.stats.stattools import durbin_watson

d_value = durbin_watson(residuals)

# Wyświetl wynik testu Durbina-Watsona
print("Wynik testu Durbina-Watsona:")
print(f"Wartość statystyki Durbina-Watsona: {d_value}")

if d_value < 1.5:
    interpretation = "Wartość statystyki Durbina-Watsona poniżej 1.5 sugeruje obecność silnej autokorelacji dodatniej."
elif d_value > 2.5:
    interpretation = "Wartość statystyki Durbina-Watsona powyżej 2.5 sugeruje obecność silnej autokorelacji ujemnej."
elif 1.5 <= d_value <= 2.5:
    interpretation = "Wartość statystyki Durbina-Watsona w zakresie 1.5-2.5 wskazuje na brak istotnej autokorelacji."

print("Interpretacja:")
print(interpretation)