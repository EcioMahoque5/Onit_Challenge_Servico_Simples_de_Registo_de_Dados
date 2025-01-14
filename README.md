# Aplicação Flask para Registo de Clientes

Esta aplicação é uma API desenvolvida em Flask que permite o registo de clientes em memória, validação de dados e consulta dos registros.

---

## Passos para Executar a Aplicação

1. **Crie um Ambiente Virtual**

   - No diretório do projeto, crie um ambiente virtual:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **Linux/Mac**:
       ```bash
       source venv/bin/activate
       ```

2. **Crie o arquivo `.env`**

   - Na raiz do projeto, crie um arquivo chamado `.env`.
   - Adicione a variável `SECRET_KEY` com um valor qualquer:
     ```env
     SECRET_KEY=sua_chave_secreta_aqui
     ```

3. **Instale os Pacotes Necessários**

   - Certifique-se de estar com o ambiente virtual ativado.
   - Instale os pacotes listados no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Execute a Aplicação**

   - No terminal, com o ambiente virtual ativado, execute o arquivo principal:
     ```bash
     python main.py
     ```
   - A aplicação será iniciada no endereço padrão: `http://127.0.0.1:5000`.

5. **Testar as APIs**
   - Use ferramentas como [Postman](https://www.postman.com/) ou [cURL](https://curl.se/) para testar os endpoints da API.

---

## Endpoints Disponíveis

### 1. **Registrar um Cliente**

- **URL**: `POST http://127.0.0.1:5000/register_client`
- **Descrição**: Registra um novo cliente.
- **Cabeçalho**:
  ```json
  Content-Type: application/json
  ```
- **Body (JSON)**:
  ```json
  {
    "first_name": "John",
    "other_names": "Doe Smith",
    "email": "john.doe@example.com",
    "address": "123 Main St, Maputo"
  }
  ```
- **Resposta de Sucesso (201)**:
  ```json
  {
    "success": true,
    "message": "Client registered successfully!",
    "data": {
      "id": 1000,
      "first_name": "John",
      "other_names": "Doe Smith",
      "email": "john.doe@example.com",
      "address": "123 Main St, Maputo",
      "date_created": "2025-01-14 12:30:45.123"
    }
  }
  ```
- **Resposta de Erro (409 - Email Duplicado)**:
  ```json
  {
    "success": false,
    "message": "Validations errors",
    "errors": {
      "email": ["Email already registered."]
    }
  }
  ```

### 2. **Listar Clientes Registrados**

- **URL**: `GET http://127.0.0.1:5000/data`
- **Descrição**: Retorna a lista de todos os clientes registrados.
- **Resposta de Sucesso (200)**:
  ```json
  {
    "success": true,
    "message": "Clients found!",
    "data": [
      {
        "id": 1000,
        "first_name": "John",
        "other_names": "Doe Smith",
        "email": "john.doe@example.com",
        "address": "123 Main St, Maputo",
        "date_created": "2025-01-14 12:30:45.123"
      }
    ]
  }
  ```
  - **Resposta de Erro (409 - Nenhum cliente registrado)**:
  ```json
  {
    "success": false,
    "message": "There is no client registred!",
    "code": 409
  }
  ```

---

## Estrutura do Projeto

. ├── app/
│ ├── init.py
│ ├── configs.py
│ ├── routes.py
│ └── validators.py
├── venv/
├── .env
├── main.py
├── requirements.txt
└── README.md


---

## Requisitos
- Python 3.7+
- Flask
- Flask-WTF
- Python-dotenv

---

## Observações
- Certifique-se de que a variável `SECRET_KEY` está configurada no arquivo `.env` antes de executar a aplicação.
- Sempre ative o ambiente virtual antes de instalar os pacotes ou executar a aplicação:
  - **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```

---
