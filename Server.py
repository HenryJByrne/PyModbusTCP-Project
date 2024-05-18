# Server code used from 'https://github.com/pymodbus-dev/pymodbus/blob/dev/examples/server_async.py'
# accessed 22/4/23
from pymodbus.server import StartAsyncTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus import __version__ as pymodbus_version
import asyncio
import logging

logging.basicConfig
log = logging.getLogger()
log.setLevel(logging.INFO)

# Imports from the modules to run the code, mainly taken from the pymodbus library

def serversetup(): # defines the server setup function
    datablock = lambda : ModbusSequentialDataBlock(0x00, [17] * 100) # creates a data block which starts from the address 0, shown in hex, and creates 100 addresses which all hold the value 17
    slave_context = ModbusSlaveContext(di=datablock(), co=datablock(), hr=datablock(), ir=datablock(),single=True) # creates a slavecontext, which has the four registers, each assigned a data block to store data  
    server_context = ModbusServerContext(slaves=slave_context, single=True)
    server_identity = ModbusDeviceIdentification( # creates an identifier to identify the server device, giving the attributes shown below
        info_name = {"VendorName": "Pymodbus",
            "ProductCode": "PM",
            "VendorUrl": "https://github.com/pymodbus-dev/pymodbus/",
            "ProductName": "Pymodbus Server",
            "ModelName": "Pymodbus Server",
            "MajorMinorRevision": pymodbus_version}
    )
    return server_context, server_identity # returns the server context and the server identity

async def serverrun(args): # defines the function that runs the server, so that it is asynchronous
    await StartAsyncTcpServer(context=args[0],identity=args[1],address = ("127.0.0.1", 502)) # starts the server so it is asynchronous on the 502 port number which Modbus runs on
    
async def helper():
    args = serversetup() # calls the setup of the server 
    await serverrun(args) # calls the server run function
    
    
    
if __name__ == '__main__':
    asyncio.run(helper()) # uses asyncio to run the server helper function



