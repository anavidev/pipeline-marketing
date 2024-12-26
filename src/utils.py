import logging

# configuracao do logging
logging.basicConfig(
    filename='data/logs/processamento_dados.log',
    level=logging.INFO,
    format= '%(asctime)s - %(levelname)s \n%(message)s',
)

# verificacao de alteracoes no dataset
def verificar_dataset(nome_verificacao,dataset):
    logging.info(f"""{nome_verificacao}
{dataset.head()}
Quantidade de linhas: {len(dataset.index)}\n""")

# tratamento para valores ausentes por coluna
def valores_ausentes(dataset):
    if dataset.isna().any(axis=1).any():
        logging.info(f'Removendo {dataset.isna().sum()} valores ausentes\n')
        dataset = dataset.dropna()
        logging.info("Valores ausentes removidos\n")
    else:
        logging.info("Nao ha valores ausentes\n")   

    return dataset            

# tratamento para linhas duplicadas
def duplicatas(dataset):
    colunas_duplicatas = ['idade', 'ocupacao', 'estado_civil', 'escolaridade', 'inadimplencia', 'saldo_medio', 'deposito_prazo', 'emprestimo_habitacional', 'emprestimo_pessoal', 'meio_contato']
    
    if dataset.duplicated(subset=colunas_duplicatas).any():
        logging.info(f'Removendo {dataset.duplicated(subset=colunas_duplicatas).sum()} linhas duplicadas\n')
        dataset = dataset.drop_duplicates(subset=colunas_duplicatas, keep='last') # mantem a ultima ocorrencia
        logging.info("Linhas duplicadas removidas\n")
    else:
        logging.info("Nao ha duplicatas\n")

    return dataset

# traducao de valores de colunas com valores booleanos
def traducao_valores_booleanos(dataset,coluna):
    dataset[coluna] = dataset.apply(
    lambda row: 'sim' if row[coluna] == 'yes'
    else 'nao',
    axis = 1
    )

    return dataset
    
# adicao de IDs para cada linha
def adicao_index(dataset):
    dataset = dataset.reset_index()
    dataset = dataset.rename(columns={'index':'id'})
    dataset['id'] += 1

    return dataset             