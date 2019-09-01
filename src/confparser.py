import yaml

class ConfParser():

    def __init__(self, server_name):
        self.server_name = server_name
        self.conf = self._parseFile()

        # format conf :
        #self.conf["website1"]["ssh"]


    def _parseFile(self):
        try:
            with open("deploy.yaml", 'r') as stream:
                try:
                    return yaml.safe_load(stream)[self.server_name]
                except yaml.YAMLError as exc:
                    self._err("Le fichier de configuration n'est pas bien formaté")
                except KeyError:
                    self._err("Ce nom de serveur n'existe pas dans le fichier de configuration")
        except IOError:
            self._err("Chargement impossible du fichier deploy.yaml")

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



    def _err(self, msg):
        print(msg)
        exit(1)



