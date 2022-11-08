#!/usr/bin/python3
import cmd
import os
from middlewares import index
class Console(cmd.Cmd):

    """Interactive CLI for command line editing """
    prompt: str = "(hbnb)"
    def do_quit(self,line):
        """Interactive CLI for command line editing """
        return True
    def do_EOF(self):
        return True
if __name__   == "__main__":
    Console().cmdloop()
    
