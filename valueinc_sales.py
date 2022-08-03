# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 21:14:36 2022

@author: Kgopotso
"""

import pandas as pd 

# file_name = pd.read_csv('file.csv') <---- format of read_csv 

data = pd.read_csv('transaction.csv') 

data = pd.read_csv('transaction.csv', sep=';')   

# summary of data
data.info()   

# working with calculations
    # defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6 

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem 
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPerTransaction = NumberOfItemsPurchased * SellingPricePerItem 

# Column calculations for CostPerTransaction  

# CostPerTransaction = NumberOfItemsPurchased * CostPerItem
# variable = dataframe['column_name']

NumberOfItemsPurchased = data['NumberOfItemsPurchased'] 
CostPerItem = data['CostPerItem'] 
CostPerTransaction = NumberOfItemsPurchased * CostPerItem 

# adding a new column to a Dataframe 
data['CostPerTransaction'] = CostPerTransaction 

# SalesPerTransaction column
data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem'] 

# Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

# Markup Calculation = (sales - cost) / cost 
data['Markup'] =( data['SalesPerTransaction'] - data['CostPerTransaction']) /  data['CostPerTransaction'] 

data['Markup'] = (data['ProfitPerTransaction'] ) / data['CostPerTransaction']  

# Rounding markup

roundmarkup = round(data['Markup'], 2)  
data['Markup'] = round(data['Markup'], 2) 

# combine data fields
my_name = 'Kgopotso'+ ' ' +'Maifo'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

# checking columns data type 
print(data['Day'].dtype) 

# change column type
day = data['Day'].astype(str) 
year = data['Year'].astype(str) 
print(day.dtype) 
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year 
data['date'] = my_date 

# using iloc to view specific columns/rows
data.iloc[0]         # views the row with index 0
data.iloc[0:3]       # views first 3 rows
data.iloc[-5:]      # views last 5 rows 
data.head(5)      # views first 5 rows
data.iloc[:,2]      # views all rows in 2nd column 
data.iloc[4,2]      # views 4th row in 2nd column  


# using the split method to split data fields
    # new_var = column.str.split('sep', expand=True) 
    
split_col = data['ClientKeywords'].str.split(',',expand=True) 

# creating new columns for split columns
data['ClientAge'] = split_col[0] 
data['ClientType'] = split_col[1] 
data['LengthOfContract'] = split_col[2] 

# using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '') 
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '') 

# using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower() 


# how to merge files
    # bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')  

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month') 

# dropping columns 
    # df = df.drop('columnname', axis=1)
data = data.drop('ClientKeywords', axis=1) 
data = data.drop('Day', axis=1) 
data = data.drop(['Year', 'Month'], axis=1)     # dropping multiple columns in one line of code

# Export into CSV 
data.to_csv('ValueInc_Cleaned.csv', index=False)  

































