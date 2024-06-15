## Macros de OCR para Conversión de PDF a Texto

Este proyecto surge por la necesidad de acelerar la velocidad de digitalziación de documentos en mi anterior trabajo, contiene scripts de Python para convertir un archivo PDF en imágenes y luego extraer texto de esas imágenes utilizando OCR (Reconocimiento Óptico de Caracteres) con Tesseract.

Requisitos

- Python 3.6 o superior
- Tesseract OCR instalado y configurado
- Las siguientes bibliotecas de Python:
  - pdf2image
  - pytesseract
  - Pillow
## Como instalar tesseract

1. instalar tesseract directamente usando el repositorio de github: https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract
2. Ir a editar las variables del entorno del sistema.
3. Hacer click en variable de entorno.
4. Seleccionar Path y dar click en editar.
5. Añade una nueva variable de entorno, haz click en "Nuevo" y copias la dirección en la que se encuetra instalado tesseract, usualmente es: c:\Program Files\Tesseract-OCR 
6. Ahora debes añadir la variable TESSDATA_PREFIX y añadir la dirección de la carpeta "tessdata" dentro de la carpeta de Tesseract, usualmente es: C:\Program Files\Tesseract-OCR\tessdata
En tessdata es donde  descargaremos e instalaremos los distintos lenguajes enytrenados por tesseract.

## Instalación de Dependencias

Puedes instalar las dependencias necesarias usando pip:

Debes ejecutar CMD para luego escribir lo siguiente:

pip install pytesseract

Para instalar las demas dependencias, debes seguir los mismos pasos que con pytesseract pero remplazandolo por pdf2image y Pillow