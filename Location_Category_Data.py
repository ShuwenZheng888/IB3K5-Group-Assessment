import pandas as pd

#  the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

# For loop to filter the data by categories
for category_value in data['Category'].unique():
    filtered_data = data[data['Category'] == category_value]
    
    # Group the data by location, color, and calculate the mean purchase amount
    grouped_data = filtered_data.groupby(['Location', 'Color'])['Purchase Amount (USD)'].mean().reset_index()
    
    # Set a dictionary to store the absolute average value
    absolute_averages = {}

    for location in grouped_data['Location'].unique():
        # Filter the data by location
        location_data = grouped_data[grouped_data['Location'] == location]

        # Encode and set dummy varibables for color
        data_encoded = pd.get_dummies(location_data, columns=['Color']).drop(columns=['Location'])

        # Calculate the correlation matrix
        correlation_matrix = data_encoded.corr()

        # Output file to store the result for each location and category
        file_name = f'correlation_{category_value}_{location}.txt'
        with open(file_name, 'w') as file:
            # Pearson correlation calculating and exclude self-correlation
            correlations = correlation_matrix['Purchase Amount (USD)'].drop('Purchase Amount (USD)', errors='ignore')
            for index, value in correlations.items():
                file.write(f"{index}: {value}\n")
