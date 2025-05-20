import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Leitura bruta do arquivo
with open('modelo_Log_Acesso.csv', 'r') as f:
    linhas = f.readlines()


# Listas para armazenar os registros
dados_acessos = []
dados_sistema = []

# Parse de cada linha
for linha in linhas:
    partes = linha.strip().split('|')
    timestamp = partes[0].strip().strip('[]')
    tipo_evento = partes[1].strip()

    if tipo_evento == "SYSTEM":
        mensagem = partes[2].strip()
        dados_sistema.append({
            "timestamp": timestamp,
            "tipo_evento": tipo_evento,
            "mensagem": mensagem
        })
    elif tipo_evento in ["ACCESS_GRANTED", "ACCESS_DENIED"]:
        categoria = partes[2].strip()
        nome = partes[3].strip()
        documento = partes[4].strip()
        unidade = partes[5].strip()
        status = partes[6].strip()
        obs= partes[7].strip()
        dados_acessos.append({
            "timestamp": timestamp,
            "tipo_evento": tipo_evento,
            "categoria": categoria,
            "nome": nome,
            "cpf": documento,
            "unidade": unidade,
            "status": status,
            "observacao": obs,
        })

# Criação dos DataFrames
df_acessos = pd.DataFrame(dados_acessos)
df_sistema = pd.DataFrame(dados_sistema)

# Conversão de timestamp
df_acessos['timestamp'] = pd.to_datetime(df_acessos['timestamp'])
df_sistema['timestamp'] = pd.to_datetime(df_sistema['timestamp'])

df_acessos['hora'] = df_acessos['timestamp'].dt.hour
df_acessos['minuto'] = df_acessos['timestamp'].dt.minute
df_acessos['dia_da_semana'] = df_acessos['timestamp'].dt.dayofweek

df_encoded = pd.get_dummies(df_acessos[['tipo_evento', 'observacao']])

df_modelo = pd.concat([
    df_acessos[['hora', 'dia_da_semana']],
    df_encoded
], axis=1)


# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(df_modelo)

# modelo = IsolationForest(contamination=0.5, random_state=42)
# modelo.fit(X_scaled)

# # Previsão: -1 = anomalia, 1 = normal
# df_acessos['anomalia'] = modelo.predict(X_scaled)


# # Exibir os primeiros registros
# print(df_acessos)

# print(df_modelo)
