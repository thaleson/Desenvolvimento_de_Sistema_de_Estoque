from app import db
from datetime import datetime

class Expense(db.Model):
    """
    Modelo que representa uma despesa.

    **Atributos**:
    - id (int): Identificador único da despesa.
    - name (str): Nome da despesa. Máximo de 100 caracteres.
    - amount (float): Valor da despesa.
    - date (date): Data da despesa.

    **Métodos**:
    - __init__(name, amount, date): Inicializa uma nova instância de Expense.
    - __repr__(): Representação em string da despesa.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, name, amount, date):
        """
        Inicializa uma nova instância de Expense.

        **Parâmetros**:
        - name (str): Nome da despesa.
        - amount (float): Valor da despesa.
        - date (str): Data da despesa no formato 'YYYY-MM-DD'.
        """
        self.name = name
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d').date()

    def __repr__(self):
        """
        Representação em string da despesa.

        **Retorno**:
        - str: Representação da despesa no formato '<Expense nome_da_despesa>'.
        """
        return f'<Expense {self.name}>'

class Income(db.Model):
    """
    Modelo que representa uma receita.

    **Atributos**:
    - id (int): Identificador único da receita.
    - name (str): Nome da receita. Máximo de 100 caracteres.
    - amount (float): Valor da receita.
    - date (date): Data da receita.

    **Métodos**:
    - __init__(name, amount, date): Inicializa uma nova instância de Income.
    - __repr__(): Representação em string da receita.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, name, amount, date):
        """
        Inicializa uma nova instância de Income.

        **Parâmetros**:
        - name (str): Nome da receita.
        - amount (float): Valor da receita.
        - date (str): Data da receita no formato 'YYYY-MM-DD'.
        """
        self.name = name
        self.amount = amount
        self.date = datetime.strptime(date, '%Y-%m-%d').date()

    def __repr__(self):
        """
        Representação em string da receita.

        **Retorno**:
        - str: Representação da receita no formato '<Income nome_da_receita>'.
        """
        return f'<Income {self.name}>'

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    Modelo que representa um usuário.

    **Atributos**:
    - id (int): Identificador único do usuário.
    - username (str): Nome de usuário. Deve ser único e não pode ser nulo.
    - password_hash (str): Hash da senha do usuário.

    **Métodos**:
    - set_password(password): Define o hash da senha para o usuário.
    - check_password(password): Verifica se a senha fornecida corresponde ao hash armazenado.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """
        Define o hash da senha para o usuário.

        **Parâmetros**:
        - password (str): Senha do usuário.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.

        **Parâmetros**:
        - password (str): Senha fornecida para verificação.

        **Retorno**:
        - bool: Retorna True se a senha corresponder ao hash, False caso contrário.
        """
        return check_password_hash(self.password_hash, password)
