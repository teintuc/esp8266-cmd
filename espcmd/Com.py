#!/usr/bin/python

import serial
from time import *

def enum(**enums):
    return type('Enum', (), enums)

Status = enum(ERR='ERROR', OK=['OK', 'ready', 'no change'], BUSY='busy')

class com:
    def __init__(self, port):
        self.__ser = serial.Serial(port, 115200)

    def close(self):
        if self.__ser.isOpen():
            self.__ser.close()

    def sendCommand(self, command):
        print("Sending: " + command)
        self.__ser.flushInput()
        self.__ser.write(command + "\r\n")
        self.__ser.readline()
        while 1:
            while self.__ser.inWaiting():
                ret = self.__ser.readline().strip("\r\n")
                if len(ret) > 0:
                    print(ret)
                    if ret == Status.ERR or ret in Status.OK:
                        return None
            sleep(0.5)
