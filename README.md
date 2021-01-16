# Practice
for practicing snmp, kafka, socket programming


snmp_dev.py simulates an snmp device and sends data through udp port 162 to slave.py
slave.py sends to server.py through tcp port 8768.
server.py sends to snmp_cons.py through kafka
The four programs should be run in four terminals in the order given below.
py snmp_cons.py
py server.py
py slave.py
py snmp_dev.py
