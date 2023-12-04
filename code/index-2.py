import pandas as pd

# Load the dataset
data = pd.read_csv('weblog.csv')

# Display basic information about the dataset
print(data.head())
print(data.info())

# Extract URLs and requests
urls = data['URL']
requests = data['Status']

print("Extracted URLs:", urls)
print("Request Types:", requests)

from sklearn.model_selection import train_test_split

# Split the dataset into training and test sets (80% train, 20% test)
train_urls, test_urls, train_requests, test_requests = train_test_split(urls, requests, test_size=0.2, random_state=42)

print("Training URLs:", train_urls)
print("Test URLs:", test_urls)