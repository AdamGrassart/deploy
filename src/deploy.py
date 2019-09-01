import argparse, inspect
from confparser import ConfParser
from git import Git
from ssh import Ssh
import subprocess

class Deploy:

    def __init__(self, args):
        self.command = args.command
        self.server_name = args.server_name
        self.git = Git()

        if self.server_name != '':
            self.conf = self._load_conf()
            self.ssh  = Ssh(self.conf.ssh_user_host,
                            self.conf.ssh_port,
                            self.conf.server_dest)


    def run_manager(self):
        command = 'action_' + self.command
        is_hasattr  = hasattr(self, command)

        if is_hasattr and inspect.ismethod(getattr(self, command)):
            getattr(self, command)()

    def _load_conf(self):
        return ConfParser(self.server_name)

    def action_on(self):
        # appel de la methode on pour envoyer sur le serveur
        pass

    def action_check(self):
        branch, sha = self.ssh.get_rev()
        self.git.branch

        # 3.bis -> on vérifie que l'on est sur la même branche en local
        # 4. -> on compare sha | HEAD


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('command', type=str, metavar='Commande', help="")
    parser.add_argument('server_name',metavar='Server_name',help="")
    args = parser.parse_args()

    deploy = Deploy(args)
    deploy.run_manager()