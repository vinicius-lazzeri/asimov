import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')
df_data

c = conn.cursor()
#Para criar uma tabela no banco de dados
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()

#Para deletar uma:
c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

#Como enriquecer o banco de dados com tipagem
c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT,[price] INTEGER)')

#Como inserir dados SEM PANDAS

c.execute('''
    INSERT INTO products (product_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Tablet', 300)
''')
conn.commit()

#Inserindo dados COM PANDAS

df_data2 = df_data.iloc[::-2]
df_data2.to_sql('data', conn, if_exists='append')

#SELECT
# * = seleciona tudo
c.execute('SELECT * FROM data')

#aqui ele vai pegar o resultado da query acima e exibir apenas a primeira execução
c.fetchone()

#neste caso, exibiria uma lista de tuplas com todas as execuções
c.fetchall()

#Não é uma boa prática!
df = pd.DataFrame(c.fetchall())

c.execute('SELECT * FROM data WHERE A > 200')
df = pd.DataFrame(c.fetchall())

c.execute('SELECT * FROM data WHERE A > 200 AND B > 100')
df = pd.DataFrame(c.fetchall())

c.execute('SELECT A, B, C FROM data WHERE A > 200 AND B > 100')
df = pd.DataFrame(c.fetchall())

#Com Pandas

query = "SELECT * FROM data"
df = pd.read_sql(query, con=conn, index_col= 'index_name')
query2 = "SELECT A, B, C FROM data WHERE A > 200 AND B > 100"
df = pd.read_sql(query2, con=conn)

#UPDATE e DELETE no SQL

c.execute("UPDATE data SET A=218 WHERE index_name = 'b'")
conn.commit()

c.execute("UPDATE data SET A=220, B=228 WHERE index_name = 'b'")
conn.commit()

c.execute("DELETE FROM data WHERE index_name = 1")
conn.commit()