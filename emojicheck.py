import requests

# Function to check if a SHA exists
def check_sha_exists(sha):
    response = requests.get(f"https://mainnet-api.ethscriptions.com/api/ethscriptions/exists/{sha}")
    data = response.json()
    return data

# Read the lines from the "E.akak.txt" file (emojis)
with open("E.akak.txt", "r") as file:
    emojis = [line.strip() for line in file]

# Read the lines from the "hash good eth.txt" file (SHA-256 hashes)
with open("hash good eth.txt", "r") as file:
    hashes = [line.strip() for line in file]

# Create a dictionary where each emoji is a key that corresponds to its SHA-256 hash
emoji_to_hash = dict(zip(emojis, hashes))

# Get the emoji from the user
emoji = input("Please enter the emoji you want to check: ")

sha = emoji_to_hash.get(emoji)  # Returns None if the emoji is not in the dictionary

if sha is not None:
    response_data = check_sha_exists(sha)
    if response_data['result']:
        print(f"Result: {response_data['result']}")
        print(f"Current owner: {response_data['ethscription']['current_owner']}")
    else:
        print(f"Result: {response_data['result']}")
else:
    print(f"No hash found for emoji: {emoji}")
