import pandas as pd

file_path = '/home/mittesh/IAC_projects/Student-outcome-predictor/Basic_Problem_Input_Data/Year of Graduation Data/Final Lead Data.xlsx'

graduation_data = pd.read_excel(file_path)

col = graduation_data.columns
print(col)
summary = graduation_data.describe()
print(summary)

grad_filtered_data = graduation_data.dropna(axis = 0)
summary2 = grad_filtered_data.describe()
print(summary2)


y = grad_filtered_data.'Expected year of graduation'