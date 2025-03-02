from django.conf import settings 
import json 
from channels.generic.websocket  import AsyncWebsocketConsumer
import asyncio
import os 

class CameraConsumer(AsyncWebsocketConsumer):
    async def conectar(self):
        await self.accept()
        self.send_images = True
        asyncio.create_task(self.actualizar_imagenes())

    async def desconectar(self, close_code):
        self.send_images = False
    
    async def actualizar_imagenes(self):
        while self.send_images:
            #aca se guardan las fotos
            dir = os.path.join(settings.MEDIA_ROOT, 'esp32_images')

            ultima_img = None 
            if os.path.exists(image_dir):
                imgs = [f for f in os.listdir(dir) if f.endswith(',jpg')] 
                imgs.sort(reverse=True)
                if imgs: 
                    ultima_img = f'/media/esp32_images/{imgs[0]}'
            
            if ultima_img: 
                await self.send(data_txt=json.dumps({
                    'image_url': ultima_img
                }))
            
            await asyncio.sleep(1)
