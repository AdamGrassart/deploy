import subprocess
from error import Error

class Git:

    def __init__(self, sha=None):
        self.error = Error()

    @property
    def branch(self):
        """ give the current branch as variable object """
        result = self._sub_command(['rev-parse','--abbrev-ref', 'HEAD'])
        return result[0].decode('utf-8').replace('\n','')

    def diff_file_name(self, sha_remote, status = False):
        """ give diff files list name between commit_a and commit_b """
        result = self._sub_command(['diff', '--name-status', sha_remote, 'HEAD'])

        if result:
            for index, res in enumerate(result):
                result[index] = res.decode('utf-8').replace('\n', '').split('\t')
        else:
            self.error.stop_with_msg(self.error._ERR_BAD_SHA_)

        return result



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

        if error != []:
            return False

        if result == []:
            # todo: à implementer
            pass

        return result

    