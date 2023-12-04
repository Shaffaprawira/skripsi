import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate random IP addresses
def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# Function to generate synthetic SQL injection URLs
def generate_url():
    urls = [
        "/login.php?id=1' or '1'='1",
        "/process.php?user=admin';--",
        "/view.php?id=2 UNION SELECT 1,2,3--",
        "/products.php?id=5; DROP TABLE users--",
        "/search.php?q=example' AND 1=1--"
    ]
    return random.choice(urls)

# Function to generate synthetic timestamps
def generate_timestamps(start_date, end_date, n):
    delta = end_date - start_date
    random_dates = [start_date + timedelta(days=random.randint(0, delta.days)) for _ in range(n)]
    return [date.strftime('[%d/%b/%Y:%H:%M:%S') + f" +0{random.randint(0, 9)}00]" for date in random_dates]

# Function to generate random status codes
def generate_status():
    return random.choice([200, 302, 404])

# Generate synthetic data
start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 12, 31)
num_records = 1000  # Number of synthetic log records

data = {
    'IP': [generate_ip() for _ in range(num_records)],
    'Time': generate_timestamps(start_date, end_date, num_records),
    'URL': [generate_url() for _ in range(num_records)],
    'Status': [generate_status() for _ in range(num_records)]
}

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data)
df.to_csv('synthetic_web_logs_with_sql_injection.csv', index=False)
