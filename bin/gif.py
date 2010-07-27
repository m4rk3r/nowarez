import wx
import cStringIO
import wx.animate
#from wxPython.wx import *
from wx import *


class MyFrame(wx.Frame):
    def __init__ (self, parent, ID, title):
        wx.Frame.__init__(self,parent,ID,title, wx.DefaultPosition, wx.Size(800,200))
        self.x = 5
        self.panel1 = wx.Panel(self,-1,size=(self.GetClientSize()[0],self.GetClientSize()[1]),pos=(self.x,10))
        self.panel1.SetBackgroundColour(wx.Colour(255,255,255))
        self.panel2 = wx.Panel(self,-1,size=(100,70),pos=(350,70))
        self.SetBackgroundColour(wx.Colour(255,255,255))
       
        ani = wx.animate.Animation('loader.gif')
        ctrl = wx.animate.AnimationCtrl(self.panel1, -1, ani)
        ctrl.Play()
       
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,self.MoveImage)
        self.timer.Start(milliseconds=20, oneShot=False)
       
        self.Button1 = wx.Button(self.panel2, -1, "no warez", (0,0), wx.Size(100,30), 0, wx.DefaultValidator, "Nothing")
        self.dir = 1
        self.inc = 1
        

        I = wx.IconBundle() 
        I.AddIconFromFile("fux.icns", wx.BITMAP_TYPE_ICO)
        print I
        
        #t = wx.MessageDialog(self,'0 shit','uhh ohh',I)
        #t.ShowModal()
       
    def MoveImage(self,event):
        if self.x >  400:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1
           
        self.x += self.inc * self.dir
       
        self.panel1.MoveXY(self.x,5)
        self.Refresh()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "Nothing")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()