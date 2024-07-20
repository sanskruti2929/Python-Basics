import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection details
username = 'root'
password = 'root'
host = 'localhost'
database = 'your_database'
table_name = 'india_state_organization'

# Path/URL of my Excel file
excel_file_path = 'C:\\Users\\Sanskruti\\Downloads\\Pune_Engineering_Colleges.xlsx'

# Read the Excel sheet into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Length of DataFrame
row_count=len(df)

# DataFrame 2 for City
df2=pd.DataFrame({'city':['Pune']*row_count})

# DataFrame 3 for College ID
df3=pd.DataFrame({'college_id':range(1, row_count + 1)})

# Concatenate df & df2 dataframes
return_df=pd.concat([df3,df,df2],axis=1)
print(return_df.head())
print(return_df.info())

# print(df2.head())

# Create a SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# Display the DataFrame
print("Excel Data:")
print(df.head())

# Ensure column order in return_df matches the table structure
return_df = return_df[['college_id', 'college_name', 'city']]

# Write the DataFrame to the MySQL table
return_df.to_sql(name=table_name, con=engine, index=False, if_exists='replace')

# Confirm that the data has been written to the MySQL table
query = f'SELECT * FROM {table_name}'
df_from_mysql = pd.read_sql(query, con=engine)
print("\nData in MySQL:")
print(df_from_mysql)








