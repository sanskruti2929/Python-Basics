import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = 'root'
host = 'localhost'
database = 'testcase'
table_name = 'colleges'

#Path/URL of my Excel file
excel_file_path = 'D:\Pandas\Pune_Engineering_Colleges.xlsx'

# Read the Excel sheet into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Create a SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# Display the DataFrame
print("Excel Data:")
print(df)

# Display the DataFrame in MySQL
df.to_sql(name=table_name, con=engine, index=False, if_exists='replace')

# Confirm that the data has been written to the MySQL table
query = f'SELECT * FROM {table_name}'
df_from_mysql = pd.read_sql(query, con=engine)
print("\nData in MySQL:")
print(df_from_mysql)





