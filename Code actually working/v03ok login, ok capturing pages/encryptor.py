def encrypt(text, key):
    result = ""
    for char in text:
        if char.isprintable():
            shifted_char = chr((ord(char) - 32 + key) % 95 + 32)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_and_save(username, password, output_file, key):
    encrypted_text = encrypt(username + ',' + password, key)
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt(text, key):
    return encrypt(text,-key)

def decrypt_and_get(input_file, key):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()

    decrypted_text = decrypt(encrypted_text, key)
    return decrypted_text

# Example usage
username = "my_username"
password = "my_password"
output_file = "credentials.auth"
key = 1

# Encrypt and save the credentials on a single line
encrypt_and_save(username, password, output_file, key)

# Decrypt and retrieve the credentials
decrypted_credentials = decrypt_and_get(output_file, key)

decrypted_username, decrypted_password = decrypted_credentials.split(',')

print("Decrypted Username:", decrypted_username)
print("Decrypted Password:", decrypted_password)
