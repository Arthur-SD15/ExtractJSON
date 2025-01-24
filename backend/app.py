from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import json
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Extract JSON'

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
            for item in segment:
                if isinstance(item, str):
                    path.append(item)
                elif isinstance(item, int):
                    path.append(item)
    return path

def readPath(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_path = json.load(file)
        return convert_path(original_path)
    
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON no arquivo.")
        return []

def has_invalid_object(obj):
    if isinstance(obj, dict):
        return True
    if isinstance(obj, list):
        return any(has_invalid_object(item) for item in obj)
    return False

@app.route('/api/save-attributes', methods=['POST'])
def save_attributes():
    try:
        data = request.json
        attributes = data.get('attributes', [])
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, 'attributes.json')

        if not attributes or all(not attrSet or all(attr is None or (isinstance(attr, str) and not attr.strip()) for attr in attrSet) for attrSet in attributes):
            return jsonify({"error": "Pelo menos um atributo deve ser preenchido e nenhum atributo pode estar em branco."}), 400

        with open(file_path, 'w') as f:
            json.dump(attributes, f)
        return jsonify({"message": "Atributos salvos com sucesso.", "attributes": attributes}), 200

    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao salvar atributos: {str(e)}"}), 500

@app.route('/api/attributes/reset', methods=['POST'])
def reset_attributrs():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        attributes_path = os.path.join(base_dir, 'attributes.json')
        
        if os.path.exists(attributes_path):
            os.remove(attributes_path)
        return jsonify({"message": "Atributos resetados com sucesso."}), 200

    except FileNotFoundError as fnf_error:
        return jsonify({"error": "Arquivo não encontrado."}), 404

    except PermissionError as perm_error:
        return jsonify({"error": "Erro de permissão."}), 403

    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao resetar atributos: {str(e)}"}), 500 

@app.route('/api/reset', methods=['POST'])
def reset_files():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'data.json')
        excel_path = os.path.join(base_dir, 'filtered_data.xlsx')
        csv_path = os.path.join(base_dir, 'filtered_data.csv')
        
        if os.path.exists(json_path):
            os.remove(json_path)
        
        if os.path.exists(excel_path):
            os.remove(excel_path)

        if os.path.exists(csv_path):
            os.remove(csv_path)
        return jsonify({"message": "Arquivos resetados com sucesso."}), 200

    except FileNotFoundError as fnf_error:
        return jsonify({"error": "Arquivo não encontrado."}), 404

    except PermissionError as perm_error:
        return jsonify({"error": "Erro de permissão."}), 403

    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao resetar arquivos: {str(e)}"}), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_filename = os.path.join(base_dir, 'data.json')
    attributes_filename = os.path.join(base_dir, 'attributes.json')

    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo foi enviado."}), 400
    
    if file.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    if not file.filename.endswith('.json'):
        return jsonify({"error": "Formato de arquivo inválido."}), 400
    
    if not os.path.exists(attributes_filename):
        return jsonify({"error": "Os atributos não foram configurados."}), 404

    try:
        file.save(data_filename)

        with open(data_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        path_filename = 'attributes.json'
        path = readPath(path_filename)
        results = []

        def convert_value(value):
            if isinstance(value, bool):
                return str(value)
            elif isinstance(value, (int, float)):
                return str(value)
            elif isinstance(value, dict):
                return {k: convert_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [convert_value(v) for v in value]
            return value

        if isinstance(data, list):
            for item in data:
                value = extract_value(item, path)
                results.append({"value": convert_value(value)})
        else:
            value = extract_value(data, path)
            results.append({"value": convert_value(value)})

        if any(has_invalid_object(result['value']) for result in results):
            return jsonify({"error": "A configuração dos atributos está incorreta. Valores inválidos detectados em objetos."}), 400

        if any(result['value'] is None for result in results):
            return jsonify({"error": "A configuração dos atributos está incorreta."}), 400

        base_dir = os.path.dirname(os.path.abspath(__file__))
        export_filename = os.path.join(base_dir, 'filtered_data.csv')
        df = pd.DataFrame(results)
        df.to_csv(export_filename, index=False)
        return jsonify(results), 200

    except json.JSONDecodeError:
        return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 400

    except Exception as e:
        return jsonify({"error": f"Erro inesperado no upload: {str(e)}"}), 500

@app.route('/api/export', methods=['GET'])
def export_to_excel():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(base_dir, 'filtered_data.csv')

    if not os.path.exists(csv_filename):
        return jsonify({"error": "Nenhum dado para exportar."}), 404

    try:
        df = pd.read_csv(csv_filename)
        excel_filename = os.path.join(base_dir, 'filtered_data.xlsx')
        df.to_excel(excel_filename, index=False)

        return send_file(
            excel_filename,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='filtered_data.xlsx'
        )

    except Exception as e:
        return jsonify({"error": f"Erro inesperado ao exportar para Excel: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)