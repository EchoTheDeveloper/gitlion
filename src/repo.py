import os
import subprocess
import ttkbootstrap as ttk

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

    def Add(self):
        result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Successfully added files to git")
        else:
            print("Error occured while adding files to git")
            print(result.stderr)

    def GetPath(self):
        return (self.repository_path)

def run(repoPath):
    repo = Repository(repository_path = repoPath)
    repo.Commit(commit_message = "Test")

    app = ttk.Window(themename = Theme)
    app.title(f"Repository | {repoPath}")
    app.geometry('800x600')

    AddTXT = ttk.Label(master = app, text = "Add", font = (fontFamily, 14))
    AddTXT.pack(pady=2)
    CommitButton = ttk.Button(master = app, text = "Add", command = lambda: repo.Add())


    CommitTXT = ttk.Label(master = app, text = "Commit", font = (fontFamily, 14))
    CommitTXT.pack(pady=2)
    CommitMSG = ttk.Entry(master = app,  width = 50,  font = (fontFamily, 12))
    CommitMSG.pack()
    CommitButton = ttk.Button(master = app, text = "Commit", command = lambda: repo.Commit(CommitMSG.get()))
    CommitButton.pack()



    app.mainloop()