from selection  import final_model

print("Wybrane zmienne objaśniające:")
print(final_model.model.exog_names[1:])
print("Zmienna X3 nie jest statystycznie istotna. Ten model będą tworzyć zmienne X1 oraz X2")
print()
print("Model regresji krokowej w przód:")
print(final_model.summary())

beta_01 = final_model.params['X1']
beta_02 = final_model.params['X2']
const = final_model.params['const']

conf_int_const = final_model.conf_int().loc['const']
conf_int_X1 = final_model.conf_int().loc['X1']
conf_int_X2 = final_model.conf_int().loc['X2']
residuals = final_model.resid
std_residuals = residuals.std()
std_errors = final_model.bse
r_squared = final_model.rsquared

print()
print()
print(f"Model: {round(const,2)} + {round(beta_01,2)}X1 {round(beta_02,2)}X2")


print(f"Interpretacja parametru b1: Jeśli przeciętny miesięczny dochód rozporządzalny na 1 osobę (X1) wzrośnie o 1000 zł to przeciętne miesięczne wydatki na 1 osobę (Y) wzrastają średnio o {round(beta_01 * 1000, 2)} zł",
      "przy założeniu że procent osób będących poniżej ustawowej granicy ubóstwa się nie zmienia (ceteris paribus).")
print(f"Interpretacja parametru b2: Wzrost osób będących poniżej ustawowej granicy ubóstwa o 1%  (X2) powoduje,że przeciętne miesięczne wydatki na 1 osobę (Y) spada średnio o {round(beta_02, 2) * -1}%,",
       "przy założeniu że przeciętny miesięczny dochód rozporządzalny na 1 osobę pozostaje bez zmian.")
print(f"Interpretacja odchylenia standardowego reszt (Se): Wartości empiryczne przeciętnych miesięcznych wydatków na 1 osobę odchylają się przęciętne od {round(std_residuals, 2)} zł",
       "od wartości teoretycznych wyznaczonych na podstawie modelu.")
print(f"Interpretacja R^2: {r_squared * 100}% całkowitej zmienności przeciętnych miesięcznych wydatków na 1 osobę zostało wyjaśnionych modelem.")
print(f"Interpretacja współczynnika korelacji wielorakiej R: Empiryczne i teoretyczne wartości przeciętnych miesięcznych wydatków na 1 osobę są skorelowane na poziomie {(round(r_squared ** (1/2) * 100, 3))}%")
print("Parametry beta1 i beta2 są statystycznie istotne (P>|t| jest mniejszy niż 0.05 dla X1 i X2)")
print()
print("Błędy ocen parametrów:")
print(f"- Ocena b0 różni się od parametru beta0 średnio o {round(std_errors['const'], 2)}")
print(f"- Ocena b1 różni się od parametru beta1 średnio o {round(std_errors['X1'], 2)}")
print(f"- Ocena b2 różni się od parametru beta2 średnio o {round(std_errors['X2'], 2)}")
print()
print("Interpretacje przedziałów ufności:")
print(f"- można sądzić na 95% że przedział od {round(conf_int_const[0], 2)} do {round(conf_int_const[1], 2)} obejmuje nieznaną wartość parametru beta0 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X1[0], 2)} do {round(conf_int_X1[1], 2)} obejmuje nieznaną wartość parametru beta1 ")
print(f"- można sądzić na 95% że przedział od {round(conf_int_X2[0], 2)} do {round(conf_int_X2[1], 2)} obejmuje nieznaną wartość parametru beta2 ")