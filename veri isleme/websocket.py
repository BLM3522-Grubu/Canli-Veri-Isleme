import asyncio
import websockets
import json
import boto3
from datetime import datetime

kinesis_client = boto3.client("kinesis", region_name="eu-north-1")  


async def veri_al(websocket):
    async for mesaj in websocket:
        try:
            veri = json.loads(mesaj)
            veri["timestamp"] = datetime.utcnow().isoformat()

            print("Alınan veri:", veri)

           
            kinesis_client.put_record(
                StreamName="VeriAkisiStream",
                Data=json.dumps(veri),
                PartitionKey="sensor1"
            )
            print("Veri Kinesis'e  başarıyla gönderildi!")

        except Exception as e:
            print("Hata oluştu:", str(e))


async def main():
    server = await websockets.serve(veri_al, "localhost", 8765)
    print("WebSocket sunucusu başlatıldı: ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
