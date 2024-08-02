from flask import Flask, jsonify, render_template
from boa_constrictor import Boa_Constrictor
from perro import Perro
from huron import Huron
from gato import Gato
from concentrado import Concentrado

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/perro', methods=['GET'])
def perro():
    perro = Perro('mati', 'pitbull', 23, 5, Concentrado('wiskas', 43000, 223, 'ksdjsd'))
    return jsonify({"sonido": perro.ladrar()})

@app.route('/huron', methods=['GET'])
def huron():
    huron = Huron('mati', 4.3, 3, 'colombia', 12200)
    return jsonify({"sonido": huron.hacer_sonido()})

@app.route('/gato', methods=['GET'])
def gato():
    gato = Gato('lucas', 'persa', 2.3,4)
    return jsonify({"sonido": gato.maullar()})

@app.route('/boa', methods=['GET'])
def boa():
    boa = Boa_Constrictor('Lety', 28, 4, 'cambodia', 400000)
    return jsonify({"sonido": boa.hacer_sonido()})

