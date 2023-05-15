import tkinter
import threading
from tkinter import ttk
from tkinter import filedialog

from home import HomeTab

class YoutubeDownloader:
    def __init__(self) -> None:
        self.__root = tkinter.Tk()
        self.__root.config(bg='#0F969C')
        self.__root.title('Youtube Downloader')
        image = tkinter.PhotoImage(file='images/logo.png')
        self.__root.iconphoto(True,image)
        self.__root.geometry('880x600+300+100')
        self.__root.resizable(False,False)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        self._tab = ttk.Notebook(self.__root)
        self._tab.grid(sticky='wens')
    
    def _home_tab(self):
        s = ttk.Style()
        s.configure('TFrame', background='#0F969C')
        home_image = tkinter.PhotoImage(file='images/home.png')
        home_tab = ttk.Frame(self._tab)
        self._tab.add(home_tab,text='Home',image=home_image,compound='left')
        home = HomeTab(self._tab)
        home.add()

    def _downloading_tab(self):
        pass

    def _compleated_tab(self):
        pass

    def download(self):
        self._home_tab()
        self.__root.mainloop()


if __name__ == '__main__':
    downloader = YoutubeDownloader()

    downloader.download()