def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""

    for char in string:
        new_idx = alphabet.index(char) + key
        new_char = alphabet[new_idx % 26]
        encrypted_string += new_char

    return encrypted_string
