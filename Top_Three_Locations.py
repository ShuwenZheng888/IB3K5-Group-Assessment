import pandas as pd

# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

# Group the data by location, color, and calculate the mean purchase amount
grouped_data = data.groupby(['Location', 'Color'])['Purchase Amount (USD)'].mean().reset_index()

# Set a dictionary to store the absolute average value
absolute_averages = {}

for location in grouped_data['Location'].unique():
    # Filter the data by location
    location_data = grouped_data[grouped_data['Location'] == location]

    # Encode and set dummy varibables for color
    data_encoded = pd.get_dummies(location_data, columns=['Color']).drop(columns=['Location'])

    # Calculate the correlation matrix
    correlation_matrix = data_encoded.corr()

    # Write the output file to store the result for each location
    file_name = f'correlation_{location}.txt'
    with open(file_name, 'w') as file:
        # Pearson correlation calculating and exclude self-correlation
        correlations = correlation_matrix['Purchase Amount (USD)'].drop('Purchase Amount (USD)', errors='ignore')
        for index, value in correlations.items():
            file.write(f"{index} {value}\n")
            
    def calculate_absolute_average(file_name):
        """Calculate the absolute average for each location"""
        total_abs_value = 0
        count = 0

        with open(file_name, 'r') as file:
            for line in file:
                try:
                    value = float(line.split()[-1])
                    total_abs_value += abs(value)
                    count += 1
                except ValueError as e:
                    print(f"Error processing line: {line.strip()}")
        return total_abs_value / count if count > 0 else None
        

    absolute_average = calculate_absolute_average(file_name)
    absolute_averages[location] = absolute_average

# Find the top 3 cities and print the result
top_3_locations = sorted(absolute_averages.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 locations with the highest absolute average correlations:")
for location, absolute_average in top_3_locations:
    print(f"{location}: {absolute_average}")

