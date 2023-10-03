import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Prod_Name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'Jan': [1000, 1200, 800, 1500, 900],
    'Feb': [1100, 1300, 850, 1600, 950],
    'Mar': [1050, 1250, 820, 1550, 920],
    'Apr': [1150, 1350, 880, 1650, 990],
    'May': [1200, 1400, 900, 1700, 1020],
    'Jun': [1300, 1500, 950, 1750, 1050]
}

df = pd.DataFrame(data)

df['Total_Sell'] = df.iloc[:, 1:].sum(axis=1)
df['Average_Sell'] = df.iloc[:, 1:].mean(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(df['Prod_Name'], df['Total_Sell'], label='Total Sell', marker='o')
plt.plot(df['Prod_Name'], df['Average_Sell'], label='Average Sell', marker='o')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales Analysis')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig('sales_analysis.png')

df.to_csv('sell_analysis.csv', index=False)

plt.show()
