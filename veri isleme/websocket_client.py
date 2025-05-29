import asyncio
import websockets
import json
import boto3
import base64
import random
import time

async def veri_gonder():
    uri = "ws://localhost:8765" 
    async with websockets.connect(uri) as websocket:
        while True:
            veri = {
                "sicaklik": round(random.uniform(0, 50), 2),
                "nem": round(random.uniform(10, 90), 2)
            }
            await websocket.send(json.dumps(veri))
            print("Gönderilen veri:", veri)
            await asyncio.sleep(2)  

asyncio.run(veri_gonder())