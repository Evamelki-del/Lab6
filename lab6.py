# """Eva Melki, Roni Azoulay"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("wdi_wide.csv")

#Part 3
data.info()
# The null values for physician and population 
missing_physicians = data["Physicians"].isna().sum()
missing_population = data["Population"].isna().sum()

print("\nEmpty values in 'Physicians':", missing_physicians)
print("Empty values in 'Population':", missing_population)



#Question 4
#Printing the amount of unique values per column using nunique function

print(data.nunique())

#Question 5 
#Printing further information about our data

print(data.describe())

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


#Part 4



#Question 6a
#Correlation between  Internet use and emissions per capita

#Creating a new colunmn for emissions per capita by dividing greenhouse gas emission per country by total population
data["emissions per capita"] = (data["Greenhouse gas emissions"]/ data["Population"])

#Plotting with a lmplot:
sns.scatterplot(data= data, x= "Internet use", y= "emissions per capita")
plt.show()

#Plotting with a scatterplot:
sns.lmplot(data= data, x= "Internet use", y= "emissions per capita")
plt.show()

#Question 6b
#Identifying countries with high gas emissions (> 0.03)

print("The countries with high emissions per capita are: ") 

countries_with_high_emissions = []

#Isolating the country name of the country that has over 0.03 gas emissions per capita

for i, row in data.iterrows():
    if row["emissions per capita"] > 0.03 :
        name = data.loc[i, "Country Name"]
        countries_with_high_emissions.append(name)

print(countries_with_high_emissions)

#Question 6c
#Finding variation by region using the format of the previous scatterplot

sns.scatterplot(data= data, x= "Internet use", y= "emissions per capita", hue= "Region")
plt.show()

#Question 6d
#Finding relationship between high income economies and high emissions

markers= {"1":"O", "0": "X"}

sns.scatterplot(data= data, x= "Internet use", y= "emissions per capita", 
                style= "High Income Economy", markers=True)
plt.show()


#Plotting everything in one graph
sns.scatterplot(data= data, x= "Internet use", y= "emissions per capita", hue= "Region", 
                style= "High Income Economy", markers=True)
plt.show()


