import socket

class filter:
    def __init__(self, ip):
        self.ip=ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("connecting")
        #s.connect(('192.168.2.201', 5025))\
        self.s.connect((ip, 5025))
        print("sending")
        self.s.settimeout(10)
        self.s.send(b'*IDN?\r\n')
        data = self.s.recv(1024)
        print(data)

    def setWavelength(self, center):
        self.s.settimeout(10)
        self.s.send(b'LAMBDA='+str(center).encode()+b'\r\n')

    def setBandwidth(self, BW):
        self.s.settimeout(10)
        self.s.send(b'FWHM='+str(BW).encode()+b'\r\n')

    def getWavelength(self):
        print("getting wavelength")
        self.s.settimeout(1)
        self.s.send(b'LAMBDA?\r\n')
        dataWL = self.s.recv(1024)
        #print(str(dataWL))
        dataWL2=str(dataWL)[8:-5]
        print(dataWL2)
        #dataWL3=dataWL2.replace("\r\n'","")
        #dataWL3 = dataWL2[:-5]
        #print(dataWL3)
        self.s.recv(1024)
        #dataWL=str(dataWL).replace("\r\n'","")
        return dataWL2

    def getBandwidth(self):
        print("getting bandwidth")
        self.s.settimeout(1)
        self.s.send(b'FWHM?\r\n')
        dataBW = self.s.recv(1024)
        print(str(dataBW))
        dataBW2=str(dataBW)[6:-5]
        print(dataBW2)

        #dataBW=str(dataBW).replace("\r\n","")
        return dataBW2
