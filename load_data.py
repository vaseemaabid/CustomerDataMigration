import pandas as pd

df = pd.read_csv("customer_data.csv")

df = df.drop_duplicates()
df = df.dropna()

print("Data Ready for Loading")

print(df)

print("\nData Successfully Loaded into Target System")
