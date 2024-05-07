import sqlite3

conexao = sqlite3.connect('exercício_banco_de_dados')
cursor = conexao.cursor()

### 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

### 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Andresa Wendt", 26, "Relações Internacionais")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Tábata Menezes", 23, "Economia")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Talita Castro", 27, "Física")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Vinícius Reis", 20, "Engenharia Mecatrônica")')
#cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Carlos Santiago", 25, "Sistemas de Informação")')

### 3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
    #print (alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
#for alunos in dados:
    #print (alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia Mecatrônica" ORDER BY nome')
#for alunos in dados:
    #print (alunos)

#d) Contar o número total de alunos na tabela.
#dados = cursor.execute ('SELECT COUNT (nome) FROM alunos')
#for alunos in dados:
    #print (alunos)

### 4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade = 37 WHERE id = 3')

#b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id = 1')

### 5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
#cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')

#Insira alguns registros de clientes na tabela.
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Cátia Macedo", 30, 2000.53)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Pablo Neruda", 45, 1997.64)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Amado Batista", 51, 15325.10)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Carmem Miranda", 42, 65218.67)')

### 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
#for clientes in dados:
    #print(clientes)

#b) Calcule o saldo médio dos clientes.
#dados = cursor.execute('SELECT AVG (saldo) FROM clientes')
#for clientes in dados:
    #print(clientes)

#c) Encontre o cliente com o saldo máximo.
#dados = cursor.execute('SELECT nome FROM clientes ORDER BY saldo DESC LIMIT 1')
#for clientes in dados:
    #print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000
#dados = cursor.execute('SELECT COUNT (nome) FROM clientes WHERE saldo > 1000')
#for clientes in dados:
    #print(clientes)

### 7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = 3000.53 WHERE nome = "Cátia Macedo"')

#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id = 3')

### 8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

#Insira algumas compras associadas a clientes existentes na tabela "clientes".
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 2, "geladeira", 3599.99)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 2, "fogão", 489.90)')
#cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 1, "máquina de lavar", 999.80)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
#dados = cursor.execute('SELECT nome, produto, valor FROM compras INNER JOIN clientes on compras.cliente_id = clientes.id')
#for clientes in dados:
    #print(clientes)
