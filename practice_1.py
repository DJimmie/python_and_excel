"""Getting familier with xlwings"""
# %%
import xlwings as xw
import pandas as pd

excel_file='C:/Users/JDowd/OneDrive - Schlumberger/Desktop/test1.xlsx'
csv_file='C:/Users/JDowd/OneDrive - Schlumberger/Desktop/ops_list.csv'

# %%
def get_excel_data():
    df = pd.read_excel(excel_file)
    xw.view(df.head())


def get_csv_data():
    df=pd.read_csv(csv_file)
    print(df.head())


# %%
get_excel_data()


# get_csv_data()
# %%
