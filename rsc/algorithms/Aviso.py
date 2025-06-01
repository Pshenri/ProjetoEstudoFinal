import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os

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
    output_dir = "relatorio_output"
    os.makedirs(output_dir, exist_ok=True)

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
    graf1 = os.path.join(output_dir, 'acessos_por_categoria.png')
    plt.savefig(graf1)
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
    graf2 = os.path.join(output_dir,'acessos_por_unidade.png')
    plt.savefig(graf2)
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
    graf3 = os.path.join(output_dir,'acessos_por_dia.png')
    plt.savefig(graf3)
    plt.show()

    # -----------------------------
    # 5. Acessos por Hora do Dia
    # -----------------------------
    plt.figure()
    sns.histplot(data=df, x='hora', bins=24, discrete=True)
    plt.title('Distribuição de Acessos por Hora do Dia')
    plt.tight_layout()
    graf4 = os.path.join(output_dir,'acessos_por_hora.png')
    plt.savefig(graf4)
    plt.show()

    # -----------------------------
    # 6. Status dos Acessos
    # -----------------------------
    plt.figure()
    sns.countplot(data=df, x='status', order=df['status'].value_counts().index)
    plt.title('Distribuição por Status do Acesso')
    plt.xticks(rotation=0)
    plt.tight_layout()
    graf5 = os.path.join(output_dir,'status_acessos.png')
    plt.savefig(graf5)
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
    graf6 = os.path.join(output_dir,'motivos_recusa.png')
    plt.savefig(graf6)
    plt.show()

    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 14)
            self.cell(0, 10, "Relatório Operacional e de Acesso", ln=True, align="C")
            self.ln(5)

        def add_image_title(self, title, image_path):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, title, ln=True)
            self.image(image_path, w=180)
            self.ln(10)

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Texto de resumo
    total = len(df)
    autorizados = len(df[df['status'] == 'Autorizado'])
    negados = len(df[df['status'] != 'Autorizado'])
    percentual_negados = (negados / total) * 100

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10,
        f"Total de registros: {total}\n"
        f"Acessos autorizados: {autorizados}\n"
        f"Acessos negados: {negados} ({percentual_negados:.2f}%)\n"
    )

    # Adiciona gráficos
    pdf.add_image_title("Acessos por Categoria", graf1)
    pdf.add_image_title("Top 10 Unidades com Mais Acessos", graf2)
    pdf.add_image_title("Acessos por Dia da Semana", graf3)
    pdf.add_image_title("Distribuição por Hora", graf4)
    pdf.add_image_title("Status dos Acessos", graf5)
    pdf.add_image_title("Principais Motivos de Recusa", graf6)

    # Salvar PDF
    pdf_path = os.path.join(output_dir, "relatorio_acessos.pdf")
    pdf.output(pdf_path)
