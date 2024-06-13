import pytesseract
from PIL import Image
import os

# Ruta al directorio que contiene las imágenes
directory = 'C:/Users/PC/Desktop/trabajo municipalidad/images'  # Reemplaza con la ruta de tu directorio de imágenes

# Ruta al archivo de texto donde se guardará el texto extraído
output_text_file = 'C:/Users/PC/Desktop/trabajo municipalidad/extracted_texts.txt'

# Crear el archivo de texto en modo escritura
with open(output_text_file, 'w', encoding='utf-8') as f:
    # Obtener la lista de archivos de imagen en el directorio
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Iterar sobre cada archivo de imagen
    for filename in image_files:
        # Construir la ruta completa de la imagen
        image_path = os.path.join(directory, filename)

        # Abrir la imagen usando PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Utilizar OCR para extraer texto de la imagen
        text = pytesseract.image_to_string(image, lang='spa')  # Especifica el idioma según sea necesario

        # Escribir el texto extraído en el archivo de texto
        f.write(f"Texto extraído de la imagen '{filename}':\n")
        f.write(text)
        f.write('\n\n')

print("Texto extraído correctamente y guardado en:", output_text_file)