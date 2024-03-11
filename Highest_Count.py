import pandas as pd
import numpy as np
import scipy
from scipy.stats import pearsonr

# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

#Group the data and count the occurrences(per category and location)
color_counts = data.groupby(['Location', 'Category', 'Color']).size().reset_index(name='Count')

# Find the maximum count for each group
max_count = color_counts.groupby(['Location', 'Category'])['Count'].transform(max)
result= color_counts[color_counts['Count'] == max_count]

# Filter and find the result for the top 3 locations
locations = ['Arizona', 'Kansas', 'Rhode Island']
location_result = result[result['Location'].isin(locations)]
print(location_result.to_string(index=False))