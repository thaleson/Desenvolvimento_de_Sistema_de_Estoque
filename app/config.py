import os

class Config:
    """
    Configurações básicas para a aplicação Flask.

    **Atributos**:
    - SECRET_KEY (str): Chave secreta usada para sessões e segurança. O valor é obtido da variável de ambiente 'SECRET_KEY' ou é definido como 'mysecretkey' por padrão.
    - SQLALCHEMY_DATABASE_URI (str): URL de conexão com o banco de dados. O valor é obtido da variável de ambiente 'DATABASE_URL' ou é definido como 'sqlite:///site.db' por padrão.
    - SQLALCHEMY_TRACK_MODIFICATIONS (bool): Configura se as modificações no banco de dados devem ser rastreadas. Está desativado por padrão (False).
    - JWT_SECRET_KEY (str): Chave secreta usada para a criação e verificação de tokens JWT. O valor é obtido da variável de ambiente 'JWT_SECRET_KEY' ou é definido como 'my_jwt_secret_key' por padrão.

    **Exemplo de Uso**:
    Para usar estas configurações, você deve criar uma instância da classe `Config` e configurar o aplicativo Flask com ela:
    
    ```python
    app.config.from_object(Config)
    ```
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'my_jwt_secret_key')
