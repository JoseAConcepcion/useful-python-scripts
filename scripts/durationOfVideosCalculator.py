#!/home/joseac/python-env/bin/python

import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import datetime
from prettytable import PrettyTable
from plyer import notification


# Definir la ruta de la carpeta donde se encuentran los videos
ruta_carpeta = os.getcwd()

# Crear una lista vacía para almacenar los tiempos de reproducción de cada video
tiempos_reproduccion = []

# Crear una tabla para almacenar los resultados
tabla = PrettyTable()
tabla.field_names = ["Título", "Duración"]

videos = []
# Recorrer la carpeta y para cada archivo de video, obtener su título y duración
for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith(".mp4"):
        # Obtener el título del video
        titulo = os.path.splitext(archivo)[0]
        # Obtener la duración del video
        clip = VideoFileClip(os.path.join(ruta_carpeta, archivo))
        duracion = clip.duration
        clip.close()
        videos.append((titulo, duracion))
        # # Agregar la duración del video a la lista de tiempos de reproducción
        tiempos_reproduccion.append(duracion)
        # # Agregar los resultados a la tabla
        # tabla.add_row([titulo, str(datetime.timedelta(seconds=duracion))])

videos_ordenados = sorted(videos, key=lambda x: x[1])

# Recorrer la lista de videos ordenados y agregar los resultados a la tabla
for video in videos_ordenados:
    titulo = video[0]
    duracion = video[1]
    tabla.add_row([titulo, str(datetime.timedelta(seconds=duracion))])

# Calcular el tiempo total de reproducción sumando todos los tiempos de la lista
tiempo_total = sum(tiempos_reproduccion)

# Calcular el promedio de tiempo de reproducción dividiendo el tiempo total entre la cantidad de videos
promedio_tiempo = tiempo_total / len(tiempos_reproduccion)
promedio_tiempo_semanal = tiempo_total / 7

# Agregar los resultados totales a la tabla
tabla.add_row(["", ""])
tabla.add_row(["Tiempo total", str(datetime.timedelta(seconds=tiempo_total))])
tabla.add_row(["Promedio de tiempo", str(datetime.timedelta(seconds=promedio_tiempo))])
tabla.add_row(["Promedio de tiempo en una semana", str(datetime.timedelta(seconds=promedio_tiempo_semanal))])

# Obtener la tabla como una cadena de texto con formato de tabla
tabla_texto = tabla.get_string(format=True)

# Escribir la tabla en un archivo de texto
with open("tabla.txt", "w") as archivo_tabla:
    archivo_tabla.write(tabla_texto)


message = "TIME CALCULATOR"
title = "Tabla terminada con éxito"
notification.notify(title=title, message=message, app_icon='python.ico', timeout=1)