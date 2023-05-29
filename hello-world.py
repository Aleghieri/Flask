from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/index')
def index():
    # Lê a planilha de dados no formato JSON
    data = pd.read_json('caminho/para/o/arquivo.json')
    
    # Converte os dados para formato JSON
    json_data = data.to_json(orient='records')
    
    # Retorna a planilha como resposta em JSON
    return jsonify(json_data)

if __name__ == '__main__':
    app.run()
