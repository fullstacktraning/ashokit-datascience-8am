# pandas
# built on top of numpy
# data manipulation & analysis
# tabular data
# pip install pandas
# pip install openpyxl


import pandas as pd


# x = pd.Series([10,20,30,40,50]) #ID
# print(x)

# y = pd.DataFrame({
#     "name":["Std1","Std2"],           #2D
#     "age":[20,22]
# })
# print(y)


# df = pd.read_csv("Book1.csv")
# print(df)

df = pd.read_csv("Book1.csv",index_col=0,header=None)
print(df)