from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

try:
    # consulta SQL
    query = "SELECT * FROM `pipeline-marketing.marketing_dataset.marketing_table`"
    df = client.query(query).to_dataframe()  # extrair dados armazenados no BigQuery

    # salvar como excel
    df.to_excel("data/processed/exported_data_bigquery.xlsx", index=False)
    print(f'Os dados foram extraídos com sucesso.')

except Exception as e:
    print(f'Não foi possível extrair os dados.\nErro: {e}')
