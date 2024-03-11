import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Accessories': [1, 0, 1, 0, 0, 0, 1, 3, 1, 1, 1, 0, 3, 1, 1, 0, 0, 2, 1, 0, 1, 0, 2],
    'Clothing': [2, 2, 0, 2, 1, 4, 0, 0, 0, 1, 0, 3, 0, 0, 2, 2, 4, 2, 2, 1, 0, 1, 3],
    'Footwear': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    'Outerwear': [0, 0, 1, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
}
colors = ['Beige', 'Black', 'Blue', 'Brown', 'Cyan', 'Gold', 'Gray', 'Green', 'Indigo', 'Lavender', 
          'Magenta', 'Maroon', 'Olive', 'Orange', 'Peach', 'Pink', 'Purple', 'Silver', 'Teal', 'Turquoise', 
          'Violet', 'White', 'Yellow']
df = pd.DataFrame(data, index=colors)

# Draw the heatmap 
plt.figure(figsize=(10, 10))
sns.heatmap(df, annot=True, cmap=sns.cubehelix_palette(as_cmap=True))
plt.title('Heat Map of Product Purchases by Color of Arizona')
plt.ylabel('Color')
plt.xlabel('Category')
plt.show()