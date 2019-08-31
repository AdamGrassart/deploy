import yaml

class ConfParser():

    def __init__(self, remote):
        self.remote = remote
        self.conf = self._parseFile()

        # format conf :
        #self.conf["website1"]["ssh"]


    def _parseFile(self):
        # todo : handle error for failed open file
        with open("deploy.yaml", 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)



