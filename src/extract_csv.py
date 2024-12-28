import pandas as pd
from utils import verificar_dataset

# conversao arquivo csv em dataframe
dt = pd.read_csv("data/raw/bank_marketing_dataset_raw.csv", sep = ',')

verificar_dataset("Dataset importado com sucesso.",dt)