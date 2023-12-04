from faker import Faker
import random
import csv

fake = Faker()

# Function to simulate SQL injection attack in URLs
def simulate_sql_injection():
    ip = fake.ipv4()
    time = fake.date_time_this_year()
    status = random.choice([200, 302, 404])  # Simulating different HTTP status codes

    # Simulating SQL injection attacks in URLs
    urls = [
        f"GET /login.php?user=admin';--",
        f"POST /process.php?id=1; DELETE FROM users;--",
        # Add more URLs with SQL injection attacks as needed
    ]

    return [ip, time, random.choice(urls), status]

# Generate dataset with simulated SQL injection attacks
num_entries = 1000  # Number of log entries to generate

with open('simulated_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['IP', 'Time', 'URL', 'Status'])  # Writing headers

    for _ in range(num_entries):
        log_entry = simulate_sql_injection()
        writer.writerow(log_entry)

print(f"Simulated dataset with {num_entries} entries generated.")
