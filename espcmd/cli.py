#!/usr/bin/python

import sys

import espcmd.Cmd

def main():
    cliRsc = cli()
    return cliRsc.run()

class cli:
    def __usage(self):
        usage = "esp-cmd: easy to use esp8266 command sender\n"
        usage += "\tespcmd [path with at command]" 
        return usage

    def run(self):
        # Check if we have an argument
        if len(sys.argv) != 2:
            return self.__usage()

        cmdRsc = espcmd.Cmd.cmd() 
        return cmdRsc.runFile(sys.argv[1])
