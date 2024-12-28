from extract_csv import *
from utils import *

## limpeza, validacao e transformacao dos dados

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
    'campaign': 'quantidade_contato_atual',
    'pdays': 'quantidade_dias_contato',
    'previous': 'quantidade_contato_anterior',
    'poutcome': 'resultado'
}
dt = dt.rename(traducao_colunas, axis = 1)

# validacao e limpeza dos dados
dt = valores_ausentes(dt)
dt = duplicatas(dt)

# mudar coluna de posicao
mudar_coluna(dt,'deposito_prazo',5)

# mudar valores em segundos para minutos na coluna 'duracao_contato'
dt['duracao_contato'] = dt.apply(
    lambda row: row['duracao_contato'] / 60,
    axis = 1
)
# definicao de visualizacao para numeros com uma casa decimal
pd.options.display.float_format = '{:.0f}'.format

# traducao de valores
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

dt = traducao_valores_booleanos(dt,'inadimplencia')
dt = traducao_valores_booleanos(dt,'deposito_prazo')
dt = traducao_valores_booleanos(dt,'emprestimo_habitacional')
dt = traducao_valores_booleanos(dt,'emprestimo_pessoal')

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

dt.to_csv('data/processed/bank_marketing_dataset_transformed.csv', index=False, float_format='%.0f')


# verificacao final de tratamento de dados
arquivo_csv = pd.read_csv('data/processed/bank_marketing_dataset_transformed.csv', sep=',')
arquivo_csv = valores_ausentes(arquivo_csv)
arquivo_csv = duplicatas(arquivo_csv)
arquivo_csv = adicao_index(arquivo_csv)
verificar_dataset("Verificacao final.",arquivo_csv)

arquivo_csv.to_csv('data/processed/bank_marketing_dataset_transformed.csv', index=False, float_format='%.0f')

print("Transformação concluída.")