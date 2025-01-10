import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = pd.DataFrame({
    'Height': np.random.normal(170, 10, 1000),
    'Weight': np.random.normal(70, 5, 1000),
    'Age': np.random.normal(30, 5, 1000)
})

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.hist(data['Height'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Height')
plt.xlabel('Height')
plt.ylabel('Frequency')


plt.subplot(2, 2, 2)
sns.kdeplot(data['Weight'], shade=True, color='orange')
plt.title('Density Plot of Weight')
plt.xlabel('Weight')
plt.ylabel('Density')


plt.subplot(2, 2, 3)
plt.scatter(data['Height'], data['Weight'], alpha=0.5, color='green')
plt.title('Scatter Plot of Height vs. Weight')
plt.xlabel('Height')
plt.ylabel('Weight')

plt.subplot(2, 2, 4)
sns.pairplot(data[['Height', 'Weight', 'Age']], height=2)
plt.suptitle('Pair Plot of Height, Weight, and Age', y=1.02)

plt.tight_layout()
plt.show()