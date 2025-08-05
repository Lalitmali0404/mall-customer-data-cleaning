
import pandas as pd

# Load Dataset
df = pd.read_csv("C:\Users\Admin\Downloads\Mall_Customers.csv")

# Step 1: Standardize Column Names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Step 2: Standardize Text Values
df['gender'] = df['gender'].str.strip().str.capitalize()

# Step 3: Handle Missing Values
df['age'].fillna(df['age'].median(), inplace=True)
df['annual_income_(k$)'].fillna(method='ffill', inplace=True)
df['spending_score_(1-100)'].fillna(df['spending_score_(1-100)'].mean(), inplace=True)

# Step 4: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 5: Check and Fix Data Types
df['age'] = df['age'].astype(int)
df['annual_income_(k$)'] = df['annual_income_(k$)'].astype(int)
df['spending_score_(1-100)'] = df['spending_score_(1-100)'].astype(float)

# Step 6: Feature Engineering
df['income_per_age'] = df['annual_income_(k$)'] / df['age']
df['high_spender'] = df['spending_score_(1-100)'] > 50

# Step 7: Save Cleaned Dataset
df.to_csv("cleaned_data/cleaned_mall_customers.csv", index=False)

# Step 8: Display Summary
print(" Data cleaning complete. Cleaned data saved to 'cleaned_data/cleaned_mall_customers.csv'")
print(f" Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")
print(f" Columns: {list(df.columns)}")
