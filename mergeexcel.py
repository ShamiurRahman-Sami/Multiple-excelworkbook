import pandas as pd

excel1  = 'yourworkbookfilename.xlsx'
excel2  = 'yourworkbookfilename2.xlsx'
excel3  = 'yourworkbookfilename3.xlsx'
excel4  = 'yourworkbookfilename4.xlsx'
excel5  = 'yourworkbookfilename5.xlsx'
excel6  = 'Syourworkbookfilename6.xlsx'


df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)
df3 = pd.read_excel(excel3)
df4 = pd.read_excel(excel4)
df5 = pd.read_excel(excel5)
df6 = pd.read_excel(excel6)

values1 = df1[['Name','Email', 'Phone']]
values2 = df2[['Name','Email', 'Phone']]
values3 = df3[['Name','Email', 'Phone']]
values4 = df4[['Name','Email', 'Phone']]
values5 = df5[['Name','Email', 'Phone']]
values6 = df6[['Name','Email', 'Phone']]

dataframes = [values1,values2,values3,values4,values5,values6]

join =pd.concat(dataframes)
join.to_excel("final.xlsx")
