#!/usr/bin/python

import sys
import os.path

import espcmd.Com

class cmd:
    __at = "AT"

    def __init__(self, port, baudrate):
        self.__port = port
        self.__baudrate = baudrate

    def __getCommand(self):
        # Get the commands from the given file
        fd = open(self.__commandFile, 'r')
        rawCommands = fd.readlines()
        fd.close()

        # Clean the commands to be sur
        cleanCommand = []
        for command in rawCommands:
            tmpCmd = command.strip()
            if len(tmpCmd) > 0 and tmpCmd.startswith(self.__at):
                cleanCommand.append(tmpCmd)

        return cleanCommand

    def __runCommandEsp(self, espCommands):
        comRsc = espcmd.Com.com(self.__port, self.__baudrate)
        print("Running command on port " + self.__port + " baudrate " + self.__baudrate)
        for command in espCommands:
            comRsc.sendCommand(command)
        comRsc.close()

    def runFile(self, filename):
        if os.path.exists(filename) == False:
            return "File doesn't exists"
        
        self.__commandFile = filename
        commands = self.__getCommand()

        self.__runCommandEsp(commands)
