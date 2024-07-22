# Projeto Flask - Sistema de Despesas

Este projeto é uma API RESTful simples para gerenciamento de despesas, desenvolvida usando Flask e SQLAlchemy. Ele inclui funcionalidades para criar e visualizar despesas. A API está protegida por JWT para autenticação.

## Funcionalidades

- **Criar Despesas**: Adicionar novas despesas.
- **Listar Despesas**: Obter a lista de todas as despesas.

## Pré-requisitos

- Python 3.8 ou superior
- `pip`

## Configuração do Projeto

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/thaleson/Sistema_de_Despesas_python
cd  https://github.com/thaleson/Sistema_de_Despesas_python
```

### 2. Criar e Ativar o Ambiente Virtual

Crie e ative um ambiente virtual para o projeto:

```bash
python -m venv venv
```

- **No Windows**:

  ```bash
  .\venv\Scripts\activate
  ```

- **No Linux/MacOS**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

Inicialize o banco de dados e crie as tabelas:

```bash
flask db init
flask db migrate
flask db upgrade
```

### 5. Adicionar Usuários de Teste

Adicione alguns usuários de teste para autenticação. No terminal Python:

```python
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    user1 = User(username='testuser')
    user1.set_password('testpassword')

    db.session.add(user1)
    db.session.commit()
```

### 6. Executar o Servidor

Inicie o servidor Flask:

```bash
flask run
```

O servidor estará disponível em `http://127.0.0.1:5000`.

## Testar a API

### 1. Obter um Token JWT

Faça uma requisição POST para `/login` para obter um token JWT:

- **URL**: `http://127.0.0.1:5000/login`
- **Método**: POST
- **Body (JSON)**:

  ```json
  {
      "username": "testuser",
      "password": "testpassword"
  }
  ```

Você receberá um token JWT na resposta. Use este token para acessar rotas protegidas.

### 2. Criar uma Despesa

Faça uma requisição POST para `/expenses`:

- **URL**: `http://127.0.0.1:5000/expenses`
- **Método**: POST
- **Headers**:
  - `Authorization`: `Bearer <SEU_TOKEN_JWT>`
- **Body (JSON)**:

  ```json
  {
      "name": "Groceries",
      "amount": 50.5,
      "date": "2023-07-22"
  }
  ```

### 3. Listar Despesas

Faça uma requisição GET para `/expenses`:

- **URL**: `http://127.0.0.1:5000/expenses`
- **Método**: GET
- **Headers**:
  - `Authorization`: `Bearer <SEU_TOKEN_JWT>`

## Testes

Execute os testes do projeto para garantir que tudo está funcionando corretamente:

```bash
pytest
```

## Estrutura do Projeto

- `app/`: Contém o código do aplicativo Flask.
  - `__init__.py`: Inicializa o aplicativo e configura o banco de dados.
  - `models.py`: Contém os modelos de dados.
  - `routes.py`: Contém as rotas da API.
  - `config.py`: Configurações do projeto.
- `migrations/`: Scripts de migração do banco de dados.
- `tests/`: Contém os testes do projeto.
- `requirements.txt`: Lista de dependências do projeto.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

```

Sinta-se à vontade para ajustar qualquer parte conforme necessário para se adequar ao seu projeto específico. Se precisar de mais alguma coisa, é só me avisar!
