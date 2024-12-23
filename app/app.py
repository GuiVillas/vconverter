from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image
import os

app = Flask(__name__, template_folder='templates')

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/png_jpg.html')
def outra_pagina():
    return render_template('png_jpg.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado!", 400
    file = request.files['file']
    if file.filename == '':
        return "Nenhum arquivo selecionado!", 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Verifica se o arquivo é PNG e realiza a conversão
        if file.filename.lower().endswith('.png'):
            converted_filepath = convert_png_to_jpg(filepath)
            return send_file(converted_filepath, as_attachment=True)
        else:
            return "Apenas arquivos PNG são suportados no momento!", 400

def convert_png_to_jpg(filepath):
    img = Image.open(filepath)
    rgb_img = img.convert('RGB')  # Converte para RGB (necessário para JPG)
    filename = os.path.splitext(os.path.basename(filepath))[0] + '.jpg'
    converted_filepath = os.path.join(app.config['CONVERTED_FOLDER'], filename)
    rgb_img.save(converted_filepath, 'JPEG')
    return converted_filepath

if __name__ == '__main__':
    app.run(debug=True)
