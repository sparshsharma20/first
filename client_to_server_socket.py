
'''
*****************************************************************************************
*
*        =============================================
*           Rapid Rescuer (RR) Theme (eYRC 2019-20)
*        =============================================
*
*  This script is intended to check the output of the Task 3A
*  of Rapid Rescuer (RR) Theme (eYRC 2019-20).
*
*  Filename:            rr_t3_client.py
*  Created:             15/12/2019
*  Last Modified:       17/12/2019
*  Author:              e-Yantra Team
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

#sparsh
# Import modules
import time
import socket
import sys

SERVER_IP = '192.168.4.1'		# IP address of ESP32 server
SERVER_PORT = 3333				# Port address for socket communication

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (SERVER_IP, SERVER_PORT)
print('[DEBUG] Connecting to %s Port %s' % server_address)
sock.connect(server_address)

try:
	while True:
		
		print('___________________________________________')
		
		# Get data from user
		tx_data = "#tof#"
		
		# Send data
		print('[DEBUG] Sending to ESP32: "%s"' % tx_data)
		sock.sendall(tx_data.encode())
		# Look for the response
		amount_received = 0
		data = sock.recv(128)
		data = data.decode()
		amount_received += len(data)
		print('[DEBUG] Received from ESP32: "%s"' % data)

		print('___________________________________________')


except KeyboardInterrupt:
	amount_received = 0
	data = sock.recv(128)
	data = data.decode()
	amount_received += len(data)
	print('[DEBUG] Received from ESP32: "%s"' % data)
	print('___________________________________________')
	data="#start#"
	sock.sendall(data.encode())
	print('[DEBUG] Sending to ESP32: "%s"' % data)
	time.sleep(5)
	data="#stop#"
	sock.sendall(data.encode())
	print('[DEBUG] Sending to ESP32: "%s"' % data)
finally:
	print('[DEBUG] Closing Socket')
	sock.close()

