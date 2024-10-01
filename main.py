secret_message = "abcxyzABCXYZ123890"
number = 3
character_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char in character_list:
            result += character_list[(character_list.index(char) + shift) % len(character_list)]
        else:
            result += char
    return result

def decipher_with_all_shifts(ciphered_text: str):
    for shift in range(len(character_list)):
        result = ""
        for char in ciphered_text:
            if char in character_list:
                result += character_list[(character_list.index(char) - shift) % len(character_list)]
            else:
                result += char
        print(f"Shift {shift}: {result}")

# Encrypt the message
hidden_message = cipher(secret_message, number)

# Print all possible deciphered messages
print("Original message:", secret_message)
print("Encrypted message:", hidden_message)
print("All possible deciphered messages:")
decipher_with_all_shifts(hidden_message)