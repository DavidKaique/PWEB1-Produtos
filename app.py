from flask import Flask, render_template
app = Flask (__name__, template_folder='templates')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro-produtos')
def cadastroprodutos():
    return render_template('cadastro-produtos.html')

@app.route('/ver-produto')
def verproduto():
    return render_template('ver-produto.html')

@app.route('/editar-produto')
def editarproduto():
    return render_template('editar-produto.html')

@app.route('/excluir-produto')
def excluirproduto():
    return render_template('excluir-produto.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')
    
if __name__ == '__main__':
    app.run(debug=True)   