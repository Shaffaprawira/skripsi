import csv
import random
import datetime

# Function to generate a random IP address starting with "10.x.x.x"
def generate_random_ip():
    return f"10.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Function to generate a random date/time string within the specified range
def generate_random_datetime():
    start_date = datetime.datetime(2017, 11, 1)
    end_date = datetime.datetime(2018, 3, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("[%d/%b/%Y:%H:%M:%S")

# Function to generate a random file path
def generate_random_filepath():
    directories = ['home', 'user', 'data', 'files', 'docs']
    return '/' + '/'.join(random.choices(directories, k=random.randint(1, 4))) + '/'

# Function to generate the dataset
def generate_dataset(num_records):
    with open('sql_injection_dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'Time', 'URL', 'Status'])

        for _ in range(num_records):
            ip = generate_random_ip()
            time = generate_random_datetime()
            filepath = generate_random_filepath()
            sql_injection = random.choice(['SELECT', 'UNION', 'DROP', 'INSERT', 'UPDATE', 'DELETE'])
            url = f"{random.choice(['GET', 'POST'])} {filepath}?id=1; {sql_injection} FROM users;-- HTTP/1.1"
            status = random.choice([200, 302, 404])  # Random HTTP status

            writer.writerow([ip, time, url, status])

# Generate 16007 records
generate_dataset(16007)
