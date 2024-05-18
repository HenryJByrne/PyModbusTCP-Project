import pymodbus.client as modbusClient
import asyncio

def userinput():
    userinput = input("Enter the IP which we are scanning for modbus servers: ")
    return userinput

def portinput():
    while True:
        try:
            port = int(input("Enter in the port to be scanned: "))
            return port
        except:
            print("Please enter in an integer")

def clientdef(port,ip):
    client = modbusClient.AsyncModbusTcpClient(host=ip,port=port)
    return client

async def portcheck(client):
    try:
        await client.connect()
        assert client.connected
        return True
    except:
        print("No server running on this port and this address")
        return False

async def main():
    IP = userinput()
    port = portinput()
    client = clientdef(port,IP)
    if await portcheck(client):
        print("Modbus server running on this port number")

if __name__ == "__main__":
    asyncio.run(main())
    


    
    

    
