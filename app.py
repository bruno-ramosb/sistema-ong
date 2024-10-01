import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('ong.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS voluntarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
''')

conn.commit()

def registrar_voluntario():
    nome = entry_nome.get()
    contato = entry_contato.get()
    if nome and contato:
        cursor.execute('INSERT INTO voluntarios (nome, contato) VALUES (?, ?)', (nome, contato))
        conn.commit()
        messagebox.showinfo('Sucesso', 'Voluntário registrado com sucesso!')
        entry_nome.delete(0, tk.END)
        entry_contato.delete(0, tk.END)
    else:
        messagebox.showwarning('Atenção', 'Preencha todos os campos!')

def registrar_doacao():
    item = entry_item.get()
    quantidade = entry_quantidade.get()
    if item and quantidade:
        cursor.execute('INSERT INTO doacoes (item, quantidade) VALUES (?, ?)', (item, quantidade))
        conn.commit()
        messagebox.showinfo('Sucesso', 'Doação registrada com sucesso!')
        entry_item.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
    else:
        messagebox.showwarning('Atenção', 'Preencha todos os campos!')


app = tk.Tk()
app.title('Sistema de Registro - ONG')

label_voluntario = tk.Label(app, text='Registro de Voluntários')
label_voluntario.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

label_nome = tk.Label(app, text='Nome:')
label_nome.grid(row=1, column=0, padx=10, pady=5)
entry_nome = tk.Entry(app)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_contato = tk.Label(app, text='Contato:')
label_contato.grid(row=2, column=0, padx=10, pady=5)
entry_contato = tk.Entry(app)
entry_contato.grid(row=2, column=1, padx=10, pady=5)

btn_registrar_voluntario = tk.Button(app, text='Registrar Voluntário', command=registrar_voluntario)
btn_registrar_voluntario.grid(row=3, column=0, columnspan=2, pady=10)

label_doacao = tk.Label(app, text='Registro de Doações')
label_doacao.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

label_item = tk.Label(app, text='Item:')
label_item.grid(row=5, column=0, padx=10, pady=5)
entry_item = tk.Entry(app)
entry_item.grid(row=5, column=1, padx=10, pady=5)

label_quantidade = tk.Label(app, text='Quantidade:')
label_quantidade.grid(row=6, column=0, padx=10, pady=5)
entry_quantidade = tk.Entry(app)
entry_quantidade.grid(row=6, column=1, padx=10, pady=5)

btn_registrar_doacao = tk.Button(app, text='Registrar Doação', command=registrar_doacao)
btn_registrar_doacao.grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()
