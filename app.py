# app.py
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

produtos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro-produtos', methods=['GET', 'POST'])
def cadastrar_produto():

    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        descricao = request.form['descricao']
        produto = {'nome': nome, 'preco': preco, 'descricao': descricao}

        produtos.append(produto)

        return redirect('/produtos')

    return render_template('cadastro.html')

@app.route('/ver-produto/<int:id>')
def ver_produto(id):

    produto = produtos[id]

    return render_template('produto.html', produto=produto)

@app.route('/editar-produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):

    produto = produtos[id]
    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['preco'] = request.form['preco']
        produto['descricao'] = request.form['descricao']

        return redirect('/produtos')

    return render_template('editar.html', produto=produto, produto_id=id)

@app.route('/excluir-produto/<int:id>')
def excluir_produto(id):

    del produtos[id]
    return redirect('/produtos')

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
