import math
import random

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            char_code = ord(char)
            char_code += shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            result += chr(char_code)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            char_code = ord(char.upper()) - 65
            key_code = ord(key[key_index].upper()) - 65
            char_code = (char_code + key_code) % 26
            if char.isupper():
                result += chr(char_code + 65)
            else:
                result += chr(char_code + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            char_code = ord(char.upper()) - 65
            key_code = ord(key[key_index].upper()) - 65
            char_code = (char_code - key_code) % 26
            if char.isupper():
                result += chr(char_code + 65)
            else:
                result += chr(char_code + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_key_pair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    totient = (p - 1) * (q - 1)
    e = random.randint(2, totient)
    while math.gcd(e, totient) != 1:
        e = random.randint(2, totient)
    d = mod_inverse(e, totient)
    return (n, e), (n, d)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def rsa_encrypt(text, public_key):
    n, e = public_key
    result = ""
    for char in text:
        char_code = ord(char)
        cipher_code = pow(char_code, e, n)
        result += str(cipher_code) + ","
    return result[:-1]

def rsa_decrypt(text, private_key):
    n, d = private_key
    result = ""
    cipher_codes = text.split(",")
    for cipher_code in cipher_codes:
        char_code =
