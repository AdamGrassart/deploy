import argparse, inspect
from confparser import ConfParser
from ssh import Ssh
import subprocess

class Deploy:

    def __init__(self, args):
        self.command = args.command
        self.server_name = args.server_name

    def run_manager(self):
        command = 'action_' + self.command
        is_hasattr  = hasattr(self, command)

        if is_hasattr and inspect.ismethod(getattr(self, command)):
            getattr(self, command)()

    def action_on(self):
        # appel de la methode on pour envoyer sur le serveur
        pass

    def action_check(self):
        conf = ConfParser(self.server_name)
        ssh = Ssh(conf.ssh_user_host, conf.ssh_port, conf.server_dest)
        branch, rev = ssh.get_rev()
        print(branch) # test
        print(rev)
        #print(ssh_response)
        # 1. -> on se connecte en ssh
        # 2. -> on vérifie que le fichier .rev puisse être ouvert (sinon erreur)
        # 3. -> on récupère les informations du fichier .rev (branch + sha)
        # 3.bis -> on vérifie que l'on est sur la même branche en local
        # 4. -> on compare sha | HEAD


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('command', type=str, metavar='Commande', help="")
    parser.add_argument('server_name',metavar='Server_name',help="")
    args = parser.parse_args()

    deploy = Deploy(args)
    deploy.run_manager()