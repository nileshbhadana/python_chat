#!usr/bin/pyhton


#importing libraries
import commands,socket   

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#binding ip and port s
port_no=raw_input("Enter port number:")
s.bind(("192.168.43.56",int(port_no)))
'''
user=s.recvfrom(10)				#username's max length is 10 
print user
password=s.recvfrom(10)				#password's max length is 10 
print password

#if user[0]=='abc' and password[0]=='123' :		#checking username and password
s.sendto("allow",password[1])
'''
test=s.recvfrom(10)
client_ip=test[1]
while 4>1 :
	data=s.recvfrom(1000)
	print "<"+client_ip[0]+"> "+data[0] 
	reply=raw_input("<You> ")		
	s.sendto(reply,client_ip)	
s.close()

'''

reply=raw_input("Enter your message:")		
	s.sendto(reply,client_ip)		
	data=s.recvfrom(1000)
	print data[0]		
	#s.sendto(reply,data[1])  	#return output to client		
'''
