import cv2
import numpy as np
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from skimage.morphology import remove_small_objects

# 1. Se deben leer las imagenes primero (deben de estar en la misma carpeta que este codigo)
fig1 = cv2.imread('img1.jpg') # Cambien el nombre de la imagen de referencia por el que tengan
fig2 = cv2.imread('img2.jpg') # Cambien el nombre de la imagen a revisar por el que tengan

# 2. Convertir a imagen en blanco y negro
fig1BN = rgb2gray(fig1)
fig2BN = rgb2gray(fig2)

# 3. Diferencia de imágenes
dif = np.abs(fig1BN - fig2BN)

# 7. FILTRO 1 - Umbral de pixeles de diferencia
Umbral = dif > (10 / 255.0)

# 8. Filtro 2 - Rellenar huecos de la imagen
FigRellenada = remove_small_objects(Umbral, min_size=50)

# 10. Filtro 3 - Selección de objetos de una longitud determinada
FigStats1 = label(FigRellenada)
FigStats2 = regionprops(FigStats1)
FigLongs = [prop.major_axis_length for prop in props]

# Mientras mayor sea el valor requerirá de areas mas grandes para poner que si hay diferencia
tolerancia = 87 # valor ajustable (87 es el valor maximo que te dirá que hay suficiente diferencia para las imagenes de prueba de matlab)

Fig3 = [length > (tolerancia * 390 / 88) for length in FigLongs]
FigStatsFinal = [FigStats2[i] for i, val in enumerate(Fig3) if val]

if not FigStatsFinal:
    print('No hay suficiente diferencia')
    #Aquí no debería suceder nada más

else:
    print('Hay suficiente diferencia')
    #Aquí se debe activar la alarma
