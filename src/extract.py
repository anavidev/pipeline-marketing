import pandas as pd

# conversao arquivo csv em dataframe
dt = pd.read_csv("data/bank_marketing_dataset_raw.csv", sep = ',')

print(dt.head())