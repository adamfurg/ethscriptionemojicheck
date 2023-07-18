import requests
import streamlit as st

# Function to check if a SHA exists
def check_sha_exists(sha):
    response = requests.get(f"https://mainnet-api.ethscriptions.com/api/ethscriptions/exists/{sha}")
    data = response.json()
    return data

# Function to convert emoji to hex
def emoji_to_hex(emoji):
    return ''.join([f'{ord(c):x}' for c in "data:," + emoji])

# Read the lines from the "E.akak.txt" file (emojis)
with open("E.akak.txt", "r") as file:
    emojis = [line.strip() for line in file]

# Read the lines from the "hash good eth.txt" file (SHA-256 hashes)
with open("hash good eth.txt", "r") as file:
    hashes = [line.strip() for line in file]

# Create a dictionary where each emoji is a key that corresponds to its SHA-256 hash
emoji_to_hash = dict(zip(emojis, hashes))

# Get the emoji from the user
st.write("Please enter the emoji you want to check:")
st.write("请输入你想要检查的表情符号：")
emoji = st.text_input("")

if emoji:  # Only run the rest of the code if the user has entered an emoji
    sha = emoji_to_hash.get(emoji)  # Returns None if the emoji is not in the dictionary

    if sha is not None:
        response_data = check_sha_exists(sha)
        if response_data['result']:
            st.write("This emoji is taken.")
            st.write("这个表情符号已被占用。")
            st.write(f"Current owner: {response_data['ethscription']['current_owner']}")
            st.write(f"当前所有者：{response_data['ethscription']['current_owner']}")
        else:
            st.write("This emoji is not taken.")
            st.write("这个表情符号未被占用。")
            hex_value = emoji_to_hex(emoji)
            st.write(f"hex: {hex_value}")
            st.write(f"十六进制：{hex_value}")
    else:
        st.write(f"No hash found for emoji: {emoji}")
        st.write(f"找不到表情符号的哈希值：{emoji}")
