import unittest
from app import create_app

class TestConfig(unittest.TestCase):
    """
    Testes de unidade para verificar a configuração da aplicação Flask.

    **Métodos**:
    - test_app_is_testing(): Verifica se a aplicação está configurada corretamente para o ambiente de testes.

    **Detalhes dos Testes**:
    - Verifica se a chave secreta da configuração é 'mysecretkey'.
    - Verifica se o rastreamento de modificações do SQLAlchemy está desativado (False).
    """

    def test_app_is_testing(self):
        """
        Testa se a configuração da aplicação está correta para o ambiente de testes.

        **Verificações**:
        - Confirma que a chave secreta (`SECRET_KEY`) está definida como 'mysecretkey'.
        - Confirma que o rastreamento de modificações (`SQLALCHEMY_TRACK_MODIFICATIONS`) está desativado (False).

        **Observações**:
        - Este teste assume que a aplicação é criada com a configuração padrão definida em `create_app()`.
        """
        app = create_app()
        self.assertTrue(app.config['SECRET_KEY'] == 'mysecretkey')
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])

if __name__ == '__main__':
    unittest.main()
