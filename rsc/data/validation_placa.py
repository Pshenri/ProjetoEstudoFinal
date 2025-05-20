from sklearn.ensemble import IsolationForest
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import numpy as np
from collect_Logs_Placa import df_acessos,df_modelo
import joblib

# Seleciona apenas as colunas numéricas para o modelo
# colunas_numericas = df_acessos.select_dtypes(include=[np.number]).columns
# X = df_acessos[colunas_numericas]

# Normalização dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_modelo)

# Parâmetros que serão testados
param_grid = {
    'n_estimators': [100, 200],
    'max_samples': ['auto', 0.6, 0.9],
    'contamination': [0.5]
}

melhor_modelo = None
melhor_score = -np.inf
melhores_configs = {}

# Teste de combinações
for n in param_grid['n_estimators']:
    for m in param_grid['max_samples']:
        for c in param_grid['contamination']:
            modelo_temp = IsolationForest(n_estimators=n, max_samples=m, contamination=c, random_state=42)
            modelo_temp.fit(X_scaled)
            scores = modelo_temp.decision_function(X_scaled)
            media_score = scores.mean()  # Média dos scores: mais negativo → mais anomalias
            
            print(f"Testando n={n}, max_samples={m}, contamination={c} | Score médio: {media_score:.4f}")
            
            if media_score > melhor_score:
                melhor_score = media_score
                melhor_modelo = modelo_temp
                melhores_configs = {'n_estimators': n, 'max_samples': m, 'contamination': c}

# Usar o melhor modelo encontrado
df_acessos['anomalia'] = melhor_modelo.predict(X_scaled)

print("\nMelhor configuração encontrada:", melhores_configs)
df_acessos['anomalia'] = df_acessos['anomalia'].map({1: 0, -1: 1})  # 1 = anomalia

# Print para verificação
print("Melhores parâmetros:", melhores_configs)
print("Arquivo 'resultado_anomalias_Placa.csv' salvo com sucesso.")
print(df_acessos['anomalia'].value_counts())

# Adiciona a coluna de scores ao DataFrame
df_acessos['score de anomalia'] = scores

# Salvar resultado em CSV
df_acessos.to_csv('resultado_anomalias_Placa.csv', index=False)

model = IsolationForest(contamination=0.5, random_state=42)
model.fit(X_scaled)

# joblib.dump(model, 'modelo_isolation.pkl')
# joblib.dump(scaler, 'scaler.pkl')