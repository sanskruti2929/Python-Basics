import pandas as pd

# Get input data from the user
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

# Display the DataFrame in the terminal
print("\nUser Input Data:")
print(df_user_input)


