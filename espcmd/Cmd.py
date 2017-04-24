#!/usr/bin/python

import sys
import os.path

import espcmd.Com

class cmd:
    __at = "AT"

    __verbose = False

    def __init__(self, port, baudrate, verbose):
        self.__port = port
        self.__baudrate = baudrate
        self.__verbose = verbose

    def __getCommandFromFile(self):
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
        if self.__verbose == True:
            print("Running commands on port " + self.__port + " baudrate " + self.__baudrate)
            print("")
        for command in espCommands:
            comRsc.sendCommand(command)
        comRsc.close()

    def runFile(self, filename):
        if os.path.exists(filename) == False:
            return "File doesn't exists"

        self.__commandFile = filename
        commands = self.__getCommandFromFile()

        self.__runCommandEsp(commands)
