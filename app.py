from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acougue.db'
db = SQLAlchemy(app)

# Modelos do banco de dados
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    unidade = db.Column(db.String(10))  # kg, g, etc.

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)

# Rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'GET':
        produtos = Produto.query.all()
        return jsonify([{'id': p.id, 'nome': p.nome, 'preco': p.preco, 
                        'quantidade': p.quantidade, 'unidade': p.unidade} for p in produtos])
    
    if request.method == 'POST':
        dados = request.json
        novo_produto = Produto(
            nome=dados['nome'],
            preco=dados['preco'],
            quantidade=dados['quantidade'],
            unidade=dados['unidade']
        )
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify({'mensagem': 'Produto cadastrado com sucesso'})

@app.route('/api/vendas/nova', methods=['POST'])
def nova_venda():
    dados = request.json
    venda = Venda(total=dados['total'])
    db.session.add(venda)
    db.session.commit()
    return jsonify({'mensagem': 'Venda registrada com sucesso'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 