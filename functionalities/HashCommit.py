from git import Repo

class HashCommit:

    def get_commit_hash(repo_path='.'):

        try:
            repo = Repo(repo_path)
        except:
            return "unknown"

        if not repo.bare:
            commit_hash = list(repo.iter_commits('master'))[0].hexsha
            return commit_hash

