from selection  import final_model

print("Wybrane zmienne objaśniające:")
print(final_model.model.exog_names[1:])
print("Zmienne X2, X3, X5, X6, X8, X9 nie jest statystycznie istotna. Ten model będą tworzyć zmienne X1, X4 oraz X7")
print()
print("Model regresji krokowej w przód:")
print(final_model.summary())

beta_01 = final_model.params['X1']
beta_02 = final_model.params['X4']
beta_03 = final_model.params['X7']
const = final_model.params['const']

conf_int_const = final_model.conf_int().loc['const']
conf_int_X1 = final_model.conf_int().loc['X1']
conf_int_X4 = final_model.conf_int().loc['X4']
conf_int_X7 = final_model.conf_int().loc['X7']
residuals = final_model.resid
std_residuals = residuals.std()
std_errors = final_model.bse
r_squared = final_model.rsquared

print()
print()
print(f"Model: {round(const, 2)} + {round(beta_01, 2)}X1 + {round(beta_02, 2)}X4 + {round(beta_03, 2)}X7")


print(f"Interpretacja parametru b1: Jeśli gęstość zaludniena (X1) wzrośnie o 1000 osób na km2 to ilość odnotowanych przestępstw na 1000 mieszkańców (Y) wzrasta średnio o {round(beta_01, 2)} 6.12 przypadków",
      "przy założeniu ceteris paribus.")
print(f"Interpretacja parametru b2: Wzrost poziomu ubóstwa (X4) o 1% powoduje wzrost odnotowanych przestępstw na 1000 mieszkańców (Y) średnio o {round(beta_02, 2)} przypadków,",
       "przy założeniu ceteris paribus.")
print(f"Interpretacja parametru b3: Wzrost wskaźnika osób posiadających co najmniej 60 lat (X7) o 1% powoduje spadek odnotowanych przestępstw na 1000 mieszkańców (Y) średnio o {round(beta_03, 2)} przypadków,",
       "przy założeniu ceteris paribus.")
print(f"Interpretacja odchylenia standardowego reszt (Se): Wartości empiryczne ilości odnotowanych przestępstw odchylają się przęciętne od {round(std_residuals, 2)}",
       "od wartości teoretycznych wyznaczonych na podstawie modelu.")
print(f"Interpretacja R^2: {r_squared * 100}% całkowitej zmienności liczby odnotowanych przestępstw zostało wyjaśnionych modelem.")
print(f"Interpretacja współczynnika korelacji wielorakiej R: Empiryczne i teoretyczne wartości liczby odnotowanych przestępstw są skorelowane na poziomie {(round(r_squared ** (1/2) * 100, 3))}%")
print("Parametry beta1 i beta2 są statystycznie istotne (P>|t| jest mniejszy niż 0.05 dla X1, X4, X7 )")
print()
print("Błędy ocen parametrów:")
print(f"- Ocena b0 różni się od parametru beta0 średnio o {round(std_errors['const'], 2)}")
print(f"- Ocena b1 różni się od parametru beta1 średnio o {round(std_errors['X1'], 2)}")
print(f"- Ocena b2 różni się od parametru beta2 średnio o {round(std_errors['X4'], 2)}")
print(f"- Ocena b3 różni się od parametru beta3 średnio o {round(std_errors['X7'], 2)}")
print()
print("Interpretacje przedziałów ufności:")
print(f"- można sądzić na 95% że przedział od {round(conf_int_const[0], 2)} do {round(conf_int_const[1], 2)} obejmuje nieznaną wartość parametru beta0 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X1[0], 2)} do {round(conf_int_X1[1], 2)} obejmuje nieznaną wartość parametru beta1 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X4[0], 2)} do {round(conf_int_X4[1], 2)} obejmuje nieznaną wartość parametru beta2 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X7[0], 2)} do {round(conf_int_X7[1], 2)} obejmuje nieznaną wartość parametru beta2 ")