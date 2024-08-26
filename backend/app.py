from flask import Flask, jsonify, request, send_file
import json
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/save-attributes', methods=['POST'])
def save_attributes():
    try:
        data = request.json
        attributes = data.get('attributes', [])

        if not attributes or all(not attrSet or all(not attr.strip() for attr in attrSet) for attrSet in attributes):
            return jsonify({"error": "Pelo menos um atributo deve ser preenchido e nenhum atributo pode estar em branco!"}), 400

        with open('attributes.json', 'w') as f:
            json.dump(attributes, f)
        return jsonify({"message": "Atributos salvos com sucesso.", "attributes": attributes}), 200

    except Exception as e:
        return jsonify({"error": "Erro inesperado ao salvar atributos."}), 500

@app.route('/api/reset', methods=['POST'])
def reset_files():
    try:
        json_path = 'data.json'
        attributes_path = 'attributes.json'
        excel_path = 'data.xlsx'
        
        if os.path.exists(json_path):
            os.remove(json_path)
        
        if os.path.exists(excel_path):
            os.remove(excel_path)
        
        if os.path.exists(attributes_path):
            os.remove(attributes_path)

        return jsonify({"message": "Todos os arquivos foram excluídos com sucesso."}), 200

    except FileNotFoundError as fnf_error:
        return jsonify({"error": "Arquivo não encontrado."}), 404

    except PermissionError as perm_error:
        return jsonify({"error": "Erro de permissão."}), 403

    except Exception as e:
        return jsonify({"error": "Erro inesperado."}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo foi enviado."}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    if not file.filename.endswith('.json'):
        return jsonify({"error": "Formato de arquivo inválido."}), 400
    
    try:
        print("oi")

    except json.JSONDecodeError:
        return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 400
    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)