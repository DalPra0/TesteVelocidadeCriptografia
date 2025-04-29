# Análise de Desempenho Criptográfico

**Aluno:** Lucas Dal Pra Brascher  
**Data:** 29/04/2025

---

## 📜 Descrição da Atividade

Esta atividade consiste em analisar o desempenho dos algoritmos de criptografia simétrica (AES) e de chave pública (RSA), utilizando diferentes tamanhos de chave e avaliando o tempo de execução em cada cenário.

O texto criptografado foi:
> "RSA: algoritmo dos professores do MIT: Rivest, Shamir e Adleman."

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Biblioteca `rsa`
- Biblioteca `pycryptodome` ou `pycryptodomex`
- IDE: PyCharm

---

## 📂 Como Executar

1. Clone o projeto ou copie o script.
2. Instale as dependências:
   ```bash
   pip install rsa pycryptodome
   ```
   ou, caso necessário:
   ```bash
   pip install rsa pycryptodomex
   ```
3. Execute o script no terminal do PyCharm:
   ```bash
   python script.py
   ```
4. Faça 5 execuções manuais de cada teste, anotando o tempo de geração de chave e criptografia.

5. Tire prints de cada execução para o relatório.

---

## ⚙️ Configuração da Máquina de Testes

| Item                 | Especificação                          |
|----------------------|----------------------------------------|
| Sistema Operacional  | macOS Sonoma (provável 14.x, confirme no menu Apple > Sobre este Mac) |
| Processador (CPU)    | Apple M4 Pro                           |
| Frequência do CPU    | ~3.5 GHz (estimado, Apple Silicon não publica exato, mas é referência comum) |
| Núcleos da CPU       | 12 núcleos (8 de performance + 4 de eficiência, típico do M4 Pro) |
| Memória RAM          | 24 GB unificada                        |
| Armazenamento (SSD)  | 512 GB                                 |
---

## 📊 Resultados

| Algoritmo          | Execução 1 | Execução 2 | Execução 3 | Execução 4 | Execução 5 | Média |
|--------------------|------------|------------|------------|------------|------------|-------|
| RSA-1024 (Geração)  | -          | -          | -          | -          | -          | -     |
| RSA-1024 (Criptografia) | -      | -          | -          | -          | -          | -     |
| RSA-2048 (Geração)  | -          | -          | -          | -          | -          | -     |
| RSA-2048 (Criptografia) | -      | -          | -          | -          | -          | -     |
| RSA-4096 (Geração)  | -          | -          | -          | -          | -          | -     |
| RSA-4096 (Criptografia) | -      | -          | -          | -          | -          | -     |
| RSA-8192 (Geração)  | -          | -          | -          | -          | -          | -     |
| RSA-8192 (Criptografia) | -      | -          | -          | -          | -          | -     |
| AES-128 (Criptografia)  | -      | -          | -          | -          | -          | -     |
| AES-256 (Criptografia)  | -      | -          | -          | -          | -          | -     |

---

## 📸 Prints de Execução

Execução 1:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/1d3be443-659a-4e5a-9e93-ad93e6fcd643" />

Execução 2:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/2a07d8aa-b323-4a6c-8e75-f23d94770ebf" />

Execução 3:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/4bf825f8-26f1-4581-aeab-4356d0a0b448" />

---

## 📜 Código Fonte

O script utilizado encontra-se no arquivo `script.py`.

```python
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
```

---

## 🔗 Referências

- Documentação da biblioteca [rsa](https://stuvel.eu/python-rsa-doc/)
- Documentação da biblioteca [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
- StackOverflow para resolução de dúvidas específicas
