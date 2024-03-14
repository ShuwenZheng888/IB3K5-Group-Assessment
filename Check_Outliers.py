import matplotlib.pyplot as plt
import pandas as pd

# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

# Interquartile Range (IQR) method to check is there is any outliers of Purchase Amount
Q1 = data['Purchase Amount (USD)'].quantile(0.25)
Q3 = data['Purchase Amount (USD)'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data['Purchase Amount (USD)'] < lower_bound) | (data['Purchase Amount (USD)'] > upper_bound)]
print(outliers)

# Boxplot to visualize outliers
data['Purchase Amount (USD)'].plot(kind='box')
plt.title('Boxplot of Purchse Amount')
plt.show()

# Interquartile Range (IQR) method to check if there is any outliers of Age
Q1_age = data['Age'].quantile(0.25)
Q3_age = data['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
lower_bound_age = Q1_age - 1.5 * IQR_age
upper_bound_age = Q3_age + 1.5 * IQR_age

outliers_age = data[(data['Age'] < lower_bound_age) | (data['Age'] > upper_bound_age)]
print(outliers_age)

# Boxplot to visualize outliers
data['Age'].plot(kind='box')
plt.title('Boxplot of Age')
plt.show()
