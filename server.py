import socket, time
#from mysocket import mysocket
from Nao import Nao

class RR(object):
    def __init__(self):
        self.nao = Nao()
        #IP = "elmer.local"
        IP = "169.254.16.208"
        
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        self.BUFFER_SIZE = 20  # Normally 1024, but we want fast response
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "before bind"
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        print "before listen"
        self.s.listen(2)
        print 'before accept'
        
    def connectWait(self):
        conn, addr = self.s.accept()
        print "Connection established"
       
        print 'Connection address:', addr
        data = "anything"
        while data != 'exit':
            word = conn.recv(self.BUFFER_SIZE)
            if data: 
                print "received data:", data, len(data),
                data = word[:-2]
                for i in data:
                    print "i: " + i
                if data == "gui":
                    self.nao.main();
                else:
                    print data + " not recognized as internal or external command"
                conn.send(word)
                time.sleep(.3)
        conn.close()

ser = RR()
ser.connectWait()
