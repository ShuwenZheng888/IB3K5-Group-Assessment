import pandas as pd

#Check if there is any null or duplicate data
# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

check_null = data.isnull().sum()
check_duplicate = data.duplicated().sum()

print(check_null)
print(f"The data has {check_duplicate} duplicate variables.")

#Check if any purchase amount column has other variables except from number
converted_column = pd.to_numeric(data['Purchase Amount (USD)'], errors='coerce')
has_non_numerics = converted_column.isnull().any()
print(f"Purchase Amount (USD) column contains non-numeric values: {has_non_numerics}")

#Check if any age column has other variables except from number
converted_column = pd.to_numeric(data['Age'], errors='coerce')
has_non_numerics = converted_column.isnull().any()
print(f"Age column contains non-numeric values: {has_non_numerics}")

#Check if any color column has other variables except from string
color_non_string = data['Color'].apply(lambda x: not isinstance(x, str))
color_has_non_strings = color_non_string.any()
print(f"Color column contains non-string values: {color_has_non_strings}")

#Check if any location column has other variables except from string
location_non_string = data['Location'].apply(lambda x: not isinstance(x, str))
location_has_non_strings = location_non_string.any()
print(f"Location column contains non-string values: {location_has_non_strings}")

#Check if any category column has other variables except from string
category_non_string = data['Category'].apply(lambda x: not isinstance(x, str))
category_has_non_strings = category_non_string.any()
print(f"Category column contains non-string values: {category_has_non_strings}")