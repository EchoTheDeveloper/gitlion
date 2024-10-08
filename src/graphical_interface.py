from repo_manager import *
from gitlion import *
import repo
import os

def Clone():
    Repo = RepositoryManager(repo_url = repoUrl.get())
    Repo.clone()

def Init():
    Repo = RepositoryManager()
    Repo.init()

def Open():
    root = tk.Tk()
    root.withdraw()
    repo_path = filedialog.askdirectory()

    if repo_path:
        repo.run(repoPath = repoUrl.get())

fontPath = os.path.join('resources', 'fonts', 'monofonto rg.otf')
fontFamily = 'Monofonto RG'
Theme = 'cyborg'

app = GitLion(fontPath = fontPath, theme = Theme, fontFamily = fontFamily)

repoUrl = GitLion.createInput (
    self = app,
    input_text = 'Enter URL',
    width = 50
)

button = GitLion.createButton (
    self = app,
    button_text = 'Clone Repo',
    button_command = Clone,
    pady = 10
)

buttonother = GitLion.createButton (
    self = app,
    button_text = 'Init Repo',
    button_command = Init,
    pady = 20
)

openRepo = GitLion.createButton (
    self = app,
    button_text = 'Open Repo',
    button_command = Open,
    pady = 5
)

quitButton = GitLion.createButton (
    self = app,
    button_text = 'Quit',
    button_command = quit
)



app.run()