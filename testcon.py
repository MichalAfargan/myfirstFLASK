import sys

class Log(object):
    def __init__(self):
        self.orgstdout = sys.stdout
        self.log = open("log.txt", "a")

    def write(self, msg):
        self.orgstdout.write(msg)
        self.log.write(msg)  

sys.stdout = Log()
print('Hello World')