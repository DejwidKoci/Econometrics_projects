import pandas as pd


def SMK(data, destimulants):
    normalized = data.copy()
    numeric = data.columns[1:]
    for col in numeric:
        if col in destimulants:
            min_val = data[col].min()
            max_val = data[col].max()
            normalized[col] = data[col].apply(lambda x: (max_val - x) / (max_val - min_val))
        else:
            min_val = data[col].min()
            max_val = data[col].max()
            normalized[col] = data[col].apply(lambda x: (x - min_val) / (max_val - min_val))
        
    normalized['Mean'] = normalized.iloc[:, 1:].mean(axis = 1)
    normalized['Position'] = normalized['Mean'].rank(ascending = False)
    ranking = normalized[['Dzielnica', 'Position']]
    ranking = ranking.sort_values(by = 'Position')

    return ranking

rodzina_2012 = SMK(pd.read_excel('data.xlsx','2012 Rodzina'), [])
rodzina_2017 = SMK(pd.read_excel('data.xlsx','2017 Rodzina'), [])
rodzina_2021 = SMK(pd.read_excel('data.xlsx','2021 Rodzina'), [])

single_2012 = SMK(pd.read_excel('data.xlsx', '2012 Single'), ['X18'])
single_2017 = SMK(pd.read_excel('data.xlsx', '2017 Single'), ['X18'])
single_2021 = SMK(pd.read_excel('data.xlsx', '2021 Single'), ['X18'])

general_2012 = SMK(pd.read_excel('data.xlsx', '2012 Ogólne'), ['X3', 'X11', 'X17', 'X18'])
general_2017 = SMK(pd.read_excel('data.xlsx', '2017 Ogólne'), ['X3', 'X11', 'X17', 'X18'])
general_2021 = SMK(pd.read_excel('data.xlsx', '2021 Ogólne'), ['X3', 'X11', 'X17', 'X18'])

seniorzy_2012 = SMK(pd.read_excel('data.xlsx', '2012 Seniorzy'), ['X11', 'X17'])
seniorzy_2017 = SMK(pd.read_excel('data.xlsx', '2017 Seniorzy'), ['X11', 'X17'])
seniorzy_2021 = SMK(pd.read_excel('data.xlsx', '2021 Seniorzy'), ['X11', 'X17'])

data_to_save = {
    'rodzina_2012': rodzina_2012,
    'rodzina_2017': rodzina_2017,
    'rodzina_2021': rodzina_2021,
    'single_2012': single_2012,
    'single_2017': single_2017,
    'single_2021': single_2021,
    'general_2012': general_2012,
    'general_2017': general_2017,
    'general_2021': general_2021,
    'seniorzy_2012': seniorzy_2012,
    'seniorzy_2017': seniorzy_2017,
    'seniorzy_2021': seniorzy_2021
}


output_path = 'SMK.xlsx'
with pd.ExcelWriter(output_path) as writer:
    for sheet_name, data_frame in data_to_save.items():
        data_frame.to_excel(writer, sheet_name=sheet_name, index=False)

print(f'Zapisano dane do arkusza Excela: {output_path}')