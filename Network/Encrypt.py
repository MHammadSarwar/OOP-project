from cryptography.fernet import Fernet
import os

# Your code for generating an AES key
def generate_aes_key():
    key = Fernet.generate_key()
    return key

# Your code for saving the encryption key to a configuration file
def save_aes_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)

# Your code for saving credentials to a file using AES
def save_credentials_aes(username, password, key, filename):
    cipher_suite = Fernet(key)
    encrypted_username = cipher_suite.encrypt(username.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())
    
    with open(filename, 'wb') as file:
        file.write(encrypted_username)
        file.write(b'\n')  # Separate username and password
        file.write(encrypted_password)

# Your code for loading and decrypting credentials from a file using AES
def load_credentials_aes(key, filename):
    cipher_suite = Fernet(key)

    with open(filename, 'rb') as file:
        lines = file.readlines()
        if len(lines) != 2:
            raise ValueError("Invalid credential file format")

        encrypted_username = lines[0].strip()
        encrypted_password = lines[1].strip()

        username = cipher_suite.decrypt(encrypted_username).decode()
        password = cipher_suite.decrypt(encrypted_password).decode()

    return username, password

# Main execution
if __name__ == "__main__":
    # Generate an AES key
    aes_key = generate_aes_key()
    
    # Set the configuration file path
    config_dir = "Config"
    key_filename = os.path.join(config_dir, "encryption_key.txt")

    # Save the AES key to a file
    save_aes_key(aes_key, key_filename)
    
    # Set restrictive file permissions (e.g., readable only by the owner)
    os.chmod(key_filename, 0o600)

    print("AES key saved securely.")
    
    # Replace 'credentials.txt' with your desired filename
    filename = "Credentials.qalam"
    # Replace 'your_username' and 'your_password' with your actual credentials
    username = 'arehman.bee22seecs'
    password = 'Eesucks80085'
    
    # Save encrypted credentials to a file using AES
    save_credentials_aes(username, password, aes_key, filename)
    print("Credentials saved securely using AES.")
    
    # Load and decrypt credentials from the file using AES
    loaded_username, loaded_password = load_credentials_aes(aes_key, filename)
    print("Loaded Username:", loaded_username)
    print("Loaded Password:", loaded_password)
