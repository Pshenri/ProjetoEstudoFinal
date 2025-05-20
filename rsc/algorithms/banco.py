import sqlite3

def inicializar_banco():
    conn = sqlite3.connect("acessos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros_acesso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            apartamento TEXT,
            tipo TEXT,
            status TEXT,
            autorizado_por TEXT,
            data_hora TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def salvar_no_banco(nome, cpf, apartamento, tipo, status, autorizado_por):
    conn = sqlite3.connect("acessos.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO registros_acesso (nome, cpf, apartamento, tipo, status, autorizado_por)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cpf, apartamento, tipo, status, autorizado_por))
    conn.commit()
    conn.close()
