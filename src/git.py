import subprocess

class Git:

    def __init__(self, sha=None):
        pass

    @property
    def branch(self):
        """ give the current branch as variable object """
        self._sub_command(['rev-parse','--abbrev-ref', 'HEAD'])

    @property
    def commit(self):
        """ give the current commit Object """
        pass
    
    def get_commit(self, sha):
        """ give specific commit Object with sha """
        pass
    
    def diff_commit_file_name(self, commit_a, commit_b):
        """ give diff files list name between commit_a and commit_b """
        pass

    def diff_commit_file_name_state(self, commit_a, commit_b):
        """ give diff files list with state name between commit_a and commit_b """
        pass


    def _sub_command(self, command):
        command = ['git'] + command

        response = subprocess.Popen(
            command,
            shell = False,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

        result = response.stdout.readlines()
        error = response.stderr.readlines()

        print(result)
        print(error)

        #gestion des erreurs head détaché ou autre
        #if error != []:
        #    self._err("")
        #if result == []:
        #    self._err("")

        #return result

    