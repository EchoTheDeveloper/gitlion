import tkinter as tk
import tkinter.font as tkFont
import ttkbootstrap as ttk

class GitLion():
    def __init__(self, fontPath, theme, fontFamily) -> None:
        self.fontPath = fontPath
        self.fontFamily = fontFamily
        self.theme = theme

        self.master = ttk.Window(themename = theme)
        self.font = tkFont.Font(family=self.fontFamily, size = 14)
        self.titleFont = tkFont.Font(family=self.fontFamily, size = 25)

        self.createWindow()

    def createWindow(self):
        self.master.geometry('800x600')
        self.master.title('GitLion')

        Title = ttk.Label(text='GitLion', master=self.master, font=self.titleFont)
        Title.pack()

    def createButton(self, button_text, button_command, padx = 0, pady = 0) -> None:
        button = ttk.Button(master = self.master, text = button_text, command = button_command)
        button.pack(padx = padx, pady = pady)

    def createInput(self, input_text = 'GITLION ERROR NO INPUT TEXT PROVIDED', width = 40, padx = 0, pady = 0) -> None:
        input = ttk.Entry(master = self.master, width = width)
        input.pack(padx = padx, pady = pady)
        return (input)

    def run(self):
        self.master.mainloop()