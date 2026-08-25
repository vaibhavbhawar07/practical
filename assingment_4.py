import pandas as pd

df = pd.read_csv("data.csv")

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()

print("\nDataset After Removing Duplicates:")
print(df)

age_mean = df["Age"].mean()

salary_mean = df["Salary"].mean()

print("\nMean Age:", age_mean)
print("Mean Salary:", salary_mean)

df["Age"] = df["Age"].fillna(age_mean)
df["Salary"] = df["Salary"].fillna(salary_mean)

print("\nFinal Preprocessed Dataset:")
print(df)
print("\nMissing Values After Preprocessing:")
print(df.isnull().sum())
