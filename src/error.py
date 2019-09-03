import sys

class Error():

    _ERR_DIFF_BRANCH_   = "You are not on the right branch"
    _ERR_FORMAT_CONF_   = "The config file is not valid"
    _ERR_SERV_NOEXIST_  = "The Server name don't exist in config file"
    _ERR_LOADING_CONF_  = "Unable to load config file"

    def __init__(self):
        pass

    def stop_with_msg(self, msg):
        sys.exit(msg)