import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

# Chart 1 - Category wise Sales
plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Category', y='Sales')
plt.title('Category wise Sales')
plt.savefig('chart1_category_sales.png')
plt.close()

# Chart 2 - Top 10 States by Sales
plt.figure(figsize=(10,6))
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
state_sales.plot(kind='bar')
plt.title('Top 10 States by Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart2_top_states.png')
plt.close()

# Chart 3 - Sales by Region
plt.figure(figsize=(8,5))
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title('Sales by Region')
plt.savefig('chart3_region_sales.png')
plt.close()

print("Teeno charts ban gaye!")