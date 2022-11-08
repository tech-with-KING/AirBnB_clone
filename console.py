#!/usr/bin/python3
import cmd


class Console(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):

        """this command ends the command prompt"""
        return True

    def do_quit(self, line):
        """this command ends the command prompt"""
        return True


if __name__ == "__main__":
    Console().cmdloop()
