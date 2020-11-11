import pandas as pd


df = pd.read_csv('MDR_RR_TB_burden_estimates_2020-11-11.csv', 
    usecols=["iso_numeric"])
print(df.describe())

