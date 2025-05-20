# import datetime
# import os

# def log_evento(evento, arquivo="modelo_Log_Acesso.log"):
#     timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#     caminho = os.path.join(os.path.dirname(__file__), arquivo)
#     with open(caminho, "a", encoding="utf-8") as f:
#         f.write(f"{timestamp} {evento}\n")

import datetime
import os

def log_evento(evento, arquivo="modelo_Log_Acesso.csv"):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    caminho = os.path.join(os.getcwd(), arquivo)  # Caminho para a raiz do projeto
    with open(caminho, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {evento}\n")
