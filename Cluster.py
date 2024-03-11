import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the data and set the preference
data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')
pd.set_option('display.max_rows', None)

# Cluster data by KMeans
cluster_data = data[['Age', 'Purchase Amount (USD)']]
kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(cluster_data)

# Draw the Scatter Plot
plt.figure(figsize=(12, 9)) 
plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1], c=clusters, cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Purchase Amount (USD)')
plt.title('Clustering of Purchase Amount and Age')
plt.show()

# Name the Cluster
cluster_map = {0: 'ClusterPurple', 1: 'ClusterGreen', 2: 'ClusterYellow'} 

# Set a new column 'Cluster' and 'ClusterType'
data['Cluster'] = clusters
data['ClusterType'] = data['Cluster'].map(cluster_map)

# Cluster for Arizona
arizona_data = data[data['Location'] == 'Arizona']
arizona_cluster_counts = arizona_data['ClusterType'].value_counts()
plt.scatter(arizona_data['Age'], arizona_data['Purchase Amount (USD)'], c=arizona_data['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Purchase Amount (USD)')
plt.title('Cluster Distribution of Arizona')
plt.show()
print('Cluster Type Number of Arizona is: ')
for item in arizona_cluster_counts.items():
    print(f"{item[0]}    {item[1]}")


# Cluster for Kansas
kansas_data = data[data['Location'] == 'Kansas']
kansas_cluster_counts = kansas_data['ClusterType'].value_counts()
plt.scatter(kansas_data['Age'], kansas_data['Purchase Amount (USD)'], c=kansas_data['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Purchase Amount (USD)')
plt.title('Cluster Distribution of Kansas')
plt.show()
print('Cluster Type Number of Kansas is: ')
for item in kansas_cluster_counts.items():
    print(f"{item[0]}    {item[1]}")

# Cluster for Rhode Island
rhode_island_data = data[data['Location'] == 'Rhode Island']
rhode_island_cluster_counts = rhode_island_data['ClusterType'].value_counts()
plt.scatter(rhode_island_data['Age'], rhode_island_data['Purchase Amount (USD)'], c=rhode_island_data['Cluster'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Purchase Amount (USD)')
plt.title('Cluster Distribution of Rhode Island')
plt.show()
print('Cluster Type Number of Rhode Island is: ')
for item in rhode_island_cluster_counts.items():
    print(f"{item[0]}    {item[1]}")


