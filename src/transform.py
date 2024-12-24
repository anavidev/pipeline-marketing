from extract import *

## limpeza, validacao e transformacao dos dados

print(dt.info())
print()

# verificacao de valores ausentes por coluna
if dt.isna().any(axis=1).any():
    print("Há valores ausentes")
    valores_ausentes = dt.isna().sum()
    print(f'Valores ausentes:\n\n{valores_ausentes}\n')
else:
    print("Não há valores ausentes\n")

# verificacao de linhas duplicadas
if dt.duplicated().any():
    print("Há linhas duplicadas")
    linhas_duplicadas = dt.duplicated().sum()
    print(f'Linhas duplicadas:\n\n{linhas_duplicadas}\n')
else:
    print("Não há linhas duplicadas\n")

# mudar coluna de posicao
coluna = dt.pop('deposit')
dt.insert(6,'deposit',coluna)

# adicao de IDs para cada linha
dt = dt.reset_index()
dt['index'] += 1

# mudar valores em segundos para minutos na coluna 'duration'
dt['duration'] = dt.apply(
    lambda row: row['duration'] / 60,
    axis = 1
)
# definicao de visualizacao para numeros com uma casa decimal
pd.options.display.float_format = '{:.0f}'.format 


# traducao de colunas
traducao_colunas = {
    'index': 'id',
    'age': 'idade',
    'job': 'ocupacao',
    'marital': 'estado_civil',
    'education': 'escolaridade',
    'default': 'inadimplencia',
    'deposit': 'deposito_prazo',
    'balance': 'saldo_medio',
    'housing': 'emprestimo_habitacional',
    'loan': 'emprestimo_pessoal',
    'contact': 'meio_contato',
    'day': 'dia_contato',
    'month': 'mes_contato',
    'duration': 'duracao_contato',
    'campaign': 'quantidade_contato',
    'pdays': 'quantidade_dias_contato',
    'previous': 'quantidade_contato',
    'poutcome': 'resultado'
}

dt = dt.rename(traducao_colunas, axis = 1)

# traducao de valores
def traducao_valores_booleanos(coluna):
    dt[coluna] = dt.apply(
    lambda row: 'sim' if row[coluna] == 'yes'
    else 'nao',
    axis = 1
)


dt['ocupacao'] = dt.apply(
    lambda row: 'gestao' if row['ocupacao'] == 'management'
    else 'administracao' if row['ocupacao'] == 'admin.'
    else 'tecnico' if row['ocupacao'] == 'technician'
    else 'servicos' if row['ocupacao'] == 'services'
    else 'operario',
    axis = 1
)

dt['estado_civil'] = dt.apply(
    lambda row: 'casado' if row['estado_civil'] == 'married'
    else 'divorciado' if row['estado_civil'] == 'divorced'
    else 'solteiro',
    axis = 1
)

dt['escolaridade'] = dt.apply(
    lambda row: 'fundamental' if row['escolaridade'] == 'primary'
    else 'medio' if row['escolaridade'] == 'secondary'
    else 'superior',
    axis = 1
)

traducao_valores_booleanos('inadimplencia')
traducao_valores_booleanos('deposito_prazo')
traducao_valores_booleanos('emprestimo_habitacional')
traducao_valores_booleanos('emprestimo_pessoal')

dt['meio_contato'] = dt.apply(
    lambda row: 'celular' if row['meio_contato'] == 'cellular'
    else 'telefone' if row['meio_contato'] == 'telephone'
    else 'desconhecido',
    axis = 1
)

dt['mes_contato'] = dt.apply(
    lambda row: 'janeiro' if row['mes_contato'] == 'jan'
    else 'fevereiro' if row['mes_contato'] == 'feb'
    else 'marco' if row['mes_contato'] == 'mar'
    else 'abril' if row['mes_contato'] == 'apr'
    else 'maio' if row['mes_contato'] == 'may'
    else 'junho' if row['mes_contato'] == 'jun'
    else 'julho' if row['mes_contato'] == 'jul'
    else 'agosto' if row['mes_contato'] == 'aug'
    else 'setembro' if row['mes_contato'] == 'sep'
    else 'outubro' if row['mes_contato'] == 'oct'
    else 'novembro' if row['mes_contato'] == 'nov'
    else 'dezembro',
    axis = 1
)

dt['resultado'] = dt.apply(
    lambda row: 'desconhecido' if row['resultado'] == 'unknown'
    else 'sucesso' if row['resultado'] == 'success'
    else 'fracasso',
    axis = 1
)

dt.to_csv('data/bank_marketing_dataset_transformed.csv', index=False, float_format='%.0f')