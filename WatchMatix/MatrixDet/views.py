from django.shortcuts import render
from django.db import models
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf  import csrf_exempt
from datetime import datetime
from django.conf import settings
import requests
import os

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def obtener_imagen(request):
    if request.method == 'POST':
        datos_img = request.body
        media_dir = os.path.join(settings.MEDIA_ROOT, 'esp32_img')  # Acá se guardan las imagenes  
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        
        timestamp = datatime.now().strftime("%Y%m%d_%H%M%S")
        filename_img = f"esp32_image{timestamp}.jpg"
        path_img = os.path.join(media_dir, filename_img)

        with open(path_img, 'wb') as f: 
            f.write(datos_img) 
        
        url_img = f'/media/esp32_img/{filename_img}'

        return JsonResponse({
            'success': True,
            'message': 'ya se guardo la imagen :p',
            'url_img': url_img
        })