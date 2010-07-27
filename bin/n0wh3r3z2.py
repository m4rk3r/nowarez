import wx,os
import wx.animate
from random import choice,randrange,uniform
try:
    from numpy import zeros
    np = True
except:
    np = False

# SOUND SWITCH
soundz_on = True
if soundz_on: import pyaudio,subprocess,platform,thread


class TextDraw(wx.Frame):    
    def __init__(self,np,soundz_on):
        # audio
        self.platf0rm = platform.system()
        self.stream = None
        self.soundz_on = soundz_on
        if soundz_on: self.initSounz()
        self.data = ''
        self.chunk = 120
        self.rotation = 1
        
        wx.Frame.__init__(self, None, -1, "My Window",size=(800,600), pos=(30,50))
        #wx.Frame.__init__(self, None, -1, "My Window",size=(800,600), pos=(0,50))
        self.children = []

        self.drop_count = 10
        self.x = 0
        self.width = 800
        self.height= 600
        # count
        # particle inits

            

        # timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer_event)
        self.timer.Start(milliseconds=10, oneShot=False)
        
        self.Bind(wx.EVT_KEY_DOWN, self._onKeyDown)
    	
    def _onKeyDown(self,event):
        key =  event.GetKeyCode()
        if key == 315:
            self.chunk +=5
            print 'stream up: ',self.chunk
        elif key == 317:
            if self.chunk  >0: self.chunk -=5
            print 'stream down: ',self.chunk
        elif key == 316:
            print 'rotation up: ',self.rotation
            self.rotation += 1
        elif key == 314:
            print 'rotation down: ',self.rotation
            if self.rotation >0: self.rotation -=1
    
    def initSounz(self):
        self.chunk = 100
        FORMAT = pyaudio.paInt32
        CHANNELS = 2
        RATE = 48000
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,channels = CHANNELS, rate = RATE, input = False,output = True)

    def getData(self):
        if self.platf0rm == 'Darwin':
            p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
            retcode = p.wait()
            data = p.stdout.read()
            return data
        elif self.platf0rm == 'Linux':
            try:
                s = os.popen('xsel').read()
                return s
            except:
                print "*** xsel failed.. install it via: sudo apt-get install xsel"
                print "<3 buffer"
        else:
            print "platform unkown.. Turning off sound"
            self.soundz_on = False
        

        
    def Pipe_streamer(self):
        self.data = self.getData()
        for x in range(self.rotation):
            self.stream.write(self.data,self.chunk) #2400 #120
        
        
        
    def on_timer_event(self, event):
        self.x +=1
        if self.x%5==0 and self.soundz_on: thread.start_new(self.Pipe_streamer,())




app = wx.App(redirect=False)
win = TextDraw(np,soundz_on)
win.Show()
app.MainLoop()

