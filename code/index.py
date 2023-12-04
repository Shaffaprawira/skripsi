# Simulated log data
log_data = [
    '192.168.1.1 - - [12/Dec/2023:08:00:00 +0000] "GET /page1?id=1 HTTP/1.1" 200 1234',
    '192.168.1.2 - - [12/Dec/2023:08:01:00 +0000] "POST /login HTTP/1.1" 401 678',
    # ... add more log entries
]

# Save simulated log data to a file
with open('sample_log.txt', 'w') as file:
    for log_entry in log_data:
        file.write(log_entry + '\n')

import re

# Read log file
with open('sample_log.txt', 'r') as file:
    logs = file.readlines()

# Extract URLs and request types using regex
urls = []
requests = []

for log_entry in logs:
    # Regex pattern to extract URLs and request types
    pattern = r'\"(\w+)\s([^"]+)\"'
    match = re.search(pattern, log_entry)
    
    if match:
        request_type = match.group(1)
        url = match.group(2).split()[0]
        requests.append(request_type)
        urls.append(url)

print("Extracted URLs:", urls)
print("Request Types:", requests)

# Split data into training and test sets (50% each)
split_idx = len(urls) // 2
train_urls, test_urls = urls[:split_idx], urls[split_idx:]
train_requests, test_requests = requests[:split_idx], requests[split_idx:]

print("Training URLs:", train_urls)
print("Test URLs:", test_urls)

