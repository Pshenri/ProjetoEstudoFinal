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

    # Configuração visual
    sns.set(style='whitegrid')
    plt.rcParams['figure.figsize'] = (10, 6)

    # Carregar os dados
    df = pd.read_csv('anomalias_detectadas.csv')

    # -----------------------------
    # 1. Resumo Geral
    # -----------------------------
    total = len(df)
    autorizados = df[df['status'] == 'Autorizado']
    negados = df[df['status'] != 'Autorizado']

    print("Resumo Geral:")
    print(f"Total de registros: {total}")
    print(f"Acessos Autorizados: {len(autorizados)}")
    print(f"Acessos Negados: {len(negados)}")
    print(f"Porcentagem de acessos negados: {len(negados) / total:.2%}")

    # -----------------------------
    # 2. Acessos por Categoria
    # -----------------------------
    plt.figure()
    sns.countplot(data=df, x='categoria', order=df['categoria'].value_counts().index)
    plt.title('Acessos por Categoria')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('acessos_por_categoria.png')
    plt.show()

    # -----------------------------
    # 3. Acessos por Unidade
    # -----------------------------
    top_unidades = df['unidade'].value_counts().head(10)
    plt.figure()
    top_unidades.plot(kind='bar')
    plt.title('Top 10 Unidades com Mais Acessos')
    plt.xlabel('Unidade')
    plt.ylabel('Quantidade de Acessos')
    plt.tight_layout()
    plt.savefig('acessos_por_unidade.png')
    plt.show()

    # -----------------------------
    # 4. Acessos por Dia da Semana
    # -----------------------------
    dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
    df['dia_label'] = df['dia_da_semana'].map({i: dia for i, dia in enumerate(dias)})

    plt.figure()
    sns.countplot(data=df, x='dia_label', order=dias)
    plt.title('Acessos por Dia da Semana')
    plt.tight_layout()
    plt.savefig('acessos_por_dia.png')
    plt.show()

    # -----------------------------
    # 5. Acessos por Hora do Dia
    # -----------------------------
    plt.figure()
    sns.histplot(data=df, x='hora', bins=24, discrete=True)
    plt.title('Distribuição de Acessos por Hora do Dia')
    plt.tight_layout()
    plt.savefig('acessos_por_hora.png')
    plt.show()

    # -----------------------------
    # 6. Status dos Acessos
    # -----------------------------
    plt.figure()
    sns.countplot(data=df, x='status', order=df['status'].value_counts().index)
    plt.title('Distribuição por Status do Acesso')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('status_acessos.png')
    plt.show()

    # -----------------------------
    # 7. Motivos de Recusa
    # -----------------------------
    motivos = df[df['status'] != 'Autorizado']['observacao'].value_counts()

    plt.figure()
    motivos.head(10).plot(kind='barh')
    plt.title('Principais Motivos de Recusa')
    plt.xlabel('Quantidade')
    plt.tight_layout()
    plt.savefig('motivos_recusa.png')
    plt.show()
