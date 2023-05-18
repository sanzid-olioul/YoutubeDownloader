import tkinter
from tkinter import ttk

class DownloadTab:
    def __init__(self,download_tab):
        self.download_tab = download_tab
        


    def check_vidio():
        pass
    
    def set_download_directory():
        pass

    def run_pricess():
        pass

    def progress_bar(self,col,row):
        title = ttk.Label(self.download_tab, text='Hii there how are you',background='#0F969C',foreground='white',font="18")
        title.grid(column=0, row=2*row,sticky='W',padx=30)
        pb = ttk.Progressbar(
            self.download_tab,
            orient='horizontal',
            mode='determinate',
            length=720,
        )
        pb.grid(column=col, row=2*row+1, columnspan=2, padx=30, pady=20,ipady=8)
        pb['value'] = 120
        value_label = ttk.Label(self.download_tab, text=self.update_progress_label(pb),background='#0F969C',foreground='white',font="18")
        value_label.grid(column=col+2, row=2*row+1,sticky='E')
        return (pb,value_label)

    def update_progress_label(self,pb):
        return f"{pb['value']}%"


    def progress(self,pb,value_label):
        if pb['value'] < 100:
            pb['value'] += 20
            value_label['text'] = self.update_progress_label()
        else:
            # showinfo(message='The progress completed!')
            pass


    def stop(self,pb,value_label):
        pb.stop()
        value_label['text'] = self.update_progress_label()



    def add(self):
        title = tkinter.Label(self.download_tab,text='Downloading',bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Times',24,'bold'))
        title.grid(column=0,row=0,columnspan=5,padx=10,pady=10,sticky='WENS')

        self.progress_bar(0,2)
        self.progress_bar(0,3)
        self.progress_bar(0,4)
        self.progress_bar(0,5)

        
