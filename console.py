#!/usr/bin/python3
import cmd
import json
from unicodedata import name
from middlewares import index
import os
class Console(cmd.Cmd):

    """Interactive CLI for command line editing """
    prompt: str = "(hbnb)"
    def do_quit(self,line):
        print("quit")
    def do_objdump(self,line={}):
        json.dump(line)
    def do_EOF(self,line):
        return True
    def do_CreateTable(self,line):
        if line :
            f = open("{}.json".format(line),"w")
        else: print("must specify a file name")
    def do_DeletTable(self,line):
        os.remove("{}.json".format(line))
if __name__   == "__main__":
    Console().cmdloop()
    
