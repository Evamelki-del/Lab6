# """Eva Melki, Roni Azoulay"""

import numpy as np
import seaborn as sns
import pandas as pd


data = pd.read_csv("wdi_wide.csv")

#Part 3



#Question 4
#Printing the amount of unique values per column using nunique function

print(data.nunique())

#Question 6

#Adding the "GNI per capita" column 
#and rounding to the nearest cent (2 decimal places) in the same function

data["GNI per capita"] = round(data["GNI"] / data ["Population"], 2)

#Question 8
#Relationship between the high income economies and their region

HIE_vs_region = pd.crosstab(data["High Income Economy"], data["Region"])

print("The high income economies are in: ")

row = HIE_vs_region.iloc[1]
cols = row[row != 0].index   
print(list(cols)) 

