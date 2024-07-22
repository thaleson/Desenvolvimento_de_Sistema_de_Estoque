import unittest
import json
from app import create_app, db
from app.models import Expense, Income
from flask_jwt_extended import create_access_token

class TestRoutes(unittest.TestCase):
    """
    Testes de unidade para as rotas da API relacionadas a despesas.

    **Métodos**:
    - setUp(): Configura o ambiente de teste, criando um banco de dados em memória, configurando o contexto da aplicação e criando um cliente de teste.
    - tearDown(): Limpa o ambiente de teste, removendo sessões e excluindo o banco de dados em memória.
    - test_create_expense(): Testa a criação de uma despesa via endpoint `/expenses`.
    - test_get_expenses(): Testa a recuperação de despesas via endpoint `/expenses`.
    """

    def setUp(self):
        """
        Configura o ambiente de teste.

        **Ações**:
        - Cria uma instância da aplicação com um banco de dados em memória.
        - Configura o aplicativo para o modo de teste.
        - Cria o contexto da aplicação e o banco de dados.
        - Cria um cliente de teste para enviar requisições à API.
        - Gera um token JWT de teste para autenticação.
        """
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        # Cria um token de teste
        with self.app.test_request_context():
            self.token = create_access_token(identity='testuser')

    def tearDown(self):
        """
        Limpa o ambiente de teste.

        **Ações**:
        - Remove a sessão do banco de dados.
        - Exclui todas as tabelas do banco de dados.
        - Remove o contexto da aplicação.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_expense(self):
        """
        Testa a criação de uma despesa via endpoint `/expenses`.

        **Ações**:
        - Envia uma requisição POST para o endpoint `/expenses` com dados de despesa.
        - Verifica se a resposta tem o status code 200.
        - Verifica se a despesa foi criada no banco de dados.

        **Dados da Requisição**:
        - Headers: Contém um token JWT para autenticação.
        - Corpo: JSON com os dados da despesa ('name', 'amount', 'date').
        """
        response = self.client.post(
            '/expenses',
            headers={'Authorization': f'Bearer {self.token}'},
            data=json.dumps({'name': 'Groceries', 'amount': 50.5, 'date': '2023-07-22'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Expense.query.count(), 1)

    def test_get_expenses(self):
        """
        Testa a recuperação de despesas via endpoint `/expenses`.

        **Ações**:
        - Adiciona uma despesa ao banco de dados.
        - Envia uma requisição GET para o endpoint `/expenses`.
        - Verifica se a resposta tem o status code 200.
        - Verifica se a resposta contém a despesa adicionada.

        **Dados da Requisição**:
        - Headers: Contém um token JWT para autenticação.
        """
        expense = Expense(name='Groceries', amount=50.5, date='2023-07-22')
        db.session.add(expense)
        db.session.commit()
        response = self.client.get(
            '/expenses',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)

if __name__ == '__main__':
    unittest.main()
