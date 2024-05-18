import asyncio
import pymodbus.client as modbusClient
import logging
import time
serverport = 502
ip = "127.0.0.1"

log = logging.getLogger()
log.setLevel("DEBUG")

def setup(serverport,ip):
    client = modbusClient.AsyncModbusTcpClient(host=ip,port=serverport)
    return client
    

async def run_client(client):
    await client.connect()
    assert client.connected
    while True:
        await client.write_registers(1,1,slave=1)
        await client.write_coil(32,False,slave=1)
        rr = await client.read_coils(32, 1, slave=1)
        print(rr.bits[0])
        assert len(rr.bits) == 8
        gg = await client.read_holding_registers(1,1,slave=1)
        print(gg.registers)
        time.sleep(5)
    client.close()

async def main(serverport,ip):
    client = setup(serverport,ip)
    await run_client(client)

if __name__ == "__main__":
    asyncio.run(main(serverport,ip), debug=True)
    
