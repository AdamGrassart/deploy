import yaml
from error import Error

class ConfParser():

    def __init__(self, server_name):
        self.error = Error()
        self.server_name = server_name
        self.conf = self._parseFile()

    def _parseFile(self):
        try:
            with open("deploy.yaml", 'r') as stream:
                try:
                    return yaml.safe_load(stream)[self.server_name]
                except yaml.YAMLError as exc:
                    self.error.stop_with_msg(self.error._ERR_FORMAT_CONF_)
                except KeyError:
                    self.error.stop_with_msg(self.error._ERR_SERV_NOEXIST_)
        except IOError:
            self.error.stop_with_msg(self.error._ERR_LOADING_CONF_)

    @property
    def ssh_user_host(self):
        return "{}@{}".format(self.conf['ssh']['user'], self.conf['ssh']['host'])

    @property
    def ssh_port(self):
        if not hasattr(self, 'port'):
            return ''
        else:
            return "-p {}".format(self.port)

    @property
    def ssh_dest(self):
        return self.conf['ssh']['dest']

    @property
    def ssh_infos(self):
        return {
            'user_host': self.ssh_user_host,
            'port': self.ssh_port,
            'dest': self.ssh_dest
        }


