import sqlite3
import csv
import matplotlib.pyplot as plt

conn = sqlite3.connect('sales.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sales (
        sid INTEGER PRIMARY KEY AUTOINCREMENT,
        year INTEGER NOT NULL,
        totalsales REAL NOT NULL
    )
''')

sample_data = [(2021, 10000.0), (2022, 12000.0), (2023, 15000.0), (2022, 11000.0), (2023, 14000.0)]
cursor.executemany('INSERT INTO Sales (year, totalsales) VALUES (?, ?)', sample_data)
conn.commit()

cursor.execute('SELECT * FROM Sales')
data = cursor.fetchall()

with open('sales.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['sid', 'year', 'totalsales'])
    writer.writerows(data)

df = pd.read_csv('sales.csv')
plt.bar(df['year'], df['totalsales'], color='blue')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Sales by Year')
plt.xticks(df['year'])
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('sales_chart.png')
plt.show()

conn.close()
