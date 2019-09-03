import sys

class Error():

    def __init__(self):
        pass

    def stop_with_msg(self, msg):
        sys.exit(msg)