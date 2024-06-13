import os
from pdf2image import convert_from_path

# Ruta al archivo PDF
pdf_file = 'C:/Users/PC/Desktop/trabajo municipalidad/tu_archivo.pdf'  # Reemplaza con la ruta de tu archivo PDF

# Directorio donde se guardarán las imágenes generadas
output_directory = 'C:/Users/PC/Desktop/trabajo municipalidad/images'

# Crea el directorio de salida si no existe
os.makedirs(output_directory, exist_ok=True)

# Convertir todas las páginas del PDF en imágenes
pages = convert_from_path(pdf_file, 300)  # 300 = dpi, puedes moficarse según se necesite

# Guardar cada página como un archivo de imagen
for i, page in enumerate(pages):
    image_path = os.path.join(output_directory, f'page_{i + 1}.jpg')
    page.save(image_path, 'JPEG')

print("PDF convertido a imágenes correctamente y guardado en:", output_directory)