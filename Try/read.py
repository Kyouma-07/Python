import pandas as pd
open_csv = r"E:\Projects\Data Science Project\dataset\delhiaqi.csv"

data = pd.read_csv(open_csv)
print("\n\n=========================\n\n")
print(data.head())
print("\n\n=========================\n\n")

