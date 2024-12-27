import logging

# configuracao do logging
logging.basicConfig(
    filename='data/logs/processamento_dados.log',
    level=logging.INFO,
    format= '%(asctime)s - %(levelname)s \n%(message)s',
)

# verificacao de alteracoes no dataset
def verificar_dataset(mensagem,dataset):
    logging.info(f"""{mensagem}
Quantidade de linhas: {dataset.shape[0]}
Quantidade de colunas: {dataset.shape[1]}\n""")

# tratamento para valores ausentes por coluna
def valores_ausentes(dataset):
    logging.info("Verificacao de valores ausentes.\n")
    if dataset.isna().any(axis=1).any():
        logging.info(f'Removendo {dataset.isna().sum()} valores ausentes.\n')
        dataset = dataset.dropna()
        logging.info(f"Valores ausentes removidos. Total de linhas apos remocao: {dataset.shape[0]}\n")
    else:
        logging.info("Nao ha valores ausentes.\n")   

    return dataset            

# tratamento para linhas duplicadas
def duplicatas(dataset):
    colunas_duplicatas = ['idade', 'ocupacao', 'estado_civil', 'escolaridade', 'inadimplencia', 'saldo_medio', 'deposito_prazo', 'emprestimo_habitacional', 'emprestimo_pessoal', 'meio_contato']
    
    logging.info("Verificacao de linhas duplicadas.\n")
    if dataset.duplicated(subset=colunas_duplicatas).any():
        logging.info(f'Removendo {dataset.duplicated(subset=colunas_duplicatas).sum()} linhas duplicadas.\n')
        dataset = dataset.drop_duplicates(subset=colunas_duplicatas, keep='last') # mantem a ultima ocorrencia
        logging.info(f"Linhas duplicadas removidas. Total de linhas apos remocao: {dataset.shape[0]}.\n")
    else:
        logging.info("Nao ha duplicatas.\n")

    return dataset

# mudar posicao de coluna
def mudar_coluna(dataset,nome_coluna,posicao_final):
    coluna = dataset.pop(nome_coluna)
    dataset.insert(posicao_final,nome_coluna,coluna)
    logging.info(f'Coluna {nome_coluna} foi movida para a posicao {posicao_final} no dataset.\n')

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
    logging.info(f"A coluna 'id' foi criada para identificacao unica de registros.\n")

    return dataset             