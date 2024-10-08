import subprocess
import tkinter as tk
from tkinter import filedialog

class RepositoryManager:
    def __init__(self, repo_url = None) -> None:
        self.repo_url = repo_url

    def clone(self):
        root = tk.Tk()
        root.withdraw()
        repo_path = filedialog.askdirectory()

        if repo_path:
            result = subprocess.run(['git', 'clone', self.repo_url, repo_path], capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Repository cloned successfully into {repo_path}!")
            else:
                print("Error occurred while cloning the repository.")
                print(result.stderr)

    def init(self):
        root = tk.Tk()
        root.withdraw()
        repo_path = filedialog.askdirectory()

        if repo_path:
            result = subprocess.run(['git', 'init', repo_path], capture_output=True, text=True)

            if result.returncode == 0:
                print(f"Repository successfully initialised in {repo_path}!")
            else:
                print("Error occured while initialising the repository.")
                print(result.stderr)