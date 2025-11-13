
import pandas as pd 
import matplotlib.pyplot as plt 
data ={
    "category": ["Electronics", "Clothing", "Groceries", "Electronics", "Clothing"],
    "sales": [1200,600,500,1500,700]
}

df = pd.DataFrame(data)
print("sales dataframe")
print(df)

total_sale = df.groupby("category")["sales"].sum()
print("\n total sales for category")
print(total_sale)

total_sale.plot(kind='bar')


plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales Amount")
plt.show() 
