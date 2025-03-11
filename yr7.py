import random
from datetime import date
from faker import Faker

# Используем библиотеку Faker для генерации случайных данных
fake = Faker()

f=open('file.csv','w')


def generate_random_birthdate():
    # Генерируем дату рождения между 1950 и 2010 годом
    start_date = date(1930, 1, 1)
    end_date = date(2010, 12, 31)
    
    return fake.date_between(start_date=start_date, end_date=end_date).strftime("%d-%m-%Y")

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    username = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_unique_data(n=1000):
    data = []
    
    for i in range(1, n+1):
        record = {
            'id': i,
            'email': generate_random_email(),
            'birthdate': generate_random_birthdate(),
            'age': date.today().year - int(generate_random_birthdate()[-4:]),
            'name': fake.first_name()
        }
        
        data.append(record)
    
    return data

# Генерация данных
unique_data = generate_unique_data()

# Вывод данных в нужном формате
for entry in unique_data:
    f.write(f"{entry['id']};{entry['name']};{entry['email']};{entry['age']}")
    f.write('\n')
f.close()