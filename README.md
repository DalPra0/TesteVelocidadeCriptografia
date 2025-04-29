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


---

## 📜 Código Fonte

O script utilizado encontra-se no arquivo `script.py`.

---

## 🔗 Referências

- Documentação da biblioteca [rsa](https://stuvel.eu/python-rsa-doc/)
- Documentação da biblioteca [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/)
- StackOverflow para resolução de dúvidas específicas
