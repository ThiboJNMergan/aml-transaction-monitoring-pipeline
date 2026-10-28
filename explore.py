import duckdb

print(duckdb.sql('''
    SELECT COUNT(*) AS transacties,
           SUM("Is Laundering") AS witwas
    FROM 'data/raw/HI-Small_Trans.csv'
'''))