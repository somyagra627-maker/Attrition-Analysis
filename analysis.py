import pandas as pd

df = pd.read_csv("Palo Alto Networks.csv")

print("\n========== BASIC INFO ==========")
print("Shape:", df.shape)

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== ATTRITION RATE ==========")
print("Attrition %:", round(df["Attrition"].mean()*100,2))

print("\n========== DEPARTMENT ==========")
print(df.groupby("Department")["Attrition"].mean()*100)

print("\n========== OVERTIME ==========")
print(df.groupby("OverTime")["Attrition"].mean()*100)