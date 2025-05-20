import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from .banco import inicializar_banco, salvar_no_banco
from .logger import log_evento
import subprocess
import os

def executar_validacao():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    caminho_script = os.path.join(base_dir, "data", "validation.py")
    subprocess.run(["python", caminho_script])

def abrir_painel(usuario_logado):
    inicializar_banco()

    def gerar_log(status, tipo, nome, cpf, apartamento, resultado, autorizado_por):
        log = f"|{status}| {tipo}| {nome}| {cpf}| {apartamento}| {resultado}| {autorizado_por}"
        log_evento(log)

    def autorizar():
        nome = entry_nome.get().strip()
        cpf = entry_cpf.get().strip()
        apartamento = entry_apartamento.get().strip()
        tipo = tipo_var.get()

        if not nome or not cpf or not apartamento or not tipo:
            messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos.")
            return

        gerar_log("ACCESS_GRANTED", tipo, nome, cpf, apartamento, "Autorizado", usuario_logado)
        salvar_no_banco(nome, cpf, apartamento, tipo, "Autorizado", usuario_logado)
        executar_validacao()  # ← CHAMADA AQUI
        messagebox.showinfo("Acesso Liberado", f"Acesso liberado para {nome} ({tipo}). Porta aberta.")
        painel.destroy()

    def negar():
        nome = entry_nome.get().strip() or "Desconhecido"
        cpf = entry_cpf.get().strip() or "Desconhecido"
        apartamento = entry_apartamento.get().strip() or "Desconhecido"
        tipo = tipo_var.get() or "Não informado"

        gerar_log("ACCESS_DENIED", tipo, nome, cpf, apartamento, "Negado", usuario_logado)
        salvar_no_banco(nome, cpf, apartamento, tipo, "Negado", usuario_logado)
        executar_validacao()  # ← CHAMADA AQUI
        messagebox.showwarning("Acesso Negado", "Acesso negado ao visitante.")
        painel.destroy()

    painel = tk.Tk()
    painel.title("Painel de Autorização de Visitantes")
    painel.geometry("400x380")
    painel.resizable(False, False)

    tipo_var = tk.StringVar()

    tk.Label(painel, text=f"Usuário logado: {usuario_logado}", font=("Arial", 10)).pack(pady=5)
    tk.Label(painel, text="Autorização de Entrada", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(painel, text="Nome do Visitante:").pack()
    entry_nome = tk.Entry(painel, width=60)
    entry_nome.pack(pady=5)

    tk.Label(painel, text="CPF do Visitante:").pack()
    entry_cpf = tk.Entry(painel, width=60)
    entry_cpf.pack(pady=5)

    tk.Label(painel, text="Apartamento:").pack()
    entry_apartamento = tk.Entry(painel, width=60)
    entry_apartamento.pack(pady=5)

    tk.Label(painel, text="Tipo de Entrada:").pack(pady=5)
    tipos = [("Visitante", "Visitante"), ("Entregador", "Entregador"), ("Prestador de Serviço", "Prestador de Serviço")]
    for texto, valor in tipos:
        tk.Radiobutton(painel, text=texto, variable=tipo_var, value=valor).pack(anchor="w", padx=100)

    tk.Button(painel, text="Autorizar e Abrir Porta", bg="green", fg="white",
              font=("Arial", 10), command=autorizar, width=25).pack(pady=10)

    tk.Button(painel, text="Negar Acesso", bg="red", fg="white",
              font=("Arial", 10), command=negar, width=25).pack()

    painel.mainloop()
