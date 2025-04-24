import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

lit_df = pd.read_csv('litrates.csv', skiprows=4)
wps_df = pd.read_excel('WPS Data.xlsx', skiprows=5)
gini_df = pd.read_csv('gini_coeff.csv', skiprows=4)


#filtering literacy rate data
lit_df = lit_df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 68'])
filteredlit= lit_df[['Country Name','2020','2021','2022','2023']].copy()
filteredlitrate = filteredlit.dropna(subset=['2020','2021','2022','2023'], how='all')
filteredlitrate.loc[:,'Most Recent Value']= filteredlitrate[['2023','2022','2021','2020']].bfill(axis=1).iloc[:, 0]
filteredlitrate = filteredlitrate[['Country Name', 'Most Recent Value']]
filteredlitrate.rename(columns={'Most Recent Value': 'Literacy Rate'}, inplace=True)
