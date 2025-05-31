# 🚀 Pipeline de Logs Inteligente para Análise de Acessos em Sistema de Portaria Virtual com Foco em Modelo Preditivo de Comportamento Utilizando Isolation Forest

Melhorar a análise de logs de sistemas de portaria virtual, utilizando técnicas de aprendizado de máquina para identificar padrões de acesso e comportamentos suspeitos.
A utilização do algoritmo Isolation Forest permite identificar anomalias no fluxo de acessos.
Este estudo se torna relevante ao propor um pipeline de logs inteligente que automatiza a análise e melhora a capacidade preditiva dos sistemas de controle de acesso.

---

## 🎯 Objetivo

O projeto tem como principal objetivo desenvolver um pipeline inteligente de análise de logs para sistemas de portaria virtual, com foco na identificação de comportamentos anômalos e padrões de acesso incomuns. Para isso, será utilizado o algoritmo Isolation Forest, uma técnica de aprendizado de máquina voltada para detecção de anomalias.
Objetivos específicos:
Automatizar a coleta, limpeza e armazenamento de logs
Analisar os padrões de acesso
Aplicar o modelo Isolation Forest
Gerar relatórios automáticos
Fornecer visualizações gráficas

---

## 👨‍💻 Tecnologias Utilizadas

- Python 3.13
- scikit-learn / IsolationForest
- pandas / numpy
- matplotlib / seaborn

---

## 🗂️ Estrutura do Projeto

Caso o projeto tenha uma estrutura de pastas significativa, insira aqui um diagrama com os diretórios principais:

A estrutura a seguir é um exemplo. Vocês devem usar a estrutura do seu projeto obrigatóriamente. 
```
📦 ProjetoEstudoFinal
├── 📁 src
│   ├── algorithms/
│   ├── data/
|   |   ├── validation_facial.py
|   |   ├── validation_placa.py
|   |   ├── validation.py
│   ├── testes/
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

1. Clone o repositório:

```
git clone [https://github.com/Pshenri/ProjetoEstudoFinal.git]
cd ProjetoEstudoFinal
```

2. Crie o ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute a aplicação:

```
python main.py

python validation.py

python validation_placa.py

python validation_facial.py
```

---

## 📸 Demonstrações

Inclua aqui prints, gifs ou vídeos mostrando a interface ou o funcionamento do sistema:

- Tela inicial(Exemplo de interface para gera logs)
- ![image](https://github.com/user-attachments/assets/ef00778a-26bb-4b03-8d96-eae7e11d080b)

- Exemplo de funcionalidade(codigo escolhendo melhor parametro para o modelo e mostrando numeros de anomalias encontrados: 0 - normal, 1 - Anomalia)
- ![image](https://github.com/user-attachments/assets/1e9fa6ec-2d30-4cf2-8220-cb5eadc23295)

- Visualização de Anomalias, pontos vermelhos representa anomalias pontos azuis normal)
- ![image](https://github.com/user-attachments/assets/643158ed-804c-461d-937c-a140aa0373cc)

- Exemplo de geração de relatórios
- ![image](https://github.com/user-attachments/assets/cee24e9c-3645-4439-8ea4-ebd796d2c20f)

- Exemplos de alertas gerados os 10 ultimas deteçao de anomalias
- ![image](https://github.com/user-attachments/assets/08a844a9-aa39-482e-8810-2480d05a4476)

- Resultados esperados

---

## 👥 Equipe

| Nome | GitHub |
|------|--------|
| Pedro henrique | [@Pshenri](https://github.com/Pshenri) |
| HENRY KAUÃ | [@Henry](https://github.com/henry) |

---

## 🧠 Disciplinas Envolvidas

- Estrutura de Dados I
- Linguagens Formais e Autômatos

---

## 🏫 Informações Acadêmicas

- Universidade: **Universidade Braz Cubas**
- Curso: **Ciência da Computação / Análise e Desenvolvimento de Sistemas**
- Semestre: 7º
- Período: Noite
- Professora orientadora: **Dra. Andréa Ono Sakai**
- Evento: **Mostra de Tecnologia 1º Semestre de 2025**
- Local: Laboratório 12
- Datas: 05 e 06 de junho de 2025

---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.
