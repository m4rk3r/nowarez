#!/usr/bin/python
# -*- coding: utf-8 -*-


import pyaudio
import time
import threading
import wx
from wxPython.wx import *
from random import randrange

import os

class Loader():
    def __init__(self,window,parent):
        self.parent = parent
        self.width,self.height = window.GetClientSize()
        self.scroll_size = [10,1]
        self.width -= self.scroll_size[0]
        self.height -= self.scroll_size[1]
        self.pos = lambda: (randrange(0,self.width),randrange(0,self.height))
   
    def loader_batch(self,count):
        bin = []
        for i in range(count):
            loader = wx.Gauge(self.parent,-1, 50, size=(300,240))
            bin.append(loader)
        return bin

class Audio(threading.Thread):
    def __init__(self):
        self.chunk = 30000
        FORMAT = pyaudio.paInt32
        CHANNELS = 2
        RATE = 48000
        p = pyaudio.PyAudio()
        self.stream = p.open(format = FORMAT,channels = CHANNELS, rate = RATE, input = False,output = True)
        self.data = []
        self.bin = []
        self.lock = threading.Lock()
        
        threading.Thread.__init__(self)

    def setData(self,dat):
        #if len(self.bin) < 100:
        self.bin.append(dat)

    def run(self):
        while 1:
            if self.data:
                self.stream.write('††††',self.chunk + self.data.pop())
                if self.bin: self.data.append(self.bin.pop())
            else:
                if self.bin: self.data.append(self.bin.pop())
            time.sleep(0.01)
        


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,-1,'s', size=(1440,900))

        self.bmp1 = wx.Bitmap('screen.jpg')
        wx.EVT_PAINT(self, self.on_paint)        

        self.count = 0
        self.top = 10
        self.width,self.height = self.GetClientSize()
        self.scroll_size = [10,1]
        self.width -= self.scroll_size[0]
        self.height -= self.scroll_size[1]
        
        # self.play = True
        #  self.on = True
        #  self.steps = 10
        #  
        #  self.sound = Audio()
        self.sound = Audio()
        self.sound.start()
        self.sound_lock = self.sound.lock
        
        
        frame = wx.GetTopLevelParent(self)        
        self.timer = wx.Timer(self, 1)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.panel = wx.Panel(self, -1)

        self.loader_bin = Loader(self,self.panel).loader_batch(20)


        self.timer.Start(milliseconds=(50), oneShot=False)

    def on_paint(self, event=None):
        # create paint surface
        dc = wx.PaintDC(self)
        dc.Clear()

        iw = self.bmp1.GetWidth()
        ih = self.bmp1.GetHeight()

        dc.DrawBitmap(self.bmp1, 0, 0, True)


    def OnTimer(self, event):
        if self.count % self.top == 0:
            self.loader_bin.extend(Loader(self,self.panel).loader_batch(1))
            self.top= randrange(1,15)
            # set new position

            for loader in self.loader_bin:
                loader.Move(
                    (randrange(0,self.width),
                    randrange(0,self.height))
                )
                self.sound.setData(loader.GetValue())
                print loader.GetValue()

        self.count+=1
        for loader in self.loader_bin:
            loader.SetValue(randrange(49))

os.system('screencapture -x screen.jpg')

app = wx.App(redirect=False)
win = MyFrame()
win.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
win.Show()
app.MainLoop()


#def render(self,c):
#while self.on:
#for x in range(c*2):
#if self.play:
#self.stream.write(' ',self.chunk+c)
#self.stream.write('††††',c)
#else:
#    time.sleep(0.1)
