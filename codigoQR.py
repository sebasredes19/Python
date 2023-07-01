from re import S
import qrcode
from PIL import Image


cadena = input("Introdusca el texto")
image = qrcode.make(cadena)

nombre_image = input("intrdoduzca imagen") + '.png'
archivo_image = open(nombre_image, 'wb')
image.save(archivo_imagen)
archivo_imagen.close()

ruta_image = './'+nombre_image
image.open(ruta_image).show()


#qr = qrcode.QRcode()
#qr.add_data('https://www.youtube.com/watch?v=FD6bXAudZT0o')
#img = qr.make.image()
#img.save
