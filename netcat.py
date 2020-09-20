import socket


class Netcat:

    def __init__(self, ip, port):
        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        val = self.socket.recv(length).decode("utf-8")
        return val

    def read_until(self, data):
        while not data in self.buff:
            self.buff += self.socket.recv(1024).decode("utf-8")

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def clean(self):
        temp = self.buff
        self.buff = ""
        return temp

    def write(self, data):
        self.socket.send(str.encode(data))

    def close(self):
        self.socket.close()


