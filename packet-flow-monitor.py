from scapy.all import *

def portinput():
    while True:
        try:
            port = int(input("Enter in the port of the server to find the packet flow to the server: "))
            timeout = int(input("Enter in the period to count the packets over in seconds: "))
            packetcount = int(input("Enter in the threshold for number of packets across this time period for an alert to be sent: "))
            return port,timeout,packetcount
        except:
            print("Please enter an integer for each field")    

def packetflow(values):
    packets = 0
    trafficfilter = "tcp dst port " + str(values[0])
    snifftimeout = values[1]
    def print_packet(packet):
        nonlocal packets
        packets += 1
        if packets > values[2]:
            print("WARNING: Packet flow over the specified threshold!")
            if IP in packet:
                print("Source IP of this packet: ",packet[IP].src)
            if TCP in packet:
                print("Source port of this packet: ",packet[TCP].sport)
    sniff(iface="Software Loopback Interface 1",filter="tcp dst port 502",prn=print_packet,timeout=snifftimeout)
    print(packets," packet(s) detected over ",snifftimeout," seconds")

def main():
    values = portinput()
    while True:
        packetflow(values)
main()
