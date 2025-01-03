from flask import Flask, render_template, request, send_file
import os
from PIL import Image, ImageOps
import uuid

app = Flask(__name__)

# Checking id converted folder exist
CONVERTED_FOLDER = "converted"
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

# Pages Routes
@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/jpg-to-png.html")
def jpg_to_png_page():
    return render_template("jpg-to-png.html")

@app.route("/jpg-to-bmp.html")
def jpg_to_bmp_page():
    return render_template("jpg-to-bmp.html")

@app.route("/png-to-jpg.html")
def png_to_jpg_page():
    return render_template("png-to-jpg.html")

@app.route("/png-to-bmp.html")
def png_to_bmp_page():
    return render_template("png-to-bmp.html")

@app.route("/bmp-to-jpg.html")
def bmp_to_jpg_page():
    return render_template("bmp-to-jpg.html")

@app.route("/bmp-to-png.html")
def bmp_to_png_page():
    return render_template("bmp-to-png.html")

# Converts Routes
@app.route("/bmptojpg", methods=["POST"])
def convert_bmp_to_jpg():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.jpg")
            image.save(output_path, format="JPEG")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.jpg"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500

@app.route("/bmptopng", methods=["POST"])
def convert_bmp_to_png():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.png")
            image.save(output_path, format="PNG")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.png"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500

@app.route("/jpgtopng", methods=["POST"])
def convert_jpg_to_png():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.png")
            image.save(output_path, format="PNG")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.png"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500
    
@app.route("/jpgtobmp", methods=["POST"])
def convert_jpg_to_bmp():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.bmp")
            image.save(output_path, format="BMP")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.bmp"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500
    
@app.route("/pngtojpg", methods=["POST"])
def convert_png_to_jpg():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            image = image.convert("RGB")

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.jpg")
            image.save(output_path, format="JPEG")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.jpg"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500
    
@app.route("/pngtobmp", methods=["POST"])
def convert_png_to_bmp():

    try:
        img = request.files["file"]

        with Image.open(img) as image:

            image = ImageOps.exif_transpose(image)

            output_path = os.path.join(CONVERTED_FOLDER, f"{uuid.uuid4()}.bmp")
            image.save(output_path, format="BMP")

        return send_file(
            output_path,
            as_attachment=True,
            download_name="converted_image.bmp"
        )
    
    except Exception as e:
        return f"Erro processing file: {str(e)}", 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))