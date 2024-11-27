print("Welcome to the Caesar Cipher program.")

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift_direction = shift if action == 'e' else -shift
            result += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            result += char
    return result

def main():
    action = input("Please select an option: 'e' for encryption or 'd' for decryption: ").lower()
    while action not in ['e', 'd']:
        print("Invalid selection. Please choose 'e' for encryption or 'd' for decryption.")
        action = input("Please select an option: 'e' for encryption or 'd' for decryption: ").lower()

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    result = caesar_cipher(message, shift, action)
    action_word = "Encrypted" if action == 'e' else "Decrypted"
    print(f"\n{action_word} Message: {result}")

if __name__ == "__main__":
    main()