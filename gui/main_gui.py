import pathlib
import os
import tkinter
from tkinter import ttk
from .home_tab import HomeTab
from .download_tab import DownloadTab
from .complete_tab import Compleated

class YoutubeDownloader:
    def __init__(self) -> None:
        self.BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
        self.__root = tkinter.Tk()
        self.__root.config(bg='#0F969C')
        self.__root.title('Youtube Downloader')
        image = tkinter.PhotoImage(file= os.path.join(self.BASE_DIR,'images','logo.png'))
        self.__root.iconphoto(True,image)
        self.__root.geometry('880x600+300+100')
        self.__root.resizable(False,False)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)
        self._tab = ttk.Notebook(self.__root,height='6')
        self._tab.grid(sticky='wens')
        s = ttk.Style()
        s.configure('TFrame', background='#0F969C')
    
    def _home_tab(self):
        home_tab = ttk.Frame(self._tab)
        self.home_image = tkinter.PhotoImage(file= os.path.join(self.BASE_DIR,'images','home.png'))
        self._tab.add(home_tab,text='Home',image=self.home_image,compound=tkinter.LEFT)
        self._tab.add(home_tab)
        home = HomeTab(home_tab)
        home.add()

    def _downloading_tab(self):
        download_tab = ttk.Frame(self._tab)
        self.download_image = tkinter.PhotoImage(file=os.path.join(self.BASE_DIR,'images','download.png'))
        self._tab.add(download_tab,text='Download', image=self.download_image,compound='left')
        download = DownloadTab(download_tab)
        download.add()

    def _compleated_tab(self):
        complete_tab = ttk.Frame(self._tab)
        self.complete_image = tkinter.PhotoImage(file=os.path.join(self.BASE_DIR,'images','check.png'))
        self._tab.add(complete_tab,text='Completed',image=self.complete_image,compound='left')
        complete = Compleated(complete_tab)
        complete.sanzid()

    def download(self):
        self._home_tab()
        self._downloading_tab()
        self._compleated_tab()
        self.__root.mainloop()

