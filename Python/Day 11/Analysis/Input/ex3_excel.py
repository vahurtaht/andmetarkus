import pandas as pd

file_name  = r'C:/Users/user/Documents/Github/andmetarkus/Python/Day 11/Analysis/Input/ProductTable.xlsx'


data = pd.read_excel(file_name)
print(data)
data_dict = data.to_dict(orient='records')
print(data_dict)
