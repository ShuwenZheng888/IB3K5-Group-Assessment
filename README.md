
# Instruction of this file
This github file is used as a code reference for the IB3K5 group assessment (group 30) data analysis and data visualization. It consisits of two parts: python code for each part of data analysis result and a jupyter notebbok file for all the code included.


## Python files
There are six Python files included:
1. Top_Three_Locations.py
This code is used to find the of the top three locations' **Purchase Amount** affected most by **Color** and write all the result into a *correlation_{location}.txt* file.
2. Location_Category_Data.py
This code writes the output of the pearson coefficient of all **Color** on **Purchase Amount**, in each specific category within each location. The result is stored in a *correlation_{Category}_{location}.txt* file and the data is used to give insight later.
3. Highest_Count.py
This code finds the colour which has the most occurrence in each specific category within the top three locations.
The result is printed by the code and will be used for the final anlysis.
4. HeatMap_Arizona.py
This code is the visualization code to draw the heat map of Arizona.
5. HeatMap_Kansas.py
This code is the visualization code to draw the heat map of Kansas.
6. HeatMap_RhodeIsland.py
This code is the visualization code to draw the heat map of Rhode Island.


## Jupyter Notebook file
Combination_Final.ipynb
This jupyter notebook code contains all the python code in one file which is easier to read and compare.

## Cautions
The data we anlysis is *CustomerShoppingTrends.xlsx*.
In the python file *Top_Three_Locations.py*, *Location_Category_Data.py* and *Highest_Count.py*

The code used is :
`data = pd.read_excel('/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx')`

However, '/Users/mac/Desktop/IB3K5/CustomerShoppingTrends.xlsx' is custom path depends on the real path of the excel on the users' local space, it may need to be changed based on users' situation.


