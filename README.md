# DSA210-term-project
## Project Overview
This project aims to look at the relationship between literacy rates and gender equality. Gender equality, measured by the Women’s  Security and Peace Index, alongside the Gini Co-efficient, a measure of economic inequality, will be used to understand how education and economic factors interact to impact gender equality. 

### Motivation 
When we see countries today prosper economically, we often see thaat their success can be linked to high literacy rates. However, in 2025, despite economic prosperity, gender discrimination is still quite prevalent. Thus, in my project, I intend to:
1. Investigate whether higher literacy rates can be linked to better gender equality
2. Whether economic inequality (as measured by the Gini-Coefficient) is negatively correlated with literacy rate, and how that impacts our measure of gender equality
3. Examine whether gender equality can be accurately predicted using measurable socio-economic indicators through machine learning methods and hypothesis testing

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

<img width="662" alt="Screenshot 2025-04-25 at 12 39 49" src="https://github.com/user-attachments/assets/5cd77015-1c10-4890-944c-736d4caa8cdd" />

#### 1. Literacy Rate:
The literacy rate data taken from World Bank website, calculated each countries literacy rate as the percentage of the population where individuals aged above 15 and above are educated. In this regard, a higher score (max=100) indicates a higher literacy rate for the country. In the table attached, we see the mode to be 100, from this we can assume that from the filtered data, the countries with higher literacy rates remained while countries with lower literacy rates may have been filtered out. This belief can be backed by the median (the middle most value) to be in the 90s and the mean (average) to be in the 80s.

#### 2. Gini Coefficient:
Our measure of income inequality is the Gini Coefficient. The G.C score is on a scale of 0-1, where 0 represents perfect equality and 1 represents maximum inequality. The values in the table above, are represented as percentages, so a median of 0.35 represents a relatively lower inequality score, and a mean of 0.34 reinforces the belief that the countries in our dataset, are all, on average, leaning towards a lower inequality score. 

#### 3. WPS Index: 
The measure of our gender equality is the Women's Peace and Security Index. This index measures Women's inclusion in multiple areas such as education, justice, social inclusion etc. The overall scores range from 0-1, 1 representing a higher WPS index, thus a country with better gender equality. In the same sense, a lower WPS index, indicates a country with a higher gender inequality. It is evident from the table above, a mode of 0.7, and the median and mean ranging in 0.6, indicates, that the list of countries in our dataset have relatively better gender equality. Additionally, I included the employment index from the WPS index so that there may be one additional factor to consider when looking at the relationship between gender equality and literacy rates. 

#### 4. Employment Index:
The employment index is a measure of women's participation in the labor force, taken from the overall WPS index dataset. It takes into account women and girls, aged 15 and above who are either in or looking for work. This was an additional indicator I added to my dataset so that I could compare more variables and get better insights as to what my data is showing. The summary statistics that we see, show us that on average, the employment index score is in 60s, giving the impression that the countries in our dataset have a slightly above average index for women's participation in the work force. 

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

The above barplots, show the same observations we have already made from our histograms and summarry statistics. However, one can observe certain aspects such as the fact that lower-income countries are seen to have a lower literacy rate such as Burkina Faso or Mali. The same may be assumed for the WPS index. 

### Variable Relationships:

![download (9)](https://github.com/user-attachments/assets/c5e37315-35a5-4b8f-a19a-9932b16dc815)

The boxplot above shows us the relationship between literacy rates and the WPS index. It can be observed that there is a general positive correlation, and the boxplots towards the left show us that they have lower median literacy rates and a greater spread. Additionally, countries with higher WPS index have a tighter distribution, indicating stronger gender equality. 

![image](https://github.com/user-attachments/assets/486907c0-4330-4007-bb43-79d7881c6de5)

Here we see a barplot, showcasing the relationship between literacy rates and gini coefficient. Through this grouped barplot, we can see the difference in both scores decrease as it goes from a developed to developing country. We also observe the overall trend for Literacy Rates to fall downwards, while Gini Coefficient remain almost the same.

![image](https://github.com/user-attachments/assets/a8cf7af4-6630-4bf4-be0e-3d763f69edc3)

Here we see another barplot, showing a different relationship between Literaccy Rates and Employment Index. We observe the disparity between both score to be quite less. Additionally, we can observe a potentiall negative correlation, as when literacy rates start to decrease, employment index are seen to be relatively high. However, there are some exceptions, for example, the country of Cameroon who seems to have a relatively balanced score between both. 

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


## MACHINE LEARNING:

For the ML tasks of my project, I aimed to see whether, based on the findings of my hypothesis tests, we could predict a country's level of gender equality (as measured by the WPS Index) based on the literacy rate, gini-coefficient and employment index.

### LINEAR REGRESSION:

To enrich my dataset for my ML tasks, I engineered a new indicator which was the Adjusted Employment Literacy Index. This captured the interaction between a country’s literacy rate and the women’s participation rate in the labour force. So a country that would have a high AEL score, would also be more likely to have a high WPS index ( AKA. higher gender equality). This variable was calculated as the product of literacy rate and employment index, and the introduction of this indicator would help both linear and non-linear models. This aspect of this indicator is especially important as we had many features to look at. For instance, a country could have a high literacy rate with a lower employment index and that could still lead to low gender equality, despite a high literacy rate. Linear models such as linear regression assume straight line relationships, but here we will also be using random forest model which can explore combinations of such features.

Firstly, a linear regression model was used to predict the WPS Index. As seen in the graph below, the model achieved the R² value of 0.25 - an average result, showing that 25% of our variation could be explained by our model but the remaining 75% could be explained through other factors such as culture and religion. Additionally, the MSE (Mean Squared Error) had an average score of 0.013. This means that on average, the model’s predictions are off by +- 0.11, which indicates a moderate error. 

The navy blue line of best fit shows a positive slope, highlighting that as AEL increases, so does the WPS index, reaffirming our belief that higher literacy rates and labour force participation can be correlated with a higher gender equality score. We also see a fair amount of entries (countries) scattered near the line of best fit, showing us that our prediction for the countries closer to the line are more accurate than the ones that are far. However, there still is a good amount of variance that this model does not explain.

<img width="508" alt="Screenshot 2025-05-28 at 22 36 47" src="https://github.com/user-attachments/assets/cc2e4b95-5597-4686-937e-4d0e7527e8f8" />


### RANDOM FOREST:

To further study our data, the Random Forest model was chosen. This model was chosen because it works well with smaller data, numerical and categorical features, and non linear relationships that the linear regression model could not capture. A random forest is an algorithm that combines the prediction of multiple decision trees and averages the result, and was used in the following two ways: 1. Regression 2. Classification

#### RANDOM FOREST REGRESSOR:

A random forest regressor was used to predict the wps index (a continuous variable). In the following graph we see the relationship between the actual WPS index (X-axis) and the predicted WPS index (Y-axis), where again, each dot represents a country in our data set. The dashed line is a representation of the idea prediction, where our predicted results match our actual index scores. The regressor provided us with a R² value of 0.463 - indicating that 46% of our variation could be explained by this model, which is a significant increase from the linear regression R² value of 0.25. This reaffirms the belief that the random forest model captures more complex relationships that the linear regression could not. 

The MSE value is of 0.0094 - a value showing, that on average our predications were ±0.10 points from our actual WPS index. A value that can be considered to be very insightful given our range to be limited from 0-1. Additionally, most of our data points closely follow the ideal prediction line, verifying the effectiveness of the model. The trend of the data points show an upwards trajectory, so we can confirm there is a positive correlation between our real and predicted values. This is also an indication of the fact that the model correctly learnt the relationship between the variables and isn’t generating random guesses. 


<img width="502" alt="Screenshot 2025-05-28 at 22 36 39" src="https://github.com/user-attachments/assets/69e6ed60-779d-4ee4-a552-d41b1f4e50c8" />


#### RANDOM FOREST CLASSIFIER:

Our second use of the random forest model was in the form of the random forest classifier. The classifier helped in classifying our countries as either low gender equality or high gender equality based on our WPS index, using binary values of 1 and 0, whereby 1 indicates high gender equality and 0 indicates low gender equality. The confusion matrix below compares the actual values from our data with the model’s output showing us how accurately it classified the countries from our data set. We see:
1. 6 true negatives: 6 countries were correctly identified to be low-WPS countries.
2. 1 false positive: A misclassification of a low-WPS country incorrectly predicted as high- WPS country.
3. 5 true positives: 5 countries were correctly identified to be high-WPS countries.
4. 0 false negatives: The model didn’t miss any high-WPS countries
These results are also reiterated in the Precision, Recall, F1 and Support columns. The precision column shows all low-WPS countries were correctly classified but there was 83% accuracy in predicting high-WPS so there were some false positives. 
Secondly our recall column shows that all high-WPS countries were detected, but some low-WPS were missed - an 86% accuracy level.

The F1 score balances the precision and recall calculations and we see the values ranging from 91-92% - so our model correctly estimated 11 out of 12 countries. 
In conclusion the random forest classifier can be seen a highly reliable method of classifying countries as high or low gender equality, with only one miscalculation.

<img width="419" alt="Screenshot 2025-05-28 at 22 36 28" src="https://github.com/user-attachments/assets/47241536-f4e5-40b5-a48c-5192a29a2543" />


## CONCLUSION:

In conclusion, this project explored the dynamics between gender equality and socio-economic across countries. Through hypothesis tests and machine learning methods, our goal was to see whether these variables could meaningfully explain gender equality results. We learnt so far that gender equality can be predicted using socio economic factors such as education and income, and that we do see a significant relationship between these variables. 
