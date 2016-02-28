#!/usr/bin/python

import sys
import argparse

import espcmd.Cmd

def main():
    cliRsc = cli()
    return cliRsc.run()

class cli:
    # Parse the command line to get the values
    def __getArguments(self):
        parser = argparse.ArgumentParser() 
        parser.add_argument('port', help="Port where the esp8266 is connected")
        parser.add_argument('commandfile', help="File containing your list of at commands")
        parser.add_argument('-b', '--baudrate', default="115200", help="baudrate to talk to the esp8266. default: 115200")
        return parser.parse_args()
        
    # Run the cli
    def run(self):
        args = self.__getArguments()

        cmdRsc = espcmd.Cmd.cmd(args.port, args.baudrate) 
        return cmdRsc.runFile(args.commandfile)
