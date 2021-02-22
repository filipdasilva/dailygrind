#learning this because it is more applicable to my work right now, so far seems very similar to R which i took a grad school level business analytics class where we only used R studio

#data extraction, cleaning, wrangling, analysis, action
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib imline

#!head data/sales_data.csv

how to read csv file
#sales = pd.read_csv(
#'data/sales_data.csv', 
#parse dates = ['Date'])

sales.head()
#view as csv

sales.shape
#size of csv

sales.info 
#understand the counts we are working with

sales.describe 
#learn the statistical properties of the numbers in the table

sales['Unit Cost'].describe()
.mean
.median
.plot(kind='box', vert=False, figsize=(14,6))

box plots

.plot(kind='density', figsize(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')

.plot kind hist
ax.set_ylabel('Number of Sales')
set x label

