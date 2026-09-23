
import numpy as np
import pandas as pd

df=pd.read_csv("employe.csv")


print(df.isnull().sum())


df['salary'].fillna(df['salary'].mean())



df.replace([np.inf, -np.inf],np.nan, inplace=True)



df["salary"]=np.where(df['salary']<0,df['salary'].mean(),df['salary'])

salary_mean=df['salary'].mean()
salary_std=df['salary'].std()
lower_bound=salary_mean-(3* salary_std )
upper_bound=salary_mean+(3* salary_std )

df=df[(df['salary']>= lower_bound)&(df['salary']<= upper_bound)]


df.to_csv("CLEAN_EMPLOYEE_DATA.csv ")





