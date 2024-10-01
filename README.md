# Sistema de Gestão para ONGs

Este projeto consiste em um sistema desenvolvido em Python para auxiliar ONGs no registro de voluntários e no gerenciamento de doações. A aplicação visa automatizar processos anteriormente realizados manualmente, aumentando a eficiência e precisão no controle das informações.

## Funcionalidades

- **Registro de Voluntários:**
  - Cadastro de novos voluntários com nome e contato.
  - Armazenamento seguro das informações em um banco de dados SQLite.

- **Registro de Doações:**
  - Cadastro de doações recebidas, especificando o item e a quantidade.
  - Armazenamento das doações no banco de dados para fácil acesso e gestão.

- **Interface Gráfica Amigável:**
  - Utilização da biblioteca Tkinter para proporcionar uma interface intuitiva.
  - Fácil navegação entre as funcionalidades de registro.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação principal.
- Bibliotecas Python:
  - `tkinter` (já incluída na instalação padrão do Python).
  - `sqlite3` (também incluída por padrão).
  
## Como Rodar o Projeto

1. Clone o repositório:
```shell
   git clone https://github.com/bruno-ramosb/sistema-ong.git
   cd sistema-ong
```

2. Execute a aplicação:
```shell
python app.py
```