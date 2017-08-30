import socket

class NetError():
    def __init__(self,msg=""):
        self.messange=msg

def localhost():
    """Retruns local host name."""
    return socket.gethostbyname(socket.gethostname())

class Client():
    def __init__(self):
        #TODO: take app as argument
        self.connected=False
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.host=None
        self.port=None
        
    def connect(self,host=("time.fu-berlin.de",13),port=None):
        if port==None:
            host,port=host
        
        self.socket.connect((host,port))
        self.connected=True
        self.host,self.port=host,port
        return self
        
    def close(self):
        """Closes connection."""
        self.socket.close()
        self.connected=False
        self.host,self.port=None,None
        return self
        
    def recv(self,bit=1024):
        """Recvs data."""
        if self.connected:
            data=self.socket.recv(bit).decode()
            return data
        else:
            raise NetError("Client isn't connected.")
        
    def send(self,s):
        """Sends data."""
        if self.connected:
            self.socket.send(s.encode())
            return self
        else:
            raise NetError("Client isn't connected.")
    def update(self):
        """Updates signals and triggers."""
        pass
        #TODO: connection to gamma app, implement signals and triggers
        
        
class Server():
    def __init__(self,):
        #TODO: take app as argumnet
        self.clients=[]
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.bound=False
        self.host,self.port=None,None
    def bind(self,host=(localhost(),0),port=None):
        """Binds server to port"""
        if port==None:
            host,port=host
        self.socket.bind((host,port))
        self.bound=True
        self.host,self.port=host,port
        return self
    def listen(self,queue=5):
        """Waits for new client."""
        #TODO: test this function
        self.socket.listen(queue)
        socket,addr=self.socket.accept()
        ##print(addr)
        c=Client()
        c.socket=socket
        c.connected=True
        c.host,c.port=addr
        return c
        
        
    def update(self):
        """Updates signals and triggers."""
        pass
        #TODO: connection to gamma app, implement signals and triggers
    
        
