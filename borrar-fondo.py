#instalar pip install rembg

from rembg import remove 
from PIL import image 
#entre las comillas poner la imagen que deseas borrar
input_path = "messi.jpg"
#enrtre las comillas es la iamgen que borras el fondo 
output_path = "messi1.jpg"
input = image.open(input_path)
output = remove(input)
output.save(output_path)
