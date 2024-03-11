import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Accessories': [0, 1, 1, 0, 0, 0, 1, 1, 2, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 2, 1, 2],
    'Clothing': [3, 0, 1, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 1, 0, 1, 1, 1, 1, 0, 3, 3],
    'Footwear': [1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 1, 0, 2, 0, 0, 0, 0, 1, 2],
    'Outerwear': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
}
colors = ['Beige', 'Black', 'Blue', 'Brown', 'Charcoal', 'Cyan', 'Gold', 'Gray', 'Green', 'Indigo', 'Lavender', 
          'Magenta', 'Maroon', 'Olive','Peach', 'Purple', 'Red', 'Silver', 'Teal', 'Turquoise', 
          'Violet', 'White']
df = pd.DataFrame(data, index=colors)

# Draw the heatmap 
plt.figure(figsize=(12, 9))
sns.heatmap(df, annot=True, fmt="d", cmap='Blues') 
plt.title('Heat Map of Product Purchases by Color of Kansas')
plt.ylabel('Color')
plt.xlabel('Category')
plt.show()