import argparse, inspect
from confparser import ConfParser
from git import Git
from ssh import Ssh
from error import Error
import subprocess

class Deploy:

    clrTerm = {
        'A': '\033[92m',  # add
        'C': '\033[92m',  # copied
        'D': '\033[31m',  # deleted
        'M': '\033[92m',  # modified
        'R': '\033[94m',  # renamed
        'END': '\033[0m',  # close color
    }

    def __init__(self, args):
        self.command = args.command
        self.server_name = args.server_name
        self.git = Git()
        self.error = Error()

        if self.server_name != '':
            self.conf = self._load_conf()
            self.ssh  = Ssh(self.conf.ssh_infos)



    def run_manager(self):
        command = 'action_' + self.command
        is_hasattr  = hasattr(self, command)
        is_method   = inspect.ismethod(getattr(self, command))

        if is_hasattr and is_method:
            getattr(self, command)()

    def _load_conf(self):
        return ConfParser(self.server_name)

    def action_on(self):
        # appel de la methode on pour envoyer sur le serveur
        pass

    def action_check(self):
        remote_branch, remote_sha = self.ssh.get_rev()

        if self.git.branch != remote_branch:
            self.error.stop_with_msg(self.error._ERR_DIFF_BRANCH_)

        diff = self.git.diff_file_name(remote_sha)

        for line in diff:
            stat, file_name = line[0], line[1]
            clrTerm, clrClose = self.clrTerm[stat], self.clrTerm['END']
            print("{} {} {} {}".format(clrTerm, stat, file_name, clrClose))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('command', type=str, metavar='Commande', help="")
    parser.add_argument('server_name',metavar='Server_name',help="")
    args = parser.parse_args()

    deploy = Deploy(args)
    deploy.run_manager()