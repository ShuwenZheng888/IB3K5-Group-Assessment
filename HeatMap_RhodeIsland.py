import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Accessories': [1, 1, 1, 3, 2, 1, 1, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    'Clothing': [0, 1, 1, 0, 0, 1, 1, 5, 3, 1, 0, 0, 1, 1, 2, 1, 1, 2, 2, 5, 4, 1, 2],
    'Footwear': [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    'Outerwear': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
}
colors = ['Beige', 'Black', 'Blue', 'Brown', 'Charcoal','Cyan', 'Gold', 'Green', 'Indigo', 'Lavender', 
          'Magenta', 'Maroon', 'Olive', 'Orange', 'Peach', 'Pink', 'Purple', 'Red', 'Silver', 'Teal', 'Turquoise', 
          'Violet', 'Yellow']
df = pd.DataFrame(data, index=colors)

# Draw the heatmap 
plt.figure(figsize=(10, 10))
sns.heatmap(df, annot=True, cmap=sns.cubehelix_palette(as_cmap=True))
plt.title('Heat Map of Product Purchases by Color of Rhode Island')
plt.ylabel('Color')
plt.xlabel('Category')
plt.show()