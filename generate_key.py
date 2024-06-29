from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key to a file
with open('file.key', 'wb') as key_file:
    key_file.write(key)

print("Key has been generated and saved to file.key")
