import subprocess

class Ssh:
    def __init__(self, ssh):
        self.ssh_user_host = ssh['user_host']
        self.ssh_port = ssh['port']
        self.server_dest = ssh['dest']

    def get_rev(self):
        rev = self._sub_command("cat {}.rev".format(self.server_dest))
        return rev[0].decode('UTF-8').replace('\n', ''), \
               rev[1].decode('UTF-8').replace('\n', '')

    def get_ssh_commit_sha(self):
        """ Get sha commit from remote file through ssh """
        pass
    
    def set_ssh_commit_sha(self):
        """ Set sha commit remote file through ssh """
        pass

    def _sub_command(self, command):
        response = subprocess.Popen(
            ["ssh", self.ssh_user_host, self.ssh_port, command],
            shell = False,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

        result = response.stdout.readlines()
        error = response.stderr.readlines()

        if error != []:
            self._err("Il semblerais que le fichier .rev soit inexistant verifier bien le chemin d'acces")
        if result == []:
            self._err("fichier .rev vide ?")

        return result



    def _err(self, msg):
        print(msg)
        exit(1)

