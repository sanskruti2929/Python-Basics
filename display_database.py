import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection details
username = 'root'
password = 'root'
host = 'localhost'
database = 'data_collector'

# Get user input for the new table name
new_table_name = input("Enter the new table name: ")

# Get multiple inputs from the user
college_id = input("Enter College ID: ")
website_link = input("Enter Website Link: ")
email_id = input("Enter Email ID: ")
name = input("Enter Name: ")
country_code = input("Enter Country Code: ")
phone_number = input("Enter Phone Number: ")
position = input("Enter Position: ")

# Create a DataFrame with the user input
user_input_data = {
    'college_id': [college_id],
    'website_link': [website_link],
    'email_id': [email_id],
    'name': [name],
    'country_code': [country_code],
    'phone_number': [phone_number],
    'position': [position]
}

df_user_input = pd.DataFrame(user_input_data)

# Create a SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# Create a new table with an auto-incrementing 'id' column
df_user_input.to_sql(name=new_table_name, con=engine, index=False, if_exists='append')

# Display the DataFrame in the terminal
print("\nUser Input Data:")
print(df_user_input)

# Confirm that the data has been written to the new table
query_new_table = f'SELECT * FROM {new_table_name}'
df_from_new_table = pd.read_sql(query_new_table, con=engine)
print(f"\nData in MySQL - {new_table_name}:")
print(df_from_new_table)
