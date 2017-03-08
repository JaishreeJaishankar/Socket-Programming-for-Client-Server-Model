import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print '\n Host name of Server : ',host
port = 1996                # Reserve a port for your service.
print '\n Port number of Server : ' ,port
s.connect((host, port))
print('------------------Client-end in Client-server model-----------------')
print('Connected to   Host name : ',host , ' Port number : ' , port )
var=True
while(var):
    mesg=str(input('Enter the message to server:(Enter "quit" to quit'))
    s.sendall(mesg)
    print 'Message sent to server : ' , mesg
    print 'Waiting for message from server...Please wait :)  '
    a= s.recv(1024)
    print(' Message from Server : ')
    if(a=='quit'):
        print 'Quitting program from Client - end...Thank you :)'
        var=False
    else :
        print(a)      
   

  
s.close                     # Close the socket when done
