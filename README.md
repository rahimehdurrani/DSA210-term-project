# DSA210-term-project
## Project Overview
This project aims to look at the relationship between literacy rates and gender equality. Gender equality, measured by the Women’s  Security and Peace Index, alongside the Gini Co-efficient, a measure of economic inequality, will be used to understand how education and economic factors interact to impact gender equality. 

### Motivation 
When we see countries today prosper economically, we see thaat their success can be linked to high literacy rates. However, in 2025, despite economic prosperity, gender discrimination is still quite prevalent. Thus, in my project, I intend to:
1. Investigate whether higher literacy rates can be linked to better gender equality
2. Whether economic inequality is negatively correlated with literacy rate, and how that impacts our measure of gender equality


### Data Sources
The data sets that I intend on using my project have all been taken from data that has been made publicly available.
1. Global Literacy Rates: This data set has been taken from the World Bank website and provides the percentage of people aged 15 and above who count as literate.
2. Women's Peace and Security Index: This data set has been taken from the Georgetown Instituite for Women, Peace and Security, and will be acting as our measure of gender equality
3. Gini-Coefficient: The Gini-coefficent will be our measure of economic inequality, whose dataset has also been taken from the World Bank's website.

### Data Analysis Plan:

1. Data cleaning and preprocessing:
   a. Handle missing data through imputation or exclusion, depending on the extent of missingness.
   b. Merge the three datasets using country as the common value.

2. Exploratory Data Analysis (EDA):
   a. Conduct descriptive statistics to summarize the data (e.g., mean, median etc).
   b. Visualize relationships between variables using scatterplots, histograms, 
   c. Identify outliers and understand their impact on the analysis.

3. Correlation Analysis:
   a. Understand whether lower literact rates can be correlated with poor gender equality and a low gini-coefficient.

4. Visualization:
   a. Visualize my findings using graphs such as scatter plots and bar graphs to summarise and better understand my findings.

### Conclusion

In conclusion, I  want to determine if there’s a correlation between adult literacy rates and gender equality (Women's Security and Peace Index) and explore how economic inequality (Gini coefficient) influences these relationships. Moreover, look at other sidelined relationships such as ones pertaining to region, i.e: developing vs developed countries. Lastly, see whether regardless of literacy rates, does gender inequality still persist to the level that it does

# Report

#### IMPORTANT NOTE: 
The first step of my DSA term project was to clean and filter my data in a way that allows for an accurate representation of the provided data. In order to achieve that, I intially started off with filtering my data with the most recent year that had the most entries, however, this led to a merged data set with only 10 entries. Thus, to allow for a more holistic dataset, I filtered my datasets with the 3 most recent years, ranging from 2020-2023.

## EXPLORATORY DATA ANALYSIS
The intial analysis of my filtered data sets, was done through EDA. This method allowed me to study certain trends and understand my own data better. Starting off with summary statistics:

<img width="664" alt="Screenshot 2025-04-25 at 09 46 32" src="https://github.com/user-attachments/assets/33300176-336b-465f-a6d9-f63deb61b7a4" />

#### 1. Literacy Rate:
The literacy rate data taken from World Bank website, calculated each countries literacy rate as the percentage of the population where individuals aged above 15 and above are educated. In this regard, a higher score (max=100) indicates a higher literacy rate for the country. In the table attached, we see the mode to be 100, from this we can assume that from the filtered data, the countries with higher literacy rates remained while countries with lower literacy rates may have been filtered out. This belief can be backed by the median (the middle most value) to be in the 90s and the mean (average) to be in the 80s.

#### 2. Gini Coefficient:
Our measure of income inequality is the Gini Coefficient. The G.C score is on a scale of 0-1, where 0 represents perfect equality and 1 represents maximum inequality. The values in the table above, are represented as percentages, so a median of 0.35 represents a relatively lower inequality score, and a mean of 0.34 reinforces the belief that the countries in our dataset, are all, on average, leaning towards a lower inequality score. 

#### 3. WPS Index: 
The measure of our gender equality is the Women's Peace and Security Index. This index measures Women's inclusion in multiple areas such as education, justice, social inclusion etc. The overall scores range from 0-1, 1 representing a higher WPS index, thus a country with better gender equality. In the same sense, a lower WPS index, indicates a country with a higher gender inequality. It is evident from the table above, a mode of 0.7, and the median and mean ranging in 0.6, indicates, that the list of countries in our dataset have relatively better gender equality. Additionally, I included the employment index from the WPS index so that there may be one additional factor to consider when looking at the relationship between gender equality and literacy rates. 

### Data Visualisations:

In order to see the overall trends of each dataset, I used graphs such as histograms and barplots. 

![download](https://github.com/user-attachments/assets/31fd2686-cf47-4881-8697-cd0e47f48149)

The above histogram shows the distribution of literacy rates. We can see that this graph is slightly skewed to the left, showing us that there are more countries on the higher end, i.e: more countries have a higher literacy rate. 

![download (1)](https://github.com/user-attachments/assets/dfa550a0-0086-4d4e-a440-6e4cf3f013e6)

The above histogram shows the distribution of Gini-Coefficient Scores, and unlike the distribution of Literacy Rates, this graph shows a distribution that skews to the right. This supports the summary statistics we observed above, that there are more countries with lower scores, i.e: countries with relatively better income equality 

![download (2)](https://github.com/user-attachments/assets/e55efe6f-b682-4d55-8782-200e49f2101c)

Lastly, we see the histogram of the WPS index and just like the Literacy rate data, we see a Kernal Density line, skewed to the left, alligning with our earlier observation that in our dataset, there are more countries with a higher WPS index score, i.e: better gender equality. 



![download (6)](https://github.com/user-attachments/assets/db393f21-6e13-4b80-ae4b-cf6a06fb16af)
![download (7)](https://github.com/user-attachments/assets/3c29db16-3472-4b34-b595-eab103a115db)
![download (8)](https://github.com/user-attachments/assets/badefee9-e9b4-4659-8438-40146f192479)

The above barplots, show the same observations we have already made from our histograms and summarry statistics. 

### Variable Relationships:

![download (9)](https://github.com/user-attachments/assets/c5e37315-35a5-4b8f-a19a-9932b16dc815)

The boxplot above shows us the relationship between literacy rates and the WPS index. It can be observed that there is a general positive correlation, and the boxplots towards the left show us that they have lower median literacy rates and a greater spread. Additionally, countries with higher WPS index have a tighter distribution, indicating stronger gender equality. 

![download (10)](https://github.com/user-attachments/assets/38bf5ee5-ef19-4a89-a5a0-347fe6e89952)

Lastly, we see a heat correlation map, summarising most of the relationships between our variables that we will also see forward in our hypothesis testing. Areas highlighted in blue signifity a negative correlation, where when one variable increases, the other may decrease and vice versa. On the other hand, the areas highlighted in red, signify a positive correlation, where both variable move in the same direction. So according to our heatmap, literacy rates and Gender Equality have a positve correlation of 0.7. 

## HYPOTHESIS TESTING:

### 1. 

Our main goal in this project, was to test whether there is a relationship between gender equality and literacy rates. As we have seen in our exploratory data analysis, WPS and Literacy Rates seem to have a positive correlation. So we will first test a one tailed hypothesis regarding these variables:
   #### Null Hypothesis (H0) = There is no significant relationship between literacy rates and WPS index.
   #### Alternative Hypothesis (H1) = There is a positive correlation between literacy rates and WPS index. 

To test our hypothesis, we will use the Pearson's correlation coefficient. This test helps quantify the linear relationship between 2 countinous variables. The pearson correlation coefficient ranges from -1 - +1, where 1 defines a perfect positive linear correlation, and -1 indicates a perfect negative linear correlation. 

#### RESULTS:
Pearson Correlation Coefficient: 0.70
P-value: 4.66e-10

![download (11)](https://github.com/user-attachments/assets/2792b35d-63ca-465f-99fe-85089248f32a)

The pearon correlation coefficent of 0.7, indicates a strong positive relationship, so an increase in literacy rates can be correlated with higher gender equality. Additionally, the P-value of 4.66e-10, is quite below the significant level of 0.05, this observations shows us that the p-value is statiscally significant and so unlikely to have occured by chance.
There is a statistically significant correlation between Literacy Rate and WPS Index.

Our results of our first hypothesis test is visible in this regression plot, which combines a scatter plot with a regression line. This visualisation clearly shows how a lower literacy rate is correlated with a lower WPS index, and vice versa. 

### 2. 

Secondly, we aim to see whether a relationship between income inequality and literacy rates can be established. For that purpose, we take into account Literacy rates and the Gini Coefficient. And according to our heatmap, we see a negative correlation between both variables: 
#### Null Hypothesis (H0) = There is no significant relationship between literacy rates and income inequality (Gini Coefficient)
#### Alternative Hypothesis (H1) = There is a negative correlation between literacy rates and income inequality (Gini Coefficient)

To test this hypothesis, we use the Pearson's correlation coefficient again, alongside testing the P-value with a significance level of 0.05. Additionally, since we predicted the direction of this relationship, it would be considered a one-tailed test. 

#### RESULTS:
Pearson Correlation Coefficient: -0.06
P-value: 6.74e-01
There is no statistically significant correlation between Literacy Rate and Gini Coefficient.

![download (12)](https://github.com/user-attachments/assets/805480eb-3c5c-4cac-b2b0-e66207c7e118)

The pearson correlation coefficient is less than 0, indicating a relatively negative correlation between both variables, i.e: as one increases, the other decreases. However, the value is quite close to 0, which then suggest that there is almost no correlation between both variables, which shows that if incomce inequality changes, literacy rates do not seem to have a significant impact in the opposite direction. Additionally, since the p-value is above 0.05, we fail to reject the null hypothesis, in other words, we do not have enough evidence to accept the alternate hypothesis. In conclusion, there is no statiscally significant data that suggest that these two variables have any consistent pattern. 

### 3. 
Lastly, we use our additional indicator of the Employment Index to retest or check what we have already seen. Since, our second hypothesis test showed that there is no significant correlation between Literacy Rates and the Gini Coefficient, it is possible to suggest that the same may be said for the Employment Index and the Literacy Rates, as a lower employment index suggests more income inequality. 

#### Null Hypothesis (H0) = There is no significant relationship between Employment Index and Literacy Rates
#### Alternative Hypothesis (H1) = There is a significant correlation between Employment Index and Literacy Rates 

Just like before, as we are dealing with two continous variables, we will be using the Pearson's Correlation Coefficient, alongside testing the P-value with the significance level of 0.05.

#### RESULTS: 
Pearson Correlation Coefficient: 0.34
P-value: 7.51e-03
There is a statistically significant correlation between Employment Index and Literacy Rate.

![image](https://github.com/user-attachments/assets/8ead732d-4037-45b4-8a1f-83027d976d1b)

The pearson correlation coefficient of 0.34 indicate a relatively positve correlation between both variables and the p-value of 7.51e-03 is very well below the signifcance level of 0.05, showing us that the correlation is statistically significant. This means that there is enough evidence to reject the null hypothesis and assume that there is a significant relationship between both variables. 

## CONCLUSION:

In conclusion, through our EDA and Hypothesis testing, we have seen that there do exist correlations between higher literacy rates and gender equality. The attached pairplot provides a summary of all our relationships that we have already discussed, however, it is important to note, that just because there exist correlation between our variables, hypothesis testing is not enough to prove causation as there may be external confounding variables that may be causing the relationship that we see. 

![image](https://github.com/user-attachments/assets/245b61e1-f74c-4a90-a3bc-8e4c69d0d16e)



