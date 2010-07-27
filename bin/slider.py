#!/usr/bin/python
# -*- coding: utf-8 -*-


import pyaudio
import thread,time
import wx
from wxPython.wx import *
from random import randrange

import os

class Slider():
    def __init__(self,window,parent):
        self.parent = parent
        self.width,self.height = window.GetClientSize()
        self.scroll_size = [10,1]
        self.width -= self.scroll_size[0]
        self.height -= self.scroll_size[1]
        self.pos = lambda: (randrange(0,self.width),randrange(0,self.height))

    
    def slider_batch(self,count):
        bin = []
        for i in range(count):
            slider = wx.Slider(self.parent,-1,maxValue=10,pos=self.pos())
            bin.append(slider)
        return bin


class Audio:
    def __init__(self):
        self.chunk = 30
        FORMAT = pyaudio.paInt32
        CHANNELS = 2
        RATE = 48000
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,channels = CHANNELS, rate = RATE, input = False,output = True)
        self.play = 1#parent.play
        self.on = 1#parent.on

    def render(self,c):
        #while self.on:
        #for x in range(c*2):
        #if self.play:
        self.stream.write(' ',self.chunk+c)
        #self.stream.write('††††',c)
        #else:
        #    time.sleep(0.1)
    
    
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,-1,'s', size=(1440,900))

        self.bmp1 = wx.Bitmap('screen.jpg')
        wx.EVT_PAINT(self, self.on_paint)        
        
        self.count = 0
        self.top = 5
        self.width,self.height = self.GetClientSize()
        self.scroll_size = [10,1]
        self.width -= self.scroll_size[0]
        self.height -= self.scroll_size[1]
        
        self.play = True
        self.on = True
        self.steps = 10
        
        self.sound = Audio()
        #thread.start_new(self.sound.render,())
        
        frame = wx.GetTopLevelParent(self)        
        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.panel = wx.Panel(self, -1)
        
        self.slider_bin = Slider(self,self.panel).slider_batch(20)
        

        self.timer.Start(milliseconds=(50), oneShot=False)


    def on_paint(self, event=None):
        # create paint surface
        dc = wx.PaintDC(self)
        dc.Clear()

        iw = self.bmp1.GetWidth()
        ih = self.bmp1.GetHeight()
        
        dc.DrawBitmap(self.bmp1, 0, 0, True)


    def OnTimer(self, event):

        # set new random slider value
        for slider in self.slider_bin:
            slider.SetValue(randrange(self.steps+1))

        if self.count % self.top == 0:
            self.slider_bin.extend(Slider(self,self.panel).slider_batch(1))
            self.top= randrange(1,15)
            # set new position
            for slider in self.slider_bin:
                slider.Move(
                    (randrange(0,self.width),
                    randrange(0,self.height))
                )
      
        # trigger sound
        for slider in self.slider_bin:
            self.sound.render(slider.GetValue())
        
        self.count+=1
        



os.system('screencapture -x screen.jpg')

app = wx.App(redirect=False)
win = MyFrame()
win.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
win.Show()
app.MainLoop()


