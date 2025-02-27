from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)  # Aquí se debe usar __name__

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar')
def buscar():
    query = request.args.get('q', '').lower()
    with open('compuestos_reales.json', 'r', encoding='utf-8') as f:
        compuestos = json.load(f)
    resultados = [
        {
            'nombre': nombre,
            'formula': datos['formula'],
            'masa_molecular': datos['masa_molecular'],
            'punto_fusion': datos['punto_fusion'],
            'punto_ebullicion': datos['punto_ebullicion'],
            'solubilidad': datos['solubilidad'],
            'presion_vapor': datos['presion_vapor'],
            'densidad': datos['densidad']
        }
        for nombre, datos in compuestos.items()
        if query in nombre.lower()
    ]
    return jsonify(resultados)

if __name__ == "__main__":
    app.run(debug=True)