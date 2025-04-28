import time
import rsa
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


texto = "RSA: algoritmo dos professores do MIT: Rivest, Shamir e Adleman".encode('utf-8')


def rsa_encrypt_test(bits):
    print(f"\n===== RSA {bits} bits =====")

    start_keygen = time.time()
    (public_key, private_key) = rsa.newkeys(bits)
    end_keygen = time.time()

    keygen_time = end_keygen - start_keygen
    print(f"Tempo para gerar chaves RSA-{bits}: {keygen_time:.4f} segundos")

    start_encrypt = time.time()
    encrypted_text = rsa.encrypt(texto, public_key)
    end_encrypt = time.time()

    encrypt_time = end_encrypt - start_encrypt
    print(f"Tempo para criptografar RSA-{bits}: {encrypt_time:.4f} segundos")


def aes_encrypt_test(bits):
    print(f"\n===== AES {bits} bits =====")

    key = get_random_bytes(bits // 8)
    cipher = AES.new(key, AES.MODE_EAX)

    start_encrypt = time.time()
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(texto)
    end_encrypt = time.time()

    encrypt_time = end_encrypt - start_encrypt
    print(f"Tempo para criptografar AES-{bits}: {encrypt_time:.4f} segundos")


if __name__ == "__main__":
    print("Início do teste de desempenho criptográfico")

    # RSA
    rsa_encrypt_test(1024)
    rsa_encrypt_test(2048)
    rsa_encrypt_test(4096)
    rsa_encrypt_test(8192)

    # AES
    aes_encrypt_test(128)
    aes_encrypt_test(256)

    print("\nTeste concluído!")