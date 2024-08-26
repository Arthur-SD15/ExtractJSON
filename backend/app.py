from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def extract_value(json_obj, path):
    current = json_obj
    for key in path:
        if isinstance(current, list):
            try:
                current = current[int(key)]
            except (IndexError, ValueError):
                return None
        elif isinstance(current, dict):
            current = current.get(key, None)
        else:
            return None
    return current

def lerPath(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_path = json.load(file)
            
        return convert_path(original_path)
    
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON no arquivo {filename}.")
        return []

def convert_path(original_path):
    path = []
    first_element_added = False

    for segment in original_path:
        if len(segment) == 1:
            item = segment[0]
            if not first_element_added:
                path.append(item)
                first_element_added = True
            else:
                if isinstance(item, str):
                    path.append(item)
                elif isinstance(item, int):
                    path.append(item)
        elif len(segment) > 1:
            # Se a lista tiver mais de um item, pode ser uma combinação de índice e chave.
            for item in segment:
                if isinstance(item, str):
                    path.append(item)
                elif isinstance(item, int):
                    path.append(item)
    
    return path

@app.route('/api/save-attributes', methods=['POST'])
def save_attributes():
    try:
        data = request.json
        attributes = data.get('attributes', [])

        if not attributes or all(not attrSet or all(not attr.strip() for attr in attrSet) for attrSet in attributes):
            return jsonify({"error": "Pelo menos um atributo deve ser preenchido e nenhum atributo pode estar em branco!"}), 400

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'attributes.json')

        with open(file_path, 'w') as f:
            json.dump(attributes, f)

        return jsonify({"message": "Atributos salvos com sucesso.", "attributes": attributes}), 200

    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao salvar atributos: {str(e)}"}), 500

@app.route('/api/reset', methods=['POST'])
def reset_files():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'data.json')
        attributes_path = os.path.join(base_dir, 'attributes.json')
        excel_path = os.path.join(base_dir, 'data.xlsx')
        
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
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    # Verifica se um arquivo foi enviado
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo foi enviado."}), 400

    file = request.files['file']
    
    # Verifica se o nome do arquivo está vazio
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    # Verifica se o arquivo tem a extensão .json
    if not file.filename.endswith('.json'):
        return jsonify({"error": "Formato de arquivo inválido."}), 400
    
    # Define o caminho onde o arquivo será salvo
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_filename = os.path.join(base_dir, 'data.json')

    try:
        # Salva o arquivo enviado no caminho especificado
        file.save(data_filename)

        # Lê o arquivo JSON salvo
        with open(data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Lê e processa o arquivo attributes.json
        path_filename = 'attributes.json'
        path = lerPath(path_filename)
        
        # Exemplo de processamento dos dados
        results = []
        if isinstance(data, list):
            for item in data:
                value = extract_value(item, path)
                results.append({"value": value})
        else:
            value = extract_value(data, path)
            results.append({"value": value})

        return jsonify(results), 200

    except json.JSONDecodeError:
        return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 400
    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)