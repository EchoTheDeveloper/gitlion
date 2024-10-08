import os
import subprocess
from gitlion import *

fontPath = os.path.join('resources', 'fonts', 'monofonto rg.otf')
fontFamily = 'Monofonto RG'
Theme = 'cyborg'


class Repository:
    def __init__(self, repository_path) -> None:

        self.repository_path = repository_path

    def Commit(self, commit_message):
        result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
        if result.returncode == 0:
            print("Repository commited successfully!")
        else:
            print("Error occured while commiting the repository.")
            print(result.stderr)

    def GetPath(self):
        return (self.repository_path)

def main(repoPath, CommitMSG):
    repo = Repository(repository_path = repoPath)
    repo.Commit(commit_message = CommitMSG)

    app = GitLion(fontPath = fontPath, fontFamily = fontFamily, theme = Theme)

    app.run()