import unittest
from datetime import datetime
from app import create_app, db
from app.models import Expense, Income

class TestModels(unittest.TestCase):
    """
    Testes de unidade para os modelos `Expense` e `Income`.

    **Métodos**:
    - setUp(): Configura o ambiente de teste, criando um banco de dados em memória e configurando o contexto da aplicação.
    - tearDown(): Limpa o ambiente de teste, removendo sessões e excluindo o banco de dados em memória.
    - test_expense_creation(): Testa a criação e inserção de uma despesa no banco de dados.
    - test_income_creation(): Testa a criação e inserção de uma receita no banco de dados.
    """

    def setUp(self):
        """
        Configura o ambiente de teste.

        **Ações**:
        - Cria uma instância da aplicação com um banco de dados em memória.
        - Configura o aplicativo para o modo de teste.
        - Cria o contexto da aplicação e o banco de dados.
        """
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

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

    def test_expense_creation(self):
        """
        Testa a criação e inserção de uma despesa.

        **Verificações**:
        - Adiciona uma nova despesa ao banco de dados.
        - Confirma que a despesa foi inserida corretamente verificando a contagem de despesas.
        """
        expense = Expense(name='Groceries', amount=50.5, date='2023-07-22')
        db.session.add(expense)
        db.session.commit()
        self.assertTrue(Expense.query.count() == 1)

    def test_income_creation(self):
        """
        Testa a criação e inserção de uma receita.

        **Verificações**:
        - Adiciona uma nova receita ao banco de dados.
        - Confirma que a receita foi inserida corretamente verificando a contagem de receitas.
        """
        income = Income(name='Salary', amount=1500.0, date='2023-07-22')
        db.session.add(income)
        db.session.commit()
        self.assertTrue(Income.query.count() == 1)

if __name__ == '__main__':
    unittest.main()
