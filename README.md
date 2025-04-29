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
| RSA-1024 (Geração)  | 0.0194 segundos          | -          | -          | -          | -          | -     |
| RSA-1024 (Criptografia) | 0.0000 segundos      | -          | -          | -          | -          | -     |
| RSA-2048 (Geração)  | 2.7070 segundos          | -          | -          | -          | -          | -     |
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


Execução 4:

![image](https://github.com/user-attachments/assets/d130efbb-56f7-4136-ba03-7d673246ed21)


---

## 📜 Código Fonte

O script utilizado encontra-se no arquivo `script.py`.

### 📌 Importações

```python
import time
import rsa
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
```
- `time`: para medir os tempos de execução das operações.
- `rsa`: biblioteca usada para gerar chaves e cifrar com RSA.
- `base64`: usada para codificações, embora não tenha sido utilizada no código final.
- `Cryptodome.Cipher.AES`: biblioteca para criptografia simétrica (AES).
- `get_random_bytes`: usada para gerar chaves aleatórias para o AES.

---

### 📌 Texto base para os testes

```python
texto = "RSA: algoritmo dos professores do MIT: Rivest, Shamir e Adleman".encode('utf-8')
```
- Define o texto que será criptografado por todos os algoritmos.
- O `.encode('utf-8')` transforma a string em bytes, pois os algoritmos exigem esse formato.

---

### 🔐 Função RSA: `rsa_encrypt_test(bits)`

```python
(public_key, private_key) = rsa.newkeys(bits)
```
- Gera um par de chaves (pública e privada) com o número de bits fornecido (ex: 1024, 2048...).

```python
encrypted_text = rsa.encrypt(texto, public_key)
```
- Criptografa o texto com a chave pública RSA gerada.

```python
time.time()
```
- Mede o tempo antes e depois da operação para calcular a duração da geração da chave e da criptografia.

---

### 🔐 Função AES: `aes_encrypt_test(bits)`

```python
key = get_random_bytes(bits // 8)
```
- Gera uma chave AES aleatória (ex: 128 ou 256 bits), convertendo para bytes (dividido por 8).

```python
cipher = AES.new(key, AES.MODE_EAX)
```
- Cria um objeto de cifra no modo `EAX` (modo autenticado e seguro).

```python
ciphertext, tag = cipher.encrypt_and_digest(texto)
```
- Criptografa o texto e gera uma `tag` de verificação de integridade.

---

### ▶️ Execução principal

```python
if __name__ == "__main__":
```
- Ponto de entrada do script quando ele é executado diretamente.

```python
rsa_encrypt_test(1024)
rsa_encrypt_test(2048)
rsa_encrypt_test(4096)
rsa_encrypt_test(8192)
```
- Executa os testes com criptografia RSA em quatro tamanhos de chave.

```python
aes_encrypt_test(128)
aes_encrypt_test(256)
```
- Executa os testes com criptografia AES com chaves de 128 e 256 bits.

---

### ✅ Resultado

- O script imprime no console o tempo gasto para gerar chaves RSA e criptografar com RSA e AES.
- Os dados devem ser registrados manualmente em prints e planilhas.


---

## 🔗 Referências

- Documentação da biblioteca [rsa](https://stuvel.eu/python-rsa-doc/)
- Documentação da biblioteca [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
- StackOverflow para resolução de dúvidas específicas
