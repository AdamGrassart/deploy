import yaml

class ConfParser():

    def __init__(self, server_name):
        self.server_name = server_name
        self.conf = self._parseFile()

        print(self.conf)

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
            

    def _err(self, msg):
        print(msg)
        exit(1)



