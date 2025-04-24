{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 245,
   "metadata": {},
   "outputs": [],
   "source": [

"import pandas as pd"
"import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lit_df = pd.read_csv('litrates.csv', skiprows=4)
wps_df = pd.read_excel('WPS Data.xlsx', skiprows=5)
gini_df = pd.read_csv('gini_coeff.csv', skiprows=4)


#filtering literacy rate data with the most recent years
lit_df = lit_df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 68'])
filteredlit= lit_df[['Country Name','2020','2021','2022','2023']].copy()
filteredlitrate = filteredlit.dropna(subset=['2020','2021','2022','2023'], how='all')
filteredlitrate.loc[:,'Most Recent Value']= filteredlitrate[['2023','2022','2021','2020']].bfill(axis=1).iloc[:, 0]
filteredlitrate = filteredlitrate[['Country Name', 'Most Recent Value']]
filteredlitrate.rename(columns={'Most Recent Value': 'Literacy Rate'}, inplace=True)

# filtering the Gini Coefficient data
gini_df = gini_df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 68'])
filteredgini= gini_df[['Country Name','2020','2021','2022','2023']].copy()
filteredgini= filteredgini.dropna(subset=['2020','2021','2022','2023'], how='all')
filteredgini.loc[:,'Most Recent Value']= filteredgini[['2023','2022','2021','2020']].bfill(axis=1).iloc[:, 0]
filteredgini.rename(columns={'Most Recent Value': 'Gini Coefficient'}, inplace=True)
filteredgini = filteredgini[['Country Name', 'Gini Coefficient']]

#filtering the Women's Peace and Security Index
wps_df = wps_df.iloc[:,[1,2,5]]
wps_df= wps_df.dropna(subset=[wps_df.columns[1]])
wps_df[wps_df.columns[2]] = wps_df[wps_df.columns[2]].round(1)
wps_df.columns = ['Country Name', 'WPS Index', 'Employment Index']

#merging all datasets
merged_ds= filteredlitrate.merge(wps_df, on='Country Name', how='inner')
merged_ds= merged_ds.merge(filteredgini, on='Country Name', how='inner')
merged_ds.to_csv('merged_ds.csv', index=False)
merged_ds['Literacy Rate'] = pd.to_numeric(merged_ds['Literacy Rate'], errors='coerce')
merged_ds['WPS Index'] = pd.to_numeric(merged_ds['WPS Index'], errors='coerce')
merged_ds = merged_ds.dropna(subset=['Literacy Rate', 'WPS Index'])
display(merged_ds.head(10))"


