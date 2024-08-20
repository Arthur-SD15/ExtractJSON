from flask import Flask, jsonify, request, send_file
import json
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/reset', methods=['POST'])
def reset_files():
    try:
        json_path = 'data.json'
        excel_path = 'data.xlsx'
        
        if os.path.exists(json_path):
            os.remove(json_path)
        
        if os.path.exists(excel_path):
            os.remove(excel_path)

        return jsonify({"message": "Todos os arquivos foram excluídos com sucesso."}), 200

    except FileNotFoundError as fnf_error:
        posibleError = str(fnf_error)
        return jsonify({"error": "Arquivo não encontrado."}), 404

    except PermissionError as perm_error:
        posibleError = str(perm_error)
        return jsonify({"error": "Erro de permissão."}), 403

    except Exception as e:
        posibleError = str(e)
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
        file.save('data.json')
        
        with open('data.json', 'r') as f:
            data = json.load(f)

        filtered_data = []
        for item in data:
            students = item.get('students', [])
            for student in students:
                student_info = student.get('student', {})
                institution = student_info.get('institution', {})
                address = institution.get('address', {})
                city = address.get('city', None)
                if city:
                    filtered_data.append({"field": "City", "value": city})

        return jsonify(filtered_data)

    except json.JSONDecodeError:
        return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 400
    except Exception as e:
        return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 500

@app.route('/api/export', methods=['GET'])
def export_to_excel():
    try:
        try:
            with open('data.json', 'r') as file:
                if file.readable():
                    file.seek(0) 
                    data = json.load(file)
                else:
                    return jsonify({"error": "Nenhum arquivo foi enviado."}), 400
        except FileNotFoundError:
            return jsonify({"error": "Arquivo JSON não encontrado."}), 404
        except json.JSONDecodeError:
            return jsonify({"error": "O arquivo pode estar corrompido ou não estar no formato JSON correto."}), 400
        
        rows = []
        for item in data:
            students = item.get('students', [])
            for student in students:
                student_info = student.get('student', {})
                institution = student_info.get('institution', {})
                address = institution.get('address', {})
                city = address.get('city', None)
                if city:
                    rows.append({"City": city})

        if not rows:
            return jsonify({"error": "Nenhum dado para exportar."}), 404

        df = pd.DataFrame(rows)
        excel_path = 'data.xlsx'
        df.to_excel(excel_path, index=False)
        return send_file(excel_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": "Erro inesperado."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)
