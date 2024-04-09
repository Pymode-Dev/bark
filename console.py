from cmd import Cmd


class Console(Cmd):
    prompt = "(bark) "

    def do_EOF(self):
        return True
    
    def do_quit(self, line):
        return True
    
    def do_read(self, line)