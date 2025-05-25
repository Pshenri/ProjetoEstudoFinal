import pandas as pd
import numpy as np

# df = pd.read_csv('resultado_anomalias.csv', 'resultado_anomalias_Placas.csv', 'resultados_anomalias_Facial.csv')
# anomalias_detectadas = df[df['anomalia'] == 1]

# print("\n---")
# print("Todas as linhas onde 'anomalia' é igual a 1:")
# print(anomalias_detectadas)

arquivos_csv = ['resultado_anomalias.csv', 'resultado_anomalias_Placa.csv', 'resultado_anomalias_Facial.csv']
lista_de_dfs = []

for arquivo in arquivos_csv:
    try:
        df_temp = pd.read_csv(arquivo)
        lista_de_dfs.append(df_temp)
    except FileNotFoundError:
        print(f"Aviso: O arquivo '{arquivo}' não foi encontrado. Ele será ignorado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{arquivo}': {e}")

if not lista_de_dfs:
    print("Nenhum arquivo CSV foi carregado com sucesso. Verifique os nomes dos arquivos e seus caminhos.")
else:
    df_combinado = pd.concat(lista_de_dfs, ignore_index=True)

    df_combinado['anomalia'] = pd.to_numeric(df_combinado['anomalia'], errors='coerce')
    df_combinado['anomalia'] = df_combinado['anomalia'].fillna(0).astype(int)

    anomalias_detectadas = df_combinado[df_combinado['anomalia'] == 1]

    print("\n---")
    print("Todas as linhas onde 'anomalia' é igual a 1 no DataFrame combinado:")
    print(anomalias_detectadas)

    df_suspeitos = df_combinado.sort_values(by='score de anomalia').head(10)
    print(df_suspeitos)

    df_combinado[df_combinado['anomalia'] == 1] \
    .sort_values(by='score de anomalia') \
    .to_csv('anomalias_detectadas.csv', index=False)