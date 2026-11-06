import duckdb


print(duckdb.sql('''
    SELECT COUNT(*) FROM 'data/processed/validation.parquet'
'''))