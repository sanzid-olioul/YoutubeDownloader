import tkinter
from tkinter import ttk

class DownloadTab:
    '''
        It is a Download Tab gui creation class
        It takes 1 argument where it will be added.
    '''
    def __init__(self,download_tab):
        self.download_tab = download_tab
        title = tkinter.Label(self.download_tab,text='Downloading',bg='#0F969C',fg='#072E33',padx=10,pady=10,font=('Times',24,'bold'))
        title.grid(column=0,row=0,columnspan=3,padx=300,pady=10,sticky='WENS')

    def progress_bar(self,col,row,text):
        '''
            It adds new progress par for shoing the compleated parcentage. 
            and call update_progress_label for the text parcentage showing.
            It takes 3 arguments
                1. which columnt to show.
                2. which row ro show
                3. and the parcentage compleated.
        '''
        text = text if len(text) <=75 else text[:75]+ ' ...'
        title = ttk.Label(self.download_tab, text=text,background='#0F969C',foreground='white',font="18")
        title.grid(column=0, row=2*row,sticky='W',padx=20)
        pb = ttk.Progressbar(
            self.download_tab,
            orient='horizontal',
            mode='determinate',
            length=720,
        )
        pb.grid(column=col, row=2*row+1, columnspan=2, padx=20, pady=20,ipady=7)
        pb['value'] = 0
        value_label = ttk.Label(self.download_tab, text=self.update_progress_label(pb),background='#0F969C',foreground='white',font="18")
        value_label.grid(column=col+2, row=2*row+1,sticky='E')
        return (pb,value_label)

    def update_progress_label(self,pb):
        '''
            It updates the progrssbar level.
            It takes one argument of object of the ttk.Progressbar
        '''
        return f"{pb['value']}%"


    def progress(self,pb,value_label,parcent):
        '''
            It upgrades the progrss level and also update the parcentage.
            It takes 3 arguments
                1. object of the ttk.Progressbar
                2. Label object of showing parcentage
                3. numeric percentage
        '''
        pb['value'] = parcent%100
        value_label['text'] = self.update_progress_label(pb)

    '''
    def stop(self,pb,value_label):
        pb.stop()
        value_label['text'] = self.update_progress_label()
    '''
    
    def add_prgoress(self,col,title,parcent):
        '''
            Adds all the graphical components to download tab.
        '''
        self.progress(*self.progress_bar(0,col,title),parcent)





        
