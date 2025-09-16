import pandas as pd

df = pd.read_csv("sample_patients.csv")
print("Data Loaded:")
print(df.head())

# Basic cleaning (drop rows with nulls)
df = df.dropna()

print("\nCleaned Data:")
print(df)

print("\nSummary:")
print("Average Age:", df['Age'].mean())
print("\nGender Distribution:")
print(df['Gender'].value_counts())
