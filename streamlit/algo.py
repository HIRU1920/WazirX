import random
import base64

def generate_keys(message):
    message_length = len(message)
    key_length = message_length * 8  # Assuming 16 bits per character
    
    public_key = random.randint(1, 2**key_length - 1)  # Generating a random public key based on message length
    private_key_bytes = random.randbytes(16)  # Generating 16 random bytes for private key
    private_key = base64.b64encode(private_key_bytes).decode('utf-8')  # Base64 encoding the private key
    
    return public_key, private_key

def add_random_letters(message):
    random_letter = chr(random.randint(33, 126))  # Generate a random printable ASCII character
    modified_message = random_letter + message + random_letter  # Adding the random letter at the beginning and end
    return modified_message, random_letter

def remove_letters(modified_message, random_letter):
    # Removing the added random letter at the beginning and end from the modified message
    return modified_message[1:-1].replace(random_letter, '')


def encrypt_message(modified_message):
    encrypted_message = []
    for char in modified_message:
        ascii_value = ord(char)
        encrypted_char = chr(ascii_value + 2)  # Add 4 to the ASCII value
        encrypted_message.append(encrypted_char)
    return ''.join(encrypted_message)

def decrypt_message(encrypted_message):
    decrypted_message = []
    for char in encrypted_message:
        ascii_value = ord(char)
        decrypted_char = chr(ascii_value - 2)  # Subtract 4 from the ASCII value
        decrypted_message.append(decrypted_char)
    decrypted_message = ''.join(decrypted_message)
    
    random_letter = decrypted_message[0]  # Get the random letter added during encryption
    original_message = remove_letters(decrypted_message, random_letter)
    
    return decrypted_message, original_message
