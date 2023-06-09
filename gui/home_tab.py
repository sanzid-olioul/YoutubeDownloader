import os
import pathlib
import tkinter
import threading
from tkinter import filedialog
from downloader.base import VideoPlayList,SingleVidio
class HomeTab:
    '''
        It is the home tab gui creation class
        It takes 3 agruments,
            1. Where it will place
            2. Download object
            3. Compleated oject .
    '''
    def __init__(self,home_tab,download_obj,completed_obj):
        self.home_tab = home_tab
        self.link = tkinter.StringVar()
        self.number_of_vidios = tkinter.StringVar()
        self.download_directory = tkinter.StringVar()
        self.download_directory.set('downloads')
        self.download_directory = tkinter.StringVar()
        self.download_directory.set('downloads')
        self.download_obj = download_obj
        self.completed_obj = completed_obj
        self.BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
        self.folder = tkinter.PhotoImage(file= os.path.join(self.BASE_DIR,'images','folder.png'))

    def check_vidio(self):
        '''
            It checks whether the link is valid or not and if valid then check how
            many videos available of that playlist.
        '''
        if self.download_directory.get() != '':
            SingleVidio.set_download_path(self.download_directory.get())
        else:
            SingleVidio.set_download_path('downloads/')
        try:
            self.video = VideoPlayList(str(self.link.get()),self.download_obj,self.completed_obj)
            self.number_of_vidios.set(str(self.video._total_video)+ ' Total Number of videos')
        except Exception as e:
            try:
                self.video = SingleVidio(str(self.link.get()),self.download_obj,self.completed_obj)
                self.number_of_vidios.set('Only one video exists')
                print(e)
            except:
                self.number_of_vidios.set('Invalid Link')
    
    def set_download_directory(self):
        '''
            It opens the directory where you wnat to download the videos.
        '''
        self.download_directory.set(filedialog.askdirectory(title='Select a Folder to Download'))
        SingleVidio.set_download_path(self.download_directory.get())

    def download_vidios(self):
        '''
            It stars downloading the vidios.
        '''
        try:
            self.video.download_all()
        except:
            try:
                self.video.download(1)
            except Exception as e:
                e = str(e)
                self.number_of_vidios.set(e)

    def run_process(self):
        '''
            It starts new process for downloading YouTube videos, And call download_vidios method.
        '''
        process = threading.Thread(target=self.download_vidios)
        self.number_of_vidios.set('Download Started')
        process.start()

    def add(self):
        '''
            Adds all the graphical components to home tab.
        '''
        title = tkinter.Label(self.home_tab,text='Best Youtube Downloader',bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Times',24,'bold'))
        title.grid(column=0,row=0,columnspan=5,padx=10,pady=10,sticky='WENS')
        link_label = tkinter.Label(self.home_tab,text='Link : ',bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Helvetica',18,'bold'))
        link_label.grid(column=0,row=2,padx=10,pady=10)
        input_value = tkinter.Entry(self.home_tab,textvariable=self.link,bg='#6DA5C0',fg='#072E33',font=('Helvetica',18,),border='2',width=44)
        input_value.grid(column=1,row=2,columnspan=3,padx=10,pady=10)
        check_button = tkinter.Button(self.home_tab,text='Check',bg='#0C7075',fg='#6DA5C0',font=('Helvetica',18,'bold'),command=self.check_vidio)
        check_button.grid(column=4,row=2,padx=10,pady=10)

        download_label = tkinter.Label(self.home_tab,text='Folder:',bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Helvetica',16,'bold'))
        download_label.grid(column=0,row=1,padx=10,pady=10,sticky='WENS')

        download_folder = tkinter.Entry(self.home_tab,textvariable=self.download_directory,bg='#6DA5C0',disabledbackground='#6DA5C0',fg='#072E33',font=('Helvetica',18),border='2',width=44,state='disabled')
        download_folder.grid(column=1,row=1,columnspan=3,padx=10,pady=10)
        download_folder_button = tkinter.Button(self.home_tab,text='Select',image=self.folder,compound='left',bg='#0C7075',fg='#6DA5C0',font=('Helvetica',18,'bold'),command=self.set_download_directory,padx=8)
        download_folder_button.grid(column=4,row=1,padx=10,pady=10)


        vidio_info = tkinter.Label(self.home_tab,textvariable=self.number_of_vidios,bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Helvetica',22,'bold'))
        vidio_info.grid(column=1,row=3,columnspan=3,padx=15,pady=65,sticky='WENS')

        download_button = tkinter.Button(self.home_tab,text='Download',bg='#0C7075',fg='#6DA5C0',font=('Helvetica',22,'bold'),command=self.run_process)
        download_button.grid(column=0,row=4,columnspan=5,padx=10,pady=10)



