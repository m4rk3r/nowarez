#!/usr/bin/python
# -*- coding: utf-8 -*-


import pyaudio
import thread,time
import wx
from wxPython.wx import *
from random import randrange






class Audio:
    def __init__(self):
        self.chunk = 100
        FORMAT = pyaudio.paInt32
        CHANNELS = 2
        RATE = 48000
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,channels = CHANNELS, rate = RATE, input = False,output = True)
        self.play = 1#parent.play
        self.on = 1#parent.on

    def render(self,c):
        #while self.on:
        for x in range(c*10):
            #if self.play:
            self.stream.write('˙´ƒƒ ˙∑˙´ƒ∑˙ˆ˙∑ˆƒ∑∆ºººº00ººººººº00ººººººoøøøø∆∆∆∆∆∆∆∆∆∆¥∆¥∆∆∆¥∆∆∆∆∆∆∆∆∆ºººº∆∆∆ºº∆º∆ºººººººº∆∆∆øøøøøøøøºººººººøøøøøˆ¨¨¨¨¨¨¨¨∆∆∆∆∆∆¨¨¨¨¨¨††††˙†˙˙†˙˙∆∆∆†˙˙˙††††††ƒ†ƒ†ƒ†ƒ†ƒƒƒƒ†††††††††',c)
            #self.stream.write('††††',c)
            #else:
            #    time.sleep(0.1)
    
    
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,-1,'s', size=(300,300),style=wx.FRAME_SHAPED)#,style=wx.SP_LIVE_UPDATE)

        self.play = True
        self.on = True
        self.steps = 10
        
        self.sound = Audio()
        #thread.start_new(self.sound.render,())
        
        self.frame = wx.GetTopLevelParent(self)
        #frame.SetTransparent(100)
        #self.frame.SetShape(wx.Region(randrange(0,500),randrange(0,500),300,100))

        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.x,self.y = 0,0
        self.w,self.h = 1440,900
        self.dir_x = 1
        self.dir_y = 1


        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)
        #panel.SetTransparent(50)


        self.slider = wx.Slider(panel, 5, 6, 1, self.steps)
        self.slider1 = wx.Slider(panel, 5, 6, 1, self.steps)
        self.slider2 = wx.Slider(panel, 5, 6, 1, self.steps)
        self.slider3 = wx.Slider(panel, 5, 6, 1, self.steps)
        self.slider4 = wx.Slider(panel, 5, 6, 1, self.steps)
        self.slider5 = wx.Slider(panel, 5, 6, 1, self.steps)
        self.timer.Start(milliseconds=(50), oneShot=False)

        vbox.Add((-1,10))

        hbox.Add(self.slider, 1)
        hbox1.Add(self.slider1, 1)
        hbox2.Add(self.slider2, 1)      
        hbox3.Add(self.slider3, 1)      
        hbox4.Add(self.slider4, 1)      
        hbox5.Add(self.slider5, 1)      
        vbox.Add(hbox, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)
        vbox.Add(hbox1, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)
        vbox.Add(hbox2, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)
        vbox.Add(hbox3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)
        vbox.Add(hbox4, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)
        vbox.Add(hbox5, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 40)

        panel.SetSizer(vbox)

    def OnTimer(self, event):
        
        
        self.frame.SetShape(wx.Region(self.x,self.y,800,800))
        self.slider.SetValue(randrange(self.steps+1))
        self.slider1.SetValue(randrange(self.steps+1))
        self.slider2.SetValue(randrange(self.steps+1))
        self.slider3.SetValue(randrange(self.steps+1))
        self.slider4.SetValue(randrange(self.steps+1))
        self.slider5.SetValue(randrange(self.steps+1))
        self.sound.render(self.slider.GetValue())
        self.sound.render(self.slider1.GetValue())
        self.sound.render(self.slider2.GetValue())
        self.sound.render(self.slider3.GetValue())
        self.sound.render(self.slider4.GetValue())
        self.sound.render(self.slider5.GetValue())

        self.x+= 10 * self.dir_x
        self.y+= 10 * self.dir_y
        if self.x+800 > self.w:
            self.dir_x = -1
        if self.x < 0:
            self.dir_x = 1
        if self.y+800 > self.h:    
            self.dir_y = -1
        if self.y < 0:
            self.dir_y = 1
        

"""
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "Loading")
        frame.Show(True)
        return True

app= MyApp(0)
app.MainLoop()
"""

app = wx.App(redirect=False)
win = MyFrame()
win.Show()
app.MainLoop()
