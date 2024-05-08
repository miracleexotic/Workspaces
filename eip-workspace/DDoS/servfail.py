from scapy.all import *
from threading import Timer

def run():
	answer = sr1(IP(dst="10.1.61.2")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="asd.t1.3mper0r.cloudns.ph")),verbose=0)
	print(answer[DNS].summary())

for i in range(10_000):
	r = Timer(5.0, run)
	r.start()

