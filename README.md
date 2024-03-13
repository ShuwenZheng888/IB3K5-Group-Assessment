
# Instruction
This GitHub file is used as a code reference for the IB3K5 group assessment (group 30) data analysis and data visualization. It consists of three parts: python code for each part of the data analysis result, two Jupyter Notebook files with all the code included and a zip file includes all the data txt.

## Python Files
There are 10 Python files included:

1. `check_data.py`

This code is used to check if the excel data has any null or duplicate value. For the column which will be used for data anlysis,check the two numeric columns(Purchase Amount and Age) have any values except from number and check the other three categorical columns(Category, Color and Location) have any values except from string.

2. `check_outliers.py`

This code is used to check if the numeric data we are using (Purchase Amount and Age) have any **outliers** and draw boxplot to visualize.

3. `Pearson_Coefficient.py`

This code is used to find the Pearson correlation coefficient between **five different categorical columns**(Item Purchased, Category, Location, Color,Season) and **Purchase Amount**. 

4. `Top_Three_Locations.py`

This code is used to find the top three locations' **Purchase Amount** affected most by **Color** and write all the results into a *correlation_{location}.txt* file.

5. `Location_Category_Data.py`

This code writes the output of the Pearson Coefficient of all **Color** on **Purchase Amount**, in each specific category within each location. The result is stored in a *correlation_{Category}_{location}.txt* file and the data is used to give insight later.

6. `Highest_Count.py`

This code finds the *color* that has the most occurrences in each specific category within the top three locations. 

The result printed by the code will be used for further analysis.

7. `HeatMap_Arizona.py`

This code is the visualization code to draw the heat map of Arizona.

8. `HeatMap_Kansas.py`

This code is the visualization code to draw the heat map of Kansas.

9. `HeatMap_RhodeIsland.py`

This code is the visualization code to draw the heat map of Rhode Island.

10. `Cluster.py`

This code is used to do the K-Means Clustering of **Age** and **Purchase Amount** and find which type of cluster is the most common in the top 3 cities find in `Top_Three_Locations.py`file.
The code then draw the scatter plot of the whole data, and draw the specific scatter plot for these 3 cities.

## Jupyter Notebook

1. `Data_Cleaning.ipynb`

This Jupyter Notebook code contains all the Python code used for data cleaning and output result in one file which is easier to read and compare.

2. `Combination_Final.ipynb`

This Jupyter Notebook code contains all the other Python code (for data anlysis part) and output result in one file which is easier to read and compare.

## Zip File
`Coefficient_Data.zip`

This is a zip file included all the output txt file generated by code `Peason_Coefficient.py`, `Top_Three_Locations.py` and `Location_Category_Data.py`.
(The data in the last two files are the Pearson Correlation Coefficient of **Different Color** on **Purchase Amount**) 

## Cautions
The data we analyze is **CustomerShoppingTrends.xlsx**.
In the python file `Top_Three_Locations.py`, `Location_Category_Data.py`, `Highest_Count.py` and `Cluster.py`.

The code used is :
`data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')`

However, *'/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx'* is a custom path depends on the real path of the Excel on the users' local space, it may need to be changed based on the users' situation.


