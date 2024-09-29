import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#criada a conexão com o banco
conexao = sqlite3.connect('dados_venda.db')

#criado cursor 
cursor = conexao.cursor()

#criando a tabela vendas1 se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 ( 
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')

#executando a inserção de múltiplos valores na tabela
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00),
('2024-09-26', 'Produto Qualquer', 'Eletrônico', 500.00)
''')


conexao.commit()

#salvei a reposta da consulta da query
df = pd.read_sql_query('SELECT * FROM vendas1', conexao)

#fiz um agrupamento por categoria realizando a soma do valor pra cada categoria
agrupado = df.groupby('categoria')['valor_venda'].sum()

print(agrupado)

#remoção de toda coluna categoria
X = df.drop(['categoria'], axis=1)

Y = df.categoria

sns.barplot(x='categoria', y='valor_venda',  hue='categoria', estimator=sum , data=df)
plt.title('Relação entre Vendas e Categoria')
plt.xlabel('Categoria')
plt.ylabel('Valor de venda')
plt.show()