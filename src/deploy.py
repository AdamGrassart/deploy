import argparse, inspect
from confparser import ConfParser

class Deploy:

    def __init__(self, args):
        self.command = args.command
        self.remote = args.remote

    def run_manager(self):
        command = 'action_' + self.command
        is_hasattr  = hasattr(self, command)

        if is_hasattr and inspect.ismethod(getattr(self, command)):
            getattr(self, command)()

    def action_on(self):
        print("appel de la methode on")

    def action_check(self):
        # 1. on verifie si le fichier existe bien
        # 2. on recupere les deux ligne (branch | commit sha)
        # 3. on compare
        # deploy check remoteConf
        conf = ConfParser(self.remote)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('command', type=str, metavar='Commande', help="")
    parser.add_argument('remote',metavar='Remote',help="")
    args = parser.parse_args()

    deploy = Deploy(args)
    deploy.run_manager()