# PyModbusTCP-Project

This project mounts DoS attacks on the PyModbusTCP protocol using a client-server model as an example system. In a Modbus system the client is typically a PLC, which then makes adjustments using data fedback from the sensors which are simulated by the server. The sensors are called the server, as the PLC queries this to obtain data to then make the necessary adjustments. A packet flow analyzer was also developed alongside the attacks to warn of attacks taking place.

## Coil Scan and Attack
Scans the magnitude of the registers and coils, including the number and size. The attack then writes to these registers and coils in a while loop, to render the data written to them useless. A random value is written to these registers and coils. 


