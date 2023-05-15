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
        self._tab = ttk.Notebook(self.__root,height='580')
        self._tab.grid(sticky='wens')
        s = ttk.Style()
        s.configure('TFrame', background='#0F969C')
    
    def _home_tab(self):
        home_image = tkinter.PhotoImage(file='images/home.png')
        home_tab = ttk.Frame(self._tab)
        self._tab.add(home_tab,text='Home',image=home_image,compound='left')
        home = HomeTab(home_tab)
        home.add()

    def _downloading_tab(self):
        download_image = tkinter.PhotoImage(file='images/download.png')
        download_tab = ttk.Frame(self._tab)
        self._tab.add(download_tab,text='Download',image=download_image,compound='left')


    def _compleated_tab(self):
        complete_image = tkinter.PhotoImage(file='images/check.png')
        complete_tab = ttk.Frame(self._tab)
        self._tab.add(complete_tab,text='Completed',image=complete_image,compound='left')


    def download(self):
        self._home_tab()
        self._downloading_tab()
        self._compleated_tab()
        self.__root.mainloop()


if __name__ == '__main__':
    downloader = YoutubeDownloader()

    downloader.download()