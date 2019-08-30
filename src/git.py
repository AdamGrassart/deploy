class Git:
    
    def __init__(self):
        pass

    @property
    def branch(self):
        """ give the current branch as variable object """
        pass

    @property
    def commit(self):
        """ give the current commit Object """
        pass
    
    def get_commit(self, sha):
        """ give specific commit Object with sha """
        pass
    
    def diff_commit_file_name(self, commit_a, commit_b)
        """ give diff files list name between commit_a and commit_b """
        pass

    def diff_commit_file_name_state(self, commit_a, commit_b)
        """ give diff files list with state name between commit_a and commit_b """
        pass

    