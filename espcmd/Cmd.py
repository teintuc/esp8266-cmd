#!/usr/bin/python

import sys
import os.path

import espcmd.Com

class cmd:
    __at = "AT"

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
        comRsc = espcmd.Com.com('/dev/ttyUSB0')
        for command in espCommands:
            comRsc.sendCommand(command)
        comRsc.close()

    def runFile(self, filename):
        if os.path.exists(filename) == False:
            return "File doesn't exists"
        
        self.__commandFile = filename
        commands = self.__getCommand()

        self.__runCommandEsp(commands)
