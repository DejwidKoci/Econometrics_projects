import pandas as pd
import statsmodels.api as sm

data = pd.read_excel("data.xlsx", sheet_name = "dane")

print()
y = data['Y']
X = data[['X1','X3','X4','X5','X7','X8','X9']]


def forward_stepwise_regression(X, y, threshold = 0.05):
    included = []
    remaining_features = X.columns.tolist()
    
    while remaining_features:
        best_pvalue = 1
        best_feature = None
        
        for feature in remaining_features:
            model = sm.OLS(y, sm.add_constant(X[included + [feature]])).fit()
            p_value = model.pvalues[feature]
            
            if p_value < best_pvalue:
                best_pvalue = p_value
                best_feature = feature
        
        if best_pvalue < threshold:
            included.append(best_feature)
            remaining_features.remove(best_feature)
        else:
            break
    
    final_model = sm.OLS(y, sm.add_constant(X[included])).fit()
    return final_model


final_model = forward_stepwise_regression(X, y)