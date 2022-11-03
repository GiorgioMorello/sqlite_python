import sqlite3

# Vamos criar uma conexão persistente para salvar os dados mesmo quando sairmos do projeto
conexao = sqlite3.connect('base_dados.db')

# Temos que criar um cursor, ele que vai executar os comandos sql no banco de dados
cursor = conexao.cursor()



"""
# Criar uma tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')


# Inserir um registro na tebela
# Códigos usados pra se previnir contra ataques SQL-injection

1- cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Felipe', 63.3))


2- cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Carlos', 'peso': 63.3}
)

3- cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Giordano', 'peso': 80.5})


conexao.commit() # Vai executar esse comando na base de dados
"""



"""
# Atualizando um item da tabela
cursor.execute('UPDATE clientes SET nome = :nome WHERE id = :id',
               {'nome': 'Carlos', 'id': 2})


# Deletando um item da tabela
cursor.execute('DELETE FROM clientes WHERE id=:id',
               {'id': 2})

conexao.commit()
"""

# Buscando itens dentro da tabela clientes que possuem peso > 50
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 65})

for nome, peso in cursor.fetchall():
    print(nome, peso)







cursor.close()
conexao.close()
