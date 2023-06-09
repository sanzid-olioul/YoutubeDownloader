import tkinter

class Compleated:
    '''
        It is the complete tab gui creation class
        It takes one argument of where to add.
    '''
    __row_count = 0

    def __init__(self,complete_tab):
        self.complete_tab = complete_tab
        self.cTableContainer = tkinter.Canvas(self.complete_tab)
        self.cTableContainer.config(bg='#0F969C')
        self.fTable = tkinter.Frame(self.cTableContainer)
        self.fTable.config(bg='#0F969C')
        self.sbHorizontalScrollBar = tkinter.Scrollbar(self.complete_tab)
        self.sbVerticalScrollBar = tkinter.Scrollbar(self.complete_tab)
        title = tkinter.Label(self.fTable,text='Compleated',bg='#0F969C',fg='#072E33',padx=320,pady=10,font=('Times',24,'bold'))
        title.grid(column=0,row=0,columnspan=1,padx=10,pady=10,sticky='WENS')
        self._createScrollableContainer()

    def _updateScrollRegion(self):
        '''
            It updates the scrollbar.
        '''
        self.cTableContainer.update_idletasks()
        self.cTableContainer.config(scrollregion=self.fTable.bbox())
    
    def _createScrollableContainer(self):
        '''
        It creates the scrolbar.
        '''
        self.cTableContainer.config(xscrollcommand=self.sbHorizontalScrollBar.set,yscrollcommand=self.sbVerticalScrollBar.set, highlightthickness=0)
        self.sbHorizontalScrollBar.config(orient=tkinter.HORIZONTAL, command=self.cTableContainer.xview)
        self.sbVerticalScrollBar.config(orient=tkinter.VERTICAL, command=self.cTableContainer.yview)
        self.sbHorizontalScrollBar.pack(fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)
        self.sbVerticalScrollBar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
        self.cTableContainer.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=tkinter.TRUE)
        self.cTableContainer.create_window(0, 0, window=self.fTable, anchor=tkinter.NW)

    def addNewLabel(self,text):
        '''
            Adds videos which are compeaded to complete tab.
        '''
        Compleated.__row_count+=1
        text = text if len(text) <75 else text[:75] + '...'
        compleated_video = tkinter.Label(self.fTable,background='#0F969C',foreground='white',font="18", text=f'{Compleated.__row_count} . {text}',padx=15,pady=10)
        compleated_video.grid(row=Compleated.__row_count, column=0,sticky='W')
        self._updateScrollRegion()
        
