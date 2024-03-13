import pandas as pd

# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)  

def write_correlations_to_file(correlation_matrix, file_name):
    """Function to write the correlation result to a file"""
    correlations = correlation_matrix['Purchase Amount (USD)'].drop('Purchase Amount (USD)', errors='ignore')
    with open(file_name, 'w') as file:
        for index, value in correlations.items():
            file.write(f"{index} {value}\n")

def calculate_absolute_average(file_name):
    """Function to calculate the absolute average from the specific file"""
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

columns = ['Item Purchased', 'Category', 'Location', 'Color', 'Season']
for column in columns:
    grouped_data = data.groupby([column])['Purchase Amount (USD)'].mean().reset_index()
    data_encoded = pd.get_dummies(grouped_data, columns=[column])
    correlation_matrix = data_encoded.corr()
    file_name = f"{column}_Coefficient.txt"
    write_correlations_to_file(correlation_matrix, file_name)
    absolute_average = calculate_absolute_average(file_name)
    print(f"Absolute average correlation of {column} is: {absolute_average}")
