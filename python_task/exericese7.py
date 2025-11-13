import pandas as pd
data = {
    "Name": ["John", "Sara", "Mike", "Emma", "David"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 70000, 90000, 60000, 120000]
}

df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)
threshold = df["Salary"].quantile(0.75)
print("\n75th Percentile Salary:", threshold)
filtered_df = df[df["Salary"] > threshold]
print("\nEmployees with salary above 75th percentile:")
print(filtered_df)
