import sqlite3

connection = sqlite3.connect('admin.db')
cursor = connection.cursor()


def create_table():
    connection = sqlite3.connect('admin.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Figures (
    username TEXT,
    figures TEXT,
    position TEXT,
    color TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Game (
    username TEXT,
    time_now INTEGER,
    time_lost INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stats (
    username TEXT,
    play_time INTEGER,
    macth_won INTEGER,
    macth_lose INTEGER
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER AUTO_INCREMENT NOT NULL,
    username TEXT,
    email TEXT,
    age INTEGER,
    stats INTEGER,
    temporary INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY (username) REFERENCES Stats(username)
    FOREIGN KEY (username) REFERENCES Figures(username)
    FOREIGN KEY (username) REFERENCES Game(username)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
    )
    ''')
    connection.commit()
    connection.close()
    
def error_username(username):

    if len(username) > 20:
        print('username строчка больше 20 символов')
        return None
    
    elif len(username) < 4:
        print('username меньше 4')
        return None
    
    elif len(username.split()) > 1:
        print('username есть пробелы')
        return None
    
    else:
        print('username подходит')


def error_email(email):

    if len(email.split('@')) == 2:
        email_s = email.split('@')[1]

        if len(email_s.split('.')[0]) > 5:
            print('неподходящий email1')
            return None
        
        else:
            print('подходит email')

    else:
        print('неподходящий email2')
        return None


def error_age(age):

    try:
        age = int(age)
    except ValueError:
        print('age должно быть числом')
        return None
    else:

        if 1>age:
            print('age слишком маленькое')
            return None
        
        elif 120<age:
            print('age слишком большое')
            return None
        
        else:
            print('age подходит')
            return int(age)


def table_users():
    connection = sqlite3.connect('admin.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    filtered_results = cursor.fetchall()

    for row in filtered_results:
        print(row)

    connection.commit()
    connection.close()


def request_age_20_40():

    connection = sqlite3.connect('admin.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users WHERE age BETWEEN 20 and 40')
    filtered_results = cursor.fetchall()

    # q = open('request', 'w')

    print(filtered_results)

    for row in filtered_results:
        # q.write(row)
        print(row)

    connection.commit()
    connection.close()


def open_csv():
    f = open('chess/file.csv','r')
    s = list()

    for i in range(1,1001):
        st = f.readline()
        spl = st.split(';')
        print(spl[3].split('/n'))
        s.append(dict(id = spl[0], username = spl[1], email = spl[2], age = int(spl[3][:-1])))
    print(s)
    return s

def add_all(s):
    connection = sqlite3.connect('admin.db')
    cursor = connection.cursor()

    n = 0

    for n in range(1,1001):
        cursor.execute('INSERT INTO Users(id,username, email, age) VALUES(?, ?, ?, ?)', (s[n].get('id'), s[n].get('username'), s[n].get('email'), s[n].get('age')))
        print('добавлены')
        n += 1
    connection.commit()
    connection.close()

def add_username(username):

    connection = sqlite3.connect('admin.db')
    cursor = connection.cursor()

    if (error_username(username)) != (None):
        cursor.execute('''INSERT INTO Users (id,username) VALUES(?,?)''', (1,username))
    
    else:
        print('ошибка')

    connection.commit()
    connection.close()
