#!/usr/bin/python

import  socket 
#            type of ip v4 ,      type of protocol UDP  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#u=raw_input("enter username")
#p=raw_input("enter password")

'''
s.sendto(u,("192.168.43.56",7000))
s.sendto(p,("192.168.43.56",7000))
'''
#checking response from server
#response=s.recvfrom(20)
server_ip=raw_input("enter server ip:")
server_port=raw_input("enter server port number:")
server_info=(server_ip,int(server_port))
test="request"
s.sendto(test,server_info)
while 4>2 :   #can also be used
	msg=raw_input("<You> ")
	s.sendto(msg,server_info)
	data=s.recvfrom(10000)	
	print "<"+server_ip+"> "+data[0]
			
s.close()



'''
msg=raw_input("Enter message: ")
	s.sendto(msg,("192.168.43.56",7000))
	reply=s.recvfrom(10000)
	print reply[0]		
	s.sendto(msg,("192.168.43.56",7000))
	#recive output data

	reply=s.recvfrom(10000)
'''
