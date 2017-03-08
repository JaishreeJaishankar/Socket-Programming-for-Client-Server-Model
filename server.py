import socket               # Import socket module

s = socket.socket()         # Create a socket object
print (' --- Server end for Client-server model -------- ')
host = socket.gethostname() # Get local machine name
print '\n Host name of Server : ',host
port = 1996                # Reserve a port for your service.
print '\n Port number of Server : ' ,port
s.bind((host, port))        # Bind to the port
print '\n Finished Bind operation to the Host : ',host ,'and Port number : ',port
s.listen(5)                 # Now wait for client connection.
print ' \n Listening for connections from clients '
c, addr = s.accept()     # Establish connection with client.

print ('Got connection from', addr)
v=True
while v:
   print 'Waiting for Client request .... Please wait  :) '
   cmsg= c.recv(1024)
   print(' Message from Client : ',cmsg)
   if cmsg=='quit':
      v=False
      print 'Quitting on request by client...Thanks for using this server :)'
      quit_msg='quit'
      c.send(quit_msg)
   else:
      print('\n')
      smsg=str(input('Enter the message to be sent to client : '))
      c.send(smsg)
   
   #c.close()  
c.close()
s.close()
