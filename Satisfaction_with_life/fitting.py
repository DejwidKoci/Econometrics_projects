from selection  import final_model

print("Wybrane zmienne objaśniające:")
print(final_model.model.exog_names[1:])
print("Zmienne X1, X2, X3, X6 nie jest statystycznie istotna. Ten model będą tworzyć zmienne X4 oraz X5")
print()
print("Model regresji krokowej w przód:")
print(final_model.summary())

beta_01 = final_model.params['X4']
beta_02 = final_model.params['X5']
const = final_model.params['const']

conf_int_const = final_model.conf_int().loc['const']
conf_int_X1 = final_model.conf_int().loc['X4']
conf_int_X2 = final_model.conf_int().loc['X5']
residuals = final_model.resid
std_residuals = residuals.std()
std_errors = final_model.bse
r_squared = final_model.rsquared

print()
print()
print(f"Model: {round(const, 2)} + {round(beta_01, 2)}X4 {round(beta_02, 5)}X5")


print(f"Interpretacja parametru b1: Jeśli poziom przestępczości (X4) wzrośnie o 1 % to poziom zadowolenia z życia (Y) wzrasta średnio o {round(beta_01 * 1000, 2)} jednostkę",
      "przy założeniu ceteris paribus.")
print(f"Interpretacja parametru b2: Wzrost mediany dochodów o 1 euro  (X5) to poziom zadowolenia z życia (Y) wzrasta średnio o {round(beta_02, 2) * -1} jednostkę,",
       "przy założeniu ceteris paribus.")
print(f"Interpretacja odchylenia standardowego reszt (Se): Wartości empiryczne poziomu zadowolenia z życia odchylają się przęciętne od {round(std_residuals, 2)}",
       "od wartości teoretycznych wyznaczonych na podstawie modelu.")
print(f"Interpretacja R^2: {r_squared * 100}% całkowitej zmienności poziomu z życia zostało wyjaśnionych modelem.")
print(f"Interpretacja współczynnika korelacji wielorakiej R: Empiryczne i teoretyczne wartości poziomu zadowolenia z życia są skorelowane na poziomie {(round(r_squared ** (1/2) * 100, 3))}%")
print("Parametry beta1 i beta2 są statystycznie istotne (P>|t| jest mniejszy niż 0.05 dla X1 i X2)")
print()
print("Błędy ocen parametrów:")
print(f"- Ocena b0 różni się od parametru beta0 średnio o {round(std_errors['const'], 2)}")
print(f"- Ocena b1 różni się od parametru beta1 średnio o {round(std_errors['X4'], 2)}")
print(f"- Ocena b2 różni się od parametru beta2 średnio o {round(std_errors['X5'], 2)}")
print()
print("Interpretacje przedziałów ufności:")
print(f"- można sądzić na 95% że przedział od {round(conf_int_const[0], 2)} do {round(conf_int_const[1], 2)} obejmuje nieznaną wartość parametru beta0 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X1[0], 2)} do {round(conf_int_X1[1], 2)} obejmuje nieznaną wartość parametru beta1 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X2[0], 2)} do {round(conf_int_X2[1], 2)} obejmuje nieznaną wartość parametru beta2 ")