import tkinter as tk
from tkinter import messagebox
from .logger import log_evento
from .autorizacao import abrir_painel

usuarios = {
    "admin": "admin123",
    "morador": "1234",
    "maria": "123456",
}

def iniciar_login():
    def autenticar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        if usuario in usuarios and usuarios[usuario] == senha:
            log_evento(f"| SYSTEM         | Usuário: {usuario} logou no sistema")
            messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
            janela.destroy()
            abrir_painel(usuario)
        else:
            log_evento(f"| SYSTEM         | Tentativa com usuário: {usuario} invalido")
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def sair():
        log_evento("| SYSTEM         | Tela de saida pelo usuário")
        janela.destroy()

    log_evento("| SYSTEM         | Tela de login carregada")

    janela = tk.Tk()
    janela.title("Tela de Login")
    janela.geometry("400x280")
    janela.resizable(False, False)

    tk.Label(janela, text="Usuário:").pack(pady=7)
    entry_usuario = tk.Entry(janela)
    entry_usuario.pack()

    tk.Label(janela, text="Senha:").pack(pady=7)
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    tk.Button(janela, text="Login", width=12, command=autenticar).pack(pady=10)
    tk.Button(janela, text="Sair", width=12, command=sair).pack()

    janela.mainloop()
