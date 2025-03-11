import sqlite3
import yr_dop as yrd

connection = sqlite3.connect('admin.db')
cursor = connection.cursor()

f=open('chess/file.csv','r')

# yrd.create_table()

# username = input('username: ')
# yrd.add_username(username)

# email = input('email: ')
# yrd.error_email(email)

# age = input('age: ')
# yrd.error_age(age)

# s = yrd.open_csv()

# yrd.add_all(s)

yrd.request_age_20_40()

# yrd.table_users()