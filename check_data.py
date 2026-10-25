import pandas as pd

meal = pd.read_csv("data/meal_info.csv")
center = pd.read_csv("data/fulfilment_center_info.csv")

print("Categories:")
print(meal["category"].unique())

print("\nCuisines:")
print(meal["cuisine"].unique())

print("\nCenter Types:")
print(center["center_type"].unique())