import wx

class Main(wx.Frame):
    
    def __init__(self, parent , id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600,400))

        self.text = wx.TextCtrl(self, style=wx.TE_MULTILINE)



        self.Show(True)

if __name__ == '__main__':
    app = wx.App()

    frame = Main(None, wx.ID_ANY, 'MMC')

    app.MainLoop()