from google.cloud import bigquery

# criacao cliente do bigquery
client = bigquery.Client()

# definicao nome do dataset e da tabela
dataset_id = 'pipeline-marketing.marketing_dataset'
table_id = f'{dataset_id}.marketing_table'

# criacao do dataset no bigquery caso ainda nao exista
dataset = bigquery.Dataset(dataset_id)
dataset.location = 'US'
client.create_dataset(dataset, exists_ok=True)


# configuracao do trabalho de carregamento de dados
schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("idade", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("ocupacao", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("estado_civil", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("escolaridade", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("inadimplencia", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("deposito_prazo", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("saldo_medio", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("emprestimo_habitacional", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("emprestimo_pessoal", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("meio_contato", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("dia_contato", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("mes_contato", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("duracao_contato", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("quantidade_contato_atual", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("quantidade_dias_contato", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("quantidade_contato_anterior", "INTEGER", mode="REQUIRED"),
    bigquery.SchemaField("resultado", "STRING", mode="REQUIRED"),
]

job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV,
    skip_leading_rows = 1, # ignorar nomes das colunas
    schema = schema
)

try:
    # carregar dados para o bigquery
    with open("data/processed/bank_marketing_dataset_transformed.csv", "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config = job_config) # criacao de tarefa

    # esperar conclusao do trabalho de carregamento dos dados
    job.result()
    print(f'Os dados foram carregados.')

except Exception as e:
    print(f'Não foi possível carregar os dados.\nErro: {e}')
