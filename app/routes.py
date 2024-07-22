from flask import Blueprint, jsonify, request
from app import db
from app.models import Expense, Income, User
from flask_jwt_extended import create_access_token, jwt_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/expenses', methods=['POST'])
@jwt_required()
def create_expense():
    """
    Cria uma nova despesa.

    **Requer autenticação JWT**.

    **Request Body**:
    - name (str): Nome da despesa.
    - amount (float): Valor da despesa.
    - date (str): Data da despesa no formato 'YYYY-MM-DD'.

    **Response**:
    - 201 Created: Se a despesa for criada com sucesso.
    - 400 Bad Request: Se o corpo da requisição estiver ausente.
    - 500 Internal Server Error: Em caso de erro interno no servidor.

    **Exemplo de Resposta de Sucesso**:
    {
        "message": "Expense created successfully"
    }

    **Exemplo de Resposta de Erro**:
    {
        "error": "Internal Server Error",
        "message": "Detalhes do erro"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Bad Request', 'message': 'Request data is missing'}), 400

    try:
        expense = Expense(name=data['name'], amount=data['amount'], date=data['date'])
        db.session.add(expense)
        db.session.commit()
        return jsonify({'message': 'Expense created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@main_bp.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():
    """
    Obtém todas as despesas.

    **Requer autenticação JWT**.

    **Response**:
    - 200 OK: Se as despesas forem recuperadas com sucesso.
    - 500 Internal Server Error: Em caso de erro interno no servidor.

    **Exemplo de Resposta de Sucesso**:
    [
        {
            "id": 1,
            "name": "Aluguel",
            "amount": 1200.00,
            "date": "2024-07-22"
        },
        ...
    ]

    **Exemplo de Resposta de Erro**:
    {
        "error": "Internal Server Error",
        "message": "Detalhes do erro"
    }
    """
    try:
        expenses = Expense.query.all()
        expenses_list = [{
            'id': expense.id,
            'name': expense.name,
            'amount': expense.amount,
            'date': expense.date.strftime('%Y-%m-%d')
        } for expense in expenses]
        return jsonify(expenses_list), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@main_bp.route('/incomes', methods=['POST'])
@jwt_required()
def get_income():
    """
    Obtém todas as receitas.

    **Requer autenticação JWT**.

    **Response**:
    - 200 OK: Se as receitas forem recuperadas com sucesso.
    - 500 Internal Server Error: Em caso de erro interno no servidor.

    **Exemplo de Resposta de Sucesso**:
    [
        {
            "id": 1,
            "amount": 5000.00,
            "description": "Salário",
            "date": "2024-07-22"
        },
        ...
    ]

    **Exemplo de Resposta de Erro**:
    {
        "error": "Internal Server Error",
        "message": "Detalhes do erro"
    }
    """
    try:
        incomes = Income.query.all()
        return jsonify([{
            'id': income.id,
            'amount': income.amount,
            'description': income.description,
            'date': income.date
        } for income in incomes]), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@main_bp.route('/login', methods=['POST'])
def login():
    """
    Autentica um usuário e gera um token de acesso JWT.

    **Request Body**:
    - username (str): Nome de usuário.
    - password (str): Senha do usuário.

    **Response**:
    - 200 OK: Se a autenticação for bem-sucedida e o token for gerado.
    - 400 Bad Request: Se o corpo da requisição estiver ausente ou faltando dados.
    - 401 Unauthorized: Se o nome de usuário ou a senha estiverem incorretos.
    - 500 Internal Server Error: Em caso de erro interno no servidor.

    **Exemplo de Resposta de Sucesso**:
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNjEyMzQ1NjAwfQ.SaBAlBeVo6yD2R9-HT8EY4xRfUdFVbPCN0JAlBE5N0k"
    }

    **Exemplo de Resposta de Erro**:
    {
        "error": "Bad Request",
        "message": "Username or password is missing"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Bad Request', 'message': 'Request data is missing'}), 400

    username = data.get('username', None)
    password = data.get('password', None)

    if not username or not password:
        return jsonify({'error': 'Bad Request', 'message': 'Username or password is missing'}), 400

    try:
        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500
